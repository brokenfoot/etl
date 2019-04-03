"""
Process file for hanlding the full ETL process
"""
from extract import download_laus_data
from transform import transform_laus_data
from load import load_data_to_sqlite


def main():
    """
    Handles the full ETL process
    """
    download_laus_data()
    transform_laus_data()
    load_data_to_sqlite()


if __name__ == '__main__':
    main()
