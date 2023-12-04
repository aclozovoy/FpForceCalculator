FROM python:3.9-slim

ENV DB_PASSWORD xxmssxPzk6UBcBCAhztKVbuwRQWZPg
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY ./app /app/app
COPY ./bin /app/bin
COPY wsgi.py /app/wsgi.py
WORKDIR /app

# RUN useradd fp-user
# USER fp-user

EXPOSE 8000

ENTRYPOINT ["bash", "/app/bin/run.sh"]

