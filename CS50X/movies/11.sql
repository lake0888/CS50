SELECT movies.title FROM movies
INNER JOIN ratings ON (ratings.movie_id = movies.id)
INNER JOIN stars ON (stars.movie_id = movies.id)
WHERE stars.person_id = (SELECT id FROM people WHERE name = 'Chadwick Boseman')
ORDER BY ratings.rating DESC, movies.title ASC LIMIT 5;