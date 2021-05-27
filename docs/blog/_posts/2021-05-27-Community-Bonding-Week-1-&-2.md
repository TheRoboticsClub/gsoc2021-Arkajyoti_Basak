---
layout: post
title: Community Bonding Week 1 & 2
---

# Community Bonding Week 1 & 2

The goal was to understand ROS better. Learnt how to add sensor to a robot, create a simple PyQt5 widget and learn ROS-Control. Created a simple Qt widget to control a drone in Gazebo simulator.

## Usage

```bash
cd ~ && git clone https://github.com/TheRoboticsClub/gsoc2021-Arkajyoti_Basak.git
cd ~/gsoc2021-Arkajyoti_Basak/community_bonding
ln -s $PWD/assets/ ~/catkin_ws/src/
roscd && catkin build
```

```bash
roslaunch ~/gsoc2021-Arkajyoti_Basak/community_bonding/drone_laser.launch
```

```bash
python ~/gsoc2021-Arkajyoti_Basak/community_bonding/drone_controller/widget/widget.py
```

## Video

<iframe width="840" height="720" src="https://youtube.com/embed/L2CJCvOHqHQ?controls=1&mute=1" frameborder="0" allowfullscreen> </iframe>

## Next Goals

- Turn the PyQt5 widget into a Rqt Plugin.
- Explore and learn MoveIt.