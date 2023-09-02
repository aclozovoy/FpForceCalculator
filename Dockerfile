FROM python:3.9-slim

ENV DB_PASSWORD xxmssxPzk6UBcBCAhztKVbuwRQWZPg
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

RUN apt-get -y update && apt-get -y install nginx

COPY ./app /app/app
COPY ./bin /app/bin
COPY wsgi.py /app/wsgi.py
WORKDIR /app

# RUN useradd nginx
# USER nginx

COPY nginx.conf /etc/nginx/conf.d/flask-fp-app.conf

EXPOSE 80 443

ENTRYPOINT ["bash", "/app/bin/run.sh"]

CMD /usr/sbin/nginx -g "daemon off;"