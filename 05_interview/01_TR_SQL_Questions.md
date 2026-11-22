
# SQL Interview Questions & Answers
### BCA Fresher | TCS | Wipro | Infosys | Accenture | Cognizant

A collection of 50 important SQL interview questions with short definitions, simple explanations and practical examples.

**Level:** Beginner to Intermediate  
**Database:** MySQL

---

## PART 1 – SQL Fundamentals (1–8)

### 1. What is SQL?
**Definition:** SQL (Structured Query Language) is used to store, manage and retrieve data from relational databases.

**Example:**
```sql
SELECT * FROM STUDENT;
```

### 2. What is the difference between SQL and MySQL?

| SQL | MySQL |
|---|---|
| SQL is a query language. | MySQL is an RDBMS. |
| Used to communicate with databases. | Used to store and manage data. |

**Example:** SQL is used to write `SELECT` queries in MySQL.

### 3. Difference between DBMS and RDBMS?

| DBMS | RDBMS |
|---|---|
| Manages data. | Manages related data in tables. |
| Relationships are not necessarily enforced. | Supports relationships using keys. |
| Example: File-based systems. | Example: MySQL, Oracle. |

### 4. What are the different types of SQL commands?

**Definition:** SQL commands are divided into five main categories.

| Type | Purpose | Commands |
|---|---|---|
| DDL | Defines database structure | CREATE, ALTER, DROP, TRUNCATE |
| DML | Modifies data | INSERT, UPDATE, DELETE |
| DQL | Retrieves data | SELECT |
| DCL | Controls permissions | GRANT, REVOKE |
| TCL | Manages transactions | COMMIT, ROLLBACK, SAVEPOINT |

### 5. Difference between DDL, DML, DQL, DCL and TCL?

**Definition:** These categories define how SQL commands interact with databases.

**Example:**
```sql
CREATE TABLE STUDENT(ID INT); -- DDL

INSERT INTO STUDENT VALUES(1); -- DML

SELECT * FROM STUDENT; -- DQL

COMMIT; -- TCL
```

### 6. What is a Table, Row and Column?

- **Table:** Collection of related data.
- **Row:** A single record.
- **Column:** A specific attribute of data.

**Example:**

| ID | NAME | AGE |
|---|---|---|
| 1 | Payal | 21 |
| 2 | Rahul | 22 |

Here, STUDENT is the table, each student is a row, and ID, NAME and AGE are columns.

### 7. What is NULL in SQL?

**Definition:** NULL represents a missing or unknown value in a database.

**Example:**
```sql
SELECT * FROM STUDENT
WHERE AGE IS NULL;
```

### 8. Difference between CHAR and VARCHAR?

| CHAR | VARCHAR |
|---|---|
| Fixed-length string. | Variable-length string. |
| Uses fixed storage length. | Uses storage based on actual data length, plus overhead. |
| Suitable for fixed-size values. | Suitable for variable-size values. |

**Example:**
```sql
NAME CHAR(10),
CITY VARCHAR(50);
```

---

## PART 2 – SQL Commands (9–15)

### 9. Difference between DELETE, DROP and TRUNCATE?

| DELETE | DROP | TRUNCATE |
|---|---|---|
| Deletes selected rows or all rows. | Deletes the entire table structure. | Removes all rows. |
| Supports WHERE. | No WHERE. | No WHERE. |
| Table remains. | Table is removed. | Table remains. |

**Example:**
```sql
DELETE FROM STUDENT WHERE ID = 1;

TRUNCATE TABLE STUDENT;

DROP TABLE STUDENT;
```

### 10. Difference between INSERT and UPDATE?

- **INSERT:** Adds new records.
- **UPDATE:** Modifies existing records.

**Example:**
```sql
INSERT INTO STUDENT VALUES(1, 'Payal');

UPDATE STUDENT
SET NAME = 'Priya'
WHERE ID = 1;
```

### 11. Difference between WHERE and HAVING?

