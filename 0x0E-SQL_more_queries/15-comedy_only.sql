-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
-- Query to lists all genres of the show Dexter
SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
LEFT JOIN tv_genres g ON sg.genre_id = g.id WHERE g.name = "Comedy"
ORDER BY s.title;
