

#### 에러 로그 만들기
- 배포 과정에서 장고 처리 중 에러가 날 경우 에러를 확인할 수 있는 파일을 만들어 줄 수 있다

```
LOG_DIR = '/var/log/django'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'django.server',
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

```
#### LOG_DIR가 없어서 나는 error를 동적으로 해결(폴더 생성)
- 3번째 방법(가장 추천)까지 발전시키면서 작성해보자  

```
LOG_DIR = '/var/log/django'

# 에러폴더 만들기 다양한 방법1

ROOT_LOG = os.path.join(ROOT_DIR, '.log')
if not os.path.exists(LOG_DIR):
   if not os.path.exists(ROOT_LOG):
       os.makedirs(f'{ROOT_DIR}/.log')

# 에러폴더 만들기 다양한 방법2

if not os.path.exists(LOG_DIR):
   LOG_DIR = os.path.join(ROOT_DIR, '.log')
   if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

# 에러폴더 만들기 다양한 방법3

if not os.path.exists(LOG_DIR):
    LOG_DIR = os.path.join(ROOT_DIR, '.log')
    os.makedirs(LOG_DIR, exist_ok=True)
```
