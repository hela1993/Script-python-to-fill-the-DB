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
        all_packet = []
        i = 1
        for row in csvfile:
            val_packet = (format(i, '07d'), val[0])
            all_packet.append(val_packet)
            i += 1

    cursor = connection.cursor()

    sql2 = """
        INSERT INTO pack_gamuts (`fab_order_number`, `pack_num`, `operation_code`, `designation`, `unit_time`, `qte_h`) 
        SELECT `fab_order_number`, %s, `operation_code`, `designation`, `unit_time`, `qte_h`
        FROM gamuts 
        WHERE `fab_order_number` = %s
    """
    cursor.executemany(sql2, all_packet)
    # connection is not autocommit by default. So we must commit to save our changes.
    connection.commit()

except Error as e:
    print(e)

finally:
    # close the database connection using close() method.
    connection.close()