FROM python:3.6-alpine3.9

EXPOSE 9000

WORKDIR /inovola
RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    && apk add linux-headers python3-dev libressl-dev libffi-dev libxslt-dev libxml2-dev gcc musl-dev jpeg-dev zlib-dev g++

ADD ./requirements ./requirements
RUN pip install -r requirements

ADD . /inovola
ENTRYPOINT ["./run.sh"]
CMD ["flask"]