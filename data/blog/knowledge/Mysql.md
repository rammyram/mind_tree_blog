---
title: Mysql
date: 2021-12-30
tags: ['mysql']
draft: false
summary: 
---
## Key Ideas to cover 

- Scalability 
- Availability 
- Consistency
- Flexibility 
- How to do MySQL query optimizations ?
- Analyze MySQL query performance ?  
- How to analyze MySQL DB performance + Monitor performance + Reporting tools  ?
- MySQL with Redis 
- Can MySQL handle multi cluster / nodes ? 
- Security 
- Transactions 
- Event Schedulers
- Views 
- Procedures 
- Functions 
- Indexing
- Variables 
- Cursors
- Flow Control 
- Triggers 


## SQL terms 

| Term                            | Meaning                                                                                                                                                                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQL Parsing                     | Parsing a query is the process by which the optimizer component determines the possible ways to run this query and choose the best optimal way.                                                                   |
| Transaction                     | A logical unit of work that contains one or more SQL statements.    The effects of all SQL statements in a transaction can be either applied or rolled back                                                       |
| Character-set and Collation-set | Character-set defines the character encoding to use in a database ex:latin    Collation is a set of rules that define how to compare and sort character strings    Collate changes based on caracter-set used |
| Database seeding                | Database seeding is the initial seeding of a database with data. Seeding a database is a process in which an initial set of data is provided to a database when it is being installed.                            |
| Database Engine                 | A database engine is the underlying software component that a database management system uses to create, read, update and delete data from a database.                                                            |


## MYSQL vs MSSQL

| Attribute            | MySQL                                                                                                                                                               | MsSQL                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Native compatibility | runs smoothly on any OS                                                                                                                                             | designed for windows but can work with other (limitations exist)              |
| Custom Engines       | MyISAM, InnoDB etc                                                                                                                                                  | Does not allow other engines                                                  |
| Cost                 | Free & open source                                                                                                                                                  | Costly and licensed                                                           |
| Binary collections   | Allows data manipulation while running    Allow any process to access or manipulate binaries                                                                      | Not allowed, so more secure                                                   |
| Backup               | Can only backup data by extracting as SQL queries    Need to block DB while backup    Data restoration is time consuming, since we need to execute many queries | Doesn't block DB    Allows users to back up and restore with minimal effort |
| Stop Query Execution | Doesn't let user kill or cancel once query starts                                                                                                                   | Can truncate query while it's running without having to kill the process.                                                                              |


## Query Optimizations :

- The developer must consider the future usage of the tables in terms of the number of records, the table size on disk, the different variations of queries to be performed, and must create the appropriate indexes while designing the table. The developer is responsible for the proper index creation, not the system administrator, the DBA, or any other consultant.

| Optimization                           |                                                                                                                                                                                                                                                                                     |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Small tables                           | - No need to create index    - Small tables or less frequently updated tables like countries, clients list can be cached to in memory DB and updated at intervals from DB                                                                                                     |
| Primary key                            | - Use unsigned INT which gives you nearly (4.29 billion values)    - Do not use UUID / GUID since they compare much slower than INT and consume more space                                                                                                                        |
| Avoid redundant indexes                | - Do not include primary key in custom indexes as its already indexed    - Avoid multiple indexes indexing the same column, its useless --> Example :     - CREATE INDEX idx1 ON users (email)    - CREATE INDEX idx2 ON users (email, pass)                                  |
| Over indexing                          | - Do not create too many indexes to cover different cases for where conditionals.    - Every index created will impact CRUD speeds as index trees needs to be updated and balanced.    - Indexes are loaded into memory and therefore consume more memory.                      |
| Index from start is better             | - Once a table becomes huge, if we wanna introduce index on a table remember that indexing is done in a transaction and so table does not allow any changes while index is being created    - So it could impact production, so go to maintenance mode before indexing big tables |
| Column order matters in Compound index | - Compound Index : Means index with more than one column    - Column order matters, choose wrong order could cause full table scan    - Priorities the columns that sort the data best                                                                                          |
| Never use * -> Get all fields          | - Lazily using * even though all fields are not needed could cause more reads and nullify indexes advantage.                                                                                                                                                                                                                                                                                     |


## Views : 

| Use             | Info                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------ |
| Simplicity      | Views can be used to hide complex queries.                                                       |
| Security        | View can hide some important information from end user by creating view on some selected columns |
| Security        | Secure table to change the structure of it by using VIEW.                                        |
| Redundancy      | Reduce redundant code in every procedures/query by using a common view.                          |
| Calculation     | All the calculations can be done once in view query.                                             |
| Meaningful Name | Table may have name for id like tbl_org_emp_id which can alias like [Employee No] or some meaningful name.                                                                                                 |


## Roles :
- Role is a collection of privileges
- Roles with certain privileges are assigned to users based on their requirement. 
- For example developers are given full privilege roles.  
- We can control access to users, such as
	- Read 
	- Write 
	- Delete 
	- Update 
	- Databases 
	- Tables 
