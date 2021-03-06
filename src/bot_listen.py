#!/usr/bin/env python  
import roslib
roslib.load_manifest('lab1')
import rospy
import math
import tf
import geometry_msgs.msg

if __name__ == '__main__':

     rospy.init_node('bot_listen')
     listener = tf.TransformListener()
     
     turtle_vel = rospy.Publisher('robot_1/cmd_vel', geometry_msgs.msg.Twist)#,queue_size=10)	
     rate = rospy.Rate(10.0)
     rospy.sleep(1.0)	

     while not rospy.is_shutdown():
         try:
             now = rospy.Time.now()
	     past = now - rospy.Duration(1.0)	
	     listener.waitForTransformFull("/robot_1/odom", now,"/robot_0/odom", past,"/world", rospy.Duration(1.0))
             (trans, rot) = listener.lookupTransformFull("/robot_1/odom", now,"/robot_0/odom", past,"/world")
	     print trans	
	 except (tf.Exception, tf.LookupException, tf.ConnectivityException):
             continue
 
         angular = 4 * math.atan2(trans[1], trans[0])
         linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
         cmd = geometry_msgs.msg.Twist()
         cmd.linear.x = linear
         cmd.angular.z = angular
         turtle_vel.publish(cmd)
 
         rate.sleep()
