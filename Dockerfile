# FROM python:3.10.6-slim-buster
# 使用slim-buster,可能会有很多依赖项没有,导致报错
FROM python:3.10.6
WORKDIR /usr/app

# Error: sqlalchemy mysql_config not found
# Solution: https://blog.csdn.net/xc_zhou/article/details/80871374
# 需要更新apt软件包,不然默认的版本找不到 libmariadbd-dev 包
RUN apt-get update \
    && apt-get install -y libmariadbd-dev

COPY requirement.txt .

RUN python -m venv venv  \
    && . venv/bin/activate \
    && ./venv/bin/pip install --no-cache-dir --upgrade -r ./requirement.txt

COPY . .

CMD ["./venv/bin/python", "main.py"]

EXPOSE 8000

