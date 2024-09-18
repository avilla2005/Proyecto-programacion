import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#info relevante para el mensaje 
NOMBRE = input("Cual es su nombre: ")
MATERIA = input("Que materia dicta: ")


#establecer conexión con el servidor
smtp_server = "smtp.gmail.com"
port = 465
username = "proyectoprogramacion191@gmail.com"
password = "hgyz ziae xqrr wrva"

#crear función para enviar correo
def send_individual_email(subject, message, recipients, attachment=None):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = username
    #adjuntar archivo
    if attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=attachment.name)
        msg.attach(part)

    body = MIMEText(message)
    msg.attach(body)

    for recipient in recipients:
        recipient = recipient.strip()
        with smtplib.SMTP_SSL(smtp_server, port) as smtp:
            smtp.login(username, password)
            smtp.sendmail(username, recipient, msg.as_string())

#destinatario
correo_destinatario = input("Ingrese la dirección de correo electrónico del destinatario: ")
correos = [correo_destinatario]  # Almacenar la dirección de correo en una lista

#opciones para elegir
choice = input("Que desea informar en el correo?\n"
               "a. Enviar definitiva de la materia.\n"
               "b. preguntar por un incoveniente (ausencia, falla, retardo, malas notas).\n"
               "c. reclutamiento.\n"
               "d. Adjuntar un archivo.\n"
               "e. Redactar un correo (sin archivo).\n"
               "f. Redactar un correo (con archivo).\n")
if choice == "a":
    definitiva = input("definitiva del estudiante: ")
    subject = f"Definitiva de la materia - {NOMBRE}, {MATERIA}"
    message = f"Hola mi estudiante,\n\nEnvío este mensaje para informarle su definitiva que es de {definitiva}. \ncualquier duda estare atento \nGracias por su atención.\n\n{NOMBRE}, {MATERIA}\n."
    send_individual_email(subject, message, correos)
elif choice == "b":
    falla = input("cual es el problema con el estudiante: ")
    subject = f"¿que pasa?"
    message = f"Estimado estudiante,\n\nEspero que se encuentren bien. Le envio este correo para preguntar por: {falla} \n\n ya que esto puede implicar que se pueda atrasar en la materia y bajar sus calificaciones.\n\nespero pronta respuesta.\n\nAgradezco su comprensión y cooperación en esta situación.\n\nAtentamente,\n{NOMBRE}, {MATERIA}\n."
    send_individual_email(subject, message, correos)
elif choice == "c":
    subject = f"Traigan los siguientes materiales"
    message = f"Estimado estudiante,\n\nle mando unas felicitaciones por su rendimiento en la materia:\nme gustaria involucrarlo en una actividad relacionada con la materia, donde habran recompensas por su participacion.\n\nGracias nuevamente por su ayuda y comprensión.\n\nAtentamente,\n{NOMBRE}, {MATERIA}\n."
    send_individual_email(subject, message, correos)
elif choice == "d":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ")
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = f"Adjunto de archivo - {NOMBRE}, {MATERIA}"
            message = f"Estimados estudiantes,\n\nAdjunto un archivo para complementar el contenido de la clase. Por favor, revisen el archivo adjunto.\n\nAtentamente,\n{NOMBRE}, {MATERIA}\n."
            send_individual_email(subject, message, correos, attachment)
    except FileNotFoundError:
        print("El archivo no se encontró. ")

elif choice == "e":
    asunto = input("Ingrese el asunto: ") 
    mensaje = input("Redacte el mensaje: ")
    subject = f"{asunto}"
    message = f"{mensaje}"
    send_individual_email(subject, message, correos)

elif choice == "f":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ")
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = input("Ingrese el asunto: ")
            message = input("Redacte el mensaje: ")
            send_individual_email(subject, message, correos, attachment)
    except FileNotFoundError:
        print("El archivo no se encontró. ")
else:
    print("No está en las opciones.")
    exit()

print("Correo enviado.")
correos.clear()
