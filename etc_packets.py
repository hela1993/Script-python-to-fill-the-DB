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

    with open('PACKETS.csv') as csv_file:
        csvfile = csv.reader(csv_file, delimiter=',')
        all_value = []
        i = 1
        for row in csvfile:
            value = (format(i, '07d'), row[2], row[3], val[0])
            all_value.append(value)
            i += 1

    cursor = connection.cursor()

    sql = "INSERT INTO packets (`pack_num`, `size`, `quantity`, `fab_order_number`) VALUES (%s,%s,%s,%s)"
    cursor.executemany(sql, all_value)

    sql2 = "UPDATE packets SET `pack_status` = 'here' WHERE id = 1"
    cursor.execute(sql2)

    # connection is not autocommit by default. So we must commit to save our changes.
    connection.commit()

except Error as e:
    print(e)

finally:
    # close the database connection using close() method.
    connection.close()