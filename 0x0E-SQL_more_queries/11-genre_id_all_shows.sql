-- lists all shows contained in the database hbtn_0d_tvshows.
-- display: tv_shows.title - tv_show_genres.genre_id
-- ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL just one select
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;