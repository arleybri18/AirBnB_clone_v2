-- Create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create User
CREATE USER IF NO EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd'
-- Grant to new user
GRANT ALL PRIVILEGES ON hbnb_test_db . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON PRIVILEGES ON performance_schema . * TO 'hbnb_test'@'localhost';
