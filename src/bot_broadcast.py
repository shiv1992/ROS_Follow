#!/usr/bin/env python
 
import roslib
roslib.load_manifest('lab1')
import rospy
import tf
import turtlesim.msg
from nav_msgs.msg import Odometry
 
def handle_turtle_pose(msg, turtlename):

     br = tf.TransformBroadcaster()
     pos = (msg.pose.pose.position.x,
             msg.pose.pose.position.y,
             msg.pose.pose.position.z)
     ori = (msg.pose.pose.orientation.x,
             msg.pose.pose.orientation.y,
             msg.pose.pose.orientation.z,
             msg.pose.pose.orientation.w)	
     br.sendTransform(pos,ori,rospy.Time.now(),turtlename,"world") 


if __name__ == '__main__':
    rospy.init_node('bot_broadcast')
    rospy.Subscriber('/robot_0/base_pose_ground_truth',Odometry,handle_turtle_pose,'/robot_0/odom')
    rospy.Subscriber('/robot_1/base_pose_ground_truth',Odometry,handle_turtle_pose,'/robot_1/odom')
    rospy.spin()
