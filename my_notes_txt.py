# Semana 16 Tarea: Trabajo con Archivos de Texto en Python
# operaciones de lectura y escritura en archivos de texto en Python.

# 1. Escritura de Archivo de Texto:

#Crea un nuevo archivo llamado my_notes.txt.
nombrearchivo = 'my_notes.txt'
print('Se ha creado y guardado llamado:',nombrearchivo)

#Escribe al menos tres líneas de notas personales en el archivo.
# Archivo en modo escritura 'write'
nombrearchivo = open('my_notes.txt','w')
nombrearchivo.write ("Notas personales.\n")#El \n se coloca para indicar fin de línea
nombrearchivo.write("1. Soy estudiante de la UEA.\n")
nombrearchivo.write("2. Estoy cursando el Nivel 1.\n")
nombrearchivo.write("3. Aspiro ser Ingeniería en Tecnologias de la Informacion.\n")
nombrearchivo.close() # Cierra el archivo

# 2. Lectura de Archivo de Texto:

# Abre el archivo my_notes.txt
nombrearchivo = open ('my_notes.txt','r')
mensaje = nombrearchivo.read()
print(mensaje)
nombrearchivo.close()
#Lee el contenido del archivo línea por línea utilizando el método adecuado.
nombrearchivo = open("my_notes.txt","r")
contenido = nombrearchivo.read()
print(contenido)
nombrearchivo.close()

# Muestra en la consola cada línea leída.
nombrearchivo = open('my_notes.txt','r')
datos = nombrearchivo.readlines()
for linea in datos:
    palabras = linea.split(',')
    print(palabras)
    nombrearchivo.close()#Cierre de Archivos:

