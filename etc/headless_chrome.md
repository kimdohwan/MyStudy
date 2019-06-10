## Headless Chrome 으로 웹 크롤링하기 

### 사전 작업 

- 크롬 드라이버 최신버전(https://sites.google.com/a/chromium.org/chromedriver/downloads)
	
- 브라우져가 돌아갈 서버 컴퓨터에 chromium-chromedriver 설치  
	``` sudo apt install chromium_chromedriver ```
	
### 코드 예시 
```python3
    chrome_driver_path = f'{os.path.join(os.path.join(BASE_DIR))}/chromedriver'
    # driver = webdriver.Chrome(chrome_driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 혹은 options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
```


