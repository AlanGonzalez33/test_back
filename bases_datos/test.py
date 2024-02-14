import sys
import MySQLdb
try:
	db = MySQLdb.connect("localhost","alan","Cisco123!","Data_base_test" )
except MySQLdb.Error as e:
	print("No puedo conectar a la base de datos:",e)
	sys.exit(1)
print("Conexión correcta.")
db.close()