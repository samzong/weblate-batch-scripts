FROM python:3.9.16-alpine3.18

WORKDIR /code

COPY requirements.txt /code/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk add --no-cache git \
     && pip install --no-cache-dir --upgrade -r /code/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple \
     && rm -rf /var/cache/apk/*

COPY . /code/

ENV WEB_CONCURRENCY=2

EXPOSE 8888

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]