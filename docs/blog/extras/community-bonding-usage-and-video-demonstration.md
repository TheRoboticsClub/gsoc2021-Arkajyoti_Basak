---
layout: page
title: Usage and Video Demonstration of the Qt widget
---

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

## Video Demonstration

<div class="video_container">
<iframe src="https://youtube.com/embed/L2CJCvOHqHQ?mute=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen class="video"></iframe>
</div>