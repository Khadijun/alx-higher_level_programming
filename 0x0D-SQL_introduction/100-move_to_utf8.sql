--  converts hbtn_0c_0 database to UTF8 
-- Database hbtn_0c_0
-- table first_table
-- Field name in first_table

ALTER DATABASE hbtn_0c_0 
CHARACTER SET = utf8mb4
COLLATE = utf8mb4_unicode_ci;

USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE first_table
MODIFY COLUMN name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
