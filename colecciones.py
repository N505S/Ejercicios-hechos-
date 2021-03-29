#Escriba un programa donde tenga una lista
#y que a continuación, elimine los elementos
#repetidos, por último mostrar la lista

lista = ["Lunes","Martes","Miércoles","Jueves","Viernes","Lunes","Martes","Miércoles","Jueves","Viernes","Navidad"]
lista = list(set(lista))
print(lista)
#Los elementos repetidos han sido eliminados
