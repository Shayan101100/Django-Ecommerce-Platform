

class Config:
    BROKER_URL = 'redis://127.0.0.1:6379/0'
    RESULT_BAKEND = 'redis://127.0.0.1:6379/0'
    
    TASK_SERIALIZER = 'jason'
    RESULT_SERIALIZER = ['jason']
    ACCEPT_CONTENT = 'Asia/Tehran'
    ENABLE_UTS = True
    TIMEZONE = "asia/tehran"
    