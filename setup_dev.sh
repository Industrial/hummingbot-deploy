#!/bin/bash

# Pulling the required Docker images
sudo docker compose -f docker-compose-dev.yml pull
sudo docker pull hummingbot/hummingbot:latest

# Creating .env file with the required environment variables
echo "CONFIG_PASSWORD=a" > .env
echo "BOTS_PATH=$(pwd)" >> .env

# Running docker-compose in detached mode
sudo docker compose -f docker-compose-dev.yml up -d
