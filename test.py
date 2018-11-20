import pandas as pd
from settings import api_key
from entsoe import Entsoe
import numpy as np
from pandas import Timestamp
from matchMissing import *


def downloadData():
    e = Entsoe(api_key=api_key)
    year = 2016
    # year period to download
    start = Timestamp((str(year)+ '0101'), tz='UTC')
    end = Timestamp((str(year) + '0102'), tz='UTC')

    country = 'DE'

    print('Downloading... {}'.format(country))
    # physicalFlow_DF = e.query_crossborder_flows(country_code_from='DE', country_code_to='CZ', start=start, end=end, as_series=True)
    # gen_DF = e.query_generation('DE', start, end, as_dataframe=True, psr_type=None)
    # df = e.query_load('DE', start, end, as_series=True, lookup_bzones=False)

    #df = e.query_load(country, start, end, as_series=True, lookup_bzones=False)
    data = e.query_generation(country, start, end, as_dataframe=True, psr_type='B14')
    # import pdb; pdb.set_trace()
    if data is not None:
        print('Ja Klar, guarda datos')
    else:
        print('No descargo nachos')
    # df = matchData(df, country, samplesPerYear, start, end)
    # dfF = matchData(dfF, country, samplesPerYear, start, end)

    # np.savetxt('query_load.csv', df, delimiter=",")
    # np.savetxt('query_GenFR.csv', dfF, delimiter=",")

def main():
    downloadData()

if __name__ == "__main__":
    main()
