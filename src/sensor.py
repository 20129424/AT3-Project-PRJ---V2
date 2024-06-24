class Sensor:
    def __init__(self, sensor_id, assigned_car_park, sensor_type="unknown", status=False):
        # Initialize the attributes with the given parameters or default values
        self.sensor_id = sensor_id
        self.car_park = assigned_car_park
        self.sensor_type = sensor_type
        self.status = status

    def __str__(self):
        # Return a string with the sensor's ID, type, and status
        return f"Sensor {self.sensor_id} ({self.sensor_type}): {'Active' if self.status else 'Inactive'}"


class EntrySensor(Sensor):
    pass


class ExitSensor(Sensor):
    pass
