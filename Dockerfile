#FROM python:3.10.6-slim-buster
FROM python:3.10.6
WORKDIR /usr/app

COPY Pipfile Pipfile.lock ./

RUN python -m pip install --upgrade pip -i https://mirrors.aliyun.com/pypi/simple
RUN pip install -i https://mirrors.aliyun.com/pypi/simple pipenv
RUN pipenv install --dev --system --deploy
COPY . .
CMD ["python", "main.py"]
EXPOSE 8000


#RUN apt-get update
#RUN apt-get install -y libmysqlclient-dev

# RUN apt-get -y install default-libmysqlclient-dev

#RUN apt-get install libmysqlclient-dev

#RUN python -m venv venv

#RUN pip install --upgrade pip

#COPY requirement.txt .

#RUN . venv/bin/activate

#RUN pip install --no-cache-dir --upgrade -r ./requirement.txt


#CMD ['uvicorn', 'main:app', '--host','0.0.0.0', '--port', '80']


