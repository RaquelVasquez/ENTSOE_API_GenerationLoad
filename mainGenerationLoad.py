'''
This code downloads from ENTSO-E a dataset containing:

- Generation and Load

per country in hour timesteps for a 1 year period
data available from 2015
'''
import os
import sys

import numpy as np
from pandas import Timestamp
from datetime import datetime

from settings import api_key
from definitions import *
from matchMissing import *
from entsoe import Entsoe



################################################################################

def downloadData(year):
    # leap year verification
    now = datetime.now()
    if year >= 2016 and year <= now.year:
        if(year%4==0 and year%100!=0 or year%400==0):
            samplesPerYear = 366*24     # number of samples per Year (leap year)
        else:
            samplesPerYear = 365*24     # number of samples per Year (non leap year)
    else:
        sys.exit('No data available for year requested')

    # create object
    e = Entsoe(api_key=api_key)

    # year period to download
    start = Timestamp((str(year)+ '0101'), tz='UTC')
    end = Timestamp((str(year + 1) + '0101'), tz='UTC')

    countCountries = 0
    genData = []

    totalLen = len(countries_dict.keys())

    # pb = ProgressBar() # to see progress bar in terminal
    # for country, borders in pb(countries_dict.items()):
    for country, borders in countries_dict.items():
        # for each country
        print('\rDownloading {} data, country: {} Total: {}%'.format(year, country, (int((countCountries/totalLen)*100))), sep='', end=' ', flush=True)
        countCountries = countCountries + 1

        load_PS = e.query_load(country, start, end, as_series=True, lookup_bzones=False)
        load_hour = matchData(load_PS, country, samplesPerYear, start, end)

        gen_DF = e.query_generation(country, start, end, as_dataframe=True, psr_type=None)
        gen_hour = matchData(gen_DF, country, samplesPerYear, start, end)
        import pdb; pdb.set_trace()
        # TODO: crear dos ciclos for la misma funcion para cada uno de los tiepo de energia
        # for tipo in tiposDeEnergíaDelPaís
        #    gen_PSRtype = e.query_generation(country, start, end, as_dataframe=True, psr_type='B14')
        #    guardar datos por renovable y convencional
        # placing data in the same variable
        if countCountries == 1:
            headerGen = ''
            genData = np.c_[gen_hour, load_hour]
        else:
            headerGen = headerGen + ','
            genData = np.c_[genData, gen_hour]
            genData = np.c_[genData, load_hour]
        # create headers
        generationType = list(gen_DF.head(0))
        for type in generationType:
            headerGen = headerGen + country + '_GEN_' + type + ','
        headerGen = headerGen + country + '_Load'

    # storing data to csv file
    np.savetxt((str(year) + output_file_name), genData, delimiter=",", header=headerGen)
    print('Output file: {}'.format((str(year) + output_file_name)))

def main():
    years = [2016]
    for year in years:
        downloadData(year)

if __name__ == "__main__":
    main()
