FROM ubuntu:18.04

WORKDIR /app

COPY .env /app
COPY median /app/median
COPY Procfile /app
COPY requirements.txt /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip=9.0.1-2.3~ubuntu1.18.04.1 \
        rabbitmq-server=3.6.10-1 \
        redis-server=5:4.0.9-1ubuntu0.2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install --upgrade pip==20.0.2 && pip3 install -r requirements.txt

EXPOSE 8000

CMD ["honcho", "start"]
