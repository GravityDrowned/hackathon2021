# Database Schema setup (ER Models)
---

For starters of our implementation, the following are perhaps the most simplistic set of entities and their relationships: 

* Areas
* Sensors
* Floor plan
* operating table

---

## Areas

* id 
* areaType, areaCode
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

* maxCapacity

---

## Sensors

* id
* sensorType, sensorCode
	* temperature, TEMP
	* moisture, MOIS
	* light, LI
	* luminosity, LUMI
	* airQuality, AQI
	* airPurifier, APU
	...
* unit

---

## Floor

* id
* floorNumber
* areaType
* sensors

---

## OperatingTable

* dateTimeStamp
* floor_id
* area_id
* sensor_id
* sensorValue
* occupied
...
