from datetime import datetime
from tools.file import create_log_file, recode_info

def main():
    now = datetime.now()
    current_time_FILE = now.strftime('%Y_%m_%d.log')
    log_path = create_log_file(FILE=current_time_FILE, FOLDER='data1')
    recode_info(log_path)

if __name__ == '__main__':
    main()