- [Detailed SQL query on creating and assigning roles](https://www.mysqltutorial.org/mysql-roles/)

```

	Privilleges --> Roles --> Users 

```


## MySQL Architecture 

![/static/images/Others/mysql_architecture.png](/static/images/Others/mysql_architecture.png)


- Layer 1 : BASIC CONNECTION LAYER
	- Basic Client / Server tools 
	- Connection handling 
	- Authentication
	- Security etc
	
- Layer 2 : SERVER LEVEL LAYER
	- Query parsing 
	- Query Analysis 
	- Optimization 
	- Caching 
	- Built in function 
	- Procedure 
	- Triggers 
	- Views 

- Layer 3 : STORAGE ENGINE LAYER
	- Storage engines 
	- Responsible for storing and retrieving all data store. 
	- Server communicates with them through storage engine API 
	- Example : InnoDB, MyISAM 
	

### Connection management 


![/static/images/Others/mysql_connection.png](/static/images/Others/mysql_connection.png)

- Each connection is allocated a thread and all queries made by that connection executes with in that thread. 
- Threads are cached / destroyed once connection ends. 


### Optimization & Execution 

- Parse query to a tree 
- Apply variety of optimization's 
	- Rewrite query 
	- Find the order in which to read the tables used in query 
	- Choose indexes to use 
	- Ask storage engines corresponding to those tables about cost of certain operations. 
	- Ask storage engines on statistics of table. 
	- Finally choose the best way to execute query 

- Query Cache 
	- Before even parsing the query sql first checks if similar SELECT query exist in cache 
	- If it does, it simply sends cached results back to client. 

- Analyze MySQL optimizer decisions 
	- SQL Query analyzer helps to analyze the query and understand what steps  the SQL optimizer took to give the result. 
	- How many rows the MySQL has to inspect to get you the result. 
	- Did MySQL use any available indexes to filter rows and reduce the rows it has to through. 
	- We can also use EXPLAIN to understand which tables & columns are worth indexing. 
	- [EXPLAIN Command output is perfectly explained](https://www.eversql.com/mysql-explain-example-explaining-mysql-explain-using-stackoverflow-data/)


### Concurrency 

- In Database systems there are many problems that need's to be handled to be able to concurrently run multiple queries that access the same data at the same time. 

- Examples : 
	- Multiple queries trying to write to same table at the same time.
	- What happens when a user tries to delete/insert data when a read is happening --> User get inconsistent stale result. 

- LOCKING SYSTEM ( Solution to concurrency ) : 
	- Shared Locks 
	- Exclusive Locks or Read Locks 
	- Write Locks 
	
| Lock Type  | Use                                                                                                                                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Read Lock  | - Read locks on a resource are shared    - Many clients may read from a resource at the same time and not interfere with each other                                                                             |
| Write Lock | - Write locks block both read locks and other write locks    - Because the only safe policy is to have a single client writing to the resource at given time and to prevent all reads when a client is writing. |

- Lock Granularity : 
	- The more precise you are in locking exactly only the data that's being modified the more concurrency you can provide. 
		- EXAMPLE : 
			- Locking entire table blocks thousands of queries trying to access the same table. 
			- Locking a row alone is better for concurrency. 
	- Locking system is a comprise between  **Lock Overhead **  and   **Data safety** and **Concurrency**. 

| Lock Granularity    | OverHead | Concurrency | Engine          |
| ------------------- | -------- | ----------- | --------------- |
| Table lock          | Lowest   | Lowest      | MyISAM, Memory  |
| Row lock            | High     | High        | NDB Cluster     |
| Row level with MVCC | Highest  | Highest     | InnoDB, SolidDB |


### Transactions 

- Let's say to get a job done, like a bank transaction. You need to update or insert around 3 tables. 
- It requires around 3 queries. 
- Now we need to be able to rollback if at least one of the query fails for any reason. 
- This is why we need transactions. 
- [Query](https://www.mysqltutorial.org/mysql-transaction.aspx)
```

	Given a set of queries in a transaction, Its either implement ALL or NONE 

```

- All transaction processing system must be ACID compliant --> Atomicity, Consistency, Isolation, Durability 
- Example Storage engines : InnoDB, SolidDB

- Dead Locks :
	- A deadlock_ is when two or more transactions are mutually holding and requesting locks on the same resources, creating a cycle of dependencies.
	- InnoDB can detect dead locks and avoid issues. 

- Mixing Engines in transactions: 
	- Avoid using different storage engines in a transaction. 
	- Example:
		- A transaction has 2 queries accessing 2 tables.
		- Table1 uses InnoDB , While Table2 uses MyISAM
		- When transaction fail and need rollback, InnoDB table could rollback but MyISAM couldn't. 
	
	
### Storage Engines 


![/static/images/Others/mysql_paths.png](/static/images/Others/mysql_paths.png)

- MySQL server takes care of storing database schema in file system as shown above.
- The storage engine takes of storing data and their indexes. 
- To check storage engine a table uses : 

```
SHOW TABLE STATUS LIKE 'user' \G

Above command shows User table details
```

- **MYISAM** 

| Category     | MyISAM                                                  |
| ------------ | ------------------------------------------------------- |
| Features     | Default MySQL Engine                                    |
|              | Compression                                             |
|              | Spatial functions                                       |
|              | Full text indexing                                      |
|              |                                                         |
| Locking      | Table locking                                           |
|              | Allows concurrent writes while read queries are running |
| Repair       | Automatic Repair                                        |
|              | Manual Repair (Command -> myisamchk )                   |
| Data storage | Each table has 2 files, data file and index file        |

- **InnoDB** 

| Category         | InnoDB                                                                                             |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| Features         | Designed for short lived transactions                                                              |
|                  | Most popular engine for transactional storage                                                      |
|                  | Due to its performance and Auto recovery, people use this for non-transactional storage needs too. |
|                  | Allow foreign key constrain                                                                        |
|                  | Clustered indexes ( so heavy index data is split and can fit into memory)                                                                                                   |
| Storage          | Stores data in one or more data files that are known as tablespace.                                |
|                  |                                                                                                    |
| Locking          | Row Locking with MVCC                                                                              |
|                  | Provides high concurrency                                                                          |
|                  |                                                                                                    |
| Creating Indexes | Index creation is slow to compared to MyISAM                                                       |
|                  | Changes to table structure will rebuild entire table and indexes                                   |
|                  | Does not allow index compression                                                                   |


- **Memory Engine** 

| Category  | Memory Engine                                                                             |
| --------- | ----------------------------------------------------------------------------------------- |
| Features  | Used for data that needs very fast access and doesn't change                              |
|           | Orders of magnitude faster than MyISAM                                                    |
|           | Support HASH index, which are fast for lookups                                            |
|           |                                                                                           |
|           |                                                                                           |
| Storage   | Lives in memory so data will not persist after restart                                    |
|           | Since its lives in memory no I/O wait needed --> Fast                                     |
|           |                                                                                           |
| Cons      | Uses table level which gives low write concurrency                                        |
|           | Does not allow variable sized rows, so cannot use varchar                                 |
|           | Do not support TEXT or BLOB columns                                                       |
|           | Not suitable for general purpose disk based tables.                                       |
|           |                                                                                           |
| Use Cases | Good for lookup or mapping tables like postal codes, state names                          |
|           | Caching results of periodically aggregated data                                           |
|           | MySQL uses this engine for queries that need temporary table to hold intermediate results |


### Selecting right engine

- We can choose storage engines on a table by table basis. 
- It is important to think about which storage engine is appropriate for a given data at the design stage itself.  

- **Considerations** 

| Feature                        | Engine                                                                               |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| Don't require transactions     | MyISAM                                                                               |
| Need transactions              | InnoDB                                                                               |
| Concurrency                    | MyISAM : if just for read and write and operations doesn't interfere with each other |
|                                | InnoDB : When row level locking is needed and transaction compliant                  |
| Backups                        | For offline backup any storage engine is fine                                        |
|                                | For online backup with Db that has multiple engines the solution gets complicated    |
|                                | < Need to check on existing backup solutions >                                       |
| Crash Recovery                 | InnoDB is best and takes less recovery time                                          |
| Primary keys vs Secondary keys |                                                                                      |
| Number of i/o operations       |                                                                                      |
| Data size                      |                                                                                      |
|                                |                                                                                      |


### Example use cases : 

- Logging every call details in real-time applications 
	- Logging usually requires high write speeds and occasional read speeds to analyze logs.
	- MyISAM and Archive storage engines are perfect and can support thousands of write speeds per second. 

	- What happens when you try to read logs and create summary. 
		- Issues :
			- Depending on query used there's good chances that this could slow down the write speeds.  
		- **Solutions **:
			- **Using MySQL replication feature** : Where master servers for inserting logs and you can use of the cloned slaves for reading. 
			- **Merge Tables** : Adjust the application to log to table based on year month data etc. This way we have multiple tables like log_2020_01 , log_2020_02. This way we avoid heavy reads on table being written. 

- Mostly only read data :
	- MyISAM is the best choice if you don't mind what happens when MyISAM crashes. 
	-  So better use MyISAM when you are sure of how to retrieve from a crash or data in those tables isn't that important like catalog data... list of countries, pin codes, zips. 

- Order processing : 
	- Order processing requires transactional storage. 
	- InnoDB is the best choice if you need support for foreign key constraints as well. 

- Stock quotes :
	- MyISAM --> Only if using for personal stock quote analysis 
	- InnoDB   --> When providing a web service with real time quote table where thousands of clients could be trying to read and write. 


---
Status: #todo

Tags: #mysql

References: 

- [Short and concise tutorials on MYSQL + MYSQL in Python ](https://www.mysqltutorial.org/)
- [ Oreilly MYSQL ](https://www.oreilly.com/library/view/high-performance-mysql/9780596101718/ch01.html)
- [MySQL Connection handling](https://mysqlserverteam.com/mysql-connection-handling-and-scaling/)

Related:

