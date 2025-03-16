# Para executar o código em um container

# apt install docker 
# sudo docker build -t NEO .
# sudo docker run NEO

FROM python:3.9.21-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
