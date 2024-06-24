class Display:
    def __init__(self, display_id, car_park, message="", is_on=False):
        # Initialize the attributes with the given parameters or default values
        self.display_id = display_id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        # Return a string with the display's ID and message
        return f"Display {self.display_id}: {self.message}"
