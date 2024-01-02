# Build & Start
```bash
docker build -t free-home_mqtt .
```

```bash
docker run --name=free-home_mqtt --restart=unless-stopped -d -e USERNAME="" -e PASSWORD="" -e SYSAP_IP="" -e MQTT_IP="" -e MQTT_PORT free-home_mqtt
```
