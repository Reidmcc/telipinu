import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
import numpy as np

def import_from_dict(file_dict, sa_engine, tbl_action='replace'):
    for key in file_dict.keys():
        print('starting import for file {}'.format(key))
        records = pd.read_csv(file_dict[key], sep=',')
        records.to_sql('{}'.format(key), sa_engine, if_exists=tbl_action, index=False)
        print('file for {} done'.format(key))

def create_sqlite(db_dir, db_fname):
    # TODO add error handling for non-existant dir and existing db file
    engine = sa.create_engine('sqlite:///{}//{}'.format(db_dir, db_fname))
    Base = declarative_base()
    Base.metadata.create_all(engine)

def connect_extant(db_dir, db_fname):
    engine = sa.create_engine('sqlite:///{}//{}'.format(db_dir, db_fname))
    return engine
