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
- Automate the creation off periodic reports
- Change representation of stock quantity from an integer to an array. This will enable to take into consideration production batches (lots).
- Implement FIFO or LIFO logics
- Add multiple warehouses and the functions to manage the stock sharing system
- Create a GUI for manual inputs and integrate it with other programs to manage automatic updates

## Features (and reasoning)

### Classes
- The class Product is the base class for the different products. 
The only attribute at initiation is current_amount. It's an integer and by default is 0 at instantiation.
- The three product type classes, Pineapples, Oranges and Watermelons all inherit from the base class
- The class Warehouse provides all the functions to manage and check the stock. 
It has different attributes:
    - maximum_capacity: define the maximum amount of products that can be stored in the warehouse.
    - pineapples, oranges, watermelons: they aare all objcts instantiated from their respective class in order to store their current_amount for each type.
### Functions
All the functions are, as previously mentioned, created inside the class Warehouse:
- check_spare_capacity:
    This function returns the spare capacity by substracting the total amount of stock from the maximum capacity
- add_stock:
    This function take as input thee stock_type (str) and the quantity to add (int) to update the current_amount of a particular product.
    It also check if there is enough spare capacity (using check_spare_capacity). If this condition is not met, it raise an error and doesn't update the current_amount.
- remove_stock:
    This function take as input thee stock_type (str) and the quantity to remove (int) to update the current_amount of a particular product.
    It also check if there is enough current_amount (of that product type) to satisfy the request. If this condition is not met, it raise an error and doesn't update the current_amount.
- get_stock_amount:
    This function take as input the stock type and returns its current_amount.
- binary_search_prod:
    This function take as input the product searched and returns the product searched, if available, together with its current_amount, using binary search. 
    If the product is not available it raise an error and displays a list of available products to search (to help the user in case the product he was looking for is in the list or in case of spelling mistakes)
- get_report:
    This function returns a report (a list of tuples) with each stock type considered in the warehouse management system as well as their current amount (it also display product whose amount is 0)

## Testing

## Deployment



