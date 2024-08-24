#!/bin/bash
#用crontab叫start.sh工作
#crontab -e
#加一行 @reboot /home/pi/gitHub/path:wq/start.sh >> /tmp/cron_test.log 2>&1

#進入腳本所有目錄
cd "$(dirname "$0")"

#進入venv1
source ~/miniforge3/etc/profile.d/conda.sh
conda activate venv1

#執行python程式,一次啟動3個,必需要有&連結
python button_mqtt_withPassword.py &
python receive.py &
streamlit run webUI.py &
