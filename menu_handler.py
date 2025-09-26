from devices import Light, Fan, AC, WashingMachine

class MenuHandler:
    def __init__(self, system):
        self.system = system

    def display_main_menu(self):
        print("\n=== Smart Home Menu ===")
        print("1. Add Device")
        print("2. List All Devices")
        print("3. Get Device Status")
        print("4. Control Device")
        print("5. Create Device Schedule")
        print("6. Manage Device Schedule")
        print("7. View All Schedules")
        print("8. Exit")

    def handle_add_device(self):
        name = input("Device name: ")
        device_type = input("Type (light/fan/ac/washing): ").lower()

        if device_type == "light":
            device = Light(name)
        elif device_type == "fan":
            device = Fan(name)
        elif device_type == "ac":
            device = AC(name)
        elif device_type == "washing":
            device = WashingMachine(name)
        else:
            print("Invalid type!")
            return

        self.system.add_device(device)
        print(f"{name} added!")

    def handle_list_devices(self):
        devices = self.system.get_all_devices()
        if not devices:
            print("No devices found.")
            return
        for device in devices:
            status = "ON" if device.get_power_status() else "OFF"
            print(f"{device.name} ({device.__class__.__name__.lower()}) - {status}")

    def handle_device_status(self):
        name = input("Device name: ")
        device = self.system.get_device(name)
        if device:
            print(device.get_device_info())
        else:
            print("Device not found!")

    def handle_control_device(self):
        name = input("Device name: ")
        device = self.system.get_device(name)
        if not device:
            print("Device not found!")
            return

        action = input("Action (on/off/adjust): ").lower()
        if action == "on":
            device.turn_on()
            print(f"{name} turned ON")
        elif action == "off":
            device.turn_off()
            print(f"{name} turned OFF")
        elif action == "adjust":
            device.adjust_settings()
            print("Settings adjusted!")

    def handle_create_schedule(self):
        name = input("Device name: ")
        if not self.system.get_device(name):
            print("Device not found!")
            return
        start_time = input("Start time (HH:MM): ")
        end_time = input("End time (HH:MM): ")
        self.system.create_schedule(name, start_time, end_time)
        print("Schedule created!")

    def handle_manage_schedule(self):
        name = input("Device name: ")
        schedules = [s for s in self.system.get_all_schedules() if s.device_name == name]
        if not schedules:
            print("No schedules found for this device.")
            return

        print(f"Schedules for {name}:")
        for i, schedule in enumerate(schedules):
            print(f"{i+1}. {schedule.start_time} - {schedule.end_time}")

        choice = input("Clear schedule? (y/n): ")
        if choice.lower() == 'y':
            self.system.clear_schedule(name)
            print("Schedules cleared!")

    def handle_view_schedules(self):
        schedules = self.system.get_all_schedules()
        if not schedules:
            print("No schedules found.")
            return
        for schedule in schedules:
            print(schedule.get_schedule_info())

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Choose option (1-8): ")

            if choice == "1":
                self.handle_add_device()
            elif choice == "2":
                self.handle_list_devices()
            elif choice == "3":
                self.handle_device_status()
            elif choice == "4":
                self.handle_control_device()
            elif choice == "5":
                self.handle_create_schedule()
            elif choice == "6":
                self.handle_manage_schedule()
            elif choice == "7":
                self.handle_view_schedules()
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")