FROM python:3.10.6-slim-buster
WORKDIR /usr/app

COPY ./requirement.txt .

#RUN python3 -m pip install --upgrade pip

#RUN pip install --upgrade setuptools

#RUN pip install --upgrade pip

#RUN pip install --upgrade setuptools

#RUN python -m pip install --upgrade pip

#RUN apt-get install python-dev
RUN apt-get install libboost-python-dev

RUN apt-get --version
#python-dev-is-python3

RUN pip install --no-cache-dir --upgrade -r /usr/app/requirement.txt

COPY . .

CMD ['uvicorn', 'main:app', '--host','0.0.0.0', '--port', '80']

EXPOSE 80

