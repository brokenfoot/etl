"""Summary
"""
import pandas as pd
import os
import sqlalchemy


def load_data_to_sqlite():
    """Summary
    """
    engine = sqlalchemy.create_engine('sqlite:///db.sqlite3')
    directory = 'processed_files/'
    for filename in os.listdir(directory):
        df = pd.read_csv(
            os.path.join(directory, filename),
            index_col = False,
            low_memory = False
        )

        df.to_sql(
            name = filename.replace('.csv', ''),
            con = engine,
            index = False,
            if_exists = 'replace'
        )
