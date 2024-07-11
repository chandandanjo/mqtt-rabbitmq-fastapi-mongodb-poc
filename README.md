# MQTT Message Handling with FastAPI and MongoDB

This repository contains a client-server setup to handle MQTT messages using Python scripts. The client script (`client.py`) generates random status messages and publishes them to a specified MQTT topic. The server (`server.py`) consumes these messages, stores them in MongoDB, and provides an API endpoint to query status counts within a given time range.

## Prerequisites

Before running the scripts, ensure you have the following installed and set up:

- Python 3.x
- RabbitMQ broker (`rabbitmq`)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/chandandanjo/mqtt-rabbitmq-fastapi-mongodb-poc.git
   cd mqtt-rabbitmq-fastapi-mongodb-poc
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the root directory with the following variables:

   ```plaintext
   RABBITMQ_HOST=<your_rabbitmq_host>
   MQTT_TOPIC=<your_mqtt_topic>
   MONGODB_URI=<your_mongodb_uri>
   DB_NAME=<your_db_name>
   COLLECTION_NAME=<your_collection_name>
   ```

4. Ensure rabbitmq-mqtt plugin is enabled:

   ```bash
   rabbitmq-plugins enable rabbitmq-mqtt
   ```

5. Restart RabbitMQ broker:

   ```bash
   rabbitmq-service stop
   rabbitmq-service start
   ```

6. Run the client and server:

   - Start the client script to publish MQTT messages:

     ```bash
     python client.py
     ```

   - Start the FastAPI server to consume messages and provide API endpoints:

     ```bash
     python server.py
     ```

7. Access the API:

   After starting the server, the FastAPI application will be available at `http://127.0.0.1:8000`. Use tools like Postman or curl to interact with the API endpoints.

## API Endpoints

- **POST /status_count**

  Retrieves the count of each status within a specified time range.

  **Request Body:**

  ```json
  {
    "start_time": "YYYY-MM-DDTHH:MM:SS",
    "end_time": "YYYY-MM-DDTHH:MM:SS"
  }
  ```

  **Response:**

  ```json
  [
    {
      "status": <status_code>,
      "count": <count>
    },
    ...
  ]
  ```
