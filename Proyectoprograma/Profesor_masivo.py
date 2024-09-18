import smtplib #conexion
from email.mime.text import MIMEText    #formato al texto
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders #64

#info relevante para el mensaje
NOMBRE = input("Cual es su nombre: ")
MATERIA = input("Que materia dicta: ")


#establecer conexión con el servidor
smtp_server = "smtp.gmail.com"
port = 465
username = #Ingresa aquí tu correo
password = #Ingresa aquí tu contraseña

#crear funcion para enviar correo
def send_masive_email(subject, message, recipients, attachment=None):
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

#destinatarios
lista_correos = input("ingrese el nombre de el archivo con correos deseados: ")
with open(lista_correos, "r") as f:
    correos = f.readlines()

#opciones para elegir
choice = input("¿Que desea informar en el correo?\na. Clase cancelada.\nb. Voy a tardar en llegar a la clase.\nc. Traigan los siguientes materiales.\nd. Adjuntar un archivo.\ne. redactar un correo (sin archivo)\nf. redactar un correo (con archivo) \n")

if choice == "a":
    subject = f"Clase cancelada - {NOMBRE}, {MATERIA}"
    message = f"Hola mis estudiantes,\n\nEnvio este mensaje para informarles que la clase de hoy está cancelada. Lamento la cancelacion y pronto repondré la clase.\n\nGracias por su atención.\n\n{NOMBRE}, {MATERIA}."
    send_masive_email(subject, message, correos)
elif choice == "b":
    time = input("Ingrese cuánto tiempo aproximado se va a demorar (use minutos): ")
    subject = f"Voy a llegar tarde a la clase"
    message = f"Estimados estudiantes,\n\nEspero que se encuentren bien. Les escribo para informarles que, lamentablemente, me retrasare en mi llegada a la clase de hoy. Me tardaré aproximadamente {time} minutos debido a circunstancias imprevistas que han surgido.\n\nLes pido disculpas por cualquier inconveniente que esto pueda causarles. Hago todo lo posible por ser puntual y respetar nuestro horario académico, pero a veces surgen situaciones fuera de nuestro control.\n\nPara minimizar el impacto de mi retraso, he dejado instrucciones con el asistente de profesor para que les proporcione materiales de estudio o ejercicios que puedan realizar mientras esperamos mi llegada.\n\nAgradezco su comprensión y cooperación en esta situación.\n\nAtentamente,\n{NOMBRE}, {MATERIA}."
    send_masive_email(subject, message, correos)
elif choice == "c":
    materials = input("Ingrese los materiales para informar: ")
    subject = f"Traigan los siguientes materiales"
    message = f"Estimados estudiantes,\n\nAgradecería enormemente si pudieran proporcionarme el siguiente material:\n\n{materials}\n\nEspero que puedan traer los materiales solicitados para la próxima clase para poder realizar la actividad.\n\nGracias nuevamente por su ayuda y comprensión.\n\nAtentamente,\n{NOMBRE}, {MATERIA}."
    send_masive_email(subject, message, correos)
elif choice == "d":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ")
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = f"Adjunto de archivo - {NOMBRE}, {MATERIA}"
            message = f"Estimados estudiantes,\n\nAdjunto un archivo para complementar el contenido de la clase. Por favor, revisen el archivo adjunto.\n\nAtentamente,\n{NOMBRE}, {MATERIA}."
            send_masive_email(subject, message, correos, attachment)
    except FileNotFoundError:
        print("El archivo no se encontro. ")

elif choice == "e":
    asunto = input("Ingrese el asunto: ")
    mensaje = input("Redacte el mensaje: ")
    subject = f"{asunto}"
    message = f"{mensaje}"
    send_masive_email(subject, message, correos)

elif choice == "f":
    attachment_path = input("Ingrese la ruta del archivo que desea adjuntar: ") #archivo con correos
    try:
        with open(attachment_path, 'rb') as attachment:
            subject = input("Ingrese el asunto: ")
            message = input("Redacte el mensaje: ")
            send_masive_email(subject, message, correos, attachment)
    except:
        print("El archivo no se encontro. ")
else:
    print("No está en las opciones.")
    exit()

print("Correo enviado.")
