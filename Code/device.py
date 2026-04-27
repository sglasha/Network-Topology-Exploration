class Device:
    def __init__(self, name):
        self.name = name
        self.connections = []
        self.is_damaged = False

    def add_connection(self, connection):
        self.connections.append(connection)

    def get_connections(self):
        return self.connections

    def get_is_damaged(self):
        return self.is_damaged

    def damage(self):
        self.is_damaged = True

    def fix(self):
        self.is_damaged = False

    def __str__(self):
        return f"{self.name}"