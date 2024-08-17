import paho.mqtt.client as mqtt
import redis
from dotenv import load_dotenv
import os
load_dotenv() #載入.env的
    
redis_conn = redis.Redis(host=os.environ['REDIS_SERVER'], port=6379, password=os.environ['REDIS_PASS'])
render_redis_conn = redis.Redis.from_url(os.environ['RENDER_REDIS'])

def on_message(mosq, obj, msg):
    topic = msg.topic
    message = msg.payload.decode('utf-8')
    redis_conn.rpush(topic, message)
    render_redis_conn.rpush(topic, message)
    print(f"topic={topic}, message:{message}")
          
if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.connect(os.environ['MQTT_SERVER'])
    client.subscribe('501classroom', qos=2)
    client.loop_forever()