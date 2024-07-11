from json import loads
from os import environ
import threading
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.db import MongoDBClient, get_status_count
from utils.response_models import TimeRange
from utils.mqtt import MQTTSubscriber


# creating necessary clients
mongo_client = MongoDBClient(environ.get('MONGODB_URI'), environ.get('DB_NAME'), environ.get('COLLECTION_NAME'))
subscriber = MQTTSubscriber(environ.get('RABBITMQ_HOST'), environ.get('MQTT_TOPIC'))

app = FastAPI()

# configuring cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/status_count')
async def status_count(time_range: TimeRange):
    return get_status_count(time_range.start_time, time_range.end_time, mongo_client)



if __name__ == '__main__':
    # creating a separate thread for rabbitmq consumer to consume messages and insert them to mongodb
    subscriber_thread = threading.Thread(target=subscriber.start, args=(
        lambda client, userdata, message: mongo_client.insert(loads(message.payload)),
    ))
    subscriber_thread.start()

    # running uvicorn server
    uvicorn.run(app, host='127.0.0.1', port=8000)
