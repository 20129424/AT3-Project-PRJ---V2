class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None, displays=None):
        # Initialize the attributes with the given parameters or default values
        self.location = location
        self.capacity = capacity
        # For lists, we use an empty list if None is provided
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        # Return a string with the car park's location and capacity
        return f"Car park at {self.location}, with {self.capacity} bays."
