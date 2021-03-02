-- creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- cities: id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id ofstates table
-- name VARCHAR(256) can’t be null DO NOT FAIL

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
    FOREIGN KEY id REFERENCES states
);