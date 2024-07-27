import os.path
from datetime import datetime
import random

current_path = os.path.abspath(__name__)
print(current_path)
dir_name = os.path.dirname(current_path)
data_path = os.path.join(dir_name, 'data')
if not os.path.isdir(data_path):
    print('create the dir')
    os.mkdir(data_path)
else:
    print('data dir exist')

log_path = os.path.join(data_path, 'iot.log')
if not os.path.isfile(log_path):
    print('create log file')
    with open(log_path, mode='w', encoding='utf-8', newline='') as file:
        file.write('時間,溼度,溫度\n')
else:
    print('log file exist')

now = datetime.now()
now_str = now.strftime("%y-%m-%d %H:%M:%S")
humidity = str(random.randint(330, 820) / 10)
celsius = str(random.randint(50, 400) / 10)

with open(log_path, mode='a', encoding='utf-8', newline='') as file:
    file.write(now_str+','+humidity+','+celsius+'\n')