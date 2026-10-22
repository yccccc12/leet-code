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

-- Problem 577
SELECT e.name, b.bonus FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;

-- Problem 584
SELECT name FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;

-- Problem 595
SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000;

-- Problem 1148
SELECT DISTINCT(author_id) AS id FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;

-- Problem 1683
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;

-- Probelm 1757
SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';