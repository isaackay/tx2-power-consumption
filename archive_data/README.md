# TX2 power consumption (This README file does not consider viewport so is
# DEPRECATED!!!
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
- soc = `gpu + cpu + ddr + soc`
- wifi = `wifi`
- 360 = 1080p 360 vr video
- normal = normal 1080p video
- Render and WIFI power could be calculated using "normal" in each video
- Reproject power could be `360.soc` - `normal.soc`

```
{  
   'elephant':{  
      '360':{  
         'soc':3418.755637598899,
         'wifi':86.74614912280694
      },
      'normal':{  
         'soc':1697.451873077865,
         'wifi':55.01736450742237
      }
   },
   'rhino':{  
      '360':{  
         'soc':3245.1562674463935,
         'wifi':75.62248245614029
      },
      'normal':{  
         'soc':1538.7666179910561,
         'wifi':48.289825593395165
      }
   },
   'roller':{  
      '360':{  
         'soc':3603.7657804255855,
         'wifi':70.65156470722255
      },
      'normal':{  
         'soc':1813.3973485281895,
         'wifi':75.185109122807
      }
   }
}
```

### Reference
https://devtalk.nvidia.com/default/topic/1000830/jetson-tx2/jetson-tx2-ina226-power-monitor-with-i2c-interface-/
