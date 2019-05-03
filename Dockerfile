FROM python:alpine

WORKDIR /app

ADD . /app

COPY ./requirements.txt /etc

RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh vim

RUN pip install -r /etc/requirements.txt

EXPOSE 8080

ENV APP_HOST='0.0.0.0'
ENV APP_PORT='8000'
ENV APP_DEBUG=1

CMD ["sh", "run.sh"]