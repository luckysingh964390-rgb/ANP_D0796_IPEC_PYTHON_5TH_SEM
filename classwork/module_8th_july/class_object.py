#defining a class to perform operations on rectangle
class Rectangle:
    #member variable
    length=0
    breath=0
    #method to initialize data 
    def initialize(self,l,b):
        self.length=l
        self.breath=b
        #method to display data
        def display_data(self):
            print("-------------Rectangle--------------")
            print("Length of rectangle is : ",self.length,"cm")
            print("Breath of rectangle is : ",self.breath)
            #-------------------------------------
            #------------Main program----------------

            rect=Rectangle()
            rect.initialize(20,50)
            rect.display_data()