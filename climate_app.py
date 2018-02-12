#Climate App
#Import dependencies
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func
from flask import Flask, jsonify
import numpy as np

#Database setup
engine = create_engine("sqlite:///hawaii.sqlite")
print("Connected to DB")

#Reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)
print("Reflected tables")

#Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

#Flask Setup
app = Flask(__name__)

#Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - lists precipitation for last year of data.<br/>"

        f"/api/v1.0/stations - lists all weather stations in Honolulu.<br/>"

        f"/api/v1.0/tobs - lists temperature observations for last year of data.<br/>"

        f"/api/v1.0/&ltstart&gt  - returns the MIN, AVG, and MAX temperature for \
        all dates greater than the start date - enter date as 'yyyy-mm-dd'.<br/>"
                
        f"/api/v1.0/&ltstart&gt/&ltend&gt - returns the MIN, AVG, and MAX temperature \
        for all dates between the start and end date - enter date as 'yyyy-mm-dd'.<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Returns precipitation data for the last year of data collected"""
    #Query precipitation data for the last year of data collection
    results1 = session.query(Measurement.date, func.avg(Measurement.prcp)).\
    filter(Measurement.date>'2016-08-23').group_by(Measurement.date).all()

    #Create a list of dicts with 'date' as they key and 'prcp' as the value
    precipitation = []
    for result in results1:
        row = {}
        row["date"] = result[0]
        row["total"] = float(result[1])
        precipitation.append(row)
    #Jsonify results
    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    """Returns the list of stations in Honolulu"""
    #Query to return list of stations
    results2 = session.query(Station.name).all()
    
    #Convert to list
    station_list = list(np.ravel(results2))
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Returns temperature observations for last year of data collected"""
    #Query to return list of tobs
    results3 = session.query(Measurement.tobs).filter(Measurement.date>'2016-08-23').all()
    
    #A different approach to creating a list without using list(np.ravel())
    tobs_list = [record.tobs for record in results3]
    return jsonify(tobs_list)

@app.route("/api/v1.0")
@app.route("/api/v1.0/<start>")
def temp_summary_starting(start): #2017-08-23
    """Returns the MIN, AVG, and MAX temperature for all dates greater than the start date"""
    results4= session.query(func.min(Measurement.tobs).label("min_temp"), 
                    func.avg(Measurement.tobs).label("avg_temp"),
                    func.max(Measurement.tobs).label("max_temp")
                    ).filter(Measurement.date>=start).all()

    temp_sum_start = list(np.ravel(results4))
    return jsonify(temp_sum_start)

@app.route("/api/v1.0")
@app.route("/api/v1.0/<start>/<end>")
def temp_summary_start_end(start,end): #2017-08-23, 2017-09-20
    """Returns the MIN, AVG, and MAX temperature for all dates greater than the start date"""
    results5= session.query(func.min(Measurement.tobs).label("min_temp"), 
                    func.avg(Measurement.tobs).label("avg_temp"),
                    func.max(Measurement.tobs).label("max_temp")
                    ).filter(Measurement.date.between(start, end)).all()

    temp_sum_start_end = list(np.ravel(results5))
    return jsonify(temp_sum_start_end)

if __name__ == '__main__':
    app.run()
