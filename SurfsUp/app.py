# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine,reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route('/')
def home():
    return '<div><h1>Links</h1><p><a href ="/api/v1.0/precipitation" >/api/v1.0/precipitation</a><p></div>'#'''/api/v1.0/precipitation|| /api/v1.0/stations|| /api/v1.0/tobs|| /api/v1.0/<start>|| /api/v1.0/<start>/<end>'''

@app.route('/api/v1.0/precipitation')
def precipition():
    prcp_dict = {}
    query_data_prcp = session.query(measurement.date, measurement.prcp).filter(measurement.date >= '2016-08-23').all()
    for val in query_data_prcp:
        prcp_dict[val[0]] = val[1]
    return prcp_dict

@app.route('/api/v1.0/stations')
def stations():
    return ''
@app.route('/api/v1.0/tobs')
def tobs():
    return ''
@app.route('/api/v1.0/<start>')
def start():
    return jsonify(prcp_dict)
@app.route('/api/v1.0/<start>/<end>')
def end():
    return ''

if __name__ == "__main__":
    app.run(debug=True)
