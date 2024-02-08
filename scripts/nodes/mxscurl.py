#!/usr/bin/env python3

import rospy
import time

import numpy as np


from gym_airsim.environments import Environment

if __name__ == "__main__":
    rospy.init_node("mxscurl", anonymous=False)
    env = Environment("Hydrone")
    
    action = np.array([0, 0, -1, 0, 1, 0])
    env.vehicle.take_off()
    time.sleep(4)
    for i in range(100):
        env.step(action)
        rospy.Rate(10).sleep()
