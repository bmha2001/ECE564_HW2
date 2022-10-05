rm -rf *.dat
python parser.py ebay_data/items-*.json
sort users.dat | uniq -u > users_unique.dat
