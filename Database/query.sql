-- Problem 175
SELECT Person.firstName, Person.lastName, Address.city, Address.state FROM Person
LEFT JOIN Address ON Person.personId = Address.personId;

-- Problem 176
SELECT MAX(salary) AS SecondHighestSalary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank FROM Employee
) AS t 
WHERE salary_rank = 2;

-- Problem 180
SELECT DISTINCT a.num AS ConsecutiveNums FROM Logs a
INNER JOIN Logs b ON a.id = b.id - 1
INNER JOIN Logs c ON b.id = c.id - 1
WHERE a.num = b.num AND b.num = c.num

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

-- Problem 185
WITH Ranked_Employee AS (
    SELECT
    d.name AS Department,
    e.name AS Employee,
    DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS salary_rank,
    e.salary AS Salary
    FROM Employee e
    LEFT JOIN department d ON e.departmentId = d.id
)

SELECT Department, Employee, Salary FROM Ranked_Employee
WHERE salary_rank <= 3;

-- Problem 196
DELETE b FROM Person a
LEFT JOIN Person b ON a.email = b.email AND b.id > a.id;

-- Problem 197
SELECT a.id FROM Weather a
INNER JOIN Weather b ON DATEDIFF(a.recordDate, b.recordDate) = 1
WHERE a.temperature > b.temperature

-- Problem 511
SELECT player_id, MIN(event_date) AS first_login FROM Activity
GROUP BY player_id;

-- Problem 550
SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity 
WHERE (player_id, event_date) IN
(SELECT player_id, MIN(event_date) + INTERVAL 1 DAY AS first_login_date FROM Activity
GROUP BY player_id)

-- Problem 570
SELECT b.name FROM Employee a
INNER JOIN Employee b ON a.managerId = b.id
GROUP BY b.id
HAVING COUNT(*) >= 5;

-- Problem 577
SELECT e.name, b.bonus FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;

-- Problem 584
SELECT name FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;

-- Problem 585
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM Insurance 
WHERE tiv_2015 IN 
    (
    SELECT tiv_2015 FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) >= 2
    )
AND (lat, lon) IN 
    (
    SELECT lat, lon FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) <= 1
    )
    
-- Problem 595
SELECT name, population, area FROM World
WHERE area >= 3000000 OR population >= 25000000;

-- Problem 596
SELECT class FROM Courses
GROUP BY class
HAVING COUNT(*) >= 5;

-- Problem 602
SELECT id, num FROM
(
    SELECT id, SUM(cnt) as num FROM
    (
        SELECT requester_id AS id, COUNT(*) AS cnt FROM RequestAccepted
        GROUP BY requester_id

        UNION ALL

        SELECT accepter_id, COUNT(*) FROM RequestAccepted
        GROUP BY accepter_id
    ) AS t
    GROUP BY id
) AS s
ORDER BY num DESC
LIMIT 1;

-- Problem 610
SELECT *,
    CASE
        WHEN x + y > z AND x + z > y AND y + z > x THEN "Yes"
        ELSE "No"
    END AS triangle
FROM Triangle

-- Problem 619
SELECT MAX(num) AS num FROM
(
    SELECT num FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS t;

-- Problem 620
SELECT * FROM Cinema
WHERE description != "boring" AND id % 2 = 1
ORDER BY rating DESC;

-- Problem 626
SELECT
    CASE
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id

-- Problem 1045
SELECT customer_id FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT customer_id, product_key) = (SELECT COUNT(*) FROM Product);

-- Problem 1068
SELECT p.product_name, s.year, s.price FROM Sales s
INNER JOIN Product p ON s.product_id = p.product_id;

-- Problem 1070
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN
(
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
)

-- Problem 1075
SELECT 
    p.project_id, 
    ROUND(IFNULL(SUM(e.experience_years) / COUNT(p.project_id) , 0), 2) AS average_years
FROM Project p 
LEFT JOIN Employee e ON e.employee_id = p.employee_id
GROUP BY p.project_id

-- Problem 1141
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date > "2019-06-27" AND activity_date <= "2019-07-27"
GROUP BY activity_date;

-- Problem 1148
SELECT DISTINCT(author_id) AS id FROM Views
WHERE author_id = viewer_id
ORDER BY author_id;

-- Problem 1164
WITH latest AS (
    SELECT *, MAX(change_date) AS latest_date
    FROM Products
    WHERE change_date <= "2019-08-16"
    GROUP BY product_id
)

