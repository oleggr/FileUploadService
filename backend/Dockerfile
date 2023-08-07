FROM python:3.9 as builder

RUN python3 -m venv /app
RUN /app/bin/pip install -U pip

COPY requirements.txt /mnt/
RUN /app/bin/pip install -Ur /mnt/requirements.txt

FROM python:3.9 as app

WORKDIR /app

COPY --from=builder /app /app
COPY . .

RUN apt-get update
RUN apt-get install -y cron

COPY crontab /etc/cron.d/request-notification-cron
RUN chmod 0644 /etc/cron.d/request-notification-cron
RUN crontab /etc/cron.d/request-notification-cron
RUN touch /app/logs/cron.log

EXPOSE 8000

CMD cron && /app/bin/uvicorn app.app:app --host=0.0.0.0 --port=8000 --proxy-headers