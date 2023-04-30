SELECT distinct battle
FROM Classes c
         JOIN Outcomes o ON c.class = o.ship or s.name = o.ship
         JOIN Ships s ON s.class = c.class
WHERE c.class = 'Kongo';
