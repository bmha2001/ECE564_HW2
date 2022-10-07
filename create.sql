DROP TABLE IF EXISTS EbayUser;
DROP TABLE IF EXISTS Bid;
DROP TABLE IF EXISTS Items;
DROP TABLE IF EXISTS Category;

CREATE TABLE EbayUser(
	UserID TEXT PRIMARY KEY, 
	Location TEXT, 
	Country TEXT, 
	Rating REAL
);

CREATE TABLE Items(
	ItemID TEXT PRIMARY KEY, 
	SellerID TEXT,
	Name TEXT, 
	Description TEXT, 
	Buy_Price REAL,
	Number_of_Bids INTEGER,
	First_Bid REAL,
	Started TEXT,
	Currently REAL,
	Ends TEXT,
	FOREIGN KEY (SellerID)
		REFERENCES EbayUser(UserID)
);

CREATE TABLE Bid(
	UserID TEXT, 
	ItemID TEXT, 
	Amount REAL, 
	Time TEXT,
	PRIMARY KEY (UserID, ItemID, Amount),
	FOREIGN KEY (UserID)
		REFERENCES EbayUser(UserID),
	FOREIGN KEY (ItemID)
		REFERENCES Item(ItemID)
);

CREATE TABLE Category(
	Name TEXT,
	ItemID TEXT,
	PRIMARY KEY (Name, ItemID),
	FOREIGN KEY (ItemID)
		REFERENCES Item(ItemID)
);