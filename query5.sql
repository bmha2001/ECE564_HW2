SELECT COUNT(DISTINCT EbayUser.UserID) FROM Items, EbayUser WHERE Items.SellerID = EbayUser.UserID AND EbayUser.Rating > 1000;