SELECT
    p.product_id,
    IFNULL(q.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN latest l ON p.product_id = l.product_id
LEFT JOIN Products q ON l.latest_date = q.change_date AND l.product_id = q.product_id

-- Problem 1174
SELECT
    ROUND(SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / COUNT(*) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (SELECT customer_id, MIN(order_date) FROM Delivery GROUP BY customer_id)

-- Problem 1193
SELECT
    DATE_FORMAT(trans_date, "%Y-%m") AS month,
    country, 
    COUNT(*) AS trans_count,
    SUM(IF(state = 'approved', 1, 0)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY month, country

-- Problem 1204
SELECT person_name FROM (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn ASC) AS total_weight
    FROM Queue
) AS t
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1

-- Problem 1211
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(AVG(IF(rating < 3, 1, 0)) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name

-- Problem 1251
SELECT 
    p.product_id, 
    ROUND(IFNULL(SUM(u.units * p.price) / SUM(u.units), 0), 2) AS average_price
FROM Prices p
LEFT JOIN UnitsSold u ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY p.product_id;

-- Problem 1280
SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub -- return every possible combination of rows from students and subjects
LEFT JOIN Examinations e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name

-- Problem 1321
SELECT visited_on, amount, average_amount FROM (
    SELECT 
        visited_on, 
        SUM(total_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,
        ROUND(AVG(total_amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount,
        ROW_NUMBER() OVER (ORDER BY visited_on) AS rn
    FROM (
        SELECT visited_on, SUM(amount) AS total_amount FROM Customer
        GROUP BY visited_on
    ) AS t
) AS u
WHERE rn >= 7

-- Problem 1327
SELECT p.product_name, SUM(o.unit) AS unit FROM Products p
LEFT JOIN Orders o ON p.product_id = o.product_id
WHERE order_date BETWEEN "2020-02-01" AND "2020-02-29"
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100

-- Problem 1341
(
    SELECT c.name AS results FROM MovieRating a
    LEFT JOIN Movies b ON a.movie_id = b.movie_id
    LEFT JOIN Users c ON a.user_id = c.user_id
    GROUP BY a.user_id
    ORDER BY COUNT(*) DESC, name ASC
    LIMIT 1
)

UNION ALL

(
    SELECT b.title FROM MovieRating a
    LEFT JOIN Movies b ON a.movie_id = b.movie_id
    LEFT JOIN Users c ON a.user_id = c.user_id
    WHERE a.created_at BETWEEN "2020-02-01" AND "2020-02-29"
    GROUP BY a.movie_id
    ORDER BY AVG(rating) DESC, b.title ASC
    LIMIT 1
)

-- Problem 1378
SELECT u.unique_id, e.name FROM Employees e
LEFT JOIN EmployeeUNI u ON e.id = u.id; 

-- Problem 1484
SELECT 
    sell_date, 
    COUNT(DISTINCT product) AS num_sold, 
    GROUP_CONCAT(DISTINCT product SEPARATOR ",") AS products 
FROM Activities
GROUP BY sell_date;

-- Problem 1517
SELECT * FROM Users
WHERE REGEXP_LIKE(mail, "^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\\.com$", "c");

-- Problem 1527
SELECT * FROM Patients
WHERE conditions LIKE "DIAB1%" OR conditions LIKE "% DIAB1%";

-- Problem 1581
SELECT customer_id, COUNT(*) AS count_no_trans FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY customer_id;

-- Problem 1633
SELECT 
    r.contest_id, 
    ROUND(
        IFNULL(COUNT(*) / (SELECT COUNT(*) FROM Users), 0) * 100, 2
    ) AS percentage
FROM Register r
LEFT JOIN Users u ON r.user_id = u.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC;

-- Problem 1661
SELECT a.machine_id, ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time FROM Activity a
INNER JOIN Activity b ON a.machine_id = b.machine_id AND a.process_id = b.process_id
WHERE a.activity_type = "start" AND b.activity_type = "end"
GROUP BY a.machine_id;

-- Problem 1667
SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name FROM Users
ORDER BY user_id;

-- Problem 1683
SELECT tweet_id FROM Tweets
WHERE LENGTH(content) > 15;

-- Problem 1729
SELECT user_id, COUNT(*) AS followers_count FROM Followers
GROUP BY user_id
ORDER BY user_id ASC;

-- Problem 1731
SELECT a.employee_id, a.name, COUNT(*) AS reports_count, ROUND(AVG(b.age), 0) AS average_age
FROM Employees a
INNER JOIN Employees b ON a.employee_id = b.reports_to
GROUP BY a.employee_id
ORDER BY a.employee_id;

-- Problem 1757
SELECT product_id FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';

-- Problem 1789
SELECT employee_id, department_id FROM Employee
WHERE primary_flag = "Y" OR employee_id IN 
    (
        SELECT employee_id FROM Employee
        GROUP BY employee_id
        HAVING COUNT(*) = 1
    )
    
-- Problem 1907
SELECT "Low Salary" AS category,
    COUNT(CASE WHEN income < 20000 THEN 1 END) AS accounts_count
FROM Accounts

UNION ALL

SELECT "Average Salary",
    COUNT(CASE WHEN income >= 20000 AND income <= 50000 THEN 1 END)
From Accounts

UNION ALL

SELECT "High Salary",
    COUNT(CASE WHEN income > 50000 THEN 1 END)
From Accounts

-- Problem 1934
SELECT 
    s.user_id, 
    ROUND(IFNULL(SUM(c.action = "confirmed") / COUNT(c.user_id), 0), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;

-- Problem 1978
SELECT employee_id FROM Employees
WHERE manager_id NOT IN (
    SELECT employee_id FROM Employees
) AND salary < 30000
ORDER BY employee_id;

-- Problem 2356
SELECT teacher_id, COUNT(DISTINCT teacher_id, subject_id) AS cnt FROM Teacher
GROUP BY teacher_id;