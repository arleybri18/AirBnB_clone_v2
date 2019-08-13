-- Create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create User
CREATE USER IF NO EXISTS hbnb_test;
-- Grant to new user
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON PRIVILEGES ON performance_schema . * TO 'hbnb_dev'@'localhost';
