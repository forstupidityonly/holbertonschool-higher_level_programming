-- lists number records with same score in second_table of hbtn_0c_0
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC;