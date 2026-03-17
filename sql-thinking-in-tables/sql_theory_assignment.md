SQL Theory Assignment
Understanding Relational Databases in AI Systems
1. Why Databases Are Important in Real-World AI Systems

Databases are essential in real-world AI systems because AI models rely on large volumes of structured and organized data. Databases store, manage, and retrieve this data efficiently so that AI models can use it for training, analysis, and prediction.

Without databases, handling millions of records would become slow, inconsistent, and difficult to maintain.

Types of Data Stored in Databases

Some common types of data stored in databases include:

User information (name, email, age)

Transaction records

Product details

Sensor or IoT data

Logs from applications

Medical records

Financial data

Example

A recommendation system like Netflix or Amazon stores:

User_ID	Movie_Watched	Rating
101	Inception	5
102	Avatar	4

The AI system analyzes this stored data to recommend new movies or products.

Why Structured Storage is Necessary

Structured storage is important because:

It allows fast querying and retrieval

Data becomes consistent and organized

AI pipelines can clean and process data easily

Reduces redundancy and errors

For example, structured tables allow AI systems to quickly answer queries like:

"Which products are most purchased?"

"Which users are most active?"

2. Relational Database Mental Model

A relational database organizes data in tables. These tables represent real-world entities.

Table

A table is a structured format that stores related data.

Example: Employees table

Employee_ID	Name	Department	Salary
1	Amit	IT	600000
2	Neha	HR	500000
Rows

Rows represent individual records.

Example:

Employee_ID: 1
Name: Amit
Department: IT
Salary: 600000

Each row corresponds to one entity instance.

Columns

Columns represent attributes or properties of an entity.

Example:

Employee_ID

Name

Department

Salary

Why Each Table Should Represent a Single Entity

Each table should represent a single entity to keep data organized and reduce duplication.

Example entities:

Employees

Departments

Orders

Customers

If multiple entities are mixed in one table, the database becomes hard to maintain and inefficient to query.

3. Primary Key

A primary key is a column (or set of columns) that uniquely identifies each row in a table.

Example:

Employee_ID	Name	Department
1	Amit	IT
2	Neha	HR

Here, Employee_ID is the primary key.

Properties of a Primary Key

Unique
No two rows can have the same primary key.

Example (invalid):

Employee_ID	Name
1	Amit
1	Rahul

This would create confusion.

Non-Null
A primary key must always have a value.

Example (invalid):

Employee_ID	Name
NULL	Amit

If the key is null, the row cannot be uniquely identified.

Why Primary Keys Are Important

Primary keys help:

Identify records uniquely

Prevent duplicate data

Enable relationships between tables

Improve query performance

4. Database Schema

A database schema defines the structure of a database.

It describes:

Table names

Column names

Data types

Constraints (Primary key, foreign key)

Relationships between tables

Example Schema

Table: Employees

Column	Type
Employee_ID	INT (Primary Key)
Name	VARCHAR
Department_ID	INT
Salary	FLOAT
Why Schemas Are Important

Schemas ensure:

Consistent data structure

Data integrity

Easier maintenance

Better collaboration among developers

For example, if everyone follows the same schema, the database remains predictable and well organized.

5. Relationships Between Tables

In relational databases, tables are connected using relationships.

This avoids repeating the same data multiple times.

Example
Users Table
User_ID	Name
1	Amit
2	Neha
Orders Table
Order_ID	User_ID	Product
101	1	Laptop
102	2	Phone

Here:

User_ID in the Orders table is a foreign key.

Foreign Key

A foreign key is a column that refers to the primary key of another table.

Example:

Orders.User_ID → Users.User_ID

This creates a relationship between users and their orders.

Why Relationships Are Important

Relationships help:

Maintain data integrity

Avoid duplication

Link related data across tables

Example query:

SELECT Users.Name, Orders.Product
FROM Users
JOIN Orders
ON Users.User_ID = Orders.User_ID;

This query shows which user bought which product.

Conclusion

Relational databases are a fundamental component of modern AI systems. They provide structured storage for large datasets, ensure data consistency through schemas and keys, and allow efficient data retrieval through relationships between tables. Understanding tables, primary keys, schemas, and relationships is essential for building reliable data pipelines and AI applications.