| WHERE | HAVING |
|---|---|
| Filters individual rows. | Filters grouped results. |
| Applied before GROUP BY. | Applied after GROUP BY. |
| Normally used without aggregate conditions. | Commonly used with aggregate functions. |

**Example:**
```sql
SELECT * FROM STUDENT
WHERE MARKS > 70;

SELECT DEPARTMENT, AVG(SALARY)
FROM EMPLOYEE
GROUP BY DEPARTMENT
HAVING AVG(SALARY) > 30000;
```

### 12. Difference between ORDER BY and GROUP BY?

- **ORDER BY:** Sorts records.
- **GROUP BY:** Groups records having common values.

**Example:**
```sql
SELECT * FROM STUDENT
ORDER BY MARKS DESC;

SELECT DEPARTMENT, COUNT(*)
FROM EMPLOYEE
GROUP BY DEPARTMENT;
```

### 13. Difference between DISTINCT and UNIQUE?

- **DISTINCT:** Removes duplicate values from query results.
- **UNIQUE:** A constraint that prevents duplicate values in a column or column combination.

**Example:**
```sql
SELECT DISTINCT CITY FROM STUDENT;

CREATE TABLE STUDENT(
    EMAIL VARCHAR(100) UNIQUE
);
```

### 14. Difference between COMMIT and ROLLBACK?

- **COMMIT:** Permanently saves the current transaction.
- **ROLLBACK:** Undoes uncommitted transaction changes.

**Example:**
```sql
START TRANSACTION;

UPDATE STUDENT
SET MARKS = 90
WHERE ID = 1;

COMMIT;
```

### 15. Difference between ALTER and UPDATE?

- **ALTER:** Changes the table structure.
- **UPDATE:** Changes existing table data.

**Example:**
```sql
ALTER TABLE STUDENT
ADD EMAIL VARCHAR(100);

UPDATE STUDENT
SET EMAIL = 'payal@gmail.com'
WHERE ID = 1;
```

---

## PART 3 – Keys and Constraints (16–22)

### 16. What is a Primary Key?

**Definition:** A Primary Key uniquely identifies each record in a table. It cannot contain NULL or duplicate values.

**Example:**
```sql
CREATE TABLE STUDENT(
    ID INT PRIMARY KEY,
    NAME VARCHAR(50)
);
```

### 17. What is a Foreign Key?

**Definition:** A Foreign Key connects two tables by referencing a candidate key, usually a Primary Key, in another table.

**Example:**
```sql
CREATE TABLE DEPARTMENT(
    DEPT_ID INT PRIMARY KEY
);

CREATE TABLE EMPLOYEE(
    ID INT PRIMARY KEY,
    DEPT_ID INT,
    FOREIGN KEY(DEPT_ID)
    REFERENCES DEPARTMENT(DEPT_ID)
);
```

### 18. Difference between Primary Key and Unique Key?

| Primary Key | Unique Key |
|---|---|
| Uniquely identifies records. | Prevents duplicate values. |
| Cannot contain NULL. | NULL handling depends on DBMS. |
| Only one per table. | Multiple allowed per table. |

**Example:**
```sql
CREATE TABLE STUDENT(
    ID INT PRIMARY KEY,
    EMAIL VARCHAR(100) UNIQUE
);
```

### 19. Difference between Primary Key and Foreign Key?

| Primary Key | Foreign Key |
|---|---|
| Uniquely identifies records. | Establishes relationships. |
| Cannot be NULL. | Can contain NULL unless restricted. |
| No duplicate values. | Duplicate values are allowed. |

### 20. What are SQL Constraints?

**Definition:** Constraints are rules applied to table columns to maintain data accuracy and integrity.

**Types:** PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL, CHECK, DEFAULT.

### 21. Explain NOT NULL, UNIQUE, CHECK and DEFAULT.

| Constraint | Purpose |
|---|---|
| NOT NULL | Prevents NULL values. |
| UNIQUE | Prevents duplicate values. |
| CHECK | Validates a condition. |
| DEFAULT | Provides a default value. |

