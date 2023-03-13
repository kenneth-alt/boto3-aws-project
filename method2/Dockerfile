# Use the official Python image as a parent image
FROM python:3.10-slim-buster

# Set the working directory to /app
WORKDIR /boto3-project

# Copy the current directory contents into the container at /app
COPY . /boto3-project/

# Install the necessary Python packages
RUN pip install boto3

# Run the script when the container launches
CMD python sgs_not_used.py