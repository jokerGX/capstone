# home_config.py

import numpy as np

# Define the home joint angles for the Franka Emika Panda (7 joints)
HOME_JOINT_ANGLES = np.array([ 9.28124534e-04, -7.84623185e-01, -2.10576618e-03, -2.35603544e+00,
  9.23834388e-04,  1.57056346e+00,  7.85080742e-01])

# Optionally, save to a file
np.save("home_joint_angles.npy", HOME_JOINT_ANGLES)