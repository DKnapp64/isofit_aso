from spectral import envi
import numpy as np
from isofit.core.geometry import Geometry
from isofit.core.forward import ForwardModel
from isofit.configs import configs

obs_file = envi.open("/mnt/persistent_data/isofit/examples/20230401_ASO/asoswir20230401t163434_tiny_obs.hdr")
loc_file = envi.open("/mnt/persistent_data/isofit/examples/20230401_ASO/asoswir20230401t163434_tiny_loc.hdr")

# i1 = np.random.randint(1280)
# i2 = np.random.randint(1242)
i1 = 0
i2 = 0

config = configs.create_new_config(config_file="/mnt/data/20230401_ASO/VNIR/L2A_reflectance/config/asovnir20230401t163434_isofit.json")
fm = ForwardModel(config)

obs = np.copy(obs_file[i1,i2,:][0,0,:])
loc = np.copy(loc_file[i1,i2,:][0,0,:])
geom = Geometry(obs, loc)
x_RT=np.array([0.1009, 3.48767065])
r = fm.RT.get_shared_rtm_quantities(x_RT, geom)
