SELECT COUNT(UserID) FROM EbayUser WHERE EXISTS (SELECT * FROM Item WHERE Item.UserID = EbayUser.UserID) AND EXISTS (SELECT * FROM Bid WHERE Bid.UserID = EbayUser.UserID);