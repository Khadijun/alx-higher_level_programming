-- create a table called first_table in mysql
-- The database name will be passed as an argument of the mysql command
-- If the table first_table already exists, its ignored

CREATE TABLE IF NOT EXISTS first_table(
	id INT,
	name VARCHAR(256)
);
