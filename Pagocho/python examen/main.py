import os

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
menu="""1.Agregar Producto \n2.Actualizar Cantidad \n3.Mostrar Inventario \n4.Buscar Producto \n5.Salir"""
opciones=[1,2,3,4,5]
inventario=[]
while True:
    print(menu)
    r=input("Elija una opcion: ")
    if not r.isdigit():
        print("Indique un numero valido ")
        r=None
        input("Dale enter para continuar")
        clear()
        continue
    r=int(r)
    if r<1 or r>len(opciones):
        print("Indique uan opcion valida")
        r=None
        input("Dale enter para continuar")
        clear()
        continue
    if r==5:
        exit()
    clear()    
    match r:
     
        case 1: 
            clear()
            nombre_pro=input("Ingrese nombre del producto: ")
            precio=input("Ingrese precio del producto:")
            cantidad=input("Ingrese la cantidad: ")
            inv={
                "nombre":nombre_pro,
                "precio":precio,
                "cantidad":cantidad

            }
            inventario.append(inv)
            clear()
        case 2:
            for i in range(len(inventario)):
                print(f'{i + 1} - Producto: {inventario[i]["nombre"]} Precio: {inventario[i]["precio"]} Cantidad: {inventario[i]["cantidad"]}')
            
            nombre_pro = input("Ingrese el nombre del producto a actualizar: ")
            if inv["nombre"]==nombre_pro:
                nueva_cantidad=input("Ingrese la cantidad")
                inv["cantidad"] = nueva_cantidad
                clear()
            else:
                print("Ese producto no se encuentra en el almacen")
                nombre_pro=None
                input("Dale enter para continuar")
                clear()
                
                continue    
            
     
            
        case 3:
            for i in range(len(inventario)):
                
                print(f'{i + 1} - Producto: {inventario[i]["nombre"]} Precio: {inventario[i]["precio"]} Cantidad: {inventario[i]["cantidad"]}')
                
                
            input("Dale enter para continuar")
            clear()        
        case 4:
            dato=input("Ingrese nombre del producto: ")
            resultado = list(filter(lambda elemento: elemento["nombre"].startswith(dato),inventario))
            clear()
            for invent in resultado:
                print(f'{invent["nombre"]} {invent["precio"]} {invent["cantidad"]}')
                print("==============")
            input("Presione enter para continuar...")
            clear()     


