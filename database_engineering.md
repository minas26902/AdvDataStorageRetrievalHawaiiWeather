
## Step 2 - Database Engineering


```python
!rm hawaii.sqlite
```


```python
# Import dependencies
import pandas as pd

#Import SQL Alchemy
import sqlalchemy
from sqlalchemy import create_engine, MetaData

#Import and establish Base for which classes will be constructed
from sqlalchemy.ext.declarative import declarative_base

#Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float, Date 

# To push the objects made and query the server use a Session object
from sqlalchemy.orm import Session
```


```python
# Create a schema - Measurements and Stations classes 
Base = declarative_base()

class Measurement(Base):
    __tablename__ = 'measurement'
    id = Column(Integer, primary_key=True)
    station = Column(String)
    date = Column(String)
    prcp = Column(Float)
    tobs = Column(Integer)

class Station(Base):
    __tablename__ = 'station'
    id = Column (Integer, primary_key=True)
    station = Column(String)
    name = Column(String)
    latitute = Column(Float)
    longitude = Column(Float)
    elevation = Column(Float)
```


```python
# Create and establish a database connection
engine = create_engine(f'sqlite:///hawaii.sqlite')
conn = engine.connect()

# Create the measurements and stations tables within the database
Base.metadata.create_all(engine)

# # Create a Session
session = Session(bind=engine)
```


```python
session.query(Station).all()
```




    []




```python
#Load the cleaned csv files into a Pandas dataframe -  Where did'Unnamed column?' come from? REMOVED
measurements_df=pd.read_csv("measurements_clean_df").drop(['Unnamed: 0'], axis=1)
stations_df=pd.read_csv("stations_clean_df").drop(['Unnamed: 0'], axis=1)
measurements_df
stations_df
#print(stations_df)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>station</th>
      <th>name</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>elevation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>USC00519397</td>
      <td>WAIKIKI 717.2, HI US</td>
      <td>21.27160</td>
      <td>-157.81680</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>USC00513117</td>
      <td>KANEOHE 838.1, HI US</td>
      <td>21.42340</td>
      <td>-157.80150</td>
      <td>14.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>USC00514830</td>
      <td>KUALOA RANCH HEADQUARTERS 886.9, HI US</td>
      <td>21.52130</td>
      <td>-157.83740</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>USC00517948</td>
      <td>PEARL CITY, HI US</td>
      <td>21.39340</td>
      <td>-157.97510</td>
      <td>11.9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>USC00518838</td>
      <td>UPPER WAHIAWA 874.3, HI US</td>
      <td>21.49920</td>
      <td>-158.01110</td>
      <td>306.6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>USC00519523</td>
      <td>WAIMANALO EXPERIMENTAL FARM, HI US</td>
      <td>21.33556</td>
      <td>-157.71139</td>
      <td>19.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>USC00519281</td>
      <td>WAIHEE 837.5, HI US</td>
      <td>21.45167</td>
      <td>-157.84889</td>
      <td>32.9</td>
    </tr>
    <tr>
      <th>7</th>
      <td>USC00511918</td>
      <td>HONOLULU OBSERVATORY 702.2, HI US</td>
      <td>21.31520</td>
      <td>-157.99920</td>
      <td>0.9</td>
    </tr>
    <tr>
      <th>8</th>
      <td>USC00516128</td>
      <td>MANOA LYON ARBO 785.2, HI US</td>
      <td>21.33310</td>
      <td>-157.80250</td>
      <td>152.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create a list of data to write to_dict()
measurements_dic = measurements_df.to_dict(orient='records')
stations_dic = stations_df.to_dict(orient='records')
print (stations_dic[:5])
```

    [{'station': 'USC00519397', 'name': 'WAIKIKI 717.2, HI US', 'latitude': 21.2716, 'longitude': -157.8168, 'elevation': 3.0}, {'station': 'USC00513117', 'name': 'KANEOHE 838.1, HI US', 'latitude': 21.4234, 'longitude': -157.8015, 'elevation': 14.6}, {'station': 'USC00514830', 'name': 'KUALOA RANCH HEADQUARTERS 886.9, HI US', 'latitude': 21.5213, 'longitude': -157.8374, 'elevation': 7.0}, {'station': 'USC00517948', 'name': 'PEARL CITY, HI US', 'latitude': 21.3934, 'longitude': -157.9751, 'elevation': 11.9}, {'station': 'USC00518838', 'name': 'UPPER WAHIAWA 874.3, HI US', 'latitude': 21.4992, 'longitude': -158.0111, 'elevation': 306.6}]



```python
#Use MetaData from SQLAlchemy to reflect the tables
metadata = MetaData(bind=engine)
metadata.reflect()
```


```python
#Save references to the measurements and stations tables as variables
measurement_table = sqlalchemy.Table ('measurement', metadata, autoload=True)
station_table = sqlalchemy.Table ('station', metadata, autoload=True)
```


```python
#Add function to delete tables in order to re-run code multiple times without getting error
conn.execute(measurement_table.delete())
conn.execute(station_table.delete())
```




    <sqlalchemy.engine.result.ResultProxy at 0x106bd5a20>




```python
type(measurement_table.insert())
```




    sqlalchemy.sql.dml.Insert




```python
measurement_table.insert()
```




    <sqlalchemy.sql.dml.Insert object at 0x107a96550>




```python
# Populate SQL table with data from csv
conn.execute(measurement_table.insert(), measurements_dic)
conn.execute(station_table.insert(), stations_dic)
```




    <sqlalchemy.engine.result.ResultProxy at 0x1066d8cc0>




```python
#Test to see if tables are populated
#conn.execute('select * from station limit 5').fetchall()
conn.execute('select * from measurement limit 5').fetchall()
```




    [(1, 'USC00519397', '2010-01-01', 0.08, 65),
     (2, 'USC00519397', '2010-01-02', 0.0, 63),
     (3, 'USC00519397', '2010-01-03', 0.0, 74),
     (4, 'USC00519397', '2010-01-04', 0.0, 76),
     (5, 'USC00519397', '2010-01-07', 0.06, 70)]




```python

```
