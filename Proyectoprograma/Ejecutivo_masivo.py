import smtplib
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Informacion relevante para el mensaje
NOMBRE = input("Ingrese su nombre: ")
EMPRESA = input("Ingrese el nombre de la empresa: ")
# Establecer conexion con el servidor
smtp_server = "smtp.gmail.com"
port = 465
username = #Pon aquí tu correo
password = #Pon aquí tu contraseña

# Crear funcion para enviar correo
def send_email(subject, message, recipients, attachment=None):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = username
    # Adjuntar archivo
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

# Destinatarios
lista_correos = input("Ingrese el nombre del archivo con los correos deseados: ")
with open(lista_correos, "r") as f:
    correos = f.readlines()

# Opciones para elegir
choice = input("Que desea informar en el correo?\n"
               "a. Reunion cancelada.\n"
               "b. Cambio en la agenda.\n"
               "c. Solicitud de documentos.\n"
               "d. Adjuntar un archivo.\n"
               "e. Redactar un correo (sin archivo).\n"
               "f. Redactar un correo (con archivo).\n")

if choice == "a":
    subject = f"Reunion cancelada - {EMPRESA}"
    message = f"Estimados colaboradores,\n\nLes informo que la reunion programada para hoy ha sido cancelada. Lamentamos cualquier inconveniente que esto pueda causar y pronto estaremos coordinando una nueva fecha.\n\nGracias por su comprension.\n\nAtentamente,\n{NOMBRE}\n{EMPRESA}\n."
    send_email(subject, message, correos)
elif choice == "b":
    subject = f"Cambio en la agenda - {EMPRESA}"
    message = input("Ingrese el mensaje para informar el cambio en la agenda:\n")
    message = f"Estimados colaboradores,\n\nLes informo que ha habido un cambio en nuestra agenda. {message}\n\nPor favor, tengan en cuenta esta actualizacion y ajusten sus horarios en consecuencia.\n\nGracias por su comprension y cooperacion.\n\nAtentamente,\n{NOMBRE}\n{EMPRESA}\n."
    send_email(subject, message, correos)
elif choice == "c":
    subject = f"Solicitud de documentos - {EMPRESA}"
    message = input("Ingrese los documentos que desea solicitar:\n")
    message = f"Estimados colaboradores,\n\nLes escribo para solicitarles los siguientes documentos:\n\n{message}\n\nPor favor, proporcionen los documentos solicitados a la brevedad posible.\n\nGracias por su colaboracion.\n\nAtentamente,\n{NOMBRE}\n{EMPRESA}\n."
    send_email(subject, message, correos)
elif choice == "d":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ")
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = f"Adjunto de archivo - {EMPRESA}"
            message = input("Ingrese el mensaje para acompañar el archivo adjunto:\n")
            message = f"Estimados colaboradores,\n\nAdjunto un archivo para complementar la informacion. Por favor, revisen el archivo adjunto.\n\n{message}\n\nAtentamente,\n{NOMBRE}\n{EMPRESA}\n."
            send_email(subject, message, correos, attachment)
    except FileNotFoundError:
        print("El archivo no se encontro.")
elif choice == "e":
    subject = input("Ingrese el asunto: ")
    message = input("Redacte el mensaje: ")
    send_email(subject, message, correos)
elif choice == "f":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ")
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = input("Ingrese el asunto: ")
            message = input("Redacte el mensaje: ")
            send_email(subject, message, correos, attachment)
    except FileNotFoundError:
        print("El archivo no se encontro.")
else:
    print("No esta en las opciones.")
    exit()

print("Correo enviado.")
