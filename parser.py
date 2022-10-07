
"""
FILE: skeleton_parser.py
------------------
Author: Firas Abuzaid (fabuzaid@stanford.edu)
Author: Perth Charernwattanagul (puch@stanford.edu)
Modified: 04/21/2014

Skeleton parser for CS564 programming project 1. Has useful imports and
functions for parsing, including:

1) Directory handling -- the parser takes a list of eBay json files
and opens each file inside of a loop. You just need to fill in the rest.
2) Dollar value conversions -- the json files store dollar value amounts in
a string like $3,453.23 -- we provide a function to convert it to a string
like XXXXX.xx.
3) Date/time conversions -- the json files store dates/ times in the form
Mon-DD-YY HH:MM:SS -- we wrote a function (transformDttm) that converts to the
for YYYY-MM-DD HH:MM:SS, which will sort chronologically in SQL.

Your job is to implement the parseJson function, which is invoked on each file by
the main function. We create the initial Python dictionary object of items for
you; the rest is up to you!
Happy parsing!
"""

import sys
from json import loads
from re import sub

userIDs = {1,2}

columnSeparator = "|"

# Dictionary of months used for date transformation
MONTHS = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',\
        'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

"""
Returns true if a file ends in .json
"""
def isJson(f):
    return len(f) > 5 and f[-5:] == '.json'

"""
Converts month to a number, e.g. 'Dec' to '12'
"""
def transformMonth(mon):
    if mon in MONTHS:
        return MONTHS[mon]
    else:
        return mon

"""
Transforms a timestamp from Mon-DD-YY HH:MM:SS to YYYY-MM-DD HH:MM:SS
"""
def transformDttm(dttm):
    dttm = dttm.strip().split(' ')
    dt = dttm[0].split('-')
    date = '20' + dt[2] + '-'
    date += transformMonth(dt[0]) + '-' + dt[1]
    return date + ' ' + dttm[1]

"""
Transform a dollar value amount from a string like $3,453.23 to XXXXX.xx
"""
def transformDollar(money):
    if money == None or len(money) == 0:
        return money
    return sub(r'[^\d.]', '', money)

def load_category(file, item):
    categories = item.get('Category')
    if categories is not None:
        categorySet = []
        for category in categories:
            if categorySet.__contains__(category):
                continue
            categorySet.append(category)
            file.write(category + "|")
            file.write(item.get('ItemID'))
            file.write('\n')

def load_user(file, item):
    seller = item.get('Seller')
    if seller.get('UserID') not in userIDs: 
        file.write(seller.get('UserID') + '|')
        if item.get('Location') is None:
            file.write("NULL" + "|")
        else:
            file.write(item.get('Location').replace("\"", "") + '|')
        if item.get('Country') is None:
            file.write("NULL" + "|")
        else:
            file.write(item.get('Country') + '|')
        file.write(seller.get('Rating'))
        file.write('\n')
        userIDs.add(seller.get('UserID'))
    bids = item.get('Bids')
    if bids is not None:
        for bid in bids:
            bid = bid.get("Bid")
            if bid.get('Bidder').get('UserID') not in userIDs: 
                file.write(bid.get('Bidder').get('UserID') + '|')
                if bid.get('Bidder').get('Location') is None:
                    file.write("NULL" + "|")
                else:
                    file.write(bid.get('Bidder').get('Location').replace("\"", "") + "|")
                if bid.get('Bidder').get('Country') is None:
                    file.write("NULL" + "|")
                else:
                    file.write(bid.get('Bidder').get('Country') + "|")
                file.write(bid.get('Bidder').get('Rating'))
                file.write('\n')
                userIDs.add(bid.get('Bidder').get('UserID'))

def load_bid(file, item):
    bids = item.get('Bids')
    if bids is not None:
        for bid in bids:
            bid = bid.get("Bid")
            file.write(bid.get('Bidder').get('UserID') + '|')
            file.write(item.get('ItemID') + "|")
            file.write(transformDollar(bid.get('Amount')) + "|")
            file.write(transformDttm(bid.get('Time')))
            file.write('\n')
        

def load_item(file, item):
    file.write(item.get('ItemID') + "|")
    file.write(item.get('Seller').get('UserID') + "|")
    file.write(item.get('Name').replace("\"", "") + "|")
    if item.get('Description') is None:
        file.write("NULL" + "|")
    else:
        file.write((item.get('Description').replace("\"", "")) + "|")
    if item.get('Buy_Price') is None:
        file.write("NULL" + "|")
    else:
        file.write(transformDollar(item.get('Buy_Price')) + "|")
    file.write(item.get('Number_of_Bids') + "|")
    if item.get('First_Bid') is None:
        file.write("NULL" + "|")
    else:
        file.write(transformDollar(item.get('First_Bid')) + "|")
    file.write(transformDttm(item.get('Started')) + "|")
    file.write(transformDollar(item.get('Currently')) + "|")
    file.write(transformDttm(item.get('Ends')))
    file.write('\n')

"""
Parses a single json file. Currently, there's a loop that iterates over each
item in the data set. Your job is to extend this functionality to create all
of the necessary SQL tables for your database.
"""
def parseJson(json_file):
    with open(json_file, 'r') as f:
        items = loads(f.read())['Items'] # creates a Python dictionary of Items for the supplied json file
        bids_list = open("bids.dat", "a+")
        item_list = open("items.dat", "a+")
        user_list = open("users.dat", "a+")  
        category_list = open("categories.dat", "a+") 
        for item in items:
            """
            TODO: traverse the items dictionary to extract information from the
            given `json_file' and generate the necessary .dat files to generate
            the SQL tables based on your relation design
            """
            load_category(category_list, item)
            load_user(user_list, item)
            load_bid(bids_list, item)          
            load_item(item_list, item)
            pass

"""
Loops through each json files provided on the command line and passes each file
to the parser
"""
def main(argv):
    if len(argv) < 2:
        print >> sys.stderr, 'Usage: python skeleton_json_parser.py <path to json files>'
        sys.exit(1)
    # loops over all .json files in the argument
    for f in argv[1:]:
        if isJson(f):
            parseJson(f)
            print("Success parsing " + f)

if __name__ == '__main__':
    main(sys.argv)
