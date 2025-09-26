class Device:
    def __init__(self, name):
        self.name = name
        self.power = False

    def turn_on(self):
        self.power = True

    def turn_off(self):
        self.power = False

    def get_power_status(self):
        return self.power

    def adjust_settings(self):
        pass

    def get_device_info(self):
        pass


class Light(Device):
    def __init__(self, name):
        super().__init__(name)
        self.brightness = 50

    def adjust_settings(self):
        brightness = int(input("Brightness (0-100): "))
        self.brightness = max(0, min(100, brightness))

    def get_device_info(self):
        status = "ON" if self.power else "OFF"
        return f"{self.name} (light) - {status}, Brightness: {self.brightness}"


class Fan(Device):
    def __init__(self, name):
        super().__init__(name)
        self.speed = 3

    def adjust_settings(self):
        speed = int(input("Speed (1-5): "))
        self.speed = max(1, min(5, speed))

    def get_device_info(self):
        status = "ON" if self.power else "OFF"
        return f"{self.name} (fan) - {status}, Speed: {self.speed}"


class AC(Device):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = 20

    def adjust_settings(self):
        temp = int(input("Temperature (15-25): "))
        self.temperature = max(15, min(25, temp))

    def get_device_info(self):
        status = "ON" if self.power else "OFF"
        return f"{self.name} (ac) - {status}, Temperature: {self.temperature}°C"


class WashingMachine(Device):
    def __init__(self, name):
        super().__init__(name)
        self.mode = "Wash"

    def adjust_settings(self):
        mode = input("Mode (Wash/Spin/Dry): ")
        self.mode = mode

    def get_device_info(self):
        status = "ON" if self.power else "OFF"
        return f"{self.name} (washing) - {status}, Mode: {self.mode}"