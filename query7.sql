SELECT COUNT(DISTINCT Name) FROM Category WHERE (SELECT MAX(Currently) FROM Item WHERE Category.ItemID = Item.ItemID) > 100;