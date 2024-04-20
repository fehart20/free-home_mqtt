# Build & Start

```bash
docker build -t free-home_mqtt .
```

```bash
docker run --name=free-home_mqtt --restart=unless-stopped -d -e FAH_HOME_USERNAME="" -e FAH_PASSWORD="" -e FAH_SYSAP_IP="" -e MQTT_IP="" -e MQTT_PORT -e MQTT_USERNAME="" -e MQTT_PASSWORD="" free-home_mqtt
```
