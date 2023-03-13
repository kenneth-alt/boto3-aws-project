# Use the official Python image as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /boto3-project

# Copy the current directory contents into the container at /app
COPY . /boto3-project/

# Download and install Docker CLI
RUN curl -fsSL https://get.docker.com -o get-docker.sh && \
    sh get-docker.sh

RUN service docker start

# Install the necessary Python packages
RUN pip install boto3

# Set an environment variable to store the container ID
ENV CONTAINER_ID=""

# Run the script and store the container ID as an environment variable
CMD export CONTAINER_ID=$(hostname) && python idle_sgs.py && docker cp $CONTAINER_ID:/boto3-project/idle_security_groups.txt /home/$USER