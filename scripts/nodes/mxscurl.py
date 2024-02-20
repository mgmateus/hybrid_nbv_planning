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
    env = EnvironmentROS(ip, 'Hydrone', 'stereo', 'rgb')
    
    # meshs = env.vehicle.simGetMeshPositionVertexBuffers()
    # rospy.logwarn(f"observation : {meshs[0]}")
    v = Vector3r(401.95086669921875, -2541.569580078125, 1612.45849609375)
    env.vehicle.simPlotPoints([v], size= 500, is_persistent = True)    
    # action = np.array([.3, .5, -1, .1, .1, .1])
    # env.vehicle.take_off()
    # for i in range(500):
    #     pp = env.step(action)
        
        
    #     rospy.Rate(10).sleep()
    
    # 401.95086669921875,                                                              
    #                 -2541.569580078125,                                                              
    #                 1612.45849609375
