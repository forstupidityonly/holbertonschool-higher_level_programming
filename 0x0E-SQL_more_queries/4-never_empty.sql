-- creates table id_not_null, id INT default 1
-- name VARCHAR(256) dont fail
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);