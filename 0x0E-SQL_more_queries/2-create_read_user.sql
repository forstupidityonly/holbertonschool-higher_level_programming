-- creates\database hbtn_0d_2 + user user_0d_2 w/only SELECT privilege
-- for hbtn_0d_2 pwd:user_0d_2_pwd. DO NOT FAIL
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';