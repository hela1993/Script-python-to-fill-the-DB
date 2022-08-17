from aifc import Error

import csv
import pymysql

try:
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='SmarTex2021',
                                 db='digitex')
    name = "3000002641_CAPEL_CHINOS-BLEU-INDIGO"
    val = name.split("_")

    with open('3000002641_CAPEL_CHINOS-BLEU-INDIGO.csv') as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')

        for row in csvfile:
            value = (val[0], val[2], val[1], row[15], row[2], row[14])

    cursor = connection.cursor()

    sql = "INSERT INTO fab_orders (`number`, `model`, `client`, `quantity`, `start_date`, `end_date`) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, value)

    connection.commit()

except Error as e:
    print(e)

finally:
    # close the database connection using close() method.
    connection.close()

