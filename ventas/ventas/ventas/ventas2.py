import os
os.system("cls")
fecha="13-06-2024"
folio=10000
productos =[ 

           ]
ventas=[  

        ]
archivo="productos.txt"
archivo2="ventas_prod.txt"

def cargar_ventas(archivo2):
    lista_datos2=[]
    with open (archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")
            ventas.append(datos)
    return 1

def cargar_productos(archivo):
    lista_datos=[]
    with open (archivo, "r") as file:
        for linea in file:
            linea = linea.strip()
            datos = linea.split(",")
            productos.append(datos)
    return 1

def get_folio():
    elemento= len(ventas)-1
    return (ventas[elemento])[0]

id=""
opc=0
def buscar_id(id):   
    for i in productos:
        if i[0] == id:           
           return i
    return -1   
opcion=0

while opcion<=5:

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
            while True:
                os.system("cls")
                id=input("ingrese ID: ")
                i=buscar_id(id)

                if i != -1:
                    #print("Encontrado en el elemento ",i)
                    producto=i
                    print(producto[0]," ",producto[1]," ",producto[2]," ",producto[3]," ",producto[4]," ",producto[5])
                    cantidad=int(input("ingrese cantidad a comprar: "))

                    if cantidad<= producto[4]:
                        total=cantidad*producto[5]
                        print(f"el total a pagar por {cantidad} productos es {total}")
                        respuesta=input("Desea realizar la compra s/n: ")
                        if respuesta.lower() == "s":
                            producto[4]=producto[4]-cantidad
                            ventas.append([get_folio()+1,fecha,id,cantidad,total ])

                else:
                    print("Error, la cantidad ingresada supera el stock,")
                respuesta=input("Desea comprar otro producto s/n: ")
                if respuesta.lower() == "n":
                    break
        case 2:
            os.system("cls")
            opc=0
            while opc<=4:
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
                        a=0
                        for venta in ventas:
                            a=a+venta[4]
                            print(venta[0]," ",venta[1]," ",venta[2]," ",venta[3]," ",venta[4])
                            print("total= ",a)
                            
                    case 2:#error, solo me toma una venta de esa fecha
                        a=0
                        fecha=input("ingrese una fecha: ")
                        for venta in ventas:
                            if venta[1]==fecha:
                                a=a+venta[4]
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
                os.system("cls")
                op=0
                while op<=6:
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
                                id =input("Ingrese id producto:  ")
                                producto = input("Ingrese  producto:  ")
                                tema = input("Ingrese el Tema:  ")
                                paginas =int(input("Ingrese la cantidad de paginas:  "))
                                stock = int(input("Ingrese el stock:  "))
                                precio = int(input("Ingrese el precio:  "))
                                productos.append([id,producto,tema,paginas,stock,precio])

                            case 2: 
                                id=input("Ingrese ID de los Productos a buscar: ")
                                sw=0
                                for i in productos:
                                    if i[0] == id:
                                        sw=1
                                        print(i[0],"",i[1],"",i[2],i[3],"",i[4],"",i[5])
                                        break

                                if sw==0:
                                    print("ERROR, id no existe")


              

                            case 3: 
                                
                                id=input("Ingrese id del Producto a eliminar:  ")

                                lista=buscar_id(id)

                                if lista != -1:
                                    productos.remove(lista)
                                    print(productos)
                                else:
                                    print("Error, Producto no existe")
                                    
                            
                            
                            case 4: 
                                print("\n Modificar\n")
                                id=input("Ingrese un id a buscar:  ")

                                print("\n")
                                nueva_id =input("Ingrese id nueva del producto:  ")
                                nuevo_producto = input("Ingrese  el nuevo nombre producto:  ")
                                nuevo_tema = input("Ingrese el nuevo Tema:  ")
                                nuevo_paginas = int(input("Ingrese la nueva cantidad de paginas:  "))
                                nuevo_stock = int(input("Ingrese el nuevo stock:  "))
                                nuevo_precio = int(input("Ingrese el nuevo precio:  "))

                                lista=buscar_id(id)

                                if lista != -1:
                                    lista[0]=nueva_id
                                    lista[1]=nuevo_producto
                                    lista[2]=nuevo_tema
                                    lista[3]=nuevo_paginas
                                    lista[4]=nuevo_stock
                                    lista[5]=nuevo_precio
                                    print(productos)
                                    print("\n Listo! datos modificados")
                                    break #salir del ciclo
                                else:
                                    print("Error, id no existe")


                            case 5: 
                                print("\n Listar Productos\n")
                                for i in productos:

                                    print(i[0]," ",i[1]," ",i[2]," ",i[3]," ",i[4]," ",i[5])
                    if op==5:
                        break 
                    os.system("pause")
        case 4:
                
                    os.system("cls")
                    opci=0
                    while opcion<=3:
                        
                        print("""
                                ADMINISTRACION
                                1.Cargar datos   
                                2.Respaldar datos (Grabar Actualizar)
                                3.Salir
                            """)
                    
                    opci=int(input("ingrese una opcion entre 1-3: "))

                    match opci:
                                case 1:
                                    if cargar_productos>=1 and cargar_ventas>=1:
                                        print("Ya se han cargado los datos")    
                                    else:
                                        cargar_productos=1
                                        cargar_ventas=1 
                            
        case 5:
            break 
                          
