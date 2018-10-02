# Tema Hileras

message = input("Digite lo que quiera: ")
print(message)

# len() -> Encontrar la cantidad de caracteres que tiene una hilera
print(len(message))

# Indices
print(message[0])  # Obtenemos el 1er caracter de una hilera
print(message[len(message) -1])  # Obtenemos el ultimo caracter de una hilera

# Concatenacion
hilera = "Hilera inicial"

# Concatenacion simple
print(hilera + " otra hilera")
print(hilera)

# Contenacion modificando la variable
hilera += ". Esto si modifica la variable hilera"
print(hilera)

# Inyectar texto
otra_hilera = "Hola {} {}! Como esta? {}".format("Pedro", "Guzman", hilera)
print(otra_hilera)

# "Slices" / Sub-hileras
print(otra_hilera[3:6])
print(otra_hilera[:10])
print(otra_hilera[10:])