dict_productos={}
def añadir():
      print("adfdaf")
      producto=input("ingrese el producto que desea agregar")
      cant=None
      precio=None
      while cant==None:
            cant=input("ingrese la cantidad que tiene este producto")
            if not cant.isdigit():
                  print ("solo se puede ingresar numeros enteros")
                  cant=None
                  continue
      while precio==None:
            precio=input("ingrese el precio que tiene este producto")
            if not cant.isdigit():
                  print ("solo se puede ingresar numeros enteros")
                  precio=None
                  continue       
            cant=int(cant)
            precio=int(precio)
            dict_productos[producto]={cant, precio}
            print(dict_productos[producto][precio][cant])

def mostrar():
      for key,value in dict_productos.items():
           
            print(f'producto: {key}-cantidad: {value}')
            input("presiona enter para continuar")

def actualizar():  
      x=None
      while x==None:
            x=input("Ingrese la clave del producto a cambiar")          
      
      
      
      
 