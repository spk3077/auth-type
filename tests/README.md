# Tests
Contains docker-compose file that runs a test Apache server with HTTP authentication running on certain paths:

*Basic Auth:*
http://localhost/basic/index.html

*Digest Auth:*
http://localhost/basic/index.html


## Prerequisites
The script assumes you are running the web server on the latest Ubuntu version.
Run and install the necessary dependencies below:

    # Update APT Packages
    sudo apt update

    # Install docker-compose
    sudo apt install docker-compose docker docker.io


## Running

    # Needs Root Priv
    sudo su

    # Execute Docker-compose file
    docker-compose up

    # If you'd like to re-build
    docker-compose up --build
