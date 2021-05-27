#!/usr/bin/python

import rospy
from topicService import TopicService


class RosHandler:
    def __init__(self):
        rospy.init_node('ros_handler', anonymous=True)
        rospy.loginfo("Rospy is up!!!")

    @staticmethod
    def topic_publisher(topic: TopicService):
        pub = rospy.Publisher(topic.get_name(), topic.get_type(), queue_size=10)
        pub.publish(topic.get_data())

    @staticmethod
    def topic_subscriber(topic: TopicService):
        rospy.Subscriber(topic.get_name(), topic.get_type(), topic.set_data)

    @staticmethod
    def service_caller(service: TopicService, timeout=30):
        try:
            srv = service.get_name()
            typ = service.get_type()
            data = service.get_data()

            rospy.wait_for_service(srv, timeout=timeout)
            call_srv = rospy.ServiceProxy(srv, typ)
            return call_srv(data)

        except rospy.ROSException as e:
            print("ROS ERROR:", e)
        except rospy.ROSInternalException as e:
            print("ROS ERROR:", e)
        except KeyError as e:
            print("ERROR:", e)
        return None