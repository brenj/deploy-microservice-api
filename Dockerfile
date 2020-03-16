FROM ubuntu:18.04

WORKDIR /app

COPY .env /app
COPY median /app/median
COPY Procfile /app
COPY requirements.txt /app

RUN apt-get update && apt-get install -y python3-pip rabbitmq-server redis-server
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

EXPOSE 8000

CMD ["honcho", "start"]
