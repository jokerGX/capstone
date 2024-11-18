# home_config.py

import numpy as np

# Define the home joint angles for the Franka Emika Panda (7 joints)
HOME_JOINT_ANGLES = np.array([0.0, -np.pi/4, 0.0, -3*np.pi/4, 0.0, np.pi/2, np.pi/4])

# Optionally, save to a file
np.save("home_joint_angles.npy", HOME_JOINT_ANGLES)
