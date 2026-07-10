FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python train.py

EXPOSE 5000

ENV HOST=0.0.0.0
ENV PORT=5000

CMD ["python", "api/app.py"]

#docker build -t practice-mlops .
