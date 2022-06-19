# advanced_python_esade
Repository for assignment warehouse

# Requirements
main.py requires python 3.10


# Warehouse assignment <> Technical Specifications

## Goals
Warehouses need a system to keep track and manage their stocks. Although this is a very simple problem to solve when dealing with a basic simulation of a warehouse, it becomes essential and articolate when dealing with more complex systems with a large variety of product types and logistic systems.

The scope of this program is to design a simple warehouse management system. 
The programm allow the user to keep track of the stocks for three types of products in a warehouse. 
The user will be able to add and remove stock, as well as get the number of stocks for a certain product and get a report for the whole warehouse.

It's essential to have a clear idea of the current state of the warehouse and track all the changes. This is were the program will help.

## Limitations (out of scope)
The code will serve as a barebone program to build more advanced features in future updates.
This MVP includee only basic function and it's not suitable for a real use case given that it doesn't take all the complexities into account.

To make it useful in a real world scenario it will have to be tailored based on the specific business needs.

These are possible areas for future improvements:
- Wider variety of products can be defined
- More attributes can be defined for each product to further differentiate the stock
- Automate the creation of periodic reports
- Change representation of stock quantity from an integer to an array. This will enable to take into consideration production batches (lots).
- Implement FIFO or LIFO logics
- Add multiple warehouses and the functions to manage the stock sharing system
- Create a GUI for manual inputs and integrate it with other programs to manage automatic updates

## Features (and reasoning)

### Classes
- The class Product is the base class for the different products. 
The only attribute at initiation is 'amount'. It's an integer and by default is 0 at instantiation.
- The three product type classes, Phones, Watches and Computers all inherit from the base class
- The class Warehouse provides all the functions to manage and check the stock. 
It has different attributes:
    - maximum_capacity: define the maximum amount of products that can be stored in the warehouse.
    - phones, watches and computers: they are all objects instantiated from their respective class in order to store their amount for each type.
### Functions
All the functions are, as previously mentioned, created inside the class Warehouse:
- get_free_capacity:
    This function returns the spare capacity by substracting the total amount of stock from the maximum capacity
- add_stock:
    This function take as input thee stock_type (str) and the units to add (int) to update the amount of a particular product.
    It also check if there is enough spare capacity (using check_spare_capacity). If this condition is not met, it raise an error and doesn't update the amount.
- remove_stock:
    This function take as input thee stock_type (str) and the quantity to remove (int) to update the amount of a particular product.
    It also check if there is enough amount (of that product type) to satisfy the request. If this condition is not met, it raise an error and doesn't update the amount.
- get_stock_amount:
    This function take as input the stock type and returns its amount.
- search_product:
    This function take as input the product searched and returns a dict with the product searched, if exists, together with its amount. 
    If the product is not available it raise an error and displays a list of available products to search (to help the user in case the product he was looking for is in the list or in case of spelling mistakes)
- get_report:
    This function returns a report as a dictionary with:
        - the warehouse maximum and spare capacity
        - the different products with each stock amount
- open_report:
    This function loads the existing json file containing the warehouse stock.
    The json file is thee one generated as the output of the save_report() function.
    It is used to load the existing file at the beginning of the program
- save_report:
    This function to save the report in a json file
        


## Testing
The use of assertions is used to help controlling unintended behaviours whenever the wrong input doesn't automatically raise an error (e.g. the argument for add_stock is a negative intger).
Used assert if:
    - maximum_capacity is > 0 (instantiate object with Warehouse class)
    - units are > 0 (functions add_stock and remove_stock)
    - spare capacity >= than the units we want to add (in add_stock)
    - amount of a stock is >= than units to remove (in remove_stock)

## Terminal Execution
1. When running the file the user will need to pass the argument '-file_name/-f' representing file containing the data to pass in the open_report function to set up the warehouse object that is being instantiated.
If nothing is passed in the argument, the users will have to choose if they want to start from scratch and create a new warehouse, or exit the program.

2. A while loop will ask the user to input the next step (which function to use from the displayed ones)

3. Based on the action (e.g. add_stock) the program will ask for to input the specific arguments required (e.g. stock_type and units)

4. After the action is performed, it will return to the beginning of the loop asking for the next step
If there is an exception/error raised by a wrong input, the user will be sent back to the beginning of the loop where he's asked for the next step.

5. To terminate the program, if 'quit' is selected as next step, the loop ends and the program stop running
Before ending it will ask the users if they want to save the current state of the warehouse by saving the report

