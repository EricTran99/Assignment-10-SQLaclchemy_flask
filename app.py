from flask import Flask, jsonify
import os
import csv
import pandas as pd
import numpy as np
import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func



app = Flask(__name__)

engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(autoload_with=engine)

Measurement= Base.classes.measurement
Station= Base.classes.station

@app.route("/")
def start():
    return (f"Hello, User!, here are the list of available routes.<br/>"
            f" <br/>"
            f"/api/v1.0/precipitation<br/>"
            f"/api/v1.0/stations<br/>"
            f"/api/v1.0/tobs<br/>"
            f" <br/>"
            f"/api/v1.0/(start)<br/>"
            f"/api/v1.0/(start)/(end)<br/>"
            f"For the last two routes, the template for them are (yy-mm-dd)"
            )

@app.route("/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.prcp).all()
    session.close()
    all_names = list(np.ravel(results))
    return jsonify(all_names)

    
@app.route("/stations")
def stations():
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    all_names = list(np.ravel(results))
    return jsonify(all_names)

@app.route("/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.tobs).all()
    session.close()
    all_names = list(np.ravel(results))
    return jsonify(all_names)

@app.route("/<start>")
def json_range(start=None):
    from datetime import datetime
    session = Session(engine)

    date = start
    format = "%m%d%Y"
  
    alter_date = dt.datetime.strptime(date, format)

    sel = [func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)]
    
    filtered_results = session.query(*sel).filter(Measurement.date >= alter_date).all()

    session.close()
    all_results = []
    for min, max, avg in filtered_results:
        results_dict = {}
        results_dict["min"] = min
        results_dict["max"] = max
        results_dict["avg"] = avg
        all_results.append(results_dict)

    return (all_results)

@app.route("/<start>/<end>")
def json_range(start=None,end=None):
    from datetime import datetime
    session = Session(engine)

    date_s = start
    date_e = end
    format = "%m%d%Y"
  
    alter_date_s = dt.datetime.strptime(date_s, format)
    alter_date_e = dt.datetime.strptime(date_e, format)

    sel = [func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)]
    
    filtered_results = session.query(*sel).filter(Measurement.date >= alter_date_s).filter(Measurement.date < alter_date_e).all()

    session.close()
    all_results = []
    for min, max, avg in filtered_results:
        results_dict = {}
        results_dict["min"] = min
        results_dict["max"] = max
        results_dict["avg"] = avg
        all_results.append(results_dict)

    return (all_results)


if __name__ == "__main__":
    app.run(debug=False)



