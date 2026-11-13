# DBMS – Important Interview Questions & Answers

**Target Companies:** TCS, TCS Ignite, Wipro, Infosys, Accenture, Cognizant & Deloitte.

## 🔴 Priority 1 – Most Important ⭐⭐⭐

### 1. ⭐⭐⭐ What is DBMS?

DBMS (Database Management System) is software used to store, manage, retrieve and update data efficiently.

**Example:** A college uses DBMS to manage student records, marks and attendance.

### 2. ⭐⭐⭐ What is RDBMS?

RDBMS (Relational Database Management System) is a type of DBMS that stores data in tables and establishes relationships between them.

**Example:** A bank maintains separate but related tables for customers and their accounts.

### 3. ⭐⭐⭐ What is the difference between DBMS and RDBMS?

| DBMS | RDBMS |
|---|---|
| Manages databases. | Manages relational databases. |
| May use different data models. | Uses tables to organize data. |
| Relationships are not essential. | Supports relationships between tables. |

**Example:** A simple document database vs. a banking database with related customer and account tables.

### 4. ⭐⭐ What are the advantages and disadvantages of DBMS?

**Advantages:**
- Reduces data duplication.
- Improves data security.
- Maintains data consistency.
- Makes data management easier.

**Disadvantages:**
- Can be expensive.
- Requires maintenance.
- Needs technical knowledge.
- Uses system resources.

**Example:** A college can manage thousands of student records in one database instead of separate registers.

### 5. ⭐⭐⭐ What is a Database?

A database is an organized collection of data that can be easily accessed, managed and updated.

**Example:** A college database containing student names, roll numbers, marks and attendance.

### 6. ⭐⭐ What is a Relational Database?

A relational database stores data in tables and connects related information using common columns.

**Example:** A Student table and a Department table connected through Department ID.

### 7. ⭐⭐⭐ What is a Table, Tuple and Attribute?

- **Table:** Collection of related data.
- **Tuple:** A single row in a table.
- **Attribute:** A column in a table.

**Example:** In a Student table:
- Table: Student
- Tuple: One student's complete record.
- Attribute: Name, Roll_No, Age.

### 8. ⭐⭐⭐ What is NULL?

NULL represents a missing, unknown or unavailable value in a database. It is different from zero or an empty string.

**Example:** If a student's phone number is not provided, the Phone_Number field contains NULL.

### 9. ⭐⭐⭐ What is Normalization?

Normalization is the process of organizing database tables to reduce data duplication and improve data consistency.

**Example:** Instead of storing department details repeatedly for every student, maintain a separate Department table.

### 10. ⭐⭐⭐ Explain 1NF, 2NF and 3NF.

- **1NF:** Each column contains atomic (single) values.
- **2NF:** Must be in 1NF and have no partial dependency on a composite key.
- **3NF:** Must be in 2NF and have no transitive dependency.

**Example:** Store multiple phone numbers of a student in separate rows rather than putting them together in one cell.

### 11. ⭐⭐ What is Data Redundancy?

Data redundancy means unnecessary duplication of the same data in multiple places.

**Example:** Storing the same student's address repeatedly in multiple records.

### 12. ⭐⭐ What is Data Integrity?

Data integrity means maintaining the accuracy, consistency and reliability of data in a database.

**Example:** A student's age should not be stored as a negative number.

### 13. ⭐⭐⭐ What is the difference between DBMS and File System?

| DBMS | File System |
|---|---|
| Manages data systematically. | Stores data in files and folders. |
| Provides better data security. | Has limited data security. |
| Reduces data duplication. | May contain duplicate data. |
| Supports efficient data retrieval. | Searching can be difficult. |

**Example:** Managing student records using MySQL instead of separate text files.

---

## 🟡 Priority 2 – Important ⭐⭐

### 14. ⭐⭐ What is an Entity?

An entity is a real-world object about which data is stored.

**Example:** Student, Teacher, Employee and Customer.

### 15. ⭐⭐ What is an Attribute?

An attribute is a property or characteristic of an entity.

**Example:** A Student entity has attributes such as Name, Age, Roll Number and Address.

### 16. ⭐⭐⭐ What is an ER Diagram?

An Entity Relationship Diagram (ER Diagram) is a visual representation of entities and their relationships in a database.

**Example:** A diagram showing the relationship between Students and Courses.

### 17. ⭐⭐⭐ What are the different types of relationships in DBMS?

1. **One-to-One (1:1):** One person has one passport.
2. **One-to-Many (1:M):** One department has many employees.
3. **Many-to-Many (M:N):** Many students can enroll in many courses.

### 18. ⭐⭐ What is Cardinality in DBMS?

Cardinality defines the number of possible relationships between entities in a database.

**Example:** One teacher can teach many students (One-to-Many).

### 19. ⭐⭐ What is Database Schema?

A database schema is the logical structure or design of a database. It defines tables, columns and relationships.

**Example:** A college database schema defines Student, Teacher and Course tables.

### 20. ⭐ What is Database Instance?

A database instance is the actual data stored in a database at a particular moment.

**Example:** The current student records stored in a college database.

### 21. ⭐⭐ What is Data Independence?

Data independence means changing the database structure at one level without affecting the next higher level.

**Example:** Changing physical data storage without changing the application that accesses it.

### 22. ⭐⭐⭐ What is Data Abstraction?

Data abstraction means hiding unnecessary database details from users and showing only the required information.

**Example:** A student can see marks on a college portal without knowing how the data is stored internally.

### 23. ⭐⭐⭐ What are the three levels of Data Abstraction?

1. **Physical Level:** How data is actually stored.
2. **Logical Level:** What data is stored and how tables are related.
3. **View Level:** What information users can see.

**Example:** A bank customer sees account balance, while the database administrator manages the internal database structure.

### 24. ⭐ What is Denormalization?

Denormalization is the process of combining tables or adding duplicate data to improve data retrieval performance.

**Example:** A shopping website stores frequently accessed product details together to reduce repeated table lookups.

### 25. ⭐⭐ What is Functional Dependency?

Functional dependency means one attribute determines the value of another attribute.

**Example:** A Student_ID determines the student's name in a student table.

### 26. ⭐⭐ What is the difference between Centralized and Distributed Database?

| Centralized Database | Distributed Database |
|---|---|
| Data is stored at one central location. | Data is stored across multiple locations. |
| Easier to manage centrally. | Requires coordination between locations. |
| Depends on the central system. | Provides access across locations. |

**Example:** A small college using one central database vs. a bank maintaining databases across multiple branches.

### 27. ⭐ What is Data Dictionary?

A data dictionary is a collection of information about database elements, such as table names, column names, data types and constraints.

**Example:** Information showing that Student_ID is an integer and Student_Name is a VARCHAR column.

### 28. ⭐⭐ What is Database Security?

Database security refers to protecting database information from unauthorized access, misuse or modification.

**Example:** A banking application uses passwords and access permissions to protect customer account information.

---

## 📌 Preparation Strategy

- ⭐⭐⭐ Highest Priority – Prepare thoroughly with examples.
- ⭐⭐ Important – Understand definitions and differences.
- ⭐ Additional – Revise if time permits.

**Interview Tip:** Explain every answer using a definition followed by one real-world example. Keep your answers within 30–45 seconds.
