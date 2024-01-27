#metodo capitalize -- devuelve el primer dato en mayuscula
texto = "hola mundo"
resultado = texto.capitalize
print(resultado)
#metodo find -- busca texto devuelve dato boll
texto="hola mundo"
resultado=texto.find("mundo")
print(resultado)
#metodo center
texto = "hola" # devuelve true si todos los caracteres de la cadena son afirmativos
resultado=texto.isalnum
#metodo.isdigit
texto = 2345
resultado = str(texto).isdigit()

print(resultado)

#Metodo islower devuelve True si todo los caracter en la cadena estan en minuscula
texto="asddfg"
resultado=texto.islower()
print(resultado)
#metodo isspace(): devuelve true si toda la cadena son espacios en blanco
texto=" "
resultado=texto.isspace()
print(resultado)
#isupper() Devuelve true cuando toda la cadena esta escrita en mayuscula 
texto="HOLA"
resultado=texto.isupper()
print(resultado)
#lower devuelve una copia de la cadena con las letras convertidas a minusuculas
texto="HOLA"
resultado=texto.lower()
print(resultado)
#lstrip devuelve la cadena con los primeros espacion en blancos onmitidos
texto="     hola"
resultado=texto.lstrip()
print(resultado)
#replace(v, n) sustituye v por n
texto="viño"
resultado=texto.replace("v", "n")
print(resultado)
#split([s]) devuelve una lista que contiene las palabras de la cadena
texto = "sapo"
resultado = texto.split("s")
print(resultado)
