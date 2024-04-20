FROM python:3.9.18-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

ENV FAH_HOME_USERNAME="installer"
ENV FAH_PASSWORD=""
ENV FAH_SYSAP_IP=""
ENV MQTT_IP=""
ENV MQTT_PORT=1883
ENV MQTT_USERNAME=""
ENV MQTT_PASSWORD=""


CMD [ "python", "./main.py" ]
