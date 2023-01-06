class Parts:  # for organizing the data for all products
    """Holds the information for a product"""
    def __init__(self, p_type, color, quadrant, rotation):
        self.pType = p_type
        self.color=color
        self.quadrant=quadrant
        self.rotation=rotation
class Bin:  # for holding information about present bins
    """Holds information for the bin"""
    def __init__(self, name, type, color, slots, rotation, flipped):
        self.binName=name
        self.type=type
        self.color=color
        self.slots=slots
        self.rotation=rotation
        self.flipped=flipped

class PartConv:  # for holding information about parts for the conveyor belt
    """Holds data about parts for the conveyor belt"""
    def __init__(self, type, color, number, offset, rotation):
        self.type=type
        self.color=color
        self.number=number
        self.offset=offset
        self.rotation=rotation

class Order:  # for holding information about orders
    def __init__(self,category, id, type, priority,agvNumber, trayId, destination, station):
        self.category=category
        self.id=id
        self.type=type
        self.priority=priority
        self.agvNumber=agvNumber
        self.trayId=trayId
        self.destination=destination
        self.station=station
        

class KittingProds:
    def __init__(self, orderID, type, color, quadrant):
        self.orderId=orderID
        self.type=type
        self.color=color
        self.quadrant=quadrant

class AssemblyProds:
    def __init__(self, orderID, type, color, xyz, rpy, direction):
        self.orderId=orderID
        self.type=type
        self.color=color
        self.xyz=xyz
        self.rpy=rpy
        self.direction=direction

class OrderChallenge:
    def __init__(self, orderId, challengeType, quadrant):
        self.ord=orderId
        self.type=challengeType
        self.quadrant=quadrant

class RobotMalfunction:
    def __init__(self, duration, roboToDisable, type, color, agv):
        self.duration=duration
        self.robot=roboToDisable
        self.type=type
        self.color=color
        self.agv=agv

class FaultyPart:
    def __init__(self, orderID, quadrant):
        self.orderID=orderID
        self.quadrant=quadrant