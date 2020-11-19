import pymysql
from claseUsuario import Usuario

def conectar():
    try:
        conexion = pymysql.connect(host='localhost'
                                    ,user='root'
                                    ,password=''
                                    ,db='tienda')
    except:
        print("Problemas al conectar")
    return conexion
#programa principal
conectar()
print("Estas conectado a la base de datos")

def insertar(cliente):
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO usuario(ID,Nombre,RUT) VALUES (%s,%s,%s);"
            #Podemos llamar a execute varias veces con datos diferentes
            cursor.execute(consulta,(cliente.id,cliente.nombre,cliente.rut))
        conexion.commit()
    except (pymysql.err.OperationalError,pymysql.err.InternalError) as ex:
        print("Error al momento de ingresar los datos",ex)
    conexion.close()

