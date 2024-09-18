import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#info relevante para el mensaje
NOMBRE = input("Cual es su nombre: ")
facultad = input("ingrese su curso o facultad: ")


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
correo_destinatario = input("Ingrese la direccion de correo electronico del destinatario: ")
correos = [correo_destinatario]  # Almacenar la dirección de correo en una lista

#opciones para elegir
choice = input("Que desea informar en el correo?\n"
               "a. Peticion reunion.\n"
               "b. Asesoria de tutorias.\n"
               "c. Consulta de tareas.\n"
               "d. Adjuntar un archivo.\n"
               "e. Redactar un correo (sin archivo).\n"
               "f. Redactar un correo (con archivo).\n")

if choice == "a":
    subject = f"Peticion reunion - {facultad}"
    message = f"Estimados docentes,\n Por medio del presente correo me gustaria solicitar una reunion para discutir una asunto importante.\n Preferiblemente en una ubicacion conveniente para ambas partes o a traves de una plataforma de videoconferencias.\n Aprecio sinceramente su tiempo y consideracion. Espero poder contar con la oportunidad de reunirme con usted y discutir este asunto en profundidad.\n Quedo a su disposicion para cualquier pregunta adicional o para proporcionar cualquier informacion adicional que pueda necesitar.\n Gracias por su comprension.\n\nAtentamente,\n{NOMBRE}\n{facultad}\n."
    send_individual_email(subject, message, correos)
elif choice == "b":
    subject = f"Asesoria de Turorias - {facultad}"
    message = f"Estimados docentes,\nComo estudiante comprometido con mi desarrollo academico, he estado enfrentando desafios en el desarrollo de clase y siento que podria beneficiarme de su experiencia y conocimientos como tutor. Me gustaria solicitar una asesoria personalizada para recibir orientacio y ayuda adicional en este tema.\nSi es posible, me gustaria solicitar una asesoria, ya sea en persona o a traves de una plataforma de videoconferencia. Estoy dispuesto/a a adaptarme a su disponibilidad y preferencias.\n\nGracias por su comprension y cooperacion.\n\nAtentamente,\n{NOMBRE}\n{facultad}\n."
    send_individual_email(subject, message, correos)
elif choice == "c":
    subject = f"Consulta de tareas - {facultad}"
    message = f"Estimados docentes,\nMe dirrijo a ustedes por que me gustaria solicitar informacion sobre las tareas que se encuentran pendientes, fechas de entrega y cualquier detalle adicional que pueda ser relevante. Debido a [razones personales, dificultades, etc.], me he retrasado en la organizacion y seguimiento de las tareas, y me gustaria ponerme al dia lo antes posible.\nAprecio sinceramente cualquier orientacion, instrucciones o materiales adicionales que pueda proporcionar para facilitar mi completacion de las tareas pendientes. Si hay alguna modificacion en los plazos o alguna tarea adicional, le agradeceria que me lo informara..\n\nGracias por su colaboracion.\n\nAtentamente,\n{NOMBRE}\n{facultad}\n."
    send_individual_email(subject, message, correos)
elif choice == "d":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ")
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = f"Adjunto de archivo - {facultad}"
            message = input("Ingrese el mensaje para acompañar el archivo adjunto:\n")
            message = f"Estimados docentes,\n\nPara facilitar nuestra comunicacion y proporcionarle mas detalles sobre mi solicitud, adjunto un archivo a este correo electronico. En el archivo adjunto, encontrara un resumen de los temas especificos en los que necesito su orientacion y asesoria.\nQuedo a su disposicion para proporcionar cualquier informacion adicional que pueda necesitar. Agradezco su atencion a esta solicitud y espero su respuesta.\n{message}\n\nAtentamente,\n{NOMBRE}\n{facultad}\n."
            send_individual_email(subject, message, correos, attachment)
    except FileNotFoundError:
        print("El archivo no se encontro.")
elif choice == "e":
    subject = input("Ingrese el asunto: ")
    message = input("Redacte el mensaje: ")
    send_individual_email(subject, message, correos)
elif choice == "f":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ")
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = input("Ingrese el asunto: ")
            message = input("Redacte el mensaje: ")
            send_individual_email(subject, message, correos, attachment)
    except FileNotFoundError:
        print("El archivo no se encontro.")
else:
    print("No esta en las opciones.")
    exit()
print("Correo enviado.")
correos.clear()
