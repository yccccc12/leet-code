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

-- Problem 1068
SELECT p.product_name, s.year, s.price FROM Sales s
INNER JOIN Product p ON s.product_id = p.product_id;

-- Problem 1148
SELECT DISTINCT(author_id) AS id FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;

-- Problem 1378
SELECT u.unique_id, e.name FROM Employees e
LEFT JOIN EmployeeUNI u ON e.id = u.id; 

-- Problem 1581
SELECT customer_id, COUNT(*) AS count_no_trans FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY customer_id;

-- Problem 1661
SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time FROM Activity a
INNER JOIN Activity b ON a.machine_id = b.machine_id AND a.process_id = b.process_id
WHERE a.activity_type = "start" AND b.activity_type = "end"
GROUP BY a.machine_id;

-- Problem 1683
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;

-- Probelm 1757
SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';