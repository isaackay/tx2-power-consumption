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
| ----------------- |:-----------------:|:------------------:|
| Rhino             |421.57167024210776 | 149.19671136203203 |
| Elephant          |342.9747455032526  | 123.27536187949954 |


- WIFI

| Video Name		| 		WIFI 		| 	cropped-WIFI	 |
| ----------------- |:-----------------:|:------------------:|
| Rhino             |408.2678801849605  | 76.16265801128202  |
| Elephant          |469.85200658562457 | 124.38192337517566 |

### Reference
https://devtalk.nvidia.com/default/topic/1000830/jetson-tx2/jetson-tx2-ina226-power-monitor-with-i2c-interface-/