**Example:**
```sql
CREATE TABLE STUDENT(
    ID INT PRIMARY KEY,
    NAME VARCHAR(50) NOT NULL,
    EMAIL VARCHAR(100) UNIQUE,
    AGE INT CHECK(AGE >= 18),
    CITY VARCHAR(50) DEFAULT 'Pakur'
);
```

### 22. Can a table have multiple Primary Keys and Foreign Keys?

**Answer:**
- A table can have only one PRIMARY KEY constraint.
- A Primary Key can contain multiple columns (Composite Primary Key).
- A table can have multiple FOREIGN KEY constraints.

**Example:**
```sql
CREATE TABLE STUDENT(
    ID INT PRIMARY KEY,
    DEPT_ID INT,
    COURSE_ID INT,
    FOREIGN KEY(DEPT_ID) REFERENCES DEPARTMENT(DEPT_ID),
    FOREIGN KEY(COURSE_ID) REFERENCES COURSE(COURSE_ID)
);
```

---

## PART 4 – SQL Operators and Functions (23–29)

### 23. Difference between IN and BETWEEN?

- **IN:** Checks whether a value matches any value in a list.
- **BETWEEN:** Checks whether a value falls within an inclusive range.

**Example:**
```sql
SELECT * FROM STUDENT
WHERE CITY IN ('Delhi', 'Ranchi');

SELECT * FROM STUDENT
WHERE MARKS BETWEEN 60 AND 90;
```

### 24. What is the LIKE Operator?

**Definition:** LIKE is used for pattern matching in SQL.

- `%` represents zero or more characters.
- `_` represents exactly one character.

**Example:**
```sql
SELECT * FROM STUDENT
WHERE NAME LIKE 'P%';

SELECT * FROM STUDENT
WHERE NAME LIKE '_a%';
```

### 25. Difference between AND, OR and NOT?

- **AND:** All conditions must be true.
- **OR:** At least one condition must be true.
- **NOT:** Reverses a condition.

**Example:**
```sql
SELECT * FROM STUDENT
WHERE AGE > 18 AND MARKS > 70;

SELECT * FROM STUDENT
WHERE CITY = 'Ranchi' OR CITY = 'Delhi';

SELECT * FROM STUDENT
WHERE NOT CITY = 'Delhi';
```

### 26. What are Aggregate Functions?

**Definition:** Aggregate functions perform calculations on multiple rows and return a single result per group.

**Examples:** COUNT(), SUM(), AVG(), MIN(), MAX().

```sql
SELECT COUNT(*) FROM STUDENT;
SELECT SUM(MARKS) FROM STUDENT;
SELECT AVG(MARKS) FROM STUDENT;
```

### 27. Explain COUNT(), SUM(), AVG(), MIN() and MAX().

| Function | Purpose |
|---|---|
| COUNT() | Counts rows or non-NULL values. |
| SUM() | Calculates total. |
| AVG() | Calculates average. |
| MIN() | Returns minimum value. |
| MAX() | Returns maximum value. |

**Example:**
```sql
SELECT
COUNT(*) AS TOTAL,
SUM(SALARY) AS TOTAL_SALARY,
AVG(SALARY) AS AVG_SALARY,
MIN(SALARY) AS MIN_SALARY,
MAX(SALARY) AS MAX_SALARY
FROM EMPLOYEE;
```

### 28. Difference between COUNT(*) and COUNT(column_name)?

- **COUNT(*):** Counts all rows.
- **COUNT(column_name):** Counts only non-NULL values in that column.

**Example:**
```sql
SELECT COUNT(*) FROM STUDENT;

SELECT COUNT(EMAIL) FROM STUDENT;
```

### 29. How do you handle NULL values using IFNULL() and COALESCE()?

- **IFNULL():** Returns an alternative value if the expression is NULL (MySQL).
- **COALESCE():** Returns the first non-NULL value from a list.

