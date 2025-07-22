# Smart Home Control System

class Device:
    def __init__(self, name):
        self.name = name
        self.status = False  # Off by default

    def operate(self):
        raise NotImplementedError("Subclasses must override operate() method")

    def turn_on(self):
        self.status = True
        print(f"{self.name} turned ON.")

    def turn_off(self):
        self.status = False
        print(f"{self.name} turned OFF.")


class Light(Device):
    def operate(self):
        action = "ON" if not self.status else "OFF"
        print(f"Toggling Light: Turning {action}")
        if self.status:
            self.turn_off()
        else:
            self.turn_on()


class AC(Device):
    def operate(self):
        action = "ON" if not self.status else "OFF"
        print(f"Toggling AC: Turning {action}")
        if self.status:
            self.turn_off()
        else:
            self.turn_on()


class Fan(Device):
    def operate(self):
        action = "ON" if not self.status else "OFF"
        print(f"Toggling Fan: Turning {action}")
        if self.status:
            self.turn_off()
        else:
            self.turn_on()


class SmartHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Device '{device.name}' added to SmartHub.")

    def control_all(self):
        print("\nSmartHub Operating All Devices:")
        for device in self.devices:
            device.operate()


# ----------------------
# 📌 Sample Usage
# ----------------------

if __name__ == "__main__":
    # Creating device objects
    light1 = Light("Living Room Light")
    ac1 = AC("Bedroom AC")
    fan1 = Fan("Ceiling Fan")

    # Creating SmartHub and adding devices
    hub = SmartHub()
    hub.add_device(light1)
    hub.add_device(ac1)
    hub.add_device(fan1)

    # Operate all devices
    hub.control_all()

    # Re-operate to toggle OFF
    hub.control_all()
