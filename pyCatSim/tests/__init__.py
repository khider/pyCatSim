class Owner:
    def __init__(self, name, cats_owned):
        if isinstance(cats_owned, Cat):
            self.cats_owned = [cats_owned]
        elif isinstance(cats_owned, list):
            self.cats_owned = cats_owned
        else:
            raise TypeError("Must provide Cat or list of Cats")
        self.name = name
