#!/usr/bin/env python3

import rospy
import time
import os 

import numpy as np


from gym_airsim.environments import EnvironmentROS

if __name__ == "__main__":
    rospy.init_node("mxscurl", anonymous=False)
    ip = os.environ['UE4_IP']
    env = EnvironmentROS(ip, 'Hydrone', 'stereo', 'rgb')
    
    action = np.array([.3, .5, -1, .1, .1, .1])
    env.vehicle.take_off()
    for i in range(500):
        pp = env.step(action)
        rospy.logwarn(f"observation : {pp}")
        rospy.Rate(10).sleep()
