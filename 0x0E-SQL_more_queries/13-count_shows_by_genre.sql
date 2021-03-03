-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- display: <TV Show genre> - <Number of shows linked to this genre>
-- First column genre Second column number_of_shows Don’t display a genre that
-- doesn’t have any shows linked descending order by the number of shows linked
SELECT tv_genres.name AS "genre", count(*) AS "number_of_shows"
FROM tv_show_genres
LEFT JOIN tv_show_genres
ON tv_shows.genre_id = genre_id
GROUP BY genre_id
ORDER BY count(*) DESC;