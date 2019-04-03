"""
Handles the downloading of raw data from LAUS
"""
import pandas as pd


def get_bls_dataframe(url_endpoint):
    """Downloads the data into a pandas dataframe

    Args:
        url_endpoint (string): string endpoint to the BLS LAUS dataset

    Returns:
        pd.DataFrame: dataframe of the data in the endpoint
    """
    url = 'https://download.bls.gov/pub/time.series/la/' + url_endpoint
    df = pd.read_csv(
        url,
        sep = '\t',
        dtype = str,
        index_col = False,
    )

    for column in df.columns:
        df[column] = df[column].str.strip()

    return df


def download_laus_data():
    """
    Main function for downloading the raw LAUS data from the BLS FTP site
    """

    urls = [
        'la.area',
        'la.area_type',
        'la.areamaps',
        'la.data.1.CurrentS',
        'la.data.0.CurrentU00-04',
        'la.data.0.CurrentU05-09',
        'la.data.0.CurrentU10-14',
        'la.data.0.CurrentU15-19',
        'la.measure',
        'la.period',
        'la.seasonal',
        'la.series',
        'la.state_region_division'
    ]

    for url in urls:
        df = get_bls_dataframe(url)
        df.to_csv('raw_csv_files/' + url + '.csv', index = False)


if __name__ == '__main__':
    download_laus_data()
