from aifc import Error

import csv
import pymysql

try:
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='SmarTex2021',
                                 db='digitex')

    with open('Liste-Personnels-ET02Maint.csv') as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        all_value = []
        for row in csvfile:
            value = (row[0], row[2], row[1])
            all_value.append(value)

    cursor = connection.cursor()

    sql = "INSERT INTO maintainers (`reg_num`, `first_name`, `last_name`) VALUES (%s,%s,%s)"
    cursor.executemany(sql, all_value)

    connection.commit()

except Error as e:
    print(e)

finally:
    # close the database connection using close() method.
    connection.close()