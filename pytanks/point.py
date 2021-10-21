class Point():
    def __init__(self, arg1, arg2=None):
        if arg2 is None:
            self.x = arg1[0]
            self.y = arg1[1]
        else:
            self.x = arg1
            self.y = arg2

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise Exception("Nope, only got 2")

    def __len__(self):
        return 2
