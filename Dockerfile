#use an official Python runtime as a parent image
FROM python:3.9-slim

#set the working directory in the container
WORKDIR /app

#copy the current directory contents into the container at /app
COPY . /app

#install any needed packages
RUN pip install --no-cache-dir requests flask

#make port 5000 available to the world outside this container
EXPOSE 5000

#define environment variable
ENV NAME=World

#run app.py when the container launches
CMD ["python", "app.py"]