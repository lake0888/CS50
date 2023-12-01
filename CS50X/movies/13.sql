SELECT people.name FROM people
INNER JOIN stars ON (stars.person_id = people.id)
WHERE stars.movie_id IN (SELECT movie_id FROM stars WHERE person_id = (SELECT id FROM people WHERE name = 'Kevin Bacon' AND people.birth = 1958))
AND stars.person_id NOT IN (SELECT id FROM people WHERE name = 'Kevin Bacon' AND people.birth = 1958);