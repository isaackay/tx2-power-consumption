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
- soc = `gpu + cpu + ddr + soc`
- wifi = `wifi`
- 360 = 4k 360 vr video with viewport 1280x720
- normal = normal 1080p video with viewport 1280x720
- Render and WIFI power could be calculated using "normal" in each video
- Reproject power could be `360.soc` - `normal.soc`
- Take elephant video as an example for computing power constant for each cache
  level (L1: 1600x1600, L2: 2800x2160, L3: 3840x2160):
	- SOC
		- Reprojection power constant of viewport@1280x720=`(3944.53 - 2002.86)
		  = 1941.67`
		- Rendering power constant of viewport@1280x720=`2002.86`
		- L1: `2002.86 * 1600 * 1600 / 1280 / 720` = `5563.5`
		- L2: `(2002.86 * 2800 * 2160 / 1280 / 720) + (1941.67 * 2800 * 2160 /
		  1280 / 720)` = `25885.98`
		- L3: `(3944.53 * 3840 * 2160 / 1280 / 720)` = `35500.77`
	- WIFI
		- 360 version of WIFI is a 4K video, normal version of WIFI is for 1080p
		- However, 360 version of WIFI is not four times or more than the normal
		  version of WIFI
		- And the reason might be simple - Youtube or the router in UR has
		  bandwidth management so that WIFI power has a limit that couldn't
		  afford downloading 4k 360 video smoothly
		- So I choose simply scale the normal version using pixel!
		- L1: `108.18 * 1600 * 1600 / 1920 / 1080` = `133.56`
		- L2: `108.18 * 2800 * 2160 / 1920 / 1080` = `315.53`
		- L3: `108.18 * 3840 * 2160 / 1280 / 720` = `432.72`

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
