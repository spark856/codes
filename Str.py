
class Str(str):

    def __sub__(self, obj):
        main = str(self)
        return "".join(main.split(obj))
