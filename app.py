import numpy as np
import datetime as dt
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)
print(Base.classes.keys())
# Measurement = Base.classes.measurement
# Station = Base.classes.station
session = Session(engine)
#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# @app.route("/")
# def welcome():
#     """List all available api routes."""
#     return (
#         f"Available Routes:<br/>"
#         f"/api/v1.0/precipitation"
#         f"/api/v1.0/stations"
#         f"/api/v1.0/tobs"
#         f"/api/v1.0/<start>")
#         # f"/api/v1.0/<start>/<end>")

# @app.route("/api/v1.0/stations")
# def stations():
#     """Return the list of stations from the dataset as json"""
#     session = Session(engine)
#     results = session.query(Measurement.date, Measurement.prcp).all()
#     session.close()
#     return jsonify(stations)

# @app.route("/api/v1.0/precipitation")
# def prcp():
#     """Return the justice league data as json"""
#     return()
#     # Convert the query results to a dictionary using date as the key and prcp as the value.
#     # Return the JSON representation of your dictionary.



if __name__ == '__main__':
    app.run(debug=True)