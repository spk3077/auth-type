FROM httpd:latest

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y apache2-utils vim

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./creds/.htpasswd /usr/local/apache2/.htpasswd
COPY ./creds/.htpasswd.digest /usr/local/apache2/.htpasswd.digest

EXPOSE 80/tcp