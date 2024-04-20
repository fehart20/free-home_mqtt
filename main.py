import os
import asyncio
import websockets
from base64 import b64encode
import json
import paho.mqtt.client as mqtt

username = os.environ.get('FAH_HOME_USERNAME', '')  # Set this to your username
password = os.environ.get('FAH_PASSWORD', '')  # Set this to you password
sysap_ip = os.environ.get('FAH_SYSAP_IP',
                          '')  # Set this to the IP address of your Sysap

basic_auth = b64encode((username + ":" + password).encode()).decode("ascii")


async def ws_main():
    headers = {
        "Authorization": f"Basic {basic_auth}",
    }

    async with websockets.connect('ws://' + sysap_ip + '/fhapi/v1/api/ws',
                                  extra_headers=headers) as ws:
        print("Websocket has been opened.")
        while True:
            data = await ws.recv()
            print("Received event:")
            print(
                data)  # You can use json.loads(data) to parse the JSON object

            # Parse the JSON data
            parsed_data = json.loads(data)

            # Publish the parsed data to an MQTT broker
            publish_to_mqtt(parsed_data)


def publish_to_mqtt(data):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_broker_address = os.environ.get(
        'MQTT_IP', '')  # Replace with your MQTT broker address
    mqtt_broker_port = int(os.environ.get(
        'MQTT_PORT', 1883))  # Replace with your MQTT broker port
    mqtt_username = os.environ.get('MQTT_USERNAME',
                                   '')  # Replace with your MQTT username
    mqtt_password = os.environ.get('MQTT_PASSWORD',
                                   '')  # Replace with your MQTT password

    client.username_pw_set(mqtt_username, mqtt_password)
    client.connect(mqtt_broker_address, mqtt_broker_port, 60)

    # Assuming the data structure is consistent, you can extract information
    # from the JSON data to construct the MQTT topic
    device_id = list(data.keys())[0]
    datapoints = data[device_id]["datapoints"]

    for channel_and_odp, value in datapoints.items():
        # Construct the MQTT topic
        mqtt_topic = f"freeathome/{device_id}/{channel_and_odp.replace('/', '_')}"

        # Publish to the dynamically generated topic
        client.publish(mqtt_topic, str(value))

    client.disconnect()


asyncio.get_event_loop().run_until_complete(ws_main())
