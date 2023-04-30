SELECT p.maker, l.speed
FROM Product p
         JOIN Laptop l ON p.model = l.model
WHERE p.type = 'Laptop'
  AND hd >= 10
ORDER BY l.speed;
