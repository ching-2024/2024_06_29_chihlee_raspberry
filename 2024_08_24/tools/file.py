import os.path
from datetime import datetime
import random

def create_log_file(FILE:str, FOLDER:str='data')->str:
    current_path = os.path.abspath(__name__)
    print(current_path)
    dir_name = os.path.dirname(current_path)
    data_path = os.path.join(dir_name, FOLDER)
    if not os.path.isdir(data_path):
        print(f'{FOLDER}: create')
        os.mkdir(data_path)
    else:
        print(f'{FOLDER}:exist')

    log_path = os.path.join(data_path, FILE)
    if not os.path.isfile(log_path):
        print(f'{FILE}: create')
        with open(log_path, mode='w', encoding='utf-8', newline='') as file:
            file.write('topic,時間,狀態\n')
    else:
        print(f'{FILE}: exist')
    return log_path

def recode_info(log_path:str, topic:str, date:str, status:str):
    with open(log_path, mode='a', encoding='utf-8', newline='') as file:
        file.write(topic+','+date+','+status+'\n')