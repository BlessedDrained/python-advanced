SELECT distinct c.class
FROM (SELECT s.class, s.name
      FROM Ships s
      UNION
      SELECT o.ship, o.ship
      FROM Outcomes o
      WHERE NOT EXISTS(SELECT * FROM Ships s WHERE s.name = o.ship)) s
         JOIN Classes c ON c.class = s.name AND c.class = s.class;
