# use python base image
FROM python:3.10-slim

# set working directory
WORKDIR /test

# copy files from my directory to container
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# port to listen to
EXPOSE 5000

CMD ["python", "app.py"]
