'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the data with csv.reader() and store it in a list of lists called 'data'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''
import csv
with open("chipotle.tsv", 'rU') as Chp_file:
    chipotle_data = [chp_row for chp_row in csv.reader(Chp_file, dialect = 'excel-tab')]


'''
BASIC LEVEL
PART 2: Separate the header and data into two different lists.
'''
chp_header = chipotle_data[0]
chp_body = chipotle_data[1:]


'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''
# quantity already factored into price
clean_price = []
for chp_row in chp_body:
    if chp_row[4][0] == "$":
        clean_price.append(float(chp_row[4][1:]))
        
total_all_orders = 0
for chp_row in clean_price:
    total_all_orders = total_all_orders + chp_row

avg_price_order = round((total_all_orders/1834), 2)

# Average price per order is $18.81

'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''
Sodas = []
for chp_row in chp_body:
    if chp_row[2] == "Canned Soda":
        Sodas.append(chp_row[3])
    elif chp_row[2] == "Canned Soft Drink":
        Sodas.append(chp_row[3])
set(Sodas)
len(set(Sodas))

"""
9 Soda types based on Criteria: Lemonade, Dr. Pepper, Diet Coke, Nestea
Mountain Dew, Diet Dr. Pepper, Come, Coca Cola, Sprite

"""

'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''
num_toppings = []
for chp_row in chp_body:
    if "Burrito" in chp_row[2]:
        the_toppings = chp_row[3]        
        topping_count = the_toppings.count(',') +1
        num_toppings.append(topping_count)
        
total_num_toppings = 0
for topping in num_toppings:
    total_num_toppings = total_num_toppings + topping

avg_num_toppings = round((total_num_toppings/len(num_toppings)),1)
   
# Average number of toppings per Burrito is 5
   
'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''
"""
Intermediate code written to get to answer
chip_orders = []
chip_quant = []
for chp_row in chp_body:
    if "Chips" in chp_row[2]:
        chip_orders.append(chp_row[2])
        chip_quant.append(int(chp_row[1]))

from collections import defaultdict
chip_order_count = defaultdict(int)
for chip_order in chip_orders:
    if chip_order in chip_orders:
        chip_order_count[chip_order] = chip_order_count[chip_order] +1
    else:
        chip_order_count[chip_order] = 1

"""      
chip_order_quant =[]
for chp_row in chp_body:
    if "Chips" in chp_row[2]:
        item = []
        item.append(chp_row[2])
        item.append(int(chp_row[1])) 
        chip_order_quant.append(item)
 
from collections import defaultdict
chip_order_count = defaultdict(int)
for chip_order in chip_order_quant:
    if chip_order in chip_order_quant:
        chip_order_count[chip_order[0]] = chip_order_count[chip_order[0]] +1*chip_order[1]
    else:
        chip_order_count[chip_order[0]] = 1*chip_order[1]

"""
Output
Chips: 230
Chips and Roasted Chili-Corn Salsa: 18
Chips and Tomatillo-Red Chili Salsa: 25
Chips and Mild Fresh Tomato Salsa: 1
Chips and Guacamole: 506
Chips and Fresh Tomato Salsa: 130
Chips and Tomatillo Red Chili Salsa: 50
Chips and Tomatillo-Green Chili Salsa: 33
Side of Chips: 11-
Chips and Rosasted Chili Corn Salsa: 23
Chips and Tomatillo Green Chili Salsa: 45
"""
'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
