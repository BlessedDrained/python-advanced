SELECT o.order_no, m.full_name, c.full_name
FROM "order" o
         JOIN manager m ON m.manager_id = o.manager_id
         JOIN customer c ON c.customer_id = o.customer_id
WHERE c.city != m.city;