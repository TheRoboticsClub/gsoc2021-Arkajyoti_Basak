# Community Bonding

## Week 1 & 2

**[Blog link](https://theroboticsclub.github.io/gsoc2021-Arkajyoti_Basak/blog/2021-05-27-Community-Bonding-Week-1-&-2/)**

### Usage

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