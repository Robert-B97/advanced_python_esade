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



#MAYBE:
#FIFO
#expiration date
#array() instead of amount
#Have two wearhouses were the stock can be shared between them. (send_stock)

#Optional extra functionality included:
    #Create a report of all the stock available in the wearhouse.

#TO DO:
# change get_report output from list to dict?
# exceptions handling
# input parameters
# create unittest


import argparse

class Product:
    '''Base class of generic product type'''
    def __init__(self,amount: int = 0) -> None:
        '''Initialization function
            amount: it's an int
            return: None
        '''
        self.amount = amount

class Phones(Product):
    '''Inheritance class to define Phones as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            amount of Phones: it's an int
            return: None
        '''
        super().__init__()

class Watches(Product):
    '''Inheritance class to define Watches as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            amount of Watches: it's an int
            return: None
        '''
        super().__init__()

class Computers(Product) :
    '''Inheritance class to define Computers as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            amount of Computers: it's an int
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
    units: int
        The amount of units to make an operation with
    requested_units: int
        The amount of units that is checked for retrival availablitiy
    
    Methods
    -------
    # FIXME: check_spare_capacity and CHANGE NAME is_stock_available
    add_stock(stock_type, units)
        adds stock units to current stock amount
    remove_stock(stock_type, units)
        removes stock units to current stock amount
    get_stock_amount(stock_type)
        returns current stock amount
    is_stock_available(stock_type,requested_units)
        returns boolean value for whether requested stock amount of stock type is available for retrival
    get_report()
        returns a report with each stock type in store together with their current amount

    '''
    def __init__(self,maximum_capacity: int) -> None:
        '''Initialization function
            maximum_capacity: it's an int
                The maximum capacity of the Warehouse
            phones: it's an object
            watches: it's an object
            computers: it's an object
            return: None
        '''
        assert (maximum_capacity > 0), "maximum_capacity has to be greater than 0"
        self.maximum_capacity = maximum_capacity
        self.phones = Phones()
        self.watches = Watches()
        self.computers = Computers()

    def get_free_capacity(self):
        return self.maximum_capacity - sum([self.__dict__[i].__dict__['amount'] for i in list(self.__dict__.keys())[1:]])

    def add_stock(self,stock_type: object, units: int) -> int:  
        '''adds amount to current amount of stock type
            
            returns updated amount
        '''
        assert (units > 0), "Units has to be greater than 0"
        assert (self.get_free_capacity() >= units), "Unable to process: Maximum capacity would be exceeded"
        stock_type.amount += units
        

    def remove_stock(self,stock_type: object, units: int) -> int:
        '''removes amount to current amount of stock type
            
            returns updated current amount
        '''
        assert (units > 0), "Units has to be greater than 0"
        assert (stock_type.amount >= units), "Unable to process: Requested capacity is not available"
        stock_type.amount -= units

    def get_stock_amount(self,stock_type: object) -> int:
        '''returns current amount of stock type
        '''
        return stock_type.amount

    def binary_search_prod(self, product_searched: str) -> bool:
        product_searched = product_searched.lower()
        input_list = sorted(list(self.__dict__.keys())[1:])
        l_list = len(input_list)-1
        c_index = int(len(input_list)/2.0)
        while c_index != 0 and c_index != l_list:
            if input_list[c_index] == product_searched:
                return product_searched, self.__dict__[product_searched].__dict__['amount']
            elif product_searched > input_list[c_index]:
                c_index = l_list - int((l_list-c_index)/2)
            else:
                c_index = int((c_index)/2)
        if input_list[c_index] == product_searched:
                return product_searched, self.__dict__[product_searched].__dict__['amount']
        raise ValueError("Search term not available\nSelect one of the following:\n{}".format(input_list))
        

    def get_report(self) -> list:
        '''returns a report with each stock type in store together with their current amount
        '''
        return [(i, self.__dict__[i].__dict__['amount']) for i in list(self.__dict__.keys())[1:]]

   

if __name__ == "__main__":
    #FIXME: make maximum_capacity required and remove default value
    parser = argparse.ArgumentParser(
          description="This program takes 1 argument: Maximum capacity of the warehouse")
    parser.add_argument('-maximum_capacity', '-max_cap', type=int, required=True, help='Maximum capacity warehouse') #default=1000
    argument_list = parser.parse_args()
    x = Warehouse(argument_list.maximum_capacity)

    while True:
        try:
            next_step = input("What do you want to do next: add_stock,remove_stock,get_stock_amount,binary_search_prod,get_report,exit ? ")
            match next_step:
                case 'add_stock':
                    which_stock = input('Which stock do you want to add: phones,watches,computers ? ')
                    units  = int(input('Units? '))
                    x.add_stock(getattr(x, which_stock),units)
                case 'remove_stock':
                    which_stock = input('Which stock do you want to remove: phones,watches,computers ? ')
                    units  = int(input('Units? '))
                    x.remove_stock(getattr(x, which_stock),units)
                case 'get_stock_amount':
                    which_stock = input('For which stock do you want the amount: phones,watches,computers ? ')
                    print(x.get_stock_amount(getattr(x, which_stock)))
                case 'binary_search_prod':
                    which_stock = input('Which stock do you want to search: phones,watches,computers ? ')
                    print(x.binary_search_prod(which_stock))
                case 'get_report':
                    print(x.get_report())
                case 'exit':
                    break
        except Exception as e:
            print(e)