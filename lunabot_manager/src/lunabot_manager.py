#! /usr/bin/env python

import roslib
roslib.load_manifest('lunabot_manager')
import rospy
import actionlib

from explore_lite.msg import ExploreAction, ExploreGoal

if __name__ == '__main__':
    rospy.init_node('explore_client')
    client = actionlib.SimpleActionClient('explore', ExploreAction)
    rospy.loginfo('client is waiting')
    client.wait_for_server()
    rospy.loginfo('client found server')
    goal = ExploreGoal()
    # Fill in the goal here
    client.send_goal(goal)
    client.wait_for_result(rospy.Duration.from_sec(5.0))
