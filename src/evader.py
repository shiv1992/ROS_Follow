#!/usr/bin/env python

import roslib; roslib.load_manifest('lab1')
import rospy
import random

# Twist and LaserScan
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan



x_speed = 2.0  # 2.0 m/s
p = rospy.Publisher('/cmd_vel', Twist)
twist = Twist()
twist.linear.x = x_speed;
twist.linear.y = 0; twist.linear.z = 0;     # we can't use these!        
twist.angular.x = 0; twist.angular.y = 0;   # or these!
twist.angular.z = 0; 


def callback(data):
	
	tmp=data.ranges
	ctra=0	
	k = [i for i in tmp if i<1.5]
	ctra=len(k)	
	
	if ctra>20 :
		pt = random.uniform(0,1.74)
		twist.linear.x = 0;
		twist.angular.z = pt; 
		p.publish(twist)

	else:
		twist.linear.x = x_speed;
		twist.angular.z = 0;
		p.publish(twist)
		
	return	

# Main File
if __name__=="__main__":

    rospy.init_node('evade')
    	   
    rospy.loginfo("About to be moving forward!")
   
    while(1):
	p2 = rospy.Subscriber('/base_scan', LaserScan, callback)
	rospy.sleep(0.2)	
	
    rospy.loginfo("Stopping!")



