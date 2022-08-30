class Tesla:

    CEO = 'Elon Musk'
    all_teslas = []
    
    ## ! Attributes go in the __init__
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price
        Tesla.all_teslas.append(self)
        print(self)

    ## ! instance methods, things the object does
    def drive(self):
        print(f"The {self.model} is quietly driving down the road...")
    # the model 3 is quietly driving down the road...

    # ! class methods are things the class can do.
    @classmethod
    def display_teslas(cls):
        return cls.all_teslas

my_tesla = Tesla('model 3', 'red', 1000000)
your_tesla = Tesla('model x', 'black', 1000000)