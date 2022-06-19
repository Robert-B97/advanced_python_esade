## main.py

import argparse
import json

class Product:
    '''Base class of generic product type'''
    def __init__(self,amount: int = 0) -> None:
        '''Initialization function
            amount: an int representing the stock amount
            return: None
        '''
        self.amount = amount

class Phones(Product):
    '''Subclass to define Phones as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            return: None
        '''
        super().__init__()

class Watches(Product):
    '''Subclass to define Watches as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            return: None
        '''
        super().__init__()

class Computers(Product) :
    '''Subclass to define Computers as unique product/ stock type'''
    def __init__(self) -> None:
        '''Initialization function
            return: None
        '''
        super().__init__()

class Warehouse:
    '''
    Main warehouse class with the basic warehouse functionalities and the stock amounts
    '''
    def __init__(self,maximum_capacity: int = 1000) -> None:
        '''
        Initialization function
            maximum_capacity: an int representing the maximum capacity of the Warehouse
            phones: an object instantiated with the Phones class
            watches: an object instantiated with the Watches class
            computers: an object instantiated with the Computers class
            return: None
        '''
        assert (maximum_capacity > 0), "maximum_capacity has to be greater than 0"
        self.maximum_capacity = maximum_capacity
        self.phones = Phones()
        self.watches = Watches()
        self.computers = Computers()

    def get_free_capacity(self) -> int:
        '''
        This function returns the spare capacity of the warehouse
        '''
        return self.maximum_capacity - sum([self.__dict__[i].__dict__['amount'] for i in list(self.__dict__.keys())[1:]])

    def add_stock(self,stock_type: str, units: int):  
        '''
        This function adds the specified units to the current amount of a certain stock type
        It also check if there is enough spare capacity (using check_spare_capacity). 
        If this condition is not met, it raise an error and doesn't update the amount.
            stock_type: a str representing the stock type to add
            units: an int representing the number of units to add
            returns: update the amount
        '''
        assert (units > 0), "Units has to be greater than 0"
        assert (self.get_free_capacity() >= units), "Unable to process: Maximum capacity would be exceeded"
        getattr(self, stock_type.lower()).amount += units

    def remove_stock(self,stock_type: str, units: int):
        '''
        This function removes the specified amount from the current amount of a stock type
        It also check if there is enough amount (of that product type) to satisfy the request. 
        If this condition is not met, it raise an error and doesn't update the amount.
            stock_type: a str representing the stock type to remove
            units: an int representing the number of units to remove
            returns: update the amount
        '''
        assert (units > 0), "Units has to be greater than 0"
        assert (getattr(self, stock_type.lower()).amount >= units), "Unable to process: Requested capacity exceeds the current amount"
        getattr(self, stock_type.lower()).amount -= units

    def get_stock_amount(self,stock_type: str) -> int:
        '''
        This function returns the current amount of a certain stock type
             stock_type: a str representing the stock type to get the amount
        '''
        return getattr(self, stock_type.lower()).amount

    def search_product(self, product_searched: str) -> dict:
        '''
        This function let you search if a product is available.
            Returns: 
                -if the product exist, a dictionary with the product and its stock amount
                -if it doesn't exist, raise an error and show the list of existing products in the warehouse

        '''
        if hasattr(self,product_searched.lower()) == True:
            return {product_searched.lower():self.get_stock_amount(product_searched)}
        else:
            raise ValueError("\nSearched product not available\nSelect one of the following:\n{}".format(sorted(list(self.__dict__.keys())[1:])))

    def get_report(self) -> dict:
        '''
        This function returns a report as a dictionary with:
            - the warehouse maximum and spare capacity
            - the different products with each stock amount
        '''
        report = {'warehouse':{list(self.__dict__.keys())[0]:self.__dict__[list(self.__dict__.keys())[0]],'spare_capacity':self.get_free_capacity()}}
        report['products'] = {i: self.__dict__[i].__dict__['amount'] for i in list(self.__dict__.keys())[1:]}
        return report

    def open_report(self,file_name: str):
        '''
        This function loads the existing json file containing the warehouse stock.
        The json file is generated as the output of the save_report() function
        '''
        #Open file
        with open(file_name, 'r') as f:
            warehouse_data = json.load(f)
        #Assign values to attributes
        self.maximum_capacity = warehouse_data['warehouse']['maximum_capacity']
        for product in list(warehouse_data['products'].keys()):
            getattr(self,product).amount = warehouse_data['products'][product]
    
    def save_report(self):
        '''
        Function to save the report in a json file
        '''
        with open('warehouse.json', 'w') as f:
            json.dump(self.get_report(), f)





if __name__ == "__main__":

    while True:
        parser = argparse.ArgumentParser(
            description="This program takes 1 optional argument:\nA file name/path containing the warehouse stock")
        parser.add_argument('-file_name','-f', type=str, required=False, help='File containing warehouse stock (try: warehouse.json')
        argument_list = parser.parse_args()

        try:
            x = Warehouse()
            x.open_report(argument_list.file_name)
            print('\nFile successfully loaded')
        except:
            new_file = input('\nWARNING! No file loaded using arguments in the command line\n\nDo you want to create a new file: (yes,no)? ').lower()
            if new_file == 'yes':
                x = Warehouse(maximum_capacity=int(input('\nWhat is the maximum capacity of the warehouse? ')))
            else:
                print('\nRun the program again, check if the file name passed as argument is correct\n')
                break

        while True:
            try:
                product_list = sorted(list(x.__dict__.keys())[1:])
                next_step = input("\nWhat do you want to do next: (add_stock,remove_stock,get_stock_amount,search_product,get_report,quit)? ").lower()
                match next_step:
                    case 'add_stock':
                        which_stock = input('Which stock do you want to add: {}? '.format(product_list))
                        units  = int(input('Units? '))
                        x.add_stock(which_stock,units)
                    case 'remove_stock':
                        which_stock = input('Which stock do you want to remove: {}? '.format(product_list))
                        units  = int(input('Units? '))
                        x.remove_stock(which_stock,units)
                    case 'get_stock_amount':
                        which_stock = input('For which stock do you want the amount: {}? '.format(product_list))
                        print(x.get_stock_amount(which_stock))
                    case 'search_product':
                        which_stock = input('Which stock do you want to search: {}? '.format(product_list))
                        print(x.search_product(which_stock))
                    case 'get_report':
                        print('\nReport:')
                        print(x.get_report())
                    case 'quit':
                        save_changes = input('Do you want to save the changes: (yes,no)? ').lower()
                        if save_changes == 'yes':
                            x.save_report()
                            print("\nFile successfully saved\n")
                            break
                        else:
                            if input("Are you sure you want to quit without saving: (yes,no)? ").lower() == 'yes':
                                break
                    case _:
                        print('\nWARNING: Action not allowed, check spelling')
            except Exception as e:
                print(e)
        break