
# SQL - Advanced Data Storage Retrieval
## HW#9 Due February 7

## Step 1 - Data Engineering


```python
#Import dependencies
import pandas as pd
```


```python
#Import measurements and stations CSV files and as DFs
measurements_df=pd.read_csv("resources/hawaii_measurements.csv", dtype = object)
stations_df=pd.read_csv("resources/hawaii_stations.csv", dtype = object)
#print (measurements_df)
#print(stations_df)

#Check and clean data
#print (measurements_df.count()) #1447 MISSING PRCP POINTS.
#print (stations_df.count()) #OK NO MISSING DATA IN STATIONS DF

#Drop any NaNS in measurement df and reset index
measurements_clean_df=measurements_df.dropna(how='any').reset_index(drop=True)
#print (measurements_clean_df.count())

#Check for duplicates in measurements df
measurements_clean_df=measurements_clean_df.drop_duplicates()
#print (measurements_clean_df.count()) #OK, NO DUPLICATES FOUND
print(measurements_clean_df)
```

               station        date  prcp tobs
    0      USC00519397  2010-01-01  0.08   65
    1      USC00519397  2010-01-02     0   63
    2      USC00519397  2010-01-03     0   74
    3      USC00519397  2010-01-04     0   76
    4      USC00519397  2010-01-07  0.06   70
    5      USC00519397  2010-01-08     0   64
    6      USC00519397  2010-01-09     0   68
    7      USC00519397  2010-01-10     0   73
    8      USC00519397  2010-01-11  0.01   64
    9      USC00519397  2010-01-12     0   61
    10     USC00519397  2010-01-14     0   66
    11     USC00519397  2010-01-15     0   65
    12     USC00519397  2010-01-16     0   68
    13     USC00519397  2010-01-17     0   64
    14     USC00519397  2010-01-18     0   72
    15     USC00519397  2010-01-19     0   66
    16     USC00519397  2010-01-20     0   66
    17     USC00519397  2010-01-21     0   69
    18     USC00519397  2010-01-22     0   67
    19     USC00519397  2010-01-23     0   67
    20     USC00519397  2010-01-24  0.01   71
    21     USC00519397  2010-01-25     0   67
    22     USC00519397  2010-01-26  0.04   76
    23     USC00519397  2010-01-27  0.12   68
    24     USC00519397  2010-01-28     0   72
    25     USC00519397  2010-01-31  0.03   67
    26     USC00519397  2010-02-01  0.01   66
    27     USC00519397  2010-02-04  0.01   69
    28     USC00519397  2010-02-05     0   67
    29     USC00519397  2010-02-06     0   67
    ...            ...         ...   ...  ...
    18073  USC00516128  2017-07-17  0.39   72
    18074  USC00516128  2017-07-18   2.4   77
    18075  USC00516128  2017-07-19  0.27   74
    18076  USC00516128  2017-07-20   0.7   75
    18077  USC00516128  2017-07-21   0.1   72
    18078  USC00516128  2017-07-22     4   72
    18079  USC00516128  2017-07-23   0.8   78
    18080  USC00516128  2017-07-24  0.84   77
    18081  USC00516128  2017-07-25   0.3   79
    18082  USC00516128  2017-07-26   0.3   73
    18083  USC00516128  2017-07-27     0   75
    18084  USC00516128  2017-07-28   0.4   73
    18085  USC00516128  2017-07-29   0.3   77
    18086  USC00516128  2017-07-30   0.3   79
    18087  USC00516128  2017-07-31     0   74
    18088  USC00516128  2017-08-02  0.25   80
    18089  USC00516128  2017-08-03  0.06   76
    18090  USC00516128  2017-08-07  0.05   78
    18091  USC00516128  2017-08-08  0.34   74
    18092  USC00516128  2017-08-09  0.15   71
    18093  USC00516128  2017-08-10  0.07   75
    18094  USC00516128  2017-08-12  0.14   74
    18095  USC00516128  2017-08-14  0.22   79
    18096  USC00516128  2017-08-15  0.42   70
    18097  USC00516128  2017-08-16  0.42   71
    18098  USC00516128  2017-08-17  0.13   72
    18099  USC00516128  2017-08-19  0.09   71
    18100  USC00516128  2017-08-21  0.56   76
    18101  USC00516128  2017-08-22   0.5   76
    18102  USC00516128  2017-08-23  0.45   76
    
    [18103 rows x 4 columns]



```python
#Save cleaned dataframes to csv
measurements_clean_df.to_csv("measurements_clean_df") # index=False, header=True)
stations_df.to_csv("stations_clean_df")
```


```python

```
