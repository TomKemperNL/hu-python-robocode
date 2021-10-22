class Game:
    def __init__(self):
        self.game_objects = []

    def add(self, obj):
        self.game_objects.append(obj)

    def remove(self, obj):
        self.game_objects.remove(obj)
