#!/usr/bin/env python
import rclpy
from rclpy.node import Node
import numpy as np

from snapstack_msgs2.msg import QuadFlightMode
from behavior_selector2.srv import MissionModeChange

NOT_FLYING = 0
FLYING = 1

class Behavior_Selector(Node):

    def __init__(self):
        super().__init__('behavior_selector')
        self.status = NOT_FLYING
        self.pubEvent    = self.create_publisher(QuadFlightMode, "globalflightmode", 1)
        self.flightevent = QuadFlightMode()
        
    def sendEvent(self):
        self.flightevent.header.stamp = self.get_clock().now()
        self.pubEvent.publish(self.flightevent)

    def change_mode(self,req):
        if req.mode == req.KILL:
            self.status = NOT_FLYING
            self.flightevent.mode = QuadFlightMode.KILL
            self.sendEvent()
        
        if req.mode == req.END and self.status == FLYING:
            self.flightevent.mode = QuadFlightMode.LAND
            self.sendEvent()

        if req.mode == req.START:
            self.status = FLYING
            self.flightevent.mode = QuadFlightMode.GO
            self.sendEvent()

    def srvCB(self,req):
        self.change_mode(req)
        return True
                  
def startNode():
    c = Behavior_Selector()
    # s = rclpy.Service("change_mode", MissionModeChange, c.srvCB)
    s = c.create_service(MissionModeChange, "change_mode", c.srvCB)
    rclpy.spin(c)

def main(args=None):
    rclpy.init(args=args)
    print ("Starting behavior selector")   
    startNode()

if __name__ == '__main__':
    main()
