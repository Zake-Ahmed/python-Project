
FROM python:3.6

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

RUN python3 create.py
ENTRYPOINT ["/usr/local/bin/python3", "app.py"]