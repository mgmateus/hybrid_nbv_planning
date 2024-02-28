FROM nvidia/cuda:12.3.1-devel-ubuntu20.04

USER root

RUN useradd -m airsim && echo "airsim:airsim" | chpasswd && adduser airsim sudo

RUN apt-get -y update && apt-get -yy install locales lsb-release 
ARG DEBIAN_FRONTEND=noninteractive
RUN dpkg-reconfigure locales
RUN apt install -y git 
RUN apt install -y wget

WORKDIR /home/airsim

# Install ROS Noetic
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
RUN apt-get update \
 && apt-get install -y --no-install-recommends ros-noetic-desktop-full
RUN apt-get install -y --no-install-recommends python3-rosdep
RUN rosdep init \
 && rosdep fix-permissions \
 && rosdep update

RUN apt-get install -y ros-noetic-mavros ros-noetic-mavros-extras
RUN apt-get install -y ros-noetic-tf2-sensor-msgs ros-noetic-tf2-tools
RUN apt-get install -y python3-catkin-tools
RUN apt-get install -y python3-pip

RUN git clone https://github.com/microsoft/AirSim.git

WORKDIR AirSim

RUN ./setup.sh 

RUN ./build.sh

USER airsim