**Example:**
```sql
SELECT IFNULL(SALARY, 0)
FROM EMPLOYEE;

SELECT COALESCE(PHONE, EMAIL, 'Not Available')
FROM STUDENT;
```

---

## PART 5 – Joins (30–36)

### 30. What is a JOIN in SQL?

**Definition:** JOIN combines records from two or more tables using related columns.

**Example:**
```sql
SELECT *
FROM EMPLOYEE E
INNER JOIN DEPARTMENT D
ON E.DEPT_ID = D.DEPT_ID;
```

### 31. What is INNER JOIN?

**Definition:** Returns only matching records from both tables.

**Example:**
```sql
SELECT E.NAME, D.DEPT_NAME
FROM EMPLOYEE E
INNER JOIN DEPARTMENT D
ON E.DEPT_ID = D.DEPT_ID;
```

### 32. What is LEFT JOIN?

**Definition:** Returns all records from the left table and matching records from the right table. Unmatched right-side values become NULL.

**Example:**
```sql
SELECT E.NAME, D.DEPT_NAME
FROM EMPLOYEE E
LEFT JOIN DEPARTMENT D
ON E.DEPT_ID = D.DEPT_ID;
```

### 33. What is RIGHT JOIN?

**Definition:** Returns all records from the right table and matching records from the left table.

**Example:**
```sql
SELECT E.NAME, D.DEPT_NAME
FROM EMPLOYEE E
RIGHT JOIN DEPARTMENT D
ON E.DEPT_ID = D.DEPT_ID;
```

### 34. What is FULL OUTER JOIN?

**Definition:** Returns matching and non-matching records from both tables.

**Example:**
```sql
SELECT *
FROM EMPLOYEE E
LEFT JOIN DEPARTMENT D
ON E.DEPT_ID = D.DEPT_ID

UNION

SELECT *
FROM EMPLOYEE E
RIGHT JOIN DEPARTMENT D
ON E.DEPT_ID = D.DEPT_ID;
```

*Note: MySQL does not directly support FULL OUTER JOIN. UNION of LEFT and RIGHT JOIN can simulate it.*

### 35. What is SELF JOIN?

**Definition:** SELF JOIN joins a table with itself.

**Example:**
```sql
SELECT E.NAME AS EMPLOYEE,
       M.NAME AS MANAGER
FROM EMPLOYEE E
JOIN EMPLOYEE M
ON E.MANAGER_ID = M.ID;
```

### 36. Difference between INNER JOIN and LEFT JOIN?

| INNER JOIN | LEFT JOIN |
|---|---|
| Returns matching records only. | Returns all left-table records. |
| Excludes unmatched records. | Includes unmatched left records. |
| Used for matching data. | Used when all left records are needed. |

---

## PART 6 – Subqueries and Grouping (37–42)

### 37. What is a Subquery?

**Definition:** A Subquery is a query written inside another SQL query.

**Example:**
```sql
SELECT *
FROM EMPLOYEE
WHERE SALARY > (
    SELECT AVG(SALARY)
    FROM EMPLOYEE
);
```

### 38. Difference between JOIN and Subquery?

| JOIN | Subquery |
|---|---|
| Combines data from multiple tables. | Uses one query inside another. |
| Often useful for retrieving related columns. | Useful for filtering or calculating values. |

**Example:**
```sql
-- JOIN
SELECT E.NAME, D.DEPT_NAME
FROM EMPLOYEE E
JOIN DEPARTMENT D
ON E.DEPT_ID = D.DEPT_ID;

-- SUBQUERY
SELECT *
FROM EMPLOYEE
WHERE SALARY > (SELECT AVG(SALARY) FROM EMPLOYEE);
```

### 39. What is a Correlated Subquery?

**Definition:** A Correlated Subquery depends on the outer query and executes logically for each outer row.

**Example:**
```sql
SELECT E1.*
FROM EMPLOYEE E1
WHERE SALARY > (
    SELECT AVG(E2.SALARY)
    FROM EMPLOYEE E2
    WHERE E2.DEPT_ID = E1.DEPT_ID
);
```

