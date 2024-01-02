FROM python:3.9.18-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY main.py ./

CMD [ "python", "./main.py" ]