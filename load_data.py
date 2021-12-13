import psycopg2
from sqlalchemy import create_engine, MetaData, select
from faker import Faker
import sys
import random
import datetime
import pandas as pd
import numpy as np
import faker
from IPython.display import display

def create_rows(num):
    fake = Faker()
    size_c = ['Small', 'large']
    output = [{"customer_id": x+100,  ## random without putting back
           "company_name": fake.name(),
           "created_dt": fake.date_time(),
           "company_size": np.random.choice(size_c, size=1, p=[0.7, 0.3])
           } for x in range(num)]
    return output

def num_session(company_size):
    if company_size == 'Small':
        rand_gen = np.random.uniform(low=-5, high=5) + 5  ## check if same as np.random.uniform(low=0, high=10)
    else:
        rand_gen = np.random.uniform(low=-10, high=10) + 10  ## check if same as np.random.uniform(low=0, high=20)
    return rand_gen

def randomiser(x, values_list, p=0.5):
    # possibility to pass probability (p) as list as well
    return np.random.choice(values_list, size=1, p=[p, (1 - p)])


def main():
    #engine_link = sys.arg[1]
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/fakedata")

    # df = pd.read_sql_table( "customers", con=engine)
    df = pd.DataFrame(create_rows(500))
    # df['company_size'] = df.apply(lambda x: randomiser(x,["Small", "Large"], 0.5 ), axis = 1)
    #df.speed = df.apply(lambda x: np.random.uniform(0, 1) if x.speed == 0 and x.dir == 999 else x.speed, axis=1)
    df["Session"] = df.apply(lambda x: np.random.uniform(low=-5, high=5) + 5 if x.company_size =="Small" else np.random.uniform(low=-10, high=10) + 10 ,axis=1)

    df.to_sql("customers",engine)

if __name__ == "__main__":
    main()
