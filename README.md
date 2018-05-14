# TX2 power consumption
This repository is for automated creating power consumption data from tx2. The
data produced by this repo is for vros research.

## Usage
- mode could be "wifi" or "soc" currently.
```
make
./power <mode>
```
- Example of getting the power consumption data by normalizing with power
  consumption in idle state.
```
./power wifi &> dump-orig/roller_wifi.txt
./avg.py dump-orig/roller_wifi.txt idle/idle-wifi.txt
```

## Results

- SOC

| Video Name		| 		SOC 		| 	cropped-SOC		 |
|:-----------------:|:-----------------:|:------------------:|
| Rhino             |421.57167024210776 | 149.19671136203203 |
| Elephant          |342.9747455032526  | 123.27536187949954 |
| RollerCoaster 	|387.58693896074396 | 180.34831482243237 |
| NYC(Timelapse)	|403.54892741061735 | 205.68470588235277 |
| Paris	 			|430.44743888764276 | 316.7087105700052  |

- WIFI

| Video Name		| 		WIFI 		| 	cropped-WIFI	 |
|:-----------------:|:-----------------:|:------------------:|
| Rhino             |394.8664045535304  | 120.20770895770887 |
| Elephant          |456.45053095419445 | 124.38192337517566 |
| RollerCoaster 	|459.4796288244132  | 144.55309968915543 |
| NYC(Timelapse)	|446.119584859585   | 162.14425918908688 |
| Paris				|373.82121738596544 | 105.77039512833733 |

### Reference
https://devtalk.nvidia.com/default/topic/1000830/jetson-tx2/jetson-tx2-ina226-power-monitor-with-i2c-interface-/
