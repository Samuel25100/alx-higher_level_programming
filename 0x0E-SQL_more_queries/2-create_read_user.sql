-- creates the database hbtn_0d_2 and the user user_0d_2 only SELECT privilege
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create new user with password
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grant select privilage
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
