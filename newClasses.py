class Parts:  # for organizing the data for all products
    """Holds the information for a product"""
    def __init__(self, p_type, color, quadrant, rotation):
        self.pType = p_type
        self.color=color
        self.quadrant=quadrant
        self.rotation=rotation