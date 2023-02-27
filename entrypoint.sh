#!/usr/bin/env bash

dev_up () {
    echo "Running docker-compose entrypoint script..."
    docker-compose up --build -d
}


dev_down () {
    echo "Running docker-compose down script..."
    docker-compose down

    echo "Removing all docker containers..."
    docker-compose rm -f -s

    echo "Complete! All containers have been removed."
}

"$@"
