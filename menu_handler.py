from devices import Light, Fan, AC, WashingMachine

class MenuHandler:
    def __init__(self, system):
        self.system = system

    def display_main_menu(self):
        print("\n\n")
        print("                   /\\")
        print("                  /  \\")
        print("                 /    \\")
        print("                /      \\")
        print("               /        \\")
        print("              /          \\")
        print("             /            \\")
        print("            /              \\")
        print("           /                \\")
        print("          /                  \\")
        print("         /                    \\")
        print("        /                      \\")
        print("       /                        \\")
        print("      /                          \\")
        print("     /                            \\")
        print("    /                              \\")
        print("   /                                \\")
        print("  /                                  \\")
        print(" /____________________________________\\")
        print("╔══════════════════════════════════════╗")
        print("║                                      ║")
        print("║          🏡 Smart Home Menu 🏡       ║")
        print("║                                      ║")
        print("╠══════════════════════════════════════╣")
        print("║                                      ║")
        print("║   1. Add Device                      ║")
        print("║   2. List All Devices                ║")
        print("║   3. Get Device Status               ║")
        print("║   4. Control Device                  ║")
        print("║   5. Create Device Schedule          ║")
        print("║   6. Manage Device Schedule          ║")
        print("║   7. View All Schedules              ║")
        print("║   8. Exit                            ║")
        print("║                                      ║")
        print("╚══════════════════════════════════════╝")

    def handle_add_device(self):
        name = input("Enter device name: ")
        device_type = input("Select device type (light/fan/ac/washing): ").lower()

        if device_type == "light":
            device = Light(name)
        elif device_type == "fan":
            device = Fan(name)
        elif device_type == "ac":
            device = AC(name)
        elif device_type == "washing":
            device = WashingMachine(name)
        else:
            print("Invalid device type!")
            return

        self.system.add_device(device)
        print(f"✅ {name} has been successfully added!")

    def handle_list_devices(self):
        devices = self.system.get_all_devices()
        if not devices:
            print("No devices found in the system.")
            return
        print("\n--- All Devices ---")
        for i, device in enumerate(devices):
            status = "ON" if device.get_power_status() else "OFF"
            print(f"{i + 1}. 📱 {device.name} ({device.__class__.__name__.lower()}) - {status}")
        print("--------------------")

    def select_device(self):
        devices = self.system.get_all_devices()
        if not devices:
            print("No devices found in the system.")
            return None

        self.handle_list_devices()
        try:
            choice = int(input("Select a device by number: "))
            if 1 <= choice <= len(devices):
                return devices[choice - 1]
            else:
                print("Invalid choice!")
                return None
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

    def handle_device_status(self):
        device = self.select_device()
        if device:
            print(f"\n--- Device Status ---\n{device.get_device_info()}\n----------------------")

    def handle_control_device(self):
        device = self.select_device()
        if not device:
            return

        action = input("Choose action (on/off/adjust): ").lower()
        if action == "on":
            device.turn_on()
            print(f"💡 {device.name} turned ON")
        elif action == "off":
            device.turn_off()
            print(f"🔌 {device.name} turned OFF")
        elif action == "adjust":
            device.adjust_settings()
            print("Settings have been adjusted!")

    def handle_create_schedule(self):
        device = self.select_device()
        if not device:
            return
        start_time = input("Enter start time (HH:MM): ")
        end_time = input("Enter end time (HH:MM): ")
        self.system.create_schedule(device.name, start_time, end_time)
        print("📅 Schedule created successfully!")

    def handle_manage_schedule(self):
        device = self.select_device()
        if not device:
            return

        schedules = [s for s in self.system.get_all_schedules() if s.device_name == device.name]
        if not schedules:
            print("No schedules found for this device.")
            return

        print(f"\n--- Schedules for {device.name} ---")
        for i, schedule in enumerate(schedules):
            print(f"{i+1}. {schedule.start_time} - {schedule.end_time}")
        print("--------------------------")

        choice = input("Do you want to clear the schedule? (y/n): ")
        if choice.lower() == 'y':
            self.system.clear_schedule(device.name)
            print("Schedules have been cleared!")

    def handle_view_schedules(self):
        schedules = self.system.get_all_schedules()
        if not schedules:
            print("No schedules found.")
            return
        print("\n--- All Schedules ---")
        for schedule in schedules:
            print(schedule.get_schedule_info())
        print("---------------------")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Please choose an option (1-8): ")

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
                print("👋 Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.")