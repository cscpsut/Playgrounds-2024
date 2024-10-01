-- Create a new database user with password and specific privileges
CREATE USER 'myuser'@'%' IDENTIFIED BY 'blu33y35ul71m473n30dr460n';
GRANT ALL PRIVILEGES ON *.* TO 'myuser'@'%';

-- Revoke any non-local root access for added security
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'root'@'%';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'blu33y35ul71m473n30dr460n';

-- Flush privileges to apply changes
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS shadowdimension;

-- Switch to the newly created database
USE shadowdimension;

-- Create the `accounts` table if it doesn't exist
CREATE TABLE IF NOT EXISTS `accounts` (
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
);

-- Insert data into the `accounts` table
INSERT INTO `accounts` VALUES ('ATEM', '3x0d14_7h3_f0rb1dd3n_0n3');
