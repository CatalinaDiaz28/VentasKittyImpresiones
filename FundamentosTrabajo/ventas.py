import os
import pyfiglet
from datetime import date
from datetime import datetime

today=date.today()
format=today.strftime("%d-%m-%Y")

primera_fecha=datetime(1,1,1)
ultima_fecha=datetime(1,1,1)

os.system("cls")


fecha="13-06-2024"
folio=10000
id=0



productos =[ 

           ]
ventas=[  

        ]

 
def cargar_ventas(archivo):
    lista_datos2=[]
    with open (archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")
            ventas.append(datos)
    return lista_datos2

def cargar_productos(archivo):
    lista_datos=[]
    with open (archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")
            productos.append(datos)
    return lista_datos

def get_folio():
    elemento= len(ventas)-1
    return (ventas[elemento])[0]

carga_completa_productos = 0
carga_completa_ventas = 0
def cargar_datos(peticion):
    global productos, ventas, carga_completa_productos, carga_completa_ventas
    
    try:
        if peticion == 1:
            if carga_completa_productos == 0:
                cargar_productos("productos.txt")
                cargar_ventas("ventas_prod.txt")
                carga_completa_productos = 1
                print("Datos cargados correctamente.")
                os.system("pause")
            else:
                print("Los datos ya fueron cargados previamente.")
                os.system("pause")

        elif peticion == 2:
            if carga_completa_ventas == 0:
                with open("productos.txt", "w") as file:
                    for producto in productos:
                        file.write(f"{producto[0]},{producto[1]},{producto[2]},{producto[3]},{producto[4]},{producto[5]}\n")
                
                with open("ventas_prod.txt", "w") as file:
                    for venta in ventas:
                        file.write(f"{venta[0]},{venta[1]},{venta[2]},{venta[3]},{venta[4]}\n")
                
                print("Datos respaldados correctamente.")
                carga_completa_productos = 0
                carga_completa_ventas = 1  # Se actualiza carga_completa_ventas a 1 después de respaldar
                os.system("pause")
            else:
                print("Primero carga los datos antes de respaldar.")
                os.system("pause")

    except Exception as e:
        print(f"Error: {e}")
        os.system("pause")



def nueva_venta(folio,fecha,id,cantidad,precio):
    ventas='ventas_prod.txt'
    with open(ventas,'a') as file:
        file.write(f"\n{folio},{fecha},{id},{cantidad},{precio}")

def producto_nuevo(id,producto,tema,paginas,stock,precio):
    productos="productos.txt"
    with open(productos,'a') as file:
        file.write(f"\n{id},{producto},{tema},{paginas},{stock},{precio}")


id=""
opc=0

def buscar_id(id):
    for producto in productos:
        if producto[0] == id:
            return producto
    return None


opcion=0
print(pyfiglet.figlet_format("Kitty Impresiones",font="speed",justify="center"))
print("integrantes:  Catalina Diaz")
print("              Valeria Quinteros")
os.system("pause")

while opcion<=5:
    os.system("cls")
    print("Fecha actual: ",format)

    print("""
            VENTAS DE KITY IMPRESIONES
            1.Vender Productos
            2.Reportes
            3.Mantencion de Ventas
            4.Administracion
            5.Salir
      """)
    opcion=int(input("Ingrese una Opcion entre 1-4: "))

    match opcion:
        
        case 1:
            print("VENDER PRODUCTOS")
            os.system("cls")
            cantidad = 0
            stock = 0
            id = input("Ingrese ID: ")
            try:
                for producto in productos:
                    id_producto = producto[0]
                    if id_producto == id:
                        print(f"Stock disponible: {producto[4]}")
                        cantidad = int(input("Ingrese cantidad a comprar: "))
                        stock = int(producto[4])
                        valor = int(producto[5])
                        if cantidad <= stock and cantidad > 0:
                            total = valor * cantidad
                            print(f"El total a pagar por {cantidad} productos es {total}")
                            respuesta = input("Desea realizar la compra s/n: ")
                            if respuesta.lower() == "s":
                                producto[4] = str(stock - cantidad)  # Actualiza el stock restante
                                folio = int(get_folio()) + 1
                                fecha = format
                                id = producto[0]
                                precio = valor * cantidad
                                nueva_venta(folio, fecha, id, cantidad, precio)
                                ventas.append([folio, fecha, id, cantidad, precio])
                                print("Venta registrada correctamente.")
                                os.system("pause")
                                break
                        else:
                            print("Error, la cantidad ingresada supera el stock disponible.")
                        respuesta = input("¿Desea comprar otro producto? s/n: ")
                        if respuesta.lower() == "n":
                            break
            except :
                print("Error ")
    
        case 2:
            opc=0
            while opc<=4:
                os.system("cls")
                print("""
                                   REPORTES
                      1.General de Ventas(con total)
                      2.Ventas por Fecha Especifica
                      3.Ventas por Rango de fecha(con total)
                      4.Salir al Menu Principal
                """)

                opc=int(input("ingrese una opcion entre 1-4: "))

                match opc:
                    case 1:
                        os.system("cls")
                        a=0
                        for venta in ventas:
                            a=a+(int(venta[4]))
                            print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])

                        print("total: ",a)
                        os.system("pause")    
                    case 2:#error, solo me toma una venta de esa fecha
                        a=0
                        fecha=input("ingrese una fecha: ")
                        for venta in ventas:
                            if venta[1]==fecha:
                                a=a+(int(venta[4]))
                                print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])
                            
                        print("total= ",a)
                        os.system("pause")    

                    case 3: #error, no me cuenta los meses,solo el rango
                        a=0
                        
                        fecha_inicio=input("ingrese la fecha de inicio: ")
                        fecha_termino=input("ingrese la fecha de termino: ")
                        for venta in ventas:
                            if venta[1] >= fecha_inicio and venta[1] <= fecha_termino:
                                a=a+venta[4]
                                print(ventas[0]," ",ventas[1]," ",ventas[2],ventas[3]," ",ventas[4])
                        
                        print("total= ",a)
                        os.system("pause")


                    case 4:
                        break    
        case 3:
                op=0
                while op<=6:
                    os.system("cls")
                    print("""
                            MANTENCION DE VENTAS

                        1. Agregar productos
                        2. buscar productos
                        3. Eliminar productos
                        4. modificar productos
                        5. Listar productos
                        6. Salir al menu principal


                        """)
                    op = int(input("Ingrese una opcion del 1-6: "))

                   
                    if op>=1 and op<=6:
                        os.system("cls")
                    match op:
                            case 1: 
                                print("\n Agregar Producto\n")
                                #agregar
                                try:
                                    
                                    id =int(input("Ingrese id producto:  "))
                                    producto = input("Ingrese  producto:  ")
                                    tema = input("Ingrese el Tema:  ")
                                    paginas =int(input("Ingrese la cantidad de paginas:  "))
                                    stock = int(input("Ingrese el stock:  "))
                                    precio = int(input("Ingrese el precio:  "))
                                    productos.append([id,producto,tema,paginas,stock,precio])
                                    producto_nuevo(id,producto,tema,paginas,stock,precio)

                                except:
                                    print("Ingrese los datos correctamente! ")
                            case 2: 
                                
                                id=int(input("Ingrese ID de los Productos a buscar: "))
                                for producto in productos:
                                    id_producto = producto[0]
                                    if id_producto == id:
                                        print(int(producto[0])," ",producto[1]," ",producto[2]," ",producto[3]," ",producto[4]," ",producto[5])
                                    break

                                else:
                                    print("ERROR, id no existe")




                            case 3: 
                                
                                id=input("Ingrese id del Producto a eliminar:  ")
                                for producto in productos:
                                    id_producto = producto[0]
                                    if id_producto == id:
                                        productos.remove(producto)
                                        print("Producto eliminado")
                                        
                                
                                    
                            
                            
                            case 4: 
                                print("\n Modificar\n")
                                id = input("Ingrese un id a buscar: ")
                                print("\n")
                                
                                nuevo_producto = input("Ingrese el nuevo nombre del producto: ")
                                nuevo_tema = input("Ingrese el nuevo Tema: ")
                                
                                try:
                                    nueva_id = input("Ingrese id nueva del producto: ")
                                    nuevo_paginas = int(input("Ingrese la nueva cantidad de páginas: "))
                                    nuevo_stock = int(input("Ingrese el nuevo stock: "))
                                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                                except:
                                    print("Ingresa valores numéricos!")
                                    

                                producto_encontrado = buscar_id(id)

                                if producto_encontrado:
                                    producto_encontrado[0] = nueva_id
                                    producto_encontrado[1] = nuevo_producto
                                    producto_encontrado[2] = nuevo_tema
                                    producto_encontrado[3] = nuevo_paginas
                                    producto_encontrado[4] = nuevo_stock
                                    producto_encontrado[5] = nuevo_precio
                                    print(productos)
                                    print("\n ¡Listo! Datos modificados.")
                                    break 
                                else:
                                    print("Error, el id no existe. Inténtalo de nuevo.")

                            case 5: 
                                print("\n Listar Productos\n")
                                for item in productos:
                                    print(item[0]," ",item[1]," ",item[2]," ",item[3]," ",item[4]," ",item[5])

                    if op==6:
                        break 
                    os.system("pause")
        case 4:
                
                    
                    opci=0
                    while True:
                        os.system("cls")
                        print("""
                                ADMINISTRACION
                                1.Cargar datos   
                                2.Respaldar datos (Grabar Actualizar)
                                3.Salir
                            """)
                    
                        try:
                            opci=int(input("ingrese una opcion entre 1-3: ")) 
                                
                            if opci == 1:
                                cargar_datos(1)
                            elif opci == 2:
                                cargar_datos(2)  # Intenta respaldar los datos
                                

                            elif opci ==3:
                                break
                            else:
                                print("Error ingreso no valido! ")

                            
                        except:
                            print("Ingreso erroneo! ")
                            os.system("pause")
                            
        case 5:
            break