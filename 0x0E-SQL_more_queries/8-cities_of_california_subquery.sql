-- lists all cities of California in hbtn_0d_usa. states table contains only
-- one record where name = California (but the id can be different, as per the example)
-- sorted in ascending order by cities.id no JOIN
SELECT id, state_id, name
FROM hbtn_0d_usa
WHERE name = "California";