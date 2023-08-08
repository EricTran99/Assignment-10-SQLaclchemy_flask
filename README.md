# Assignment-10-SQLaclchemy_flask
This is module 10, which focus on the using SQLalchemy and flask in order to read SQL data and port it
into a website (technically a port URL)

The repository contains various parts for this module to work.
- Resource – containing the two CSV files of Hawaii stations and temperature
- App.py – script code which uses the sqlite file to produce the Json code,
- Climate_starter.ipynb – code for the first part (used jupyterNotbook)
- Hawaii.sqlite – sqlite in which the app.py used to read (had to be placed outside as it doesn’t
successfully read the file in the resource folder, this it needs to be on the same location as the
vsvode script.)

The challenge is split into two parts:
1. Applying SQLalchemy
This challenge focus on utilising sqlalchemy in order to run the sql file through python (the code is running the hawaii.sqlite). The script filters the sqlite based on date and displaying the results with
line and histogram.

Below are the results from running code


![image](https://github.com/Nisloen/Assignment-10-SQLaclchemy_flask/assets/134130254/4964b1f4-16b4-4114-ad86-849bf9bcda4e)
![image](https://github.com/Nisloen/Assignment-10-SQLaclchemy_flask/assets/134130254/45b6df3a-73fa-49c2-ace7-89d60917f921)


3. Using vscode flask
This challenge run flask which shows the results in a URL , which is running in Google chrome and edited through vscode, uses flask which uses sqlalchemy to read the sqlite and apply the data through app.route
and have certain phrase that can be written as addition to the base HTTP.
The first three shows the jsonified results for the certain data columns.
The last two is an approute which calculate the minimum, maximum and average temperature based on the date as the filter.
NOTE: the format is "monthdateyear" this means that date needs to be type without slash or dash
      for example if the chosen date is 15/5/2015, then it needs to be type as 05152015
