FROM python:3.10.6-slim-buster
WORKDIR /usr/app

RUN python -m venv /opt/venv

COPY requirement.txt .

RUN . /opt/venv/bin/activate

RUN /opt/venv/bin/pip install --no-cache-dir --upgrade -r ./requirement.txt

COPY . .

CMD ['uvicorn', 'main:app', '--host','0.0.0.0', '--port', '80']

EXPOSE 80

