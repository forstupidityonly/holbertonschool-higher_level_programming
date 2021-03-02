-- creates the table unique_id id INT default:1 must be unique
-- name VARCHAR(256) DO NOT FAIL
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);