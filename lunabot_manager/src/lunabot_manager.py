#! /usr/bin/env python

import roslib
roslib.load_manifest('lunabot_manager')
import rospy
import actionlib
from std_msgs.msg import String
from explore_lite.msg import ExploreAction, ExploreGoal, ExploreActionResult

hasgoal=false

def setvalue(msg):
    hasgoal=false

def callback(msg):
    if(msg.data=='start'):
        goal = ExploreGoal()
        client.send_goal(goal)
        hasgoal=true
    elif(msg.data=='cancel'):
        client.cancel_all_goals()
        hasgoal=false

def manager():
    hasgoal=false
    rospy.init_node('explore_client')
    subscriber = rospy.Subscriber('operator', String, callback)
    resultListener = rospy.Subscriber('explore/result', ExploreActionResult, setvalue)
    client = actionlib.SimpleActionClient('explore', ExploreAction)
    rospy.loginfo('client is waiting')
    client.wait_for_server()
    rospy.loginfo('client found server')

    goal = ExploreGoal()
    client.send_goal(goal)


    rospy.spin()

if __name__ == '__main__':
    manager()
