from paquetes.agregar import añadir
from paquetes.agregar import mostrar


menu={ 
    1:"añadir producto",
    2:"actualizar cantidad de producto",
    3:"Mostrar inventario",
    4:"buscar producto"

}
dict_productos={} 
i=None
def main():
    while i==None: 
      for key, value in menu.items():
          print(f'{key}-{value}')
      opcion=int(input("ingrese una opcion"))
      match opcion:
        case 1:
          añadir()   
          i==None
        case 3:
            mostrar()
            i==None
       
main()
  



    


  

   