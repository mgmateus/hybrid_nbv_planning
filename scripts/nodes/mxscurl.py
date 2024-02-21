#!/usr/bin/env python3

import rospy
import time
import os 

import numpy as np


from gym_airsim.environments import EnvironmentROS
from gym_airsim.airsim_resources.airsim_base.types import Vector3r

if __name__ == "__main__":
    rospy.init_node("mxscurl", anonymous=False)
    ip = os.environ['UE4_IP']
    env = EnvironmentROS(ip, 'Hydrone', 'stereo', 'rgb', '/home/airsim/AirSim/ros/src/hybrid_nbv_planning/files/vertices', 'semi_sub_8')
    
    
    
    action = np.array([.3, .5, -1, .1, .1, .1])
    env.vehicle.take_off() 
    time.sleep(5)
    env.vehicle.test() 
    # for i in range(500):
    #     pp = env.step(action)
        
        
    #     rospy.Rate(10).sleep()
