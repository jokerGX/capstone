# main.py

import argparse
import numpy as np
from frankapy import FrankaArm
import time

def load_pose(filename):
    """Load a saved pose from a .npy file."""
    return np.load(filename, allow_pickle=True).item()

def move_to_joint_positions(fa, joint_positions, duration=2.0):
    """Move the robot to the specified joint positions."""
    fa.goto_joints(joint_positions, duration=duration, wait=True)

def open_gripper(fa, width=0.08):
    """Open the gripper to the specified width."""
    fa.open_gripper(width=width)
    time.sleep(1)  # Wait for gripper to open

def close_gripper(fa, width=0.0):
    """Close the gripper to grasp the pen."""
    fa.close_gripper(width=width)
    time.sleep(1)  # Wait for gripper to close

def main():
    # Initialize the Franka Arm
    fa = FrankaArm()

    # Load the Home Configuration
    home_joint_angles = np.load("home_joint_angles.npy")

    # Load the Pen Holder Pose (assuming calibration has been done)
    pen_holder_pose = load_pose("pen_holder_pose.npy")
    pen_position = pen_holder_pose.translation  # [x, y, z]

    # Define Pre-Pick Configuration (e.g., above the pen holder)
    pre_pick_joint_angles = np.array([0.17955062, -0.1394879,   0.17290883, -2.6898799,   0.07158609,  2.5683256,
  1.03850022])

    # Move to Home Position
    print("Moving to Home Position...")
    move_to_joint_positions(fa, home_joint_angles)
    print("Reached Home Position.")

    # Open Gripper
    print("Opening Gripper...")
    open_gripper(fa, width=0.08)
    print("Gripper Opened.")

    # Move to Pre-Pick Position
    print("Moving to Pre-Pick Position...")
    move_to_joint_positions(fa, pre_pick_joint_angles)
    print("Reached Pre-Pick Position.")

    # Move Vertically Down to Pen Holder
    print("Approaching Pen Holder...")
    # Simple approach: move down in z-axis by a fixed amount
    approach_height = 0.1  # 10 cm above the pen
    current_pose = fa.get_pose().translation
    target_pose = current_pose.copy()
    target_pose[2] -= approach_height  # Move down

    fa.goto_pose(target_pose, duration=2.0, wait=True)
    print("Reached Pen Holder.")

    # Close Gripper to Grasp the Pen
    print("Closing Gripper to Grasp Pen...")
    close_gripper(fa, width=0.0)
    print("Pen Grasped.")

    # Lift the Pen Vertically
    print("Lifting the Pen...")
    lifted_pose = target_pose.copy()
    lifted_pose[2] += approach_height  # Move up
    fa.goto_pose(lifted_pose, duration=2.0, wait=True)
    print("Pen Lifted.")

    # Move Back to Home Position
    print("Returning to Home Position...")
    move_to_joint_positions(fa, home_joint_angles)
    print("Returned to Home Position.")

    # Optionally, open the gripper to release the pen
    # print("Releasing Pen...")
    # open_gripper(fa, width=0.08)
    # print("Pen Released.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Robot Checkpoint Script")
    args = parser.parse_args()

    main()
