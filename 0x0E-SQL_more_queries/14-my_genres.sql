-- lists all genres of the show Dexter display: tv_genres.name
-- sorted in ascending order by the genre name only one SELECT statement
SELECT tv_genres.name
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.tytle = 'Dexter'
ORDER BY tv_genres.name ASC;