SELECT COUNT(DISTINCT Category.Name) FROM Category, Bid WHERE Category.ItemID = Bid.ItemID AND Bid.Amount > 100;
