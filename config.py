
# This file to contain all the config variables shared across modules

use_median_filter_throttle = True
use_throttle_manual_map = True
split_softmax = True

#camera_id = 0


# Create local_config.py to have local settings
try :
	from local_config import *
except:
	pass

