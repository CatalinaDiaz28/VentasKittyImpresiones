import os
os.system("cls")
fecha="13-06-2024"
folio=10000
#10 productos
productos =[ # id         prod        tema           paginas    stock    precio
            ["aa01",   "agenda",  "cristiana",       100,        50,      15000],
            ["aa02",   "agenda",  "pediatrica",      80,         30,      10000],
            ["aa03",   "agenda",   "letter",         100,        30,      15000],
            ["aa04",   "agenda",  "informatico",     120,        40,      18000],
            ["aa05",   "agenda",  "profesor",        100,        20,      15000],
            ["aa06",   "agenda",  "medico",          100,        35,      15000],
            ["aa07",   "agenda",  "secretaria",      100,        10,      15000],
            ["aa08",   "agenda",   "prenatal",        80,        15,      10000],
            ["aa09",   "agenda",   "escolar",         70,        28,      12000],
            ["aa10",   "agenda",   "ingeniero",       150,       30,      15000],
           ]
ventas=[  # folio,   fecha,       id,   cantidad, total
            [1001, "20-03-2024", "aa01", 2,     30000],
            [1002, "05-10-2024", "aa04", 2,     36000],
            [1003, "16-04-2023", "aa08", 4,     40000],
            [1004,  "28-04-2024", "aa09", 4,    48000],
            [1005, "20-03-2024", "aa01", 2,     30000],
            [1006,  "14-08-2022", "aa05", 3,    45000], 
            [1007,  "25-09-2022", "aa06", 1,    15000],
            [1008,  "18-12-2023", "aa02", 5,    50000],
            [1009,  "06-11-2023",  "aa03", 2,   30000],
            [1010, "01-07-2022",  "aa07", 3,    45000],
            [1011, "22-08-2023", "aa01", 2,     30000],
            [1012, "01-05-2022", "aa04", 2,     36000],
            [1013, "03-04-2023", "aa03", 2,     30000],
            [1014,  "13-05-2022", "aa10", 3,    45000],
            [1015, "10-03-2022", "aa04", 2,     30000],
            [1016,  "14-05-2022", "aa06", 3,    45000],
            [1017,  "25-09-2022", "aa06", 1,    15000],
            [1018,  "18-12-2024", "aa08", 5,    50000],
            [1019,  "06-11-2023",  "aa03", 2,   30000],
            [1020, "17-08-2024",  "aa07", 3,    45000],
            [1021,  "22-08-2021",  "aa10", 2,   30000],
        ]
def get_folio():
    elemento=len(ventas)-1
    return (ventas[elemento])[0]

print(len(productos))
os.system("pause")
opcion=0

while opcion<=4:

    print("""
            VENTAS DE KITY IMPRESIONES
            1.Vender Productos
            2.Reportes
            3.Mantencion de Ventas
            4.Salir
      """)
    opcion=int(input("Ingrese una Opcion entre 1-4: "))

    match opcion:
        

        case 1:
            print("VENDER PRODUCTOS")
            while True:
                os.system("cls")
                id=input("ingrese el Id del producto: ")
                sw=0 #no existe
                for a in productos:
                    if a[0]== id:
                        sw=1 #existe,encontrado
                        print(a[0]," ",a[1]," ",a[2]," ",a[3]," ",a[4]," ",a[5])
                    if sw==0:
                        print("ERROR, Id Producto no existe")
                        break

                    cantidad=int(input("Cuantas unidades desea comprar? "))
                    total=(cantidad*a[5])
                    if a[4]>=cantidad:
                                a[4]=a[4]-cantidad #stock actualizado
                                print("El total a pagar es: ", total)
                    else:
                                print("No hay stock suficiente")
                                break
                        
                    respuesta=input("Desea continuar con la compra? s/n: ")
                    if respuesta.lower() == "s":
                                #codigo para grabar la venta
                                ventas.append([get_folio()+1,fecha,id,cantidad,total])
                                #preguntar profe error de get folio+1
                                break
                    respuesta=input("Desea Comprar otro producto? s/n: ")
                    if respuesta.lower()=="n":
                            break
                
                    
                os.system("pause")

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
            op=int(input("Ingrese una opcion entre 1-6: "))
            if opcion>=1 and opcion<=6:
            
                match op:
                    case 1:
                        print("Agregar Productos nuevos a la Lista Productos \n")
                
                        id =input("Ingrese id producto:  ")
                        producto = input("Ingrese  producto:  ")
                        tema = input("Ingrese el Tema:  ")
                        paginas =int(input("Ingrese la cantidad de paginas:  "))
                        stock = int(input("Ingrese el stock:  "))
                        precio = int(input("Ingrese el precio:  "))
                        productos.append([id,producto,tema,paginas,stock,precio])
                    case 2: 
                        id=input("Ingrese id a buscar:")
                        sw=0 #no existe
                        for a in productos:
                            if a[0]== id:
                                sw=1 #existe,encontrado
                                print(a[0],"",a[1],"",a[2],a[3],"",a[4],"",a[5])
                                break

                        if sw==0:
                            print("ERROR, id no existe")
                    case 3: 
                    
                        id=input("Ingrese id producto a eliminar:  ")

                        i=0
                        sw=0 #id no encontrado  1 es id encontrado
                        while i<= (len(productos)-6):
                            if productos[i] == id:
                                sw=1  #encontrado
                                productos.pop(i) #elimina la id
                                productos.pop(i) #elimina el producto
                                productos.pop(i) #elimina el tema
                                productos.pop(i) #elimina las paginas
                                productos.pop(i) #elimina el stock
                                productos.pop(i) #elimina el precio
                                break #salir del ciclo
                            else:
                                i = i + 6 #salta a cada id

                        if sw==0: print("id no existe...")
                    case 4: 
                        print("\n Modificar\n")
                        id=input("Ingrese id producto a modificar:  ")

                        i=0
                        #sw es una bandera, porque almacena un estado
                        sw=0 #id no encontrado  1 es id encontrado
                        while i<= (len(productos)-6):
                            if productos[i] == id:
                                sw=1  #encontrado
                                print("id encontrado en el indice ",i)
                                print(productos[i]," ",productos[i+1]," ",productos[i+2]," ",productos[i+3]," ",
                                    productos[i+4]," ",productos[i+5])
                                
                                print("\n")
                                id =input("Ingrese id nueva del producto:  ")
                                producto = input("Ingrese  el nuevo nombre producto:  ")
                                tema = input("Ingrese el nuevo Tema:  ")
                                paginas =int(input("Ingrese la nueva cantidad de paginas:  "))
                                stock = int(input("Ingrese el nuevo stock:  "))
                                precio = int(input("Ingrese el nuevo precio:  "))

                                productos[i+1]=producto
                                productos[i+2]=tema
                                productos[i+3]=paginas
                                productos[i+4]=stock
                                productos[i+5]=precio
                                print("\n Listo! datos modificados")
                                break #salir del ciclo
                            else:
                                i = i + 6 #salta a cada id
                        if sw==0: print("id Producto no existe...")
                    case 5: 
                        print("\n Listar Productos\n")
                        for i in productos:
                           
                            print(i[0]," ",i[1]," ",i[2]," ",i[3]," ",i[4]," ",i[5])

                        
                if op==6:
                
                    break
                os.system("pause")
            else:
                print("Error, debe ingresar un valor entre 1 y 6")
                os.system("pause")
                
        
            
        