import csv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_model import Auction, Base, engine

# Bind the engine with Base
Base.metadata.bind = engine


# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Read the CSV file and insert records into the database
with open('test_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Create a record of "Auction" object
        auction = Auction(**row)

        # Add the instance to the session
        session.add(auction)

# Commit and close session
session.commit()
session.close()