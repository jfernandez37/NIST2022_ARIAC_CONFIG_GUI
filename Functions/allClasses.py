class Order:  # for organizing the data from the order menu
    """Holds the information for an order"""
    def __init__(self, priority, k_health, a_health, an_cond, cond_val, kit_info, assem_info):
        self.priority = priority
        self.kittingHealth = k_health
        self.assemblyHealth = a_health
        self.announcementCondition = an_cond
        self.conditionValue = cond_val
        self.kitting = kit_info
        self.assembly = assem_info


class Kitting:  # for organizing the data from the kitting menu
    """Holds the information for a kitting order"""
    def __init__(self, ship_count, tray, second_tray, agv, second_agv, destinations, second_dest, products):
        self.shipmentCount = ship_count
        self.tray = tray
        self.secondTray = second_tray
        self.agv = agv
        self.secondAgv = second_agv
        self.destinations = destinations
        self.secondDest = second_dest
        self.products = products


class Assembly:  # for organizing the data from the assembly menu
    """Holds the information for an assembly order"""
    def __init__(self, ship_count, stations, products):
        self.shipmentCount = ship_count
        self.stations = stations
        self.products = products


class Products:  # for organizing the data for all products
    """Holds the information for a product"""
    def __init__(self, p_type, xyz, rpy):
        self.pType = p_type
        self.xyz = xyz
        self.rpy = rpy


class ModelOverBin:  # for organizing the data from the models over bins menu
    """Holds the information for a bin for models over bins"""
    def __init__(self, bin_num, prod_temp, start, end, rpy, num_mod_x, num_mod_y):
        self.binNum = bin_num
        self.product = prod_temp
        self.xyz_start = start
        self.xyz_end = end
        self.rpy = rpy
        self.num_mod_x = num_mod_x
        self.num_mod_y = num_mod_y


class ModelOverStation:  # for organizing the data from the models over stations menu
    """Holds the information for a station for the models over stations"""
    def __init__(self, station, part, xyz, rpy):
        self.station = station
        self.part = part
        self.xyz = xyz
        self.rpy = rpy


class BeltCycle:  # for organizing the data from the belt models menu
    """Holds the information for a belt cycle"""
    def __init__(self, part, time, xyz, rpy):
        self.part = part
        self.time = time
        self.xyz = xyz
        self.rpy = rpy


class Drops:  # for organizing the data from the drops menu
    """Holds the information for a drop region"""
    def __init__(self, drops_frame, min_xyz, max_xyz, dest_xyz, dest_rpy, type_to_drop, robot_type):
        self.frame = drops_frame
        self.minXyz = min_xyz
        self.maxXyz = max_xyz
        self.destXyz = dest_xyz
        self.destRpy = dest_rpy
        self.typeToDrop = type_to_drop
        self.robotType = robot_type


class PresentProducts:  # holds the products which from bins
    """Holds the products which are present in the program"""
    def __init__(self, product_type, num):
        self.pType = product_type
        self.pNum = num


class RobotBreakdown:
    """Holds the information about robot breakdowns for the robot breakdown agility challenge"""
    def __init__(self, orderID, robot_type, location, number_of_products):
        self.orderID = orderID
        self.robotType=robot_type
        self.location = location
        self.numberProd = number_of_products