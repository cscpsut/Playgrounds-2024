FROM node:20.17.0-slim

# Install MariaDB and Supervisor
RUN apt-get update && apt-get install -y mariadb-server supervisor

# Create directory for Supervisor configuration
RUN mkdir -p /var/log/supervisor /run/mysqld /var/lib/mysql && \
    chown -R mysql:mysql /run/mysqld /var/lib/mysql

# Set the working directory
WORKDIR /app

ENV FLAG="PlaygroundsCTF{Ex0d14_0bl173r473_1999}"

# Copy package.json and install dependencies
COPY ./source/package.json /app
RUN npm install

# Copy the rest of the application files
COPY ./source/ /app

COPY ./source/db_init/init.sql /docker-entrypoint-initdb.d/init.sql

# Copy Supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose the app's port
EXPOSE 3000

# Start Supervisor to manage processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
