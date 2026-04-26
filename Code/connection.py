class Connection:
    def __init__(self, device_a, device_b = None):
        self.device_a = device_a
        self.device_b = device_b
        self.is_damaged = False

    def damage(self):
        self.is_damaged = True

    def get_is_damaged(self):
        return self.is_damaged

    def get_other_device(self, device):
        if device == self.device_a:
            return self.device_b
        else:
            return self.device_a

    def __str__(self):
        return f"Connection: {self.device_a} to {self.device_b}"