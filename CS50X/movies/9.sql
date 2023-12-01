SELECT DISTINCT(people.name) FROM people
INNER JOIN stars ON (stars.person_id = people.id)
WHERE stars.movie_id IN (SELECT id FROM movies WHERE year = 2004)
ORDER BY people.birth ASC;