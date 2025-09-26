class Schedule:
    def __init__(self, device_name, start_time, end_time):
        self.device_name = device_name
        self.start_time = start_time
        self.end_time = end_time
        self.is_active = True

    def get_schedule_info(self):
        return f"{self.device_name}: {self.start_time} - {self.end_time}"