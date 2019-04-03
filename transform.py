"""
Handles the transforming of the text data from LAUS
"""
import os
import pandas as pd


def transform_laus_data():
    """Main function for transforming the data
    """
    directory = 'raw_csv_files/'

    if not os.path.exists(directory):
        os.mkdirs(directory)

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            # load into memory
            df = pd.read_csv(
                os.path.join(directory, filename),
                dtype = str
            )

            # more processing can be done here

            # export
            if 'data' in filename:
                # export all the 'data' together into one csv
                df['value'] = pd.to_numeric(
                    df['value'],
                    errors = 'coerce',
                    downcast = 'float'
                )
                df.to_csv(
                    'processed_files/data.csv',
                    index = False,
                    header = not(os.path.exists('processed_files/data.csv')),
                    mode = 'a'
                )

            else:
                df.to_csv(
                    'processed_files/' + filename.replace('la.', ''),
                    index = False,
                    header = not(os.path.exists('processed_files/' + filename.replace('la.', '')))
                )
