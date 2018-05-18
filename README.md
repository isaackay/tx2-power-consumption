# TX2 power consumption
This repository is for automated creating power consumption data from tx2. The
data produced by this repo is for vros research.

## Usage
- power
	- mode could be `wifi`, `cpu`, `soc`, `ddr`, or `all` 
	```
	make
	./power <mode> <title w/o file extension>
	```
	- Example of getting the power consumption data by normalizing with power
	  consumption in idle state.
	```
	./power ddr dump-orig/roller
	./avg.py dump-orig/roller_ddr.txt idle/idle-ddr.txt
	```
- avg
	- no argument
		- dump all version of power constant files
	- one argument (folder such as 'dump-orig-no-drag')
		- dump power constant files in that folder
	- two arguments (first argument is same as above, second argument is the
	  position of idle foler)

## Results
TODO

### Reference
https://devtalk.nvidia.com/default/topic/1000830/jetson-tx2/jetson-tx2-ina226-power-monitor-with-i2c-interface-/