### 40. Difference between WHERE and HAVING with GROUP BY?

- WHERE filters rows before grouping.
- HAVING filters groups after grouping.

**Example:**
```sql
SELECT DEPT_ID, AVG(SALARY)
FROM EMPLOYEE
WHERE SALARY > 10000
GROUP BY DEPT_ID
HAVING AVG(SALARY) > 30000;
```

### 41. Difference between UNION and UNION ALL?

| UNION | UNION ALL |
|---|---|
| Combines query results. | Combines query results. |
| Removes duplicate rows. | Keeps duplicate rows. |
| Usually requires extra work to remove duplicates. | Usually faster when duplicates need to be retained. |

**Example:**
```sql
SELECT CITY FROM STUDENT
UNION
SELECT CITY FROM EMPLOYEE;

SELECT CITY FROM STUDENT
UNION ALL
SELECT CITY FROM EMPLOYEE;
```

### 42. Difference between IN and EXISTS?

| IN | EXISTS |
|---|---|
| Checks whether a value matches a result in a list or subquery. | Checks whether a subquery returns any row. |
| Compares values. | Checks row existence. |

**Example:**
```sql
SELECT *
FROM EMPLOYEE
WHERE DEPT_ID IN (
    SELECT DEPT_ID FROM DEPARTMENT
);
```

```sql
SELECT *
FROM DEPARTMENT D
WHERE EXISTS (
    SELECT 1
    FROM EMPLOYEE E
    WHERE E.DEPT_ID = D.DEPT_ID
);
```

---

## PART 7 – Practical SQL Queries (43–48)

Assume the following table:

**EMPLOYEE**

| ID | NAME | SALARY | DEPARTMENT |
|---|---|---:|---|
| 1 | Rahul | 30000 | IT |
| 2 | Payal | 40000 | HR |
| 3 | Aman | 50000 | IT |
| 4 | Priya | 60000 | HR |
| 5 | Ravi | 40000 | IT |

### 43. Find the Second-Highest Salary.

```sql
SELECT MAX(SALARY)
FROM EMPLOYEE
WHERE SALARY < (
    SELECT MAX(SALARY)
    FROM EMPLOYEE
);
```

**Output:** 50000

### 44. Find the Highest Salary in Each Department.

```sql
SELECT DEPARTMENT, MAX(SALARY)
FROM EMPLOYEE
GROUP BY DEPARTMENT;
```

**Output:**

| DEPARTMENT | MAX(SALARY) |
|---|---:|
| IT | 50000 |
| HR | 60000 |

### 45. Find Duplicate Records in a Table.

```sql
SELECT NAME, COUNT(*)
FROM EMPLOYEE
GROUP BY NAME
HAVING COUNT(*) > 1;
```

**Explanation:** Groups identical names and displays those occurring more than once.

### 46. Find Employees Whose Salary Is NULL.

```sql
SELECT *
FROM EMPLOYEE
WHERE SALARY IS NULL;
```

**Explanation:** Returns employees whose salary is missing.

### 47. Display the Top 5 Highest-Paid Employees.

```sql
SELECT *
FROM EMPLOYEE
ORDER BY SALARY DESC
LIMIT 5;
```

**Explanation:** Displays the five highest-paid employees.

### 48. Find Employees Earning More Than the Average Salary.

```sql
SELECT *
FROM EMPLOYEE
WHERE SALARY > (
    SELECT AVG(SALARY)
    FROM EMPLOYEE
);
```

**Explanation:** Displays employees whose salary is greater than the overall average salary.

---

## PART 8 – Additional Important Concepts (49–50)

### 49. What is an Index in SQL?

**Definition:** An Index is a database object that helps retrieve records faster.

**Advantages:**
- Faster data searching.
- Improves SELECT query performance.

**Disadvantages:**
- Requires additional storage.
- Can slow down INSERT, UPDATE and DELETE operations.

