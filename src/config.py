import os

USER_INFO = os.getenv('USER_INFO')
PUSH_KEY = os.getenv('PUSH_KEY')

USER_INFO_ARR = USER_INFO.split("|", 1)
USERNAME = USER_INFO_ARR[0]
PASSWORD = USER_INFO_ARR[1]
