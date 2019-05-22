from python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY api_server.py .
COPY findARestaurant.py .
COPY geocode.py .

EXPOSE 80
EXPOSE 8080
EXPOSE 5000

CMD [ "python", "./api_server.py" ]