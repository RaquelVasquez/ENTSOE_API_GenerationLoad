# this code makes magic
# converts quartely hour or half-hour timestamps into standard hourly timestamps
# corrupted data are assigned with the identifier = 0.00000123456789

import sys
import pandas as pd
import numpy as np

def matchData(data, country, samplesPerYear, start, end):
    data_Period = knowSampleTime(samplesPerYear, len(data), country)
    # reviewing data downloaded
    if data_Period[1] == 1:  # if downloaded data is OK
        if data_Period[0] == 4:
            return( np.add.reduceat(data, np.arange(0, len(data), 4)) ) # scales up from quarter hour to hour
        elif data_Period[0] == 2:
            return( np.add.reduceat(data, np.arange(0, len(data), 2)) ) # scales up from half hour to hour
        elif data_Period[0] == 1:
            return(data)
    else:                   # if downloaded data is NO OK (missing data)
        data = missingDataFunc(data, data_Period, start, end)
        return(data)

def knowSampleTime(samplesPerYear, length, country):
    '''
    input:
        samplesPerYear: days of the year * 24
        length: lenght of DataFrame
    factor:
        factor to know of there is data missing
    return:
        [(1 for hourly 2 for halfhour or 4 quarterhour), (1 for exact data 0 for missing data)]
    '''
    #import pdb; pdb.set_trace()
    factor = 0.90 # porcentage of length data
    if length > (samplesPerYear * 4 * factor):
        if length == (samplesPerYear * 4):return([4,1])
        else:return([4,0])
    elif length > (samplesPerYear * 2 * factor):   # for halfhour (samplesPerYear *2)
        if length == (samplesPerYear * 2):return([2,1])
        else:return([2,0])
    elif length > (samplesPerYear * factor):   # hourly (samplesPerYear)
        if length == (samplesPerYear):return([1,1])
        else:return([1,0])
    else:
        print('_ Country: {}, data vector length: {}, '.format(country, length))
        sys.exit('Error in the frequency (length) of the data')

def missingDataFunc(data, data_Period, start, end):
    if data_Period[0] == 4:
        freq = '15min'
        data = discardMissingData(freq, data, start, end)
        data = np.add.reduceat(data, np.arange(0, len(data), 4))    # scales up from quarter hour to hour
    elif data_Period[0] == 2:
        freq = '30min'
        data = discardMissingData(freq, data, start, end)
        data = np.add.reduceat(data, np.arange(0, len(data), 2))    # scales up from half hour to hour
    elif data_Period[0] == 1:
        freq = 'H'
        data = discardMissingData(freq, data, start, end)
    return(data)

def discardMissingData(f, data, start, end):
    dates_downloaded = pd.to_datetime(data.index.values, 'datetime64[ns]')
    dates_downloaded = dates_downloaded.tz_localize(None)

    original_dates = pd.to_datetime(pd.date_range(start, end, freq=f), 'datetime64[ns]')
    original_dates = original_dates.tz_localize(None)

    count = 0
    cols = 1
    identifier = 0.00000123456789
    flagSeries = False
    try:
        (rows,cols) = data.shape
    except(ValueError):
        flagSeries = True
    rows = (len(original_dates) -1)
    dataNew = np.zeros((rows,cols)) # create matrix with the size of data
    for row in range(len(original_dates)-1):
        try:
            if original_dates[row] == dates_downloaded[row - count]:
                if flagSeries:
                    dataNew[row] = data[(row - count)]
                else:
                    for col in range(cols):
                        dataNew[row,col] = data.iloc[(row - count),col]
            else:
                if flagSeries:
                    dataNew[row] = identifier
                else:
                    for col in range(cols):
                        dataNew[row,col] = identifier
                count = count + 1
        except(IndexError):
            dataNew[row] = identifier
    return(dataNew)
