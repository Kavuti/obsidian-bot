FROM python:3.10-alpine

RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev

COPY . /app

WORKDIR /app 

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "main.py"]