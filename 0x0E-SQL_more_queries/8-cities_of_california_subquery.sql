-- a script that list all the cities in califonia that can be found the database; hbtn_0d_usa.
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
