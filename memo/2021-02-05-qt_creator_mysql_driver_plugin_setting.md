### qt creator(5.14.2) mysql driver plugin setting



- qt creator 5.14.2 기준으로 작성
	
- 현상 

  - qt creator 설치 후, debug 모드로 bulid 및 debugging 시, mysql 관련 드라이버 로그 되지 않음
    ```
    QSqlDatabase: QMYSQL driver not loaded
    QSqlDatabase: available drivers: QSQLITE QODBC QODBC3 QPSQL QPSQL7
    ```
  
- 해결

  - qt creator에서 사용하는 컴파일러 plugin 디렉토리 경로에 mysql 드라이버 및 dll 파일 셋팅

    1. plugin 디렉토리 경로(qt creator5.14.2, msvc 2017 64bit 기준)

       - `C:\Qt\Qt5.14.2\5.14.2\msvc2017_64\plugins\sqldrivers` 
       - `qsqlmysqld.dll`, `qsqlmysql.dll` 파일 위 경로에 셋팅

    2. `sqldrivers` 디렉토리에 셋팅해주는 파일

       - github release : https://github.com/thecodemonkey86/qt_mysql_driver/releases

       - zip download : https://github.com/thecodemonkey86/qt_mysql_driver/files/4460984/qsqlmysql.dll_Qt_SQL_driver_5.14.2_MSVC2017_64-Bit.zip
