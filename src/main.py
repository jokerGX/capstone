# main.py

import argparse
import numpy as np
import rospy
from motionplanner import TrajectoryGenerator, TrajectoryFollower
from frankapy import FrankaArm

def load_joint_angles(filename):
    """Load joint angles from a .npy file."""
    return np.load(filename)

def main():
    # Initialize ROS node
    rospy.init_node('robot_checkpoint', anonymous=True)

    # Initialize Franka Arm
    fa = FrankaArm()

    # Initialize Trajectory Generator and Follower
    traj_gen = TrajectoryGenerator()
    traj_follower = TrajectoryFollower()

    # Load Joint Configurations
    home_joint_angles = load_joint_angles("home_joint_angles.npy")
    pre_pick_joint_angles = load_joint_angles("pre_pick_joint_angles.npy")
    pen_grasp_joint_angles = load_joint_angles("pen_grasp_joint_angles.npy")

    # Generate Trajectories
    print("Generating Trajectories...")
    traj1 = traj_gen.generate_joint_space_trajectory(home_joint_angles, pre_pick_joint_angles, steps=100)
    traj2 = traj_gen.generate_joint_space_trajectory(pre_pick_joint_angles, pen_grasp_joint_angles, steps=100)
    print("Trajectories Generated.")

    # Execute Trajectory 1: Home → Pre-Pick
    print("Executing Trajectory 1: Home → Pre-Pick...")
    traj_follower.follow_joint_trajectory(traj1)
    print("Trajectory 1 Completed.")

    # Execute Trajectory 2: Pre-Pick → Pen-Grasp
    print("Executing Trajectory 2: Pre-Pick → Pen-Grasp...")
    traj_follower.follow_joint_trajectory(traj2)
    print("Trajectory 2 Completed.")

    # Optionally, you can add gripper commands here if needed
    # e.g., Open or close gripper after grasping

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Robot Checkpoint Script")
    args = parser.parse_args()

    main()
