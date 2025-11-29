import random # Importa el módulo 'random', necesario para que la computadora elija su jugada.
# Inicialización de variables
opcion_usuario = "" # Inicializa la variable que guardará la entrada del usuario como una cadena vacía.
jugar = True # Inicializa la variable de control booleana. Mientras sea True, el juego continuará.

print("👋 ¡Bienvenido al juego de Piedra, Papel o Tijera!") # Imprime el mensaje de bienvenida al usuario.

# Bucle principal del juego
while jugar: # Inicia el bucle principal. El código dentro se repite mientras 'jugar' sea True.
    print("............................................") # Imprime una línea separadora para el formato.
    print("--- MENÚ ---") # Imprime el encabezado del menú.
    
    # Imprimir el menú de forma explícita
    print("1. Piedra") # Muestra la primera opción del menú.
    print("2. Papel") # Muestra la segunda opción del menú.
    print("3. Tijera") # Muestra la tercera opción del menú.
    print("4. Salir") # Muestra la opción para terminar el juego.
    
    print("............................................") # Imprime una línea separadora para el formato.

    # --- 1. Obtener elección del usuario ---
    opcion_usuario = input("Ingresa tu elección (1-4): ") # Pide al usuario que ingrese su opción y guarda el valor (como string).

    # --- 2. Procesar la opción ---
    
    if opcion_usuario == "4": # Comprueba si el usuario eligió la opción "4" (Salir).
        # Opción 4: Salir
        jugar = False # Cambia la bandera 'jugar' a False para terminar el bucle 'while'.
        print("Gracias por jugar. ¡SALIO DEL JUEGO! 👋") # Mensaje de despedida.
        
    elif opcion_usuario in ["1", "2", "3"]: # Comprueba si el usuario eligió una opción válida de juego (1, 2, o 3).
        
        # --- Mapeo de la entrada a la jugada usando solo condicionales ---
        eleccion_usuario = "" # Inicializa la variable que guardará la jugada del usuario (Piedra, Papel o Tijera).
        if opcion_usuario == "1": # Si la entrada es "1"...
            eleccion_usuario = "Piedra" # ...asigna "Piedra".
        elif opcion_usuario == "2": # Si la entrada es "2"...
            eleccion_usuario = "Papel" # ...asigna "Papel".
        elif opcion_usuario == "3": # Si la entrada es "3"...
            eleccion_usuario = "Tijera" # ...asigna "Tijera".
        
        # Obtener elección de la computadora
        opciones_juego = ["Piedra", "Papel", "Tijera"] # Crea una lista con las jugadas posibles.
        eleccion_computadora = random.choice(opciones_juego) # La computadora elige un elemento al azar de la lista.
        
        # --- 3. Determinar el ganador (Lógica del Juego) ---
        print(f"Tú elegiste: **{eleccion_usuario}**") # Muestra la jugada del usuario.
        print(f"La computadora eligió: **{eleccion_computadora}**") # Muestra la jugada de la computadora.
        
        ganador = "" # Inicializa la variable para guardar el resultado de la ronda.
        if eleccion_usuario == eleccion_computadora: # Comprueba si hay empate.
            ganador = "empate" # Si son iguales, establece el resultado como empate.
        # Lógica de las reglas para la victoria del usuario
        # Comprueba las tres combinaciones donde el usuario gana.
        elif (eleccion_usuario == "Piedra" and eleccion_computadora == "Tijera") or \
             (eleccion_usuario == "Papel" and eleccion_computadora == "Piedra") or \
             (eleccion_usuario == "Tijera" and eleccion_computadora == "Papel"):
            ganador = "usuario" # Si alguna condición anterior es True, el usuario gana.
        else: # Si no fue empate ni el usuario ganó,
            ganador = "computadora" # ...la computadora es el ganador.

        # --- 4. Anunciar el resultado ---
        if ganador == "usuario": # Si el resultado fue "usuario"...
            print("🎉 ¡GANO EL JUEGO!") # ...anuncia la victoria del usuario.
        elif ganador == "computadora": # Si el resultado fue "computadora"...
            print("😞 La computadora ganó ESTE JUEGO") # ...anuncia la victoria de la computadora.
        else: # Si el resultado fue "empate"...
            print("🤝 ¡ES UN EMPATE!") # ...anuncia el empate.

    else:
        # Manejo de entradas que no son 1, 2, 3 o 4
        print("❌ Opción no VALIDA. Por favor, ingresa un número válido (1, 2, 3 o 4).") # Muestra un error por entrada inválida.