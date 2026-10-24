# Database Systems

Up: [[Information Technology]]

Information Technology, Database Systems. Searching text is in [[Full-Text Search]] and files are in [[Object Storage]], both under System Design, and [[Redis]] is under Software.

**A database system stores data so many users can read and change it at once without losing or corrupting it. These notes cover the relational model and its schema, the transactions and locks that keep concurrent changes safe, the indexes that make reads fast, and splitting or copying data across machines.**

- [[Relational Database]]: A relational database stores data as tables of rows and columns, each table with a primary key, links tables by repeating one table's key in another, and answers SQL queries that join those tables; PostgreSQL, MySQL and Oracle are the common ones.
- [[Database Schema]]: A database schema is the declared shape of a database: its tables, each column's name and type, the keys and the constraints, written as DDL (`CREATE TABLE`); a schema migration is a versioned script that changes that shape, such as adding a column, without losing the rows already stored.
- [[Foreign Key]]: A primary key is the column, or set of columns, whose value is different in every row of a table; a foreign key is that primary key copied into another table, so each row there points at exactly one row of the first, and the database refuses a pointer to a row that does not exist.
- [[Unique Constraint]]: A unique constraint makes the database refuse a second row with the same value, or the same combination of values, in the columns it names; the database enforces it through a unique index, so the refusal holds even when two transactions insert at the same moment, and Attica uses one on `(provider, date)` as its guard against booking one provider twice on one day.
- [[Database Normalization]]: Database normalization splits a table so each fact is stored once: first normal form removes repeating groups, second removes columns that depend on only part of the key, third removes columns that depend on another non-key column, and each step removes an update, insert or delete anomaly.
- [[Object-Relational Mapping]]: An object-relational mapping (ORM) lets code work with database rows as objects: each class is a table and each attribute a column, and the ORM writes the SQL for every query and save, so the programmer has to read that SQL to know what actually runs.
- [[Database Index]]: A database index is a separate, sorted structure that maps a column's values to the rows holding them, so a query can jump to matching rows instead of scanning the whole table, at the cost of extra space and slower writes.
- [[Database Transaction]]: A database transaction groups several reads and writes into one unit that either commits as a whole or rolls back as if it never ran, and ACID names the four promises it keeps: atomicity, consistency, isolation and durability.
- [[Isolation Level]]: An isolation level says how much one running transaction may see of another's uncommitted or newly committed work: read uncommitted, read committed, repeatable read and serializable each forbid one more anomaly (dirty reads, non-repeatable reads, phantom reads) than the level before.
- [[Database Locking]]: Database locking keeps two transactions from changing the same row at once: pessimistic locking takes the lock before reading (`SELECT ... FOR UPDATE`) so the second writer waits, while optimistic locking takes none and instead rejects a write whose row changed since it was read, usually by checking a version column.
- [[Database Replication]]: Database replication keeps copies of one database on several servers: a primary takes the writes and streams them to replicas that serve reads and can take over if the primary fails.
- [[Sharding]]: Sharding splits one large database into smaller databases called shards, each with the same schema but its own rows, and a partition key decides which shard holds each row.
