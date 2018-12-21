# ubuntu icon customizing
기본 아이콘 모양을 바꾸는 법은 2가지가 있는 것으로 가정.

1. 파일의 아이콘이 저장된 폴더로 가서 해당 이미지 파일을 수정

	아이콘 이미지 자체를 수정하는 방법이며 /usr/share/icons 경로에 시스템에서 사용하는 아이콘이 저장되어있다.  

2. 바탕화면 또는 show application 에서 실행하는 파일을 수정

	이 방법은 desktop 에서 실행되는 파일에 들어있는 링크를 수정해주는 방식이다.

	- #### 바탕화면의 프로그램 아이콘 경로 - /home/user/Desktop
		/home/user/Desktop 경로에 *.desktop 형식으로 아래와 같이 구성되어있다.
		
		```
		[Desktop Entry]  
		Name=hi  
		Exec=foocorp-painter-pro  
		Icon=foocorp-painter-pro  
		Type=Application
		Terminal=False  
		Categories=GTK;GNOME;Utility;
		```  
		
		파일을 만들고 싶다면 내용을 desktop entry 형식에 맞게 적어주고 chmod 로 실행가능하게 바꿔줘야한다. 바탕화면에 hi 라는 파일이 생성되며 Icon 에 넣어주는 경로에 따라 아이콘 이미지가 설정된다.  
		
		show application 에 들어있는 파일의 아이콘을 바꿔주기위해서는 다른 경로를 이용한다.  

	- #### show application 화면의 프로그램 경로 - /usr/share/application/(Pycharm, Chrome, Terminator, ...)

		/usr/share/application 에는 내가 사용할 수 있는/하고 있는 .desktop 파일이 들어있다. 여기서 바꿔주려는 프로그램의 파일을 vim 으로 열어 Icon 항목을 수정하면 된다.
		
		chrome, terminator 는 .desktop 파일이 이름대로 존재해서 쉽게 수정 할 수 있었다. 하지만 files 프로그램의 아이콘을 찾는데 애를 먹었다.
		
		ubuntu 에서는 nautilus 라는 프로그램이 폴더 관리한다는 사실을 발견.
		org.gnome.Nautilus.desktop 이라는 이름의 파일의 Icon 을 위와 같은 방식으로 수정했다. applications 안에는 nautilus 로 시작하는 5개의 .desktop 파일이 있는데, 내가 찾고자 했던건 org.gnome 으로 시작한 파일이었다.
		sudo find -iname '\*nautilus\*' 라는 명령어로 org.gnome 파일의 존재를 알게되었다.

	- #### chrome extensions(keep) - /home/doh/.local/share/applications/(Google keep)

		keep 아이콘을 바꿔주기위해 위에 적은 두가지 경로를 쥐 잡듯 뒤졌지만 찾지 못 했다. 하지만 그 과정에서 크롬 확장프로그램이 user/.config 경로에 존재한다는 것을 알게 되었다.
		
		크롬 확장프로그램 경로: /home/doh/.config/google-chrome/Default/Extensions/hmjkmjkepdijhoojdojkdfohbdgmmhki/3.1.18495.1257_0  
		경로를 자세히 살펴 보면 Extensions/program id(keep)/version 형식으로 저장되어 있다. 하지만 안타깝게도 .desktop 파일은 없었다.
		
		고통스러운 검색과 삽질 끝에 결국 찾았다.  
		
		/home/doh/.local/share/applications/chrome-hmjkmjkepdijhoojdojkdfohbdgmmhki-Default.desktop  
		보다시피 keep 의 프로그램 아이디로 파일명을 구성하고 있다.  
		
	-  #### 고정된 값이 아닌 프로그램?(system monitor) - /var/lib/snapd/desktop/applications(log, calculator, system monitor, .....)
	
		작업종료해주는 system monitor 의 .desktop 이 위치한 곳이다.
		
		usr 이나 home 이 아닌 왜 var 에 위치한걸까? 작업관리자라서 계속 변하는 프로세스를 관리하기 때문에 var 라는 이름의 폴더에 들어가 있을거라고 추측했지만 그건 아닌 듯 하다. 왜냐하면 계산기 앱이 있기때문에.


.desktop 파일을 찾는 방법을 터득함.(파일 검색 or 소스코드 검색)

- File 에서 .desktop 을 검색 후 찾고자하는 이미지의 property 를 통해 경로를 알아낼 수 있다.
- 예상되는 경로에서 Pycharm 을 실행해서 소스코드 검색(Name=Google keep)을 한다.

##### 18.12.16 메모 

 리눅스에서 root 디렉토리에 있는 파일의 역할, 내가 사용하는 어플리케이션이 어떻게 우분투 파일 시스템에 배치되는지 약간의 감을 잡을 수 있었다. 허나 파일 시스템이나 리눅스에 대한 이해없이 그냥 맨땅에 헤딩하는 방식으로는 한계가 있으며 시간도 많이 들었다. 특히 keep .desktop 파일 찾을 때는 정말 힘들었다. c 를 통해 소프트웨어를 직접 만들어본다면 더 이해가 빠를 것 같지만 안타깝게도 지금은 그럴 시간이 없다. 이런 하드한 삽질은 다음부터 자제하자. 그래도 뿌듯하다.
