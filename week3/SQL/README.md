# Pure SQL

- Create SQL by hand using MySQL client
- Create a database
- Create a table

## Trade table structure
```sql
Trades (
  Trade_ID INT AUTO_INCREMENT PRIMARY KEY,
  Desk VARCHAR(50),
  Stock VARCHAR(50),
  Qty INT,
  Price DECIMAL(10, 2)
);
```
## Use SQL raw
- Use SQL in python to connect to MySQL
  - >pip install mysql-connector-python

- db connector
```python

host='localhost',
username='root',
password='',
database='sqfunda'

```

## Use SQL ORM - sqlalchemy
- [SQL Alchemy Document](https://docs.sqlalchemy.org/en/20/dialects/)
- install SQL Alchemy
  - >pip install sqlalchemy

```

connection = f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"

```

ORM Class

```
Trade_ID = Column(Integer, primary_key=True)
Desk = Column(String)
Stock = Column(String)
Qty = Column(Integer)
Price = Column(Float)

# Trade_time = Column(DateTime)

```

- quick way to view all records in mysql

```
mysql -u root -pcft108 -D sqfunda -e "DESC Trades"
```

### Create new table using SQL Alchemy


```
class Desk(Base):
  __tablename__ = 'Desk'

  id = Column(Integer, primary_key=True)
  name = Column(String(50))
  desc = Column(String(100))

Base.metadata.create_all(engine)
```

### Migrations : Alembic
## Install Alembic
> pip install alembic

- Initialize alembic
  - > alembic init alembic
- configure alembic
  - Edit alembic.ini
  - change sqlalchemy.url, dont have "" in value
  ```ini
  sqlalchemy.url = mysql+mysqlconnector://root:cft108@localhost/sqfunda
  ```
