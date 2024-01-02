FROM python:3.9.18-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

ENV USERNAME="installer"
ENV PASSWORD=""
ENV SYSAP_IP=""
ENV MQTT_IP=""
ENV MQTT_PORT=1883

CMD [ "python", "./main.py" ]
