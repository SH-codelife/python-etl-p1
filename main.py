import sql   #get the sql.py file
from pgsql import query
import csv

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # insert data
    #query(sql.test_insert, ["My Insert!"]);

    # select data
    #results = query(sql.test_select);
    #print("results: ", results)

# (python) to call query from sql.py, create_schema
#    query(sql.create_schema);

# (python) to call query from sql.py, create_table
    #query(sql.create_table, [])
    #print("results: ", results)


#'with' open and closes object
    with open('datasets/hollywood-theatrical-market-synopsis-1995-to-2021/AnnualTicketSales.csv', newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=',')
        next(reader)
        #i=0
        for row in reader:
            row.pop()
            #if i >0:
            query(sql.insert_row, row)
            #i+=1

# See PyCharm help at https://www.jetbrains.com/help/pycharm/