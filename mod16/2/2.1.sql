SELECT c.full_name, m.full_name, purchase_amount, date
FROM "order"
         JOIN customer c on "order".customer_id = c.customer_id
         JOIN manager m on "order".manager_id = m.manager_id;