**Example:**
```sql
CREATE INDEX idx_name
ON EMPLOYEE(NAME);
```

### 50. What is a View in SQL?

**Definition:** A View is a virtual table based on the result of an SQL query.

**Example:**
```sql
CREATE VIEW IT_EMPLOYEES AS
SELECT *
FROM EMPLOYEE
WHERE DEPARTMENT = 'IT';
```

To access the View:
```sql
SELECT * FROM IT_EMPLOYEES;
```

**Difference between View and Table:**

| View | Table |
|---|---|
| Virtual table based on a query. | Stores data in database. |
| Usually does not store the result data itself. | Stores actual records. |
| Created using CREATE VIEW. | Created using CREATE TABLE. |

---






# SQL – Important Difference Between Questions
### BCA Fresher | TCS | Wipro | Infosys | Accenture | Cognizant

## Priority 1 – Must Prepare

### 1. DBMS vs RDBMS

| DBMS | RDBMS |
|---|---|
| Manages databases. | Manages relational databases. |
| Relationships may not be enforced. | Supports relationships using keys. |
| Example: File-based systems. | Example: MySQL, Oracle. |

### 2. SQL vs MySQL

| SQL | MySQL |
|---|---|
| SQL is a query language. | MySQL is an RDBMS. |
| Used to communicate with databases. | Used to store and manage data. |

### 3. CHAR vs VARCHAR

| CHAR | VARCHAR |
|---|---|
| Fixed-length string. | Variable-length string. |
| Uses fixed storage length. | Uses storage based on actual data length, plus overhead. |
| Suitable for fixed-size data. | Suitable for variable-size data. |

### 4. DELETE vs DROP vs TRUNCATE

| DELETE | DROP | TRUNCATE |
|---|---|---|
| Deletes rows. | Deletes the entire table. | Removes all rows. |
| Supports WHERE. | Does not support WHERE. | Does not support WHERE. |
| Table remains. | Table is removed. | Table remains. |
| DML | DDL | DDL |

### 5. DDL vs DML

| DDL | DML |
|---|---|
| Defines database structure. | Modifies table data. |
| CREATE, ALTER, DROP. | INSERT, UPDATE, DELETE. |

### 6. WHERE vs HAVING

| WHERE | HAVING |
|---|---|
| Filters individual rows. | Filters groups. |
| Applied before GROUP BY. | Applied after GROUP BY. |
| Cannot directly use aggregate conditions. | Can use aggregate functions. |

### 7. GROUP BY vs ORDER BY

| GROUP BY | ORDER BY |
|---|---|
| Groups similar records. | Sorts records. |
| Commonly used with aggregate functions. | Uses ASC or DESC. |

### 8. Primary Key vs Foreign Key

| Primary Key | Foreign Key |
|---|---|
| Uniquely identifies each row. | Establishes relationships between tables. |
| Cannot contain NULL. | Can contain NULL unless restricted. |
| Does not allow duplicates. | Allows duplicate values. |

### 9. Primary Key vs Unique Key

| Primary Key | Unique Key |
|---|---|
| Uniquely identifies records. | Prevents duplicate values. |
| Cannot contain NULL. | NULL handling depends on DBMS. |
| One PRIMARY KEY constraint per table. | Multiple UNIQUE constraints allowed. |

### 10. INNER JOIN vs LEFT JOIN

| INNER JOIN | LEFT JOIN |
|---|---|
| Returns matching records only. | Returns all left-table records. |
| Excludes unmatched records. | Unmatched right-side values become NULL. |

### 11. LEFT JOIN vs RIGHT JOIN

| LEFT JOIN | RIGHT JOIN |
|---|---|
| Returns all left-table records. | Returns all right-table records. |
| Unmatched right values become NULL. | Unmatched left values become NULL. |

### 12. UNION vs UNION ALL

| UNION | UNION ALL |
|---|---|
| Combines query results. | Combines query results. |
| Removes duplicate rows. | Retains duplicate rows. |
| Usually requires extra processing. | Usually requires less processing. |

