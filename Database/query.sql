-- Problem 175
SELECT Person.firstName, Person.lastName, Address.city, Address.state FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;

-- Problem 181
SELECT e.name AS Employee FROM Employee e
WHERE e.salary > (SELECT m.salary FROM Employee m WHERE m.id = e.managerID);

-- Problem 182
SELECT email AS Email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;

-- Problem 183
SELECT c.name AS Customers FROM Customers c
LEFT JOIN Orders o ON c.id = o.customerId
WHERE o.customerId IS NULL;

-- Problem 511
SELECT player_id, MIN(event_date) AS first_login FROM Activity
GROUP BY player_id;