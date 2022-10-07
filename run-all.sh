./runParser.sh
echo create database
sqlite3 test_db < create.sql
echo load database 
sqlite3 test_db < load.txt
echo query 1 result
sqlite3 test_db < query1.sql
echo query 2 result
sqlite3 test_db < query2.sql
echo query 3 result
sqlite3 test_db < query3.sql
echo query 4 result
sqlite3 test_db < query4.sql
echo query 5 result
sqlite3 test_db < query5.sql
echo query 6 result
sqlite3 test_db < query6.sql
echo query 7 result
sqlite3 test_db < query7.sql
