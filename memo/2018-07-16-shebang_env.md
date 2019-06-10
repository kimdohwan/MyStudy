
#### ```./manage.py```  vs  ```python manage.py```  
- [env(링크)](https://en.wikipedia.org/wiki/Env), [Shebang(링크)](https://en.wikipedia.org/wiki/Shebang_(Unix))
- python 을 붙이지 않고 실행 할 수 있게 해주는 이유  
  - ```#!/usr/bin/env python```
  - In computing, a shebang is the character sequence consisting of the characters number sign and exclamation mark (#!) at the beginning of a script. It is also called sha-bang, hashbang, pound-bang, or hash-pling.
  - shebang(#!)은 파일 상단에 위치해서 파일이 실행되는 환경을 설정(인터프리터를 설정)  
  - example
    - #!/bin/sh – Execute the file using the Bourne shell, or a compatible shell, with path /bin/sh  
    - #!/bin/bash – Execute the file using the Bash shell.  
    - #!/bin/csh -f – Execute the file using csh, the C shell, or a compatible shell, and suppress the execution of the user’s .cshrc file on startup  
    - #!/usr/bin/perl -T – Execute using Perl with the option for taint checks  
    - #!/usr/bin/env python – Execute using Python by looking up the path to the Python interpreter automatically via env  
    - #!/bin/false – Do nothing, but return a non-zero exit status, indicating failure. Used to prevent stand-alone execution of a script file intended for execution in a specific context, such as by the . command from sh/bash, source from csh/tcsh, or as a .profile, .cshrc, or .login file.
