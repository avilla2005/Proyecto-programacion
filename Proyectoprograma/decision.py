
def decision():
    usuario = input("Seleccione su tipo de usuario: \n a = Estudiante \n b = profesor \n c = ejecutivo \n d = Correo Html ")
    if usuario == "a":
        from Estudiantes import send_individual_email
    elif usuario == "b":
        profesor = input("desea mandar un correo masivo o individual:\n a = MASIVO \n b individual ")
        if profesor == "a":
            from Profesor_masivo import send_masive_email
        elif profesor == "b":
            from Profesor_individual import send_individual_email
        else:
            print("usted ha seleccionado una opcion no valida")
    elif usuario == "c":
        ejecutivo = input("desea mandar un correo masivo o individual:\n a = MASIVO \n b individual ")
        if ejecutivo == "a":
            from Ejecutivo_masivo import send_email
        elif ejecutivo == "b":
            from ejecutivo_individual import send_individual_email
        else:
            print("usted ha seleccionado una opcion no valida")
    elif usuario =="d":
        from Correo_html import Correo_html
    else: 
        print("usted ha seleccionado una opcion no valida")
decision()    
