
import pymysql

connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='SmarTex2021',
                                     db='digitex')
cursor = connection.cursor()
connection2 = pymysql.connect(host='localhost',
                                     user='root',
                                     password='SmarTex2021',
                                     db='db_isa')
cursor2 = connection2.cursor()

# cursor2.execute("SELECT OF, Tiers, Date_creation FROM ofs")
# for row in cursor2.fetchall():
#              cursor.execute("INSERT INTO fab_orders (`number`, `client`, `start_date`) VALUES (%s,%s,%s)", row)
#
# cursor2.execute("SELECT `N_pipelette`, `Taille`, `Coloris`, `Qte_a_monter`, `OF` FROM pipelettes")
# for row in cursor2.fetchall():
#     cursor.execute("INSERT INTO packets (`pack_num`, `size`, `color`, `quantity`, `fab_order_number`) VALUES (%s,%s,%s,%s,%s)", row)


cursor2.execute("SELECT `OF`, `N_pipelette`, `Ligne_gamme`, `Operation_gamme`, `Tps_ope_uni` FROM gamme")
for row in cursor2.fetchall():
    #value = (row[0], row[1], row[2], row[3], row[4], int(60 / float(row[4])))
    value = (row[0], row[1], row[2], row[3], row[4], '')
    cursor.execute("INSERT INTO pack_gamuts (`fab_order_number`, `pack_num`, `operation_code`, `designation`, `unit_time`, `qte_h`) VALUES (%s,%s,%s,%s,%s,%s)", value)



connection.commit()
connection2.commit()
connection.close()
connection2.close()