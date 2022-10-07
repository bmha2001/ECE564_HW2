rm -rf *.dat
python parser.py ebay_data/items-*.json
sort users.dat | uniq -u > users_unique.dat
sort bids.dat | uniq -u > bids_unique.dat
sort categories.dat | uniq -u > categories_unique.dat
sort items.dat | uniq -u > items_unique.dat
