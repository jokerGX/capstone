# pick_config.py

import numpy as np

# Load home configuration
HOME_JOINT_ANGLES = np.load("home_joint_angles.npy")

# Define Pre-Pick Configuration (e.g., slightly move joint 2 and joint 4)
PRE_PICK_JOINT_ANGLES = np.array([0.17955062, -0.1394879,   0.17290883, -2.6898799,   0.07158609,  2.5683256,
  1.03850022])

# Define Pen-Grasp Configuration (e.g., further adjust joint angles to lower the gripper)
PEN_GRASP_JOINT_ANGLES = np.array([ 0.17859062,  0.08323015,  0.18945552, -2.65747235,  0.06592363,  2.67681484,
  1.03845873])

# Optionally, save to files
np.save("pre_pick_joint_angles.npy", PRE_PICK_JOINT_ANGLES)
np.save("pen_grasp_joint_angles.npy", PEN_GRASP_JOINT_ANGLES)
