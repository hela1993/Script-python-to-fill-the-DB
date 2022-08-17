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
        all_value = []
        for row in csvfile:
            value = (val[0], row[0], row[7], row[59], row[61])
            all_value.append(value)

    cursor = connection.cursor()

    sql = "INSERT INTO gamuts (`fab_order_number`, `operation_code`, `designation`, `unit_time`, `qte_h`) VALUES (%s,%s,%s,%s,%s)"
    cursor.executemany(sql, all_value)

    connection.commit()

except Error as e:
    print(e)

finally:
    # close the database connection using close() method.
    connection.close()