### 13. COUNT(*) vs COUNT(Column)

| COUNT(*) | COUNT(Column) |
|---|---|
| Counts all rows. | Counts non-NULL values. |
| Includes rows containing NULL. | Excludes NULL values in that column. |

### 14. JOIN vs Subquery

| JOIN | Subquery |
|---|---|
| Combines data from multiple tables. | Uses a query inside another query. |
| Useful for retrieving related columns. | Useful for filtering and calculations. |

### 15. IN vs EXISTS

| IN | EXISTS |
|---|---|
| Checks whether a value matches a list or subquery result. | Checks whether a subquery returns any row. |
| Value comparison. | Existence check. |

---

## Priority 2 – Important

### 16. ALTER vs UPDATE

| ALTER | UPDATE |
|---|---|
| Changes table structure. | Changes existing records. |
| DDL | DML |

### 17. COMMIT vs ROLLBACK

| COMMIT | ROLLBACK |
|---|---|
| Saves transaction changes. | Undoes uncommitted changes. |
| Makes changes permanent. | Reverts transaction changes. |

### 18. Candidate Key vs Super Key

| Candidate Key | Super Key |
|---|---|
| Minimal set of columns that uniquely identifies a row. | Any set of columns that uniquely identifies a row. |
| Contains no unnecessary attributes. | May contain extra attributes. |

### 19. WHERE vs ON

| WHERE | ON |
|---|---|
| Filters query results. | Specifies the JOIN matching condition. |
| Used to filter rows. | Used to connect tables. |

### 20. NULL vs ZERO vs BLANK

| NULL | ZERO | BLANK |
|---|---|---|
| Missing or unknown value. | Numeric value 0. | Empty string (''). |
| Not equal to zero. | Actual number. | A string value. |

### 21. Correlated vs Non-Correlated Subquery

| Correlated | Non-Correlated |
|---|---|
| Depends on the outer query. | Independent of the outer query. |
| Logically evaluated for outer rows. | Can execute independently. |

### 22. View vs Table

| View | Table |
|---|---|
| Virtual table based on a query. | Stores actual records. |
| Usually does not store result data itself. | Stores data physically. |
| Created using CREATE VIEW. | Created using CREATE TABLE. |

### 23. Stored Procedure vs Function

| Stored Procedure | Function |
|---|---|
| Performs a set of operations. | Computes and returns a value. |
| Can return result sets or output parameters. | Returns a value. |
| Called using CALL in MySQL. | Can be used in SQL expressions when permitted. |

### 24. Normalization vs Denormalization

| Normalization | Denormalization |
|---|---|
| Reduces data redundancy. | Intentionally introduces redundancy. |
| Improves data integrity. | Can improve read performance. |
| Uses related tables. | May combine or duplicate data. |

### 25. RANK vs DENSE_RANK vs ROW_NUMBER

| RANK() | DENSE_RANK() | ROW_NUMBER() |
|---|---|---|
| Same rank for ties. | Same rank for ties. | Unique sequential numbers. |
| Skips subsequent ranks. | Does not skip ranks. | Does not skip numbers. |

**Example:**

| Salary | RANK | DENSE_RANK | ROW_NUMBER |
|---:|---:|---:|---:|
| 50000 | 1 | 1 | 1 |
| 50000 | 1 | 1 | 2 |
| 40000 | 3 | 2 | 3 |
| 30000 | 4 | 3 | 4 |

---

## Final Revision Priority

- Priority 1: Prepare all 15 thoroughly.
- Priority 2: Understand all 10 with examples.
- Practise SQL queries in MySQL Workbench.
- Explain every difference in your own words.

## Important Note

These 50 questions cover the foundational SQL concepts for BCA fresher interviews. Also practise writing queries independently in MySQL Workbench instead of only memorizing answers.

**Target Companies:** TCS | Wipro | Infosys | Accenture | Cognizant | Capgemini | Deloitte

**Goal:** Understand the concept, explain it confidently and write the query without help.
