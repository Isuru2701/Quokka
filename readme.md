# QUOKKA

---
A Python-based ML model trained using sci-kit learn to predict whether certain conditions will lead to a wildfire.

## Aspects

---
Aspects will refer to the variables that are considered. They include:

- Temperature (point)
- Relative Humidity (point)
- Soil Moisture (point)
- Temperature (local via Weather API)
- Relative Humidity (local via Weather API)
- Wind Speed (point AND local via Weather API)
- Rainfall (local via Weather API)
- Month

## Datasets

### forestfires.csv
Columns: X, Y, month, day, FFMC, DMC, DC, ISI, temp, RH, wind, rain, area
<p>
X - x-axis spatial coordinate within the Montesinho park map: 1 to 9
<br>
Y - y-axis spatial coordinate within the Montesinho park map: 2 to 9
<br>
month - month of the year: 'jan' to 'dec'
<br>
day - day of the week: 'mon' to 'sun'
<br>
FFMC - FFMC index from the FWI system: 18.7 to 96.20
<br>
DMC - DMC index from the FWI system: 1.1 to 291.3
<br>
DC - DC index from the FWI system: 7.9 to 860.6
<br>
ISI - ISI index from the FWI system: 0.0 to 56.10
<br>
temp - temperature in Celsius degrees: 2.2 to 33.30
<br>
RH - relative humidity in %: 15.0 to 100
<br>
wind - wind speed in km/h: 0.40 to 9.40
<br>
rain - outside rain in mm/m2 : 0.0 to 6.4
<br>
area - the burned area of the forest (in hectacres): 0.00 to 1090.84


Source: [**Portugal Forest Fires**](https://archive.ics.uci.edu/ml/datasets/forest+fires)
<br>
*Cortez,Paulo and Morais,Anbal. (2008). Forest Fires. UCI Machine Learning Repository. https://doi.org/10.24432/C5D88D.*
---

### WildFire_Prediction_Data_Set.csv


Source: [**Data for: Predictive Modeling of Forest Fires: A New Dataset and Machine Learning Approach**](https://data.mendeley.com/datasets/85t28npyv7/1)
<br> 
*OULAD SAYAD, YOUNES; Mousannif, Hajar; Al Moatassime, Hassan (2019), “Data for: Predictive Modeling of Forest Fires: A New Dataset and Machine Learning Approach”, Mendeley Data, V1, doi: 10.17632/85t28npyv7.1*