### awsebcli 사용 시 UnicodeDecodeError 

eb 생성 시 나타나는 아스키 코드 에러 해결하기

####  issue 1
- 사용한 명령어
```eb init --profile <credential key name>```
- 에러 구문
```
2019-03-12 17:59:33,113 (INFO) eb : UnicodeDecodeError - 'ascii' codec can't decode byte 0xec in position 8: ordinal not in range(128)
```
- 해결 과정
unicode encoding 에 대한 문제로 인식하여 내 ubuntu unicode encoding 설정에 관한 구글 검색을 하였고 ```locale``` 이라는 명령어로 Language 와 encoding 설정을 utf-8 로 볼 수 있었다.  
그 후 ```locale-gen``` 명령어를 이용해 en_US.utf8 설정을 해주었으나 여전히 같은 에러 발생.  
내 system 환경과 다른 환경에서의 차이점을 확인하기 위해 docker container 안 쪽에서 awsebcli 를 설치 후 ```eb init``` 을 시도했더니 잘 동작하는 것을 확인. locale 설정도 크게 다르지 않았고 난관에 봉착.  
locale 문제가 아닌 듯 하여 awsebcli 사용 시 나타나는 에러에 초점을 맞춰서 구글 검색해보니 eb init 시에 profile 확인시 home/.aws/credential 파일을 인식한다는 사실 확인.  
credentail 을 확인해보니 한글 주석이 존재. 지운 후 잘 동작.  

#### issue 2
- 사용한 명령어/에러 발생 시점 
```eb init --profile <credential key name>```, 위 과정 진행 후 CodeCommit 설정 시 
- 에러 구문
```
File "/home/doh/.local/share/virtualenvs/Project-ijLdZslq/lib/python3.6/site-packages/ebcli/objects/sourcecontrol.py", line 294, in set_up_ignore_file
    for line in f:
File "/home/doh/.local/share/virtualenvs/Project-ijLdZslq/lib/python3.6/encodings/ascii.py", line 26, in decode
    return codecs.ascii_decode(input, self.errors)[0]
UnicodeDecodeError: 'ascii' codec can't decode byte 0xec in position 8: ordinal not in range(128)

2019-03-12 17:59:33,113 (INFO) eb : UnicodeDecodeError - 'ascii' codec can't decode byte 0xec in position 8: ordinal not in range(128)
```
- 해결 과정
위의 과정을 겪었기에 encoding 관련 설정은 문제가 아니라고 판단.  
내 프로젝트의 파일 중 한글이 들어간 어떤 파일의 문제일거라고 짐작했지만 딱히 어떤 파일인지 짐작이 가지않아 구글 검색(검색어: unicodedecodeerror codecommit).  
같은 문제를 해결한 블로그 발견. 에러 구문에 적힌 파일을 뒤져서 .gitignore 에서 문제가 발생했음을 인지함.  
에러 구문(File "/home/doh/.local/share/virtualenvs/Project-ijLdZslq/lib/python3.6/site-packages/ebcli/objects/sourcecontrol.py", line 294, in set_up_ignore_file for line in f:) 에 나온 suorcecontrol.py line 294 를 확인해보니 .gitignore 에 관한 코드가 존재했고 .gitignore 에 적어둔 한글 주석을 모두 지워주니 잘 동작하게 되었다.  
```
		def set_up_ignore_file(self):
		    if not os.path.exists('.gitignore'):
			open('.gitignore', 'w')
		    else:
			with open('.gitignore', 'r') as f:
			    for line in f:
			        if line.strip() == git_ignore[0]:
			            return
	
		    with open('.gitignore', 'a') as f:
			f.write(os.linesep)
			for line in git_ignore:
			    f.write(line + os.linesep)
```

### 문제 해결 key point
awsebcli 의 경우 인코딩 설정이 ascii 로 동작한다. 내 시스템에서는 utf-8 이라는 인코딩 방식이 동작해서 한글 주석이 들어간 파일을 읽는데 문제가 없었지만 awsebcli 시스템은 ascii 인코딩 방식으로 돌아가기 때문에 생긴 문제였다. 따라서 credential 과 .gitignore 파일을 awsbcli 에서는 US-ASCII 로 인코딩을 하게되고 한글 인식이 되지 않는다.  

