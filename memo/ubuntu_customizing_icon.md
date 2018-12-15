## ubuntu customize icon
- 기본 아이콘 모양을 바꾸는 법은 2가지가 있는 것으로 추정.
    1. 파일의 아이콘이 저장된 폴더로 가서 해당 이미지 파일을 수정  

        - 아이콘 이미지 자체를 수정하는 방법이며 /usr/share/icons 경로에 시스템에서 사용하는 아이콘이 저장되어있다.
    2. 바탕화면 또는 show application 에서 실행하는 파일을 수정   
        - 이 방법은 desktop 에서 실행되는 파일에 들어있는 링크를 수정해주는 방식이다. 예를 들어 /home/user/Desktop 경로에 *.desktop 이라는 파일을 생성하고
        ```
        [Desktop Entry]  
        Name=hi  
        Exec=foocorp-painter-pro  
        Icon=foocorp-painter-pro  
        Type=Application
        Terminal=False  
        Categories=GTK;GNOME;Utility;
        ```
        
        파일 내용을 desktop entry 형식에 맞게 적어주고 chmod 로 실행가능하게 바꿔준다. 바탕화면에 hi 라는 파일이 생성되며 Icon 에 넣어주는 경로에 따라 아이콘 이미지가 설정된다. show application 에 들어있는 파일의 아이콘을 바꿔주기위해서는 다른 경로를 이용한다.  
        
        /usr/share/application 에는 내가 사용할 수 있는/하고 있는 .desktop 파일이 들어있다. 여기서 바꿔주려는 프로그램의 파일을 vim 으로 열어 Icon 항목을 수정하면 된다. chrome 과 terminator 는 쉽게 .desktop 파일을 찾아 수정했다. 하지만 files 프로그램의 아이콘을 찾는데 애를 먹었다. 
        
        18.04 ubuntu 에서는 nautilus 라는 프로그램이 폴더 관리를 담당한다. org.gnome.Nautilus.desktop 이라는 이름의 파일의 Icon 을 위와 같은 방식으로 수정하면 된다. applications 안에는 nautilus 로 시작하는 5개의 .desktop 파일이 있는데, 내가 찾고자 했던건 org.gnome 으로 시작한 저 파일이었다.
        sudo find -iname '\*nautilus\*' 라는 명령어로 org.gnome 으로 시작하는 저 파일을 찾을 수 있었다.



리눅스에서 root 디렉토리에 있는 파일의 역할, 내가 사용하는 어플리케이션이 어떻게 우분투 파일 시스템에 배치되는지 약간의 감을 잡을 수 있었다. 
