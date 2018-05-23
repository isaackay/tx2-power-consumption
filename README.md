# TX2 power consumption
This repository is for automated creating power consumption data from tx2. The
data produced by this repo is for vros research.

## Usage
- power.cpp
	- mode could be `wifi`, `cpu`, `soc`, `ddr`, or `all` 
	```
	make
	./power <mode> <title w/o file extension>
	```
	- Example of getting the power consumption data by normalizing with power
	  consumption in idle state.
	```
	./power all dump-orig/roller
	python3 avg.py
	```
- avg.py
	- `python3 avg.py`
		- dump the 360 and 1080p version of power constant in each video as json

## Results
- soc = `gpu + cpu + ddr + soc`
- wifi = `wifi`
- 360 = 4k 360 vr video with viewport 1280x720
- normal = normal 1080p video with viewport 1280x720
- Render and WIFI power could be calculated using "normal" in each video
- Reproject power of Level 2 frame is HARD TO KNOW CURRENTLY, so skip it for now
- Take elephant video as an example for computing power constant for each cache
  level (L1: 1440x1440, L3: 3840x2160):
	- SOC
		- Rendering of L1=`2905.3881458682936`
		- Rendering + Reprojection of full size 360 video=`3944.5344700918963`
		- L1: `2905.3881458682936`
		- L3: `3944.5344700918963`
	- WIFI
		- L1: `54.331439445387616`
		- L3: `355.14874912280703`

```
{  
   'elephant':{  
      '360':{  
         'soc':3944.5344700918963,
         'wifi':355.14874912280703
      },
      'normal':{  
         'soc':2905.3881458682936,
         'wifi':54.331439445387616
      }
   },
   'nyc':{  
      '360':{  
         'soc':4034.926912949039,
         'wifi':337.8103713450292
      },
      'normal':{  
         'soc':2107.6333267155032,
         'wifi':34.04614912280701
      }
   },
   'paris':{  
      '360':{  
         'soc':4019.510108187135,
         'wifi':326.522399122807
      },
      'normal':{  
         'soc':2956.486142147428,
         'wifi':26.981449122806964
      }
   },
   'rhino':{  
      '360':{  
         'soc':3892.9772034252296,
         'wifi':284.177549122807
      },
      'normal':{  
         'soc':1816.2819824741846,
         'wifi':22.40641578947364
      }
   },
   'roller':{  
      '360':{  
         'soc':3936.285384088642,
         'wifi':378.30801868802445
      },
      'normal':{  
         'soc':2231.2324830262596,
         'wifi':85.84479777145563
      }
   }
}
```

### Reference
https://devtalk.nvidia.com/default/topic/1000830/jetson-tx2/jetson-tx2-ina226-power-monitor-with-i2c-interface-/
