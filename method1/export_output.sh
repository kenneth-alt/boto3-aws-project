#!/bin/bash
sudo docker cp $1:/boto3-project/idle_security_groups.txt /home/$USER

echo "idle_security_groups.txt file exported to /home/$USER"