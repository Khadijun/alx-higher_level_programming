-- count and group data
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score;
