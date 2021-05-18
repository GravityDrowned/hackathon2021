# Database Schema setup (ER Models)
---

For starters of our implementation, the following are perhaps the most simplistic set of entities and their relationships: 

* Areas
* Sensors
* Floor plan
* operating table

---

## AreaType
* id 
* type, code
	* deskArea, DA
	* meetingRoom1, MR1
	* meetingRoom2, MR2
	* seminarRoom1, SR1
	* seminarRoom2, SR2
	* auditorium, AU
	* recreation, RE
	* launge, LU
	* restroomMen, RR1
	* restroomWomen, RR2
	* cafeteria, CF
	* kitchen, KI
	* misc, MISC

* max_capacity

---

## Area

* id (uuid)
* name (formatted name; user-readable; unique within floors and not necessarily across the floors)
* type (FK on AreaType)
* floor 
* sensors (a json list of sensors (ids) in the area)

---

## SensorType

* id
* type, code
	* temperature, TEMP
	* moisture, MOIS
	* light, LI
	* luminosity, LUMI
	* interiorAirQuality, IAQ
	* airPurifier, APU
	...
* unit

---

## Sensor

* id (uuid)
* type (FK on SensorType)

---

## WorkingTable

* timestamp
* area
* sensor
* sensor_value
...
