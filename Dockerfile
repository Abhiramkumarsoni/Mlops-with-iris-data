# base image with Python 3.11
FROM python:3.11-slim

# working directory inside container
WORKDIR /app

# copy dependency list
COPY requirements.txt ./

# install packages
RUN pip install --no-cache-dir -r requirements.txt

# copy app files into container
COPY . .

# run training script once
RUN python train.py

# declare port for runtime
EXPOSE 5000

# bind to all addresses
ENV HOST=0.0.0.0

# set server port
ENV PORT=5000

# start API app
CMD ["python", "api/app.py"]

# docker build -t practice-mlops .
# docker build -t practice-mlops .

# to detete the image docker iamgage
 # docker rmi practice-mlops          by name 
 # docker rmi a1b2c3d4e5f6            by image id 