그렇다면 awsebcli 에서 ascii 인코딩 방식을 사용한다는 것을 어떻게 알 수 있을까?  
위에 올려놓은 에러코드 중 마지막 UnicodeDecodeError 부분을 다시 한번 살펴보자.
```
2019-03-12 17:59:33,113 (INFO) eb : UnicodeDecodeError - 'ascii' codec can't decode byte 0xec in position 8: ordinal not in range(128)
```
에러구문에는 친절하게 ```'ascii' codec``` 이 바이트 문자를 디코드 할 수 없다고 나와있다. 여기서 ```ascii``` 는 ```utf-8``` 과 같은 인코딩 방식을 의미하는 것이었다. 수십번이나 읽은 에러 코드인데 코덱이 뭘 의미하는지, 인코딩 방식에 어떤 것들이 있는지 몰랐기 때문에 awsebcli 에서 내 시스템과 다른 인코딩 방식을 사용한다고 생각조차 못한 것이었다.  

- ebcli 소스코드에서 locale 설정 찾아보기
내가 사용하는 가상환경 파이썬의 사이트 패키지에 ebcli/display/ 디렉토리 안쪽에 ebcli 가 사용하는 locale 설정 코드를 발견 할 수 있다.  
path: ```~/.local/share/virtualenvs/Project-ijLdZslq/lib/python3.6/site-packages/ebcli/display```  
locale 설정 코드: ```locale.setlocale(locale.LC_ALL, 'C')```  

### 더 알아보기
- 인코딩의 이해
ascii code 또는 unicode 는 영어, 한글과 같은 각각의 문자, 기호를 특정 숫자에 매핑해 놓는다.  매핑된 특정 숫자는 인코딩 방식(ex:utf-8, utf-16, ascii, ansi)에 따라서 컴퓨터가 인식할 수 있는 바이트 형태로 변환되며 이 부분이 encode(암호화)에 해당한다.  
unicode, ascii code 의 경우 단순히 특정 숫자에 매핑된 테이블이며 인코딩이라는 개념과 헷갈릴 수 있으니 주의하자. utf-8 은 Universal Coded Character Set + Transformation Format – 8-bit 의 약자로 unicode 를 기반으로 문자를 인코딩하는 방식이다. utf-16 은 16bit 를 사용한다.  
- locale 과 encoding 
locale 은 프로그램 수행 시 사용자가 선택할 수 있는 환경을 의미한다. 숫자표현법, 시간표현법, 언어 와 같은 각각의 category 를 설정할 수 있다. 사용자가 설정한 locale 에 따라서 입/출력 인코딩을 적용하여 메시지를 출력한다.  
encoding 은 locale 설정에 적용되는 한 부분에 해당하며 locale-```C```는 가장 기본적인(호환가능한?충돌이 없는?) 설정이라고 할 수 있다. ```C``` locale 을 설정할 경우 encoding 방식은 ascii 로 설정되며 ascii 는 영어만 지원한다.  
locale 설정 중 ```LC_ALL``` 은 가장 우선시되는 설정으로 ```LANG```, ```LC_TIME``` 등과 같은 모든 설정을 덮어써서 작동한다.  

#### 얻어가야할 부분
- 이미 확인된 사항에 목매지 말 것
처음에 해당 에러를 접했을 때 유일한 해결수단은 구글 검색이었고 중간이 그마저도 제대로된 결과를 못엇어서 issue 1 에 해당하는 아주 간단한 에러를 해결하기까지 하루를 통쨰로 날렸다. 내 시스템 인코딩 환경에 문제가 없다는 것을 locale 명령어를 통해 확인하고도 locale 관련 검색에 반나절을 날렸다. locale 에 문제가 없다는 것을 확인 했을 때 더 빨리 ebcli 관련 에러를 살펴보는 쪽으로 알아봤어야 한다. 
- 에러구문에 나오는 소스코드 파일을 통해 해결방법을 찾아 볼 것
issue2 를 해결하기위해 찾은 블로그(https://lioliolio.github.io/awseclie-unicodedecodeerror/)에서는 내가 상상치도 못한 소스코드 파일을 살펴봄으로써 문제를 해결했다. 소스코드를 읽기도 힘들고 많은 시간을 써야할 수도 있지만 문제를 해결하는데 더욱더 근본적인 해결 방식이고 프로그래밍 실력에도 훨씬 도움이 될 것이 분명하다. 명심하자 문제의 근본적인 원인은 결국 소스코드라는 것을.