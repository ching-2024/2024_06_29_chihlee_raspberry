import streamlit as st
import redis
import json
import pandas as pd
from dotenv import load_dotenv
import os
from streamlit_autorefresh import st_autorefresh

load_dotenv()
st_autorefresh()
redis_conn = redis.Redis(host=os.environ['REDIS_SERVER'], port=6379, password=os.environ['REDIS_PASS'])

st.title('訓練通教室')
st.header("感測器:blue[cool] :sunglasses:")

#取redis上的資料
bytes_list = redis_conn.lrange('501classroom', -5, -1)
#將bytes string 轉換為str
str_list = [bytes_str.decode('utf-8') for bytes_str in reversed(bytes_list)]
#將str轉成json，key/value需是字串
dict_list = [json.loads(data) for data in str_list]
#st.write(dict_list)
df1 = pd.DataFrame(dict_list)
st.dataframe(df1,
             hide_index=True,
             column_config={
                "status":st.column_config.CheckboxColumn(label='按鈕狀態',width='small'),
                "date":st.column_config.DatetimeColumn(label='時間',width='medium')
             })
