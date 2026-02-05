import random

user_input = input("Piedra, Papel o Tijeras: ")
opciones = ["Piedra","Papel", "Tijeras"]
opc_computadora = random.choice(opciones)

def validacion(user: str, opcCompu: str):
    if user == opcCompu:
        return "Empate"
        
    elif user == "Piedra":
        if opcCompu == "Tijeras":
            return "Piedra mas que tijeras. Ganas"
        elif opcCompu == "Piedra":
            return "Papel mas que piedra. Pierdes"
            
    elif user == "Papel":
        if opcCompu == "Piedra":
            return "Papel mas que roca. Ganas"
        elif opcCompu == "Tijeras":
            return "Tijeras mas que papel. Pierdes"
            
    elif user == "Tijeras":
        if opcCompu == "Papel":
            return "Tijeras mas que papel. Ganas"
        elif opcCompu == "Piedra":
            return "Piedra mas que papel. Pierdes"
    else:
        return "Que hace?"


resultado = validacion(user_input , opc_computadora)
print(f"user selecciono {user_input}. El pc selecciono {opc_computadora}")
print(resultado)