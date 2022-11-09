# FROM python:3.10.6-slim-buster
# 使用slim-buster,可能会有很多依赖项没有,导致报错
FROM python:3.10.6
WORKDIR /usr/app

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN cat /etc/apt/sources.list
RUN apt-get clean

# Error: sqlalchemy mysql_config not found
# Solution: https://blog.csdn.net/xc_zhou/article/details/80871374
# 需要更新apt软件包,不然默认的版本找不到 libmariadbd-dev 包
RUN apt-get update \
    && apt-get install -y libmariadbd-dev

# 设置CST时区
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y tzdata \
    && ln -fs /usr/share/zoneinfo/${TZ} /etc/localtime \
    && echo ${TZ} > /etc/timezone \
    && dpkg-reconfigure --frontend noninteractive tzdata \
    && rm -rf /var/lib/apt/lists/*

# 设置apt国内源
RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN cat /etc/apt/sources.list
RUN apt-get clean

COPY requirement.txt .

RUN python -m venv venv  \
    && . venv/bin/activate \
    && ./venv/bin/pip install --no-cache-dir --upgrade -r ./requirement.txt -i https://mirrors.aliyun.com/pypi/simple

COPY . .

CMD ["./venv/bin/python", "main.py"]

EXPOSE 8000

