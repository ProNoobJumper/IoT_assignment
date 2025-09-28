from schedule import Schedule
from menu_handler import MenuHandler


class SmartHomeSystem:
    def __init__(self):
        self.devices = {}
        self.schedules = []

    def add_device(self, device):
        self.devices[device.name] = device

    def remove_device(self, device_name):
        if device_name in self.devices:
            del self.devices[device_name]
            self.clear_schedule(device_name)  # Also remove associated schedules
            return True
        return False

    def get_device(self, device_name):
        return self.devices.get(device_name)

    def get_all_devices(self):
        return list(self.devices.values())

    def create_schedule(self, device_name, start_time, end_time):
        if device_name in self.devices:
            schedule = Schedule(device_name, start_time, end_time)
            self.schedules.append(schedule)
            return True
        return False

    def get_all_schedules(self):
        return self.schedules

    def clear_schedule(self, device_name):
        self.schedules = [s for s in self.schedules if s.device_name != device_name]


if __name__ == "__main__":
    system = SmartHomeSystem()
    menu = MenuHandler(system)
    menu.run()