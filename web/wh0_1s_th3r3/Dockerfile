FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/

RUN apt-get update && apt-get install -y whois

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
