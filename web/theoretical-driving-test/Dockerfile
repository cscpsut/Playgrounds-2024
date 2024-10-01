FROM python:3.9-slim

WORKDIR /app

COPY source/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY source/. /app

EXPOSE 3000
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]