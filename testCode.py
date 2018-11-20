'''
testing code
'''
import pandas as pd
from settings import api_key
from entsoe import Entsoe
import numpy as np
from pandas import Timestamp
from getYear import yearInputFnc

year = 2016
e = Entsoe(api_key=api_key)

# year period to download
start = Timestamp((str(year)+ '0101000000'), tz='UTC')
end = Timestamp((str(year) + '0101010000'), tz='UTC')

print('Downloading...')
physicalFlow_DF = e.query_crossborder_flows(country_code_from='DE', country_code_to='CZ', start=start, end=end, as_series=True)
# gen_DF = e.query_generation('DE', start, end, as_dataframe=False, psr_type=None)
# df = e.query_load('DE', start, end, as_series=True, lookup_bzones=False)
# dfF = e.query_load('FR', start, end, as_series=True, lookup_bzones=False)

#import pdb; pdb.set_trace()
importH = list(physicalFlow_DF.head(0))
print(physicalFlow_DF)
print(importH)

# data = np.array([[1, 2],[3, 4],[5,6]])
# #data = np.array([1, 2, 3])
# count = 0
# cols = 1
# try:
#     (rows,cols) = data.shape
#     print(data.shape)
# except(ValueError):
#     rows = len(data)
# dataNew = np.zeros((rows,cols))
# print(dataNew.shape)
# print(dataNew)
# pdb.set_trace()
# print(dataNew[0,1])



#
# print(gen_DF)












# dates = pd.date_range('1/1/2000', periods=8)
# df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

#dates = pd.date_range('1/1/2017', periods=35035, freq='15min')
# year = 2016
# start = Timestamp((str(year)+ '0101'), tz='UTC')
# end = Timestamp((str(year + 1) + '0101'), tz='UTC')
#
# dates = pd.date_range(start, end,  dtype='datetime64[ms]', freq='H', tz='UTC')
# #dates = pd.to_datetime(dates, 'datetime64[ns]')
#
# df = pd.DataFrame(np.random.randn(len(dates), 1), index=dates, columns=['A'])
#
# print(start,end)
# print(dates)
# a = df.iloc[[0]]
# indexes = df.index.values

#pdb.set_trace()



# df2 = pd.DataFrame(np.zeros((5, 1)))
# print(df2)
#
# df.append(df2, ignore_index=True)
# print(df)

#pdb.set_trace()
#db = np.pad(df, ((0,5),(0,0)), 'constant')


# country = 'DE'
# header = ''
# columnNames = list(df.head(0))
# for name in columnNames:
#     header = header + country + '_' + name + ','

# magia
# newVector = np.add.reduceat(df, np.arange(0, len(df), 4))
#
# file = open('testfile.csv','w')
# file.write((header + '\n'))
# file.close
#
# file = open('testfile.csv','a')
# file.write(str(newVector))
# file.close
#
# file = open('testfile.csv','a')
# file.write((header + '\n'))
# file.close


# def scaleTo1Hour(df):
#     newVector = np.add.reduceat(df, np.arange(0, len(df), 4))
#     print(newVector)

# # create headers
# if countCountries == 1:
#     headerGen = 'Country'
#     generationType = list(gen_DF.head(0))
#     for type in generationType:
#         headerGen = headerGen + country + '_GEN_' + type + ','
#     headerGen = headerGen + country + '_Load'
#     file.write(headerGen)
