## WarehouseMngtSys_20220524.py

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

#Optional extra functionality included:
    #Create a report of all the stock available in the wearhouse.

#TO DO:
# minimum capacity of warehouse
# change get_report output from list to dict?
# exceptions handling
# input parameters
# create unittest




class Product:
    '''Base class of generic product type'''
    def __init__(self,current_amount: int = 0) -> None:
        '''Initialization function
            current_amount: it's an int
            return: None
        '''
        self.current_amount = current_amount

class Pineapples(Product):
    '''Inheritance class to define Pineapples as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            current_amount of Pineapples: it's an int
            return: None
        '''
        super().__init__()

class Oranges(Product):
    '''Inheritance class to define Oranges as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            current_amount of Oranges: it's an int
            return: None
        '''
        super().__init__()

class Watermelons(Product) :
    '''Inheritance class to define Watermelons as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            current_amount of Watermelons: it's an int
            return: None
        '''
        super().__init__()

class Warehouse:
    '''Main warehouse class with the warehouse functionalities
    Attributes
    ----------
    maximum_capacity: int
        The maximum capacity of the Warehouse
    stock_type: object
        The type of stock to operate on
    quantity: int
        The amount of units to make an operation with
    requested_quantity: int
        The amount of units that is checked for retrival availablitiy
    
    Methods
    -------
    add_stock(stock_type, quantity)
        adds stock quantity to current stock amount
    remove_stock(stock_type, quantity)
        removes stock quantity to current stock amount
    get_stock_amount(stock_type)
        returns current stock amount
    is_stock_available(stock_type,requested_quantity)
        returns boolean value for whether requested stock amount of stock type is available for retrival
    get_report()
        returns a report with each stock type in store together with their current amount

    '''
    def __init__(self,maximum_capacity: int) -> None:
        '''Initialization function
            maximum_capacity: it's an int
                The maximum capacity of the Warehouse
            pineapples: it's an object
            oranges: it's an object
            watermelons: it's an object
            return: None
        '''
        self.maximum_capacity = maximum_capacity
        self.pineapples = Pineapples()
        self.oranges = Oranges()
        self.watermelons = Watermelons()

    def check_spare_capacity(self):
        return self.maximum_capacity - sum([self.__dict__[i].__dict__['current_amount'] for i in list(self.__dict__.keys())[1:]])

    def add_stock(self,stock_type: str, quantity: int) -> int:  #what data type is stock_type? str? object?
        '''adds amount to current amount of stock type
            
            returns updated current amount
        '''
        if self.check_spare_capacity() >= quantity:
            stock_type.current_amount += quantity
        else:
            raise ValueError("Unable to process: Maximum capacity would be exceeded")

    def remove_stock(self,stock_type: str, quantity: int) -> int:
        '''removes amount to current amount of stock type
            
            returns updated current amount
        '''
        if stock_type.current_amount >= quantity:
            stock_type.current_amount -= quantity
        else:
            raise ValueError("Unable to process: Requested capacity is not available")

    def get_stock_amount(self,stock_type: str) -> int:
        '''returns current amount of stock type
        '''
        return stock_type.current_amount

    def binary_search_prod(self, product_searched: str) -> bool:
        product_searched = product_searched.lower()
        input_list = sorted(list(self.__dict__.keys())[1:])
        l_list = len(input_list)-1
        c_index = int(len(input_list)/2.0)
        while c_index != 0 and c_index != l_list:
            if input_list[c_index] == product_searched:
                return product_searched, self.__dict__[product_searched].__dict__['current_amount']
            elif product_searched > input_list[c_index]:
                c_index = l_list - int((l_list-c_index)/2)
            else:
                c_index = int((c_index)/2)
        if input_list[c_index] == product_searched:
                return product_searched, self.__dict__[product_searched].__dict__['current_amount']
        raise ValueError("Search term not available\nSelect one of the following:\n{}".format(input_list))
        

    def get_report(self) -> list:
        '''returns a report with each stock type in store together with their current amount
        '''
        return [(i, self.__dict__[i].__dict__['current_amount']) for i in list(self.__dict__.keys())[1:]]




    



if __name__ == "__main__":
    x = Warehouse(100)
    x.add_stock(x.pineapples, 10)
    x.add_stock(x.oranges, 20)
    x.add_stock(x.watermelons, 12)
    #x.remove_stock(x.pineapples, 3)
    #print(x.pineapples.current_amount)
    #print(x.is_stock_available(x.strawberries,3))
    print(x.get_report())
    print(type(x.get_report()))
    print(type(x.get_report()[0]))


    '''print('a' > 'b')
    print('pine' > 'pinel')
    print(sorted(list(x.__dict__.keys())[1:]))'''

    #print(x.binary_search('pinepples'))
    #print(x.binary_search_prod('melons'))
    #print(sum([x.__dict__[i].__dict__['current_amount'] for i in list(x.__dict__.keys())[1:]]))
    