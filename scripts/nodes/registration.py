#!/usr/bin/env python3

import rospy

import numpy as np

from open3d_resources.noetic import R3DROS

if __name__ == "__main__":
    rospy.init_node("registration", anonymous=False)
    vehicle_name = "Hydrone"
    depth_trunc = 100
    width = 672
    height = 376
    fov = 90
    rospy.logwarn('registration.py - main')
    # map = R3DROS(vehicle_name, depth_trunc, width, height, fov)
    

    # rospy.spin()
