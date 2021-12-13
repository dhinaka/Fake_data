# create_tables.py
from sqlalchemy import create_engine, MetaData, \
    Column, Integer, Numeric, String, Date, Table, ForeignKey

# Set up connection between sqlalchemy and postgres dbapi
engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/fakedata"
)
# Create a metadata object
metadata = MetaData()

#DDL for customers, products, stores, and transactions
customers_fake = Table(
    "customers",
    metadata,
    Column("customer_id", Integer, primary_key=True),
     Column("customer_name", Integer, primary_key=True),
    Column("company_dt", String, nullable=False),
    Column("created_size", String, nullable=False),
   Column("session",String, nullable=False)
)



# Start transaction to commit DDL to postgres database
with engine.begin() as conn:
    metadata.create_all(conn)
    # Log the tables as they are created
    for table in metadata.tables.keys():
        print(f"{table} successfully created")




