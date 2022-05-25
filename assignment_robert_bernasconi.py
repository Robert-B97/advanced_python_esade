## assignment_robert_bernasconi.py

# MIT License
# 
# Copyright (c) 2022 Robert Bernasconi
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Conceptual Specifications


# Technical Specifications

# Architectur/execution model

#MAYBE:
#FIFO
#expiration date
#array() instead of quantity
#Have two wearhouses were the stock can be shared between them.
#Create a report of all the stock available in the wearhouse.

#TO DO:
# exceptions handling
# input parameterds
# create unittest




class Product:
    def __init__(self,current_amount: int = 0):
        self.current_amount = current_amount

class Pineapples(Product):
    def __init__(self):
        super().__init__()
class Oranges(Product):
    def __init__(self):
        super().__init__()
        pass

class Watermelon(Product):
    def __init__(self):
        super().__init__()
        pass

class Warehouse:
    def __init__(self,maximum_capacity: int):
        self.maximum_capacity = maximum_capacity
        self.pineapples = Pineapples()
        self.oranges = Oranges()
        self.watermelon = Watermelon()

    def add_stock(self,quantity,stock_type):
        stock_type.current_amount += quantity

    def remove_stock(self,quantity,stock_type):
        stock_type.current_amount -= quantity

    def get_stock_amount(self,stock_type):
        return stock_type.current_amount

    def is_stock_available(self,stock_type,required_amount:int = 0) -> bool:
        return self.get_stock_amount(stock_type) >= required_amount

    def get_report(self) -> dict:
        return [(i, x.__dict__[i].__dict__['current_amount']) for i in list(self.__dict__.keys())[1:]]




    



if __name__ == "__main__":
    x = Warehouse(100)
    '''x.add_stock(5,x.pineapples)
    x.remove_stock(3,x.pineapples)
    print(x.pineapples.current_amount)
    print(x.is_stock_available(x.pineapples,3))'''
    print(x.get_report())
