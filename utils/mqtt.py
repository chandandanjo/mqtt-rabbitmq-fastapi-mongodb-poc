import paho.mqtt.client as mqtt


class MQTTSubscriber:

    def __init__(self, broker_host, topic):
        self._broker_host = broker_host
        self._topic = topic
        self._client = mqtt.Client()
        self._client.on_connect = lambda client, userdata, flags, rc: self._client.subscribe(self._topic)

    def _connect(self, on_message):
        if on_message:
            self._client.on_message = on_message
        self._client.connect(self._broker_host, 1883, 60)

    def start(self, on_message=None):
        self._connect(on_message)
        self._client.loop_forever()