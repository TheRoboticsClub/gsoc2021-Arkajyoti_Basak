---
layout: post
title: Final Blog
---

# Final Blog
> *Final Blog and Report*


## **Project Overview**

[JdeRobot](https://jderobot.github.io/)'s [Robotics-Academy](https://github.com/JdeRobot/RoboticsAcademy) is a framework for learning robotics and computer vision. It consists of a collection of robot programming exercises using Python language where the student has to code the behavior of a given (either simulated or real) robot to fit some task related to robotics or computer vision. It uses standard middleware and libraries as ROS and OpenCV, so the student learns the state-of-the-art tools.

The main [goal](https://jderobot.github.io/activities/gsoc/2021#project-2-robotics-academy-new-drone-based-exercises) of my project is to migrate the drone exercises from v2.1 (ROS node based) to v2.3 (Web/Docker-based) of the Robotics Academy. Introduce a new drone-based exercise: Drone Package Delivery in ROS-noetic and Gazebo-11 and create their requisite gazebo models.


## **Completed**

![img](/gsoc2021-Arkajyoti_Basak/assets/img/blogs/ohyeah.gif)

All the 9 drone exercises of RoboticsAcademy are now available in a web-based template. 3 new Gazebo models are now available in drone_assets. Almost all the web-based exercises of RoboticsAcademy are now available in ROS1-Noetic (with hardware acceleration support only for Ubuntu+NVIDIA). The 9 drone exercises have support for on-demand logs ([instructions](https://github.com/JdeRobot/RoboticsAcademy/pull/1100#issuecomment-874701845)). The drone-cat-mouse exercise has support for automatic evaluation of the cat robot (testing).


## **Important Links**

| Name | Docs | Teaser |
| ---- | ---- | ------ |
| Drone Cat and Mouse | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/drone_cat_mouse) | [Teaser](https://youtu.be/0dV8OkTG0pM) |
| Follow Turtlebot | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/follow_turtlebot) | [Teaser](https://youtu.be/r4etz1-pm4k) |
| Follow Road |[Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/follow_road) | [Teaser](https://youtu.be/DdwsbH944M8) |
| Labyrinth Escape | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/labyrinth_escape) | [Teaser](https://youtu.be/e2-BE1KKtm0) |
| Position Control | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/position_control) | [Teaser](https://youtu.be/VF5tj0xFpe0) |
| Rescue People | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/rescue_people) | [Teaser](https://youtu.be/ee_T46fpHN8) |
| Drone Gymkhana | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/drone_gymkhana) | [Teaser](https://youtu.be/68GSXnOTUNs) |
| Drone Hangar | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/drone_hangar) | - |
| Visual Lander | [Docs](https://jderobot.github.io/RoboticsAcademy/exercises/Drones/visual_lander) | [Teaser](https://youtu.be/ScQbVwzqGZA) |


## **Future Work**

Comparing to the proposal, few changes were made in the last week to focus on the automatic evaluation of the drone-cat-mouse exercise. Thus, the new exercise - Drone Package Delivery remains as future work.

The connection protocol for the multi-drone exercise ([issue #1165](https://github.com/JdeRobot/RoboticsAcademy/issues/1165)) discussed in the Week 4 blog remains as future work.


## **Issues and Pull Requests**

| Issue | New drone_assets | PR |
| ---------- | ---------- | -- |
| [126](https://github.com/JdeRobot/drones/issues/126)| ocean | [127](https://github.com/JdeRobot/drones/pull/127), [128](https://github.com/JdeRobot/drones/pull/128)|
| [109](https://github.com/JdeRobot/drones/issues/109)|  simple_labyrinth_green | [110](https://github.com/JdeRobot/drones/pull/110), [111](https://github.com/JdeRobot/drones/pull/111) |
| [119](https://github.com/JdeRobot/drones/issues/119)| slab | [121](https://github.com/JdeRobot/drones/pull/121), [120](https://github.com/JdeRobot/drones/pull/120)|

| Issue | Web Templates | PR |
| ---------- | ---------- | -- |
| [1019](https://github.com/JdeRobot/RoboticsAcademy/issues/1019)| Labyrinth-Escape | [1020](https://github.com/JdeRobot/RoboticsAcademy/pull/1020)|
| [1042](https://github.com/JdeRobot/RoboticsAcademy/issues/1042)| Position-Control | [1043](https://github.com/JdeRobot/RoboticsAcademy/pull/1043)|
| [1056](https://github.com/JdeRobot/RoboticsAcademy/issues/1056)| Rescue People | [1057](https://github.com/JdeRobot/RoboticsAcademy/pull/1057)|
| [1061](https://github.com/JdeRobot/RoboticsAcademy/issues/1061)| Drone Hangar | [1075](https://github.com/JdeRobot/RoboticsAcademy/pull/1075)|
| [1061](https://github.com/JdeRobot/RoboticsAcademy/issues/1061)| Drone Gymkhana | [1075](https://github.com/JdeRobot/RoboticsAcademy/pull/1075)|
| [1061](https://github.com/JdeRobot/RoboticsAcademy/issues/1061)| Visual Lander | [1075](https://github.com/JdeRobot/RoboticsAcademy/pull/1075)|

| Issue | RADI-3(ROS1-Noetic) | PR |
| ---------- | ---------- | -- |
| [1026](https://github.com/JdeRobot/RoboticsAcademy/issues/1026)| New RADI 3.1.0 | [1027](https://github.com/JdeRobot/RoboticsAcademy/pull/1027) |
| [1026](https://github.com/JdeRobot/RoboticsAcademy/issues/1028)| Remaining exercises| [1051](https://github.com/JdeRobot/RoboticsAcademy/pull/1051) |

| Issue | Other features | PR |
| ---------- | ---------- | -- |
| [1099](https://github.com/JdeRobot/RoboticsAcademy/issues/1099)| On-demand logs | [1100](https://github.com/JdeRobot/RoboticsAcademy/pull/1100)|
| [1021](https://github.com/JdeRobot/RoboticsAcademy/issues/1021)| Sequential launching | [1038](https://github.com/JdeRobot/RoboticsAcademy/pull/1038)|
| [1121](https://github.com/JdeRobot/RoboticsAcademy/issues/1121)| Automatic evaluator | [1202](https://github.com/JdeRobot/RoboticsAcademy/pull/1202)|

Above is the list of important pull requests. The complete list of issues solved and all the merged PRs can be found [here](https://theroboticsclub.github.io/gsoc2021-Arkajyoti_Basak/progress/) or [here](https://github.com/JdeRobot/RoboticsAcademy/pulls?q=is%3Apr+is%3Aclosed+author%3Aiamarkaj).


## **Final Thoughts** 

It has been a great journey till now and I can only see it becoming better. The tasks I’ve completed so far have really allowed me to tie all of my knowledge together and create an overall view of what I know.

Thank You to JdeRobot and Google Summer of Code. Writing open-source source software has been a valuable learning experience for me, and I am excited to keep contributing to the JdeRobot community. Thank you to Pedro, Nikhil, Prof. JoseMaría Cañas and other admins. Your mentorship and support have made this a very special experience for me.

![img](/gsoc2021-Arkajyoti_Basak/assets/img/blogs/bye.gif)

*[ROS]: Robot Operating System
*[PID]: Proportional-Integral-Derivative Controller
*[RADI]: RoboticsAcademy Docker Image
*[SITL]: Software In The Loop
*[MAVROS]: MAVLink extendable communication node for ROS