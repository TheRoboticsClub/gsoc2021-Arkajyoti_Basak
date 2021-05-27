#!/usr/bin/python

import mavros_msgs.msg
import mavros_msgs.srv
import geometry_msgs.msg
import threading
import sys

from rospyHandler import RosHandler
from topicService import TopicService

MODE_OFFBOARD = "OFFBOARD"

class RoverHandler(RosHandler):
    def __init__(self):
        super().__init__()
        self.armed = False
        self.mode = ""

        self.TOPIC_STATE = TopicService("/mavros/state", mavros_msgs.msg.State)
        self.SERVICE_ARM = TopicService("/mavros/cmd/arming", mavros_msgs.srv.CommandBool)
        self.SERVICE_LAND = TopicService("/mavros/cmd/land", mavros_msgs.srv.CommandTOL)
        self.SERVICE_SET_MODE = TopicService("/mavros/set_mode", mavros_msgs.srv.SetMode)
        self.TOPIC_SET_POSE_LOCAL = TopicService('/mavros/setpoint_raw/local', mavros_msgs.msg.PositionTarget)
        self.TOPIC_GET_POSE_LOCAL = TopicService('/mavros/local_position/pose', geometry_msgs.msg.PoseStamped)

        self.is_z = threading.Event()
        self.is_landing = threading.Event()
        self.is_setting_pos = threading.Event()

    def enable_topics_for_read(self):
        self.topic_subscriber(self.TOPIC_STATE)
        self.topic_subscriber(self.TOPIC_GET_POSE_LOCAL)

    def arm(self, status: bool):
        data = mavros_msgs.srv.CommandBoolRequest()
        data.value = status
        self.SERVICE_ARM.set_data(data)
        result = self.service_caller(self.SERVICE_ARM, timeout=30)

    def takeoff(self, z: float):
        print("Taking off!!!")
        self.is_z.clear()
        self.is_landing.clear()
        self.is_setting_pos.clear()
        while True:
            self.update_parameters_from_topic(z)
            vx = 0.0
            vy = 0.0
            vz = 0.5 if not self.is_z.is_set() else 0.0001
            if not self.armed:
                self.arm(True)
            if not self.mode == MODE_OFFBOARD:
                self.change_mode(MODE_OFFBOARD)
            if self.is_landing.is_set() or self.is_setting_pos.is_set():
                sys.exit()
            else:
                self.move(vx,vy,vz)

    def land(self):
        print("Landing!!!")
        self.is_landing.set()
        self.is_z.clear()
        self.is_setting_pos.clear()
        data = mavros_msgs.srv.CommandTOLRequest()
        data.latitude = self.local_position_x
        data.longitude = self.local_position_y
        data.altitude = 0
        self.SERVICE_LAND.set_data(data)
        result = self.service_caller(self.SERVICE_LAND, timeout=30)

    def set_vel(self, vx: float, vy: float, z: float):
        self.is_z.clear()
        self.update_parameters_from_topic(z)
        vz = 1.0 if not self.is_z.is_set() else 0.0001
        if not self.armed:
            self.arm(True)
        if not self.mode == MODE_OFFBOARD:
            self.change_mode(MODE_OFFBOARD)
        else:
            self.move(vx, vy, vz)

    def change_mode(self, mode: str):
        data = mavros_msgs.srv.SetModeRequest()
        data.custom_mode = mode
        self.SERVICE_SET_MODE.set_data(data)
        result = self.service_caller(self.SERVICE_SET_MODE, timeout=30)

    def move(self, vx: float, vy:float, vz: float):
        data = mavros_msgs.msg.PositionTarget()
        data.coordinate_frame = 8
        data.position.x = 0.0
        data.position.y = 0.0
        data.position.z = 0.0
        data.velocity.x = vx
        data.velocity.y = vy
        data.velocity.z = vz
        self.TOPIC_SET_POSE_LOCAL.set_data(data)
        self.topic_publisher(topic=self.TOPIC_SET_POSE_LOCAL)

    def update_parameters_from_topic(self, z: float):
        data_state = self.TOPIC_STATE.get_data()
        if data_state is not None:
            self.armed = data_state.armed
            self.mode = data_state.mode

        data_get_pose_local = self.TOPIC_GET_POSE_LOCAL.get_data()
        if data_get_pose_local is not None:
            self.local_position_x = data_get_pose_local.pose.position.x
            self.local_position_y = data_get_pose_local.pose.position.y
            self.local_position_z = data_get_pose_local.pose.position.z

            if self.local_position_z >= z:
                self.is_z.set()