import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
username = #Ingresa aqui tu correo
password = #Ingresa aquí la contraseña de tu correo
# Configración del servidor SMTP
smtp_server = "smtp.gmail.com"
port = 465  # Puerto para SSL
# Función para enviar correo con archivos adjuntos
def Correo_html(subject, message, recipients, attachment=None):
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = ", ".join(recipients)  # Unir los correos para el campo 'To'
    msg["Subject"] = subject
    msg.attach(MIMEText(message, 'html'))
    if attachment:
        try:
            with open(attachment, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment', filename=attachment.split("/")[-1])
                msg.attach(part)
        except FileNotFoundError:
            print(f"El archivo {attachment} no se encontró.")
    with smtplib.SMTP_SSL(smtp_server, port) as smtp:
        smtp.login(username, password)
        smtp.sendmail(username, recipients, msg.as_string())  # Enviar el correo
lista_correos = "correos.csv"
with open(lista_correos, "r") as f:
    correos = [email.strip() for email in f.readlines()]  # Eliminar espacios en blanco
subject = "Proyecto"
message = """
<!DOCTYPE html>
<html xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office" lang="en">

<head>
	<title></title>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0"><!--[if mso]><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch><o:AllowPNG/></o:OfficeDocumentSettings></xml><![endif]--><!--[if !mso]><!-->
	<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@100;200;300;400;500;600;700;800;900" rel="stylesheet" type="text/css"><!--<![endif]-->
	<style>
		* {
			box-sizing: border-box;
		}

		body {
			margin: 0;
			padding: 0;
		}

		a[x-apple-data-detectors] {
			color: inherit !important;
			text-decoration: inherit !important;
		}

		#MessageViewBody a {
			color: inherit;
			text-decoration: none;
		}

		p {
			line-height: inherit
		}

		.desktop_hide,
		.desktop_hide table {
			mso-hide: all;
			display: none;
			max-height: 0px;
			overflow: hidden;
		}

		.image_block img+div {
			display: none;
		}

		sup,
		sub {
			line-height: 0;
			font-size: 75%;
		}

		.menu_block.desktop_hide .menu-links span {
			mso-hide: all;
		}

		#memu-r1c1m0:checked~.menu-links {
			background-color: #000000 !important;
		}

		#memu-r1c1m0:checked~.menu-links a,
		#memu-r1c1m0:checked~.menu-links span {
			color: #ffffff !important;
		}

		@media (max-width:700px) {
			.desktop_hide table.icons-outer {
				display: inline-table !important;
			}

			.desktop_hide table.icons-inner,
			.social_block.desktop_hide .social-table {
				display: inline-block !important;
			}

			.icons-inner {
				text-align: center;
			}

			.icons-inner td {
				margin: 0 auto;
			}

			.image_block div.fullWidth {
				max-width: 100% !important;
			}

			.menu-checkbox[type=checkbox]~.menu-links {
				display: none !important;
				padding: 5px 0;
			}

			.menu-checkbox[type=checkbox]:checked~.menu-trigger .menu-open {
				display: none !important;
			}

			.menu-checkbox[type=checkbox]:checked~.menu-links,
			.menu-checkbox[type=checkbox]~.menu-trigger {
				display: block !important;
				max-width: none !important;
				max-height: none !important;
				font-size: inherit !important;
			}

			.menu-checkbox[type=checkbox]~.menu-links>a,
			.menu-checkbox[type=checkbox]~.menu-links>span.label {
				display: block !important;
				text-align: center;
			}

			.menu-checkbox[type=checkbox]:checked~.menu-trigger .menu-close {
				display: block !important;
			}

			.mobile_hide {
				display: none;
			}

			.row-content {
				width: 100% !important;
			}

			.stack .column {
				width: 100%;
				display: block;
			}

			.mobile_hide {
				min-height: 0;
				max-height: 0;
				max-width: 0;
				overflow: hidden;
				font-size: 0px;
			}

			.desktop_hide,
			.desktop_hide table {
				display: table !important;
				max-height: none !important;
			}

			.reverse {
				display: table;
				width: 100%;
			}

			.reverse .column.first {
				display: table-footer-group !important;
			}

			.reverse .column.last {
				display: table-header-group !important;
			}

			.row-25 td.column.first .border,
			.row-25 td.column.last .border,
			.row-27 td.column.first .border,
			.row-27 td.column.last .border,
			.row-29 td.column.first .border,
			.row-29 td.column.last .border {
				padding: 15px;
				border-top: 0;
				border-right: 0px;
				border-bottom: 0;
				border-left: 0;
			}

			.row-4 .column-1 .block-1.image_block td.pad {
				padding: 20px !important;
			}

			.row-10 .column-1 .block-2.heading_block h2,
			.row-10 .column-1 .block-2.menu_block label .menu-trigger .menu-label,
			.row-10 .column-1 .block-3.heading_block h2,
			.row-10 .column-1 .block-3.menu_block label .menu-trigger .menu-label,
			.row-10 .column-1 .block-7.heading_block h2,
			.row-10 .column-1 .block-7.menu_block label .menu-trigger .menu-label,
			.row-17 .column-1 .block-2.heading_block h2,
			.row-17 .column-1 .block-2.menu_block label .menu-trigger .menu-label,
			.row-18 .column-1 .block-1.heading_block h2,
			.row-18 .column-1 .block-1.menu_block label .menu-trigger .menu-label,
			.row-18 .column-2 .block-1.icons_block td.pad,
			.row-20 .column-1 .block-2.heading_block h3,
			.row-20 .column-1 .block-2.menu_block label .menu-trigger .menu-label,
			.row-20 .column-1 .block-3.heading_block h3,
			.row-20 .column-1 .block-3.menu_block label .menu-trigger .menu-label,
			.row-20 .column-2 .block-8.heading_block h3,
			.row-20 .column-2 .block-8.menu_block label .menu-trigger .menu-label,
			.row-20 .column-2 .block-9.heading_block h3,
			.row-20 .column-2 .block-9.menu_block label .menu-trigger .menu-label,
			.row-22 .column-1 .block-1.heading_block h2,
			.row-22 .column-1 .block-1.menu_block label .menu-trigger .menu-label,
			.row-22 .column-2 .block-1.icons_block td.pad,
			.row-23 .column-1 .block-1.heading_block h2,
			.row-23 .column-1 .block-1.menu_block label .menu-trigger .menu-label,
			.row-25 .column-1 .block-1.heading_block h3,
			.row-25 .column-1 .block-1.menu_block label .menu-trigger .menu-label,
			.row-25 .column-1 .block-2.paragraph_block td.pad>div,
			.row-27 .column-1 .block-1.heading_block h3,
			.row-27 .column-1 .block-1.menu_block label .menu-trigger .menu-label,
			.row-27 .column-1 .block-2.paragraph_block td.pad>div,
			.row-29 .column-1 .block-1.heading_block h3,
			.row-29 .column-1 .block-1.menu_block label .menu-trigger .menu-label,
			.row-29 .column-1 .block-2.paragraph_block td.pad>div,
			.row-3 .column-1 .block-3.heading_block h1,
			.row-3 .column-1 .block-3.menu_block label .menu-trigger .menu-label,
			.row-4 .column-2 .block-1.heading_block h1,
			.row-4 .column-2 .block-1.menu_block label .menu-trigger .menu-label,
			.row-5 .column-2 .block-1.heading_block h1,
			.row-5 .column-2 .block-1.menu_block label .menu-trigger .menu-label,
			.row-6 .column-1 .block-2.heading_block h1,
			.row-6 .column-1 .block-2.menu_block label .menu-trigger .menu-label,
			.row-8 .column-1 .block-1.heading_block h3,
			.row-8 .column-1 .block-1.menu_block label .menu-trigger .menu-label,
			.row-8 .column-1 .block-2.heading_block h3,
			.row-8 .column-1 .block-2.menu_block label .menu-trigger .menu-label,
			.row-8 .column-2 .block-1.heading_block h3,
			.row-8 .column-2 .block-1.menu_block label .menu-trigger .menu-label,
			.row-8 .column-2 .block-2.heading_block h3,
			.row-8 .column-2 .block-2.menu_block label .menu-trigger .menu-label,
			.row-8 .column-3 .block-1.heading_block h3,
			.row-8 .column-3 .block-1.menu_block label .menu-trigger .menu-label,
			.row-8 .column-3 .block-2.heading_block h3,
			.row-8 .column-3 .block-2.menu_block label .menu-trigger .menu-label {
				text-align: center !important;
			}

			.row-4 .column-2 .block-1.heading_block h1 {
				font-size: 32px !important;
			}

			.row-10 .column-1 .block-2.heading_block h2,
			.row-10 .column-1 .block-3.heading_block h2,
			.row-10 .column-1 .block-7.heading_block h2,
			.row-17 .column-1 .block-2.heading_block h2,
			.row-18 .column-1 .block-1.heading_block h2,
			.row-22 .column-1 .block-1.heading_block h2,
			.row-23 .column-1 .block-1.heading_block h2,
			.row-3 .column-1 .block-3.heading_block h1,
			.row-6 .column-1 .block-2.heading_block h1 {
				font-size: 56px !important;
			}

			.row-5 .column-2 .block-1.heading_block h1 {
				font-size: 16px !important;
			}

			.row-7 .column-1 .block-2.heading_block h3 {
				font-size: 26px !important;
			}

			.row-10 .column-1 .block-1.spacer_block,
			.row-9 .column-1 .block-1.spacer_block {
				height: 20px !important;
			}

			.row-10 .column-1 .block-4.paragraph_block td.pad>div,
			.row-13 .column-2 .block-1.paragraph_block td.pad>div,
			.row-15 .column-1 .block-1.paragraph_block td.pad>div,
			.row-15 .column-2 .block-1.paragraph_block td.pad>div {
				font-size: 25px !important;
			}

			.row-10 .column-1 .block-8.spacer_block {
				height: 6px !important;
			}

			.row-10 .column-1 .block-6.spacer_block {
				height: 45px !important;
			}

			.row-2 .column-1,
			.row-2 .column-2 {
				padding: 10px !important;
			}

			.row-12 .column-1,
			.row-13 .column-1 {
				padding: 0 !important;
			}
		}
	</style><!--[if mso ]><style>sup, sub { font-size: 100% !important; } sup { mso-text-raise:10% } sub { mso-text-raise:-10% }</style> <![endif]-->
</head>

<body class="body" style="background-color: #000000; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
	<table class="nl-container" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;">
		<tbody>
			<tr>
				<td>
					<table class="row row-1" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:25px;line-height:25px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-2" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="left" style="line-height:10px">
																	<div style="max-width: 51px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/logo_light.png" style="display: block; height: auto; border: 0; width: 100%;" width="51" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="menu_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<table width="100%" cellpadding="0" cellspacing="0" border="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																	<tr>
																		<td class="alignment" style="text-align:right;font-size:0px;"><!--[if !mso]><!--><input class="menu-checkbox" id="memu-r1c1m0" type="checkbox" style="display:none !important;max-height:0;visibility:hidden;"><!--<![endif]-->
																			<div class="menu-trigger" style="display:none;max-height:0px;max-width:0px;font-size:0px;overflow:hidden;"><label class="menu-label" for="memu-r1c1m0" style="height: 36px; width: 36px; display: inline-block; cursor: pointer; mso-hide: all; user-select: none; align: right; text-align: center; color: #ffffff; text-decoration: none; background-color: #000000; border-radius: 0;"><span class="menu-open" style="word-break: break-word; mso-hide: all; font-size: 26px; line-height: 31.5px;">☰</span><span class="menu-close" style="word-break: break-word; display: none; mso-hide: all; font-size: 26px; line-height: 36px;">✕</span></label></div>
																			<div class="menu-links"><!--[if mso]><table role="presentation" border="0" cellpadding="0" cellspacing="0" align="right" style=""><tr style="text-align:right;"><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:15px;padding-bottom:5px;padding-left:15px"><![endif]--><a href="www.example.com" target="_self" style="mso-hide:false;padding-top:5px;padding-bottom:5px;padding-left:15px;padding-right:15px;display:inline-block;color:#ffffff;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:16px;text-decoration:none;letter-spacing:normal;">Our work</a><!--[if mso]></td><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:15px;padding-bottom:5px;padding-left:15px"><![endif]--><a href="www.example.com" target="_self" style="mso-hide:false;padding-top:5px;padding-bottom:5px;padding-left:15px;padding-right:15px;display:inline-block;color:#ffffff;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:16px;text-decoration:none;letter-spacing:normal;">Services</a><!--[if mso]></td><![endif]--><!--[if mso]><td style="padding-top:5px;padding-right:15px;padding-bottom:5px;padding-left:15px"><![endif]--><a href="www.example.com" target="_self" style="mso-hide:false;padding-top:5px;padding-bottom:5px;padding-left:15px;padding-right:15px;display:inline-block;color:#ffffff;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:16px;text-decoration:none;letter-spacing:normal;">Dashboard </a><!--[if mso]></td><![endif]--><!--[if mso]></tr></table><![endif]--></div>
																		</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-3" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:20px;line-height:20px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-2" style="height:25px;line-height:25px;font-size:1px;">&#8202;</div>
													<table class="heading_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 87px; font-weight: 700; letter-spacing: 3px; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 104.39999999999999px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Automatizador de correos</span></h1>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-4" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="41.666666666666664%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:15px;padding-right:15px;width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div class="fullWidth" style="max-width: 253.333px;"><a href="www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/CTA.png" style="display: block; height: auto; border: 0; width: 100%;" width="253.333" alt="Dashboard" title="Dashboard" height="auto"></a></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="58.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 34px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 40.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Dive into the Dynamic Dashboard Metrics of the Last Month</span></h1>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-5" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="41.666666666666664%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="divider_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="right">
																	<table border="0" cellpadding="0" cellspacing="0" role="presentation" width="75%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
																		<tr>
																			<td class="divider_inner" style="font-size: 1px; line-height: 1px; border-top: 1px solid #dddddd;"><span style="word-break: break-word;">&#8202;</span></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="58.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 13px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 15.6px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Dive into the Dynamic Dashboard Metrics of the Last Month</span></h1>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-6" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:10px;line-height:10px;font-size:1px;">&#8202;</div>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 97px; font-weight: 700; letter-spacing: 3px; line-height: 120%; text-align: right; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 116.39999999999999px;"><span class="tinyMce-placeholder" style="word-break: break-word;">REPORT</span></h1>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3" style="height:15px;line-height:15px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-7" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1f1f1f; border-radius: 26px 26px 0 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:25px;line-height:25px;font-size:1px;">&#8202;</div>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<h3 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 34px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 40.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;"><span style="word-break: break-word; background-color: #95b2f9;"><span style="word-break: break-word; color: #000000;">&nbsp;Analytics</span>&nbsp;</span> This month</span></h3>
															</td>
														</tr>
													</table>
													<table class="image_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div class="fullWidth" style="max-width: 680px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/Graph_32.png" style="display: block; height: auto; border: 0; width: 100%;" width="680" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-8" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #1f1f1f; border-radius: 0 0 26px 26px; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:25px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #c2b7b7; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 16px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 19.2px;"><span class="tinyMce-placeholder" style="word-break: break-word;">New subscribers</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;padding-right:10px;padding-top:5px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 44px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 52.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">2,689</span></h3>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-2" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:25px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #c2b7b7; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 16px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 19.2px;"><span class="tinyMce-placeholder" style="word-break: break-word;">SMS revenue</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;padding-right:10px;padding-top:5px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 44px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 52.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">$650</span></h3>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-3" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:25px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #c2b7b7; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 16px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 19.2px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Email open rate</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;padding-right:10px;padding-top:5px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 44px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 52.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">26.4</span></h3>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-3" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-9" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:35px;line-height:35px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-2" style="height:15px;line-height:15px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-10" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<h2 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 70px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 84px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Top-Performing</span></h2>
															</td>
														</tr>
													</table>
													<table class="heading_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<h2 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 82px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: right; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 98.39999999999999px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Campaign</span></h2>
															</td>
														</tr>
													</table>
													<table class="paragraph_block block-4" width="100%" border="0" cellpadding="15" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#ffffff;direction:ltr;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:32px;font-weight:400;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:38.4px;">
																	<p style="margin: 0;">The Marketing campaign outperformed expectations, generating 100k leads and 65% engagement.</p>
																</div>
															</td>
														</tr>
													</table>
													<table class="button_block block-5" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center"><!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="www.example.com" style="height:62px;width:660px;v-text-anchor:middle;" arcsize="7%" strokeweight="1.5pt" strokecolor="#ffffff" fillcolor="#ffffff">
<w:anchorlock/>
<v:textbox inset="0px,0px,0px,0px">
<center dir="false" style="color:#000000;font-family:sans-serif;font-size:19px">
<![endif]--><a href="www.example.com" target="_blank" style="background-color:#ffffff;border-bottom:2px solid #ffffff;border-left:2px solid #ffffff;border-radius:4px;border-right:2px solid #ffffff;border-top:2px solid #ffffff;color:#000000;display:block;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:19px;font-weight:400;mso-border-alt:none;padding-bottom:10px;padding-top:10px;text-align:center;text-decoration:none;width:100%;word-break:keep-all;"><span style="word-break: break-word; padding-left: 20px; padding-right: 20px; font-size: 19px; display: inline-block; letter-spacing: normal;"><span style="word-break: break-word; line-height: 38px;">VIEW MONTHLY REPORT</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-6" style="height:75px;line-height:75px;font-size:1px;">&#8202;</div>
													<table class="heading_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h2 style="margin: 0; color: #95b2f9; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 82px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 98.39999999999999px;"><span class="tinyMce-placeholder" style="word-break: break-word;">ENAGED</span></h2>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-8" style="height:15px;line-height:15px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-11" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:1px;line-height:1px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="button_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;">
																<div class="alignment" align="center"><!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="www.example.com" style="height:46px;width:320px;v-text-anchor:middle;" arcsize="55%" strokeweight="0.75pt" strokecolor="#ffffff" fill="false">
<w:anchorlock/>
<v:textbox inset="0px,0px,0px,0px">
<center dir="false" style="color:#ffffff;font-family:sans-serif;font-size:17px">
<![endif]--><a href="www.example.com" target="_blank" style="background-color:transparent;border-bottom:1px solid #ffffff;border-left:1px solid #ffffff;border-radius:25px;border-right:1px solid #ffffff;border-top:1px solid #ffffff;color:#ffffff;display:block;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:17px;font-weight:400;mso-border-alt:none;padding-bottom:5px;padding-top:5px;text-align:center;text-decoration:none;width:100%;word-break:keep-all;"><span style="word-break: break-word; padding-left: 5px; padding-right: 5px; font-size: 17px; display: inline-block; letter-spacing: normal;"><span style="word-break: break-word; line-height: 34px;">Signed up for newsletter</span></span></a><!--[if mso]></center></v:textbox></v:roundrect><![endif]--></div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-3" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:1px;line-height:1px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-12" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center; line-height: 0;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #000000; font-family: inherit; font-size: 14px; font-weight: 400; text-align: center;">
																<table class="icons-outer" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-table;">
																	<tr>
																		<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px;"><img class="icon" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/dots.png" height="auto" width="4" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-13" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:1px;line-height:1px;font-size:1px;">&#8202;</div>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #ffffff; border-left: 11px solid #000000; border-right: 11px solid #000000; vertical-align: top; border-top: 0px; border-bottom: 0px;">
													<table class="paragraph_block block-1" width="100%" border="0" cellpadding="15" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#000000;direction:ltr;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:27px;font-weight:400;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:32.4px;">
																	<p style="margin: 0;">2,938 By email</p>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-3" width="25%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:1px;line-height:1px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-14" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 238px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/lines.png" style="display: block; height: auto; border: 0; width: 100%;" width="238" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-15" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #ffffff; border-left: 10px solid #000000; border-right: 10px solid #000000; vertical-align: top; border-top: 0px; border-bottom: 0px;">
													<table class="paragraph_block block-1" width="100%" border="0" cellpadding="15" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#000000;direction:ltr;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:27px;font-weight:400;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:32.4px;">
																	<p style="margin: 0;">2,938 By email</p>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #ffffff; border-left: 10px solid #000000; border-right: 10px solid #000000; vertical-align: top; border-top: 0px; border-bottom: 0px;">
													<table class="paragraph_block block-1" width="100%" border="0" cellpadding="15" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad">
																<div style="color:#000000;direction:ltr;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:27px;font-weight:400;letter-spacing:0px;line-height:120%;text-align:center;mso-line-height-alt:32.4px;">
																	<p style="margin: 0;">2,938 By email</p>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-16" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 238px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/da008a46-441b-412e-b23a-5f58c5f7f4fd.png" style="display: block; height: auto; border: 0; width: 100%;" width="238" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 136px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/reached.png" style="display: block; height: auto; border: 0; width: 100%;" width="136" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-17" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h2 style="margin: 0; color: #95b2f9; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 70px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 84px;"><span class="tinyMce-placeholder" style="word-break: break-word;">LOOKING&nbsp;<span style="word-break: break-word; background-color: #95b2f9;"> <span style="word-break: break-word; color: #ffffff;"><span style="word-break: break-word; color: #000000;">AHEAD</span>&nbsp;</span></span></span></h2>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-18" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="66.66666666666667%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:10px;padding-right:10px;text-align:center;width:100%;">
																<h2 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 87px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 104.39999999999999px;"><strong>STRATEGY</strong></h2>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; line-height: 0;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #ffffff; font-family: inherit; font-size: 17px; font-weight: 400; text-align: left;"><!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																<!--[if !vml]><!-->
																<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]-->
																	<tr>
																		<td style="vertical-align: middle; text-align: center; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; padding-right: 10px;"><img class="icon" alt="Number 1" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/01.png" height="auto" width="43" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																		<td style="font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 17px; font-weight: 400; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: left; line-height: normal;">SEO Enhancements</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-19" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-20" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #000000; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #95b2f9; border-bottom: 8px solid #000000; border-left: 8px solid #000000; border-right: 8px solid #000000; border-top: 8px solid #000000; vertical-align: top;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/spacer.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 44px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 52.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">180,000</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:20px;padding-left:25px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 19px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 22.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Reach</span></h3>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-4" style="height:10px;line-height:10px;font-size:1px;">&#8202;</div>
													<table class="image_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/4d714cc0-ca08-4021-a3c8-2aea30bb86e9.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/spacer.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 32px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 38.4px;"><span style="word-break: break-word; background-color: #000000;">Conversion Rate</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-8" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 59px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 70.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">12%+</span></h3>
															</td>
														</tr>
													</table>
													<table class="image_block block-9" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center" style="line-height:10px">
																	<div class="fullWidth" style="max-width: 194.4px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/audience.png" style="display: block; height: auto; border: 0; width: 100%;" width="194.4" alt="people looking at devices" title="people looking at devices" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-10" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/4d714cc0-ca08-4021-a3c8-2aea30bb86e9.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="50%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; background-color: #95b2f9; border-bottom: 8px solid #000000; border-left: 8px solid #000000; border-right: 8px solid #000000; border-top: 8px solid #000000; vertical-align: top;">
													<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/spacer.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:20px;padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 19px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 22.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Engagement Rate</span></h3>
															</td>
														</tr>
													</table>
													<table class="image_block block-3" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 210.6px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/percentage.png" style="display: block; height: auto; border: 0; width: 100%;" width="210.6" alt="Engagement graph" title="Engagement graph" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 19px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 22.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Return on Investment</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 44px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 52.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">200%</span></h3>
															</td>
														</tr>
													</table>
													<table class="image_block block-6" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/4d714cc0-ca08-4021-a3c8-2aea30bb86e9.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="image_block block-7" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/spacer.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
													<table class="heading_block block-8" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 44px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 52.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">250,000</span></h3>
															</td>
														</tr>
													</table>
													<table class="heading_block block-9" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:20px;padding-left:25px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 19px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 22.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Sessions</span></h3>
															</td>
														</tr>
													</table>
													<div class="spacer_block block-10" style="height:10px;line-height:10px;font-size:1px;">&#8202;</div>
													<table class="image_block block-11" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="width:100%;">
																<div class="alignment" align="center" style="line-height:10px">
																	<div style="max-width: 324px;"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/4d714cc0-ca08-4021-a3c8-2aea30bb86e9.png" style="display: block; height: auto; border: 0; width: 100%;" width="324" height="auto"></div>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-21" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:35px;line-height:35px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-2" style="height:15px;line-height:15px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-22" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="66.66666666666667%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;text-align:center;width:100%;">
																<h2 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 92px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 110.39999999999999px;"><strong>DETAILED</strong></h2>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-left: 5px; padding-right: 5px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: left; line-height: 0;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #ffffff; font-family: inherit; font-size: 17px; font-weight: 400; text-align: left;"><!--[if vml]><table align="left" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																<!--[if !vml]><!-->
																<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]-->
																	<tr>
																		<td style="vertical-align: middle; text-align: center; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; padding-right: 10px;"><img class="icon" alt="Number 2" src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/02.png" height="auto" width="52" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></td>
																		<td style="font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 17px; font-weight: 400; color: #ffffff; vertical-align: middle; letter-spacing: undefined; text-align: left; line-height: normal;">SEO Enhancements</td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-23" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																<h2 style="margin: 0; color: #95b2f9; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 66px; font-weight: 400; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 79.2px;">Performance <span style="word-break: break-word; background-color: #95b2f9;">&nbsp;</span><span style="word-break: break-word; background-color: #95b2f9; color: #000000;">Metrics&nbsp;</span></h2>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-24" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:30px;line-height:30px;font-size:1px;">&#8202;</div>
													<div class="spacer_block block-2" style="height:40px;line-height:40px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-25" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e4e2fd; border-radius: 14px; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr class="reverse">
												<td class="column column-1 first" width="66.66666666666667%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 15px; padding-left: 15px; padding-right: 15px; padding-top: 15px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																	<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 29px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 34.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Customer Acquisition Cost (CAC): <span style="word-break: break-word; color: #ffffff; background-color: #000000;">$20</span></span></h3>
																</td>
															</tr>
														</table>
														<table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad">
																	<div style="color:#393d47;direction:ltr;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:18px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:left;mso-line-height-alt:27px;">
																		<p style="margin: 0;">This signifies that in the last month, on average, your company spent <strong>$20</strong> to acquire each new customer</p>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
												<td class="column column-2 last" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 15px; padding-left: 15px; padding-right: 15px; padding-top: 15px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																	<div class="alignment" align="center" style="line-height:10px">
																		<div class="fullWidth" style="max-width: 196.667px;"><a href="www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/graph_1_1.png" style="display: block; height: auto; border: 0; width: 100%;" width="196.667" alt="CAC graph" title="CAC graph" height="auto"></a></div>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-26" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:35px;line-height:35px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-27" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e4e2fd; border-radius: 14px; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr class="reverse">
												<td class="column column-1 first" width="66.66666666666667%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 15px; padding-left: 15px; padding-right: 15px; padding-top: 15px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																	<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 29px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 34.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Social Media Followers Growth: <span style="word-break: break-word; color: #ffffff; background-color: #000000;">10%</span></span></h3>
																</td>
															</tr>
														</table>
														<table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad">
																	<div style="color:#393d47;direction:ltr;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:18px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:left;mso-line-height-alt:27px;">
																		<p style="margin: 0;">The <strong>10%</strong> growth in Social Media Followers reflects the your company successful efforts in expanding its online presence and engaging.</p>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
												<td class="column column-2 last" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 15px; padding-left: 15px; padding-right: 15px; padding-top: 15px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																	<div class="alignment" align="center" style="line-height:10px">
																		<div class="fullWidth" style="max-width: 196.667px;"><a href="www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/data_1.png" style="display: block; height: auto; border: 0; width: 100%;" width="196.667" alt="Girl smiling" title="Girl smiling" height="auto"></a></div>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-28" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:45px;line-height:45px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-29" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e4e2fd; border-radius: 14px; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr class="reverse">
												<td class="column column-1 first" width="66.66666666666667%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 15px; padding-left: 15px; padding-right: 15px; padding-top: 15px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;width:100%;">
																	<h3 style="margin: 0; color: #000000; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 29px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 34.8px;"><span class="tinyMce-placeholder" style="word-break: break-word;">Average Session Duration: <span style="word-break: break-word; color: #ffffff; background-color: #000000;">25 mins</span></span></h3>
																</td>
															</tr>
														</table>
														<table class="paragraph_block block-2" width="100%" border="0" cellpadding="10" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
															<tr>
																<td class="pad">
																	<div style="color:#393d47;direction:ltr;font-family:Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif;font-size:18px;font-weight:400;letter-spacing:0px;line-height:150%;text-align:left;mso-line-height-alt:27px;">
																		<p style="margin: 0;">We've noticed a growing interest from <strong>US market,</strong> particularly around <strong>[SpecificProduct]</strong>.</p>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
												<td class="column column-2 last" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 15px; padding-left: 15px; padding-right: 15px; padding-top: 15px; vertical-align: middle; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="border">
														<table class="image_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
															<tr>
																<td class="pad" style="width:100%;padding-right:0px;padding-left:0px;">
																	<div class="alignment" align="center" style="line-height:10px">
																		<div class="fullWidth" style="max-width: 196.667px;"><a href="www.example.com" target="_blank" style="outline:none" tabindex="-1"><img src="https://d1oco4z2z1fhwp.cloudfront.net/templates/default/8766/progress.png" style="display: block; height: auto; border: 0; width: 100%;" width="196.667" alt="Girl smiling" title="Girl smiling" height="auto"></a></div>
																	</div>
																</td>
															</tr>
														</table>
													</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-30" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:35px;line-height:35px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-31" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #131313;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:45px;line-height:45px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-32" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #131313;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;text-align:center;width:100%;">
																<h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 18px; font-weight: normal; line-height: 200%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 36px;"><strong>About Us</strong></h1>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; mso-line-height-alt: 24px; color: #ffffff; line-height: 2;">
																		<p style="margin: 0; font-size: 14px; mso-line-height-alt: 28px;">Lorem ipsum dolor sit amet, consectetuer adipiscing elit,&nbsp;</p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-2" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;text-align:center;width:100%;">
																<h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 18px; font-weight: normal; line-height: 200%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 36px;"><strong>Links</strong></h1>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener">Services</a></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener">Team</a></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener">About us</a></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-5" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener">Unsubscribe</a></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
												</td>
												<td class="column column-3" width="33.333333333333336%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="heading_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-left:20px;text-align:center;width:100%;">
																<h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; font-size: 18px; font-weight: normal; line-height: 200%; text-align: left; margin-top: 0; margin-bottom: 0; mso-line-height-alt: 36px;"><strong>Contact</strong></h1>
															</td>
														</tr>
													</table>
													<table class="text_block block-2" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener">Info@company.com</a></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="text_block block-3" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:20px;padding-top:10px;">
																<div style="font-family: sans-serif">
																	<div class style="font-size: 12px; font-family: Fira Sans, Lucida Sans Unicode, Lucida Grande, sans-serif; mso-line-height-alt: 14.399999999999999px; color: #a9a9a9; line-height: 1.2;">
																		<p style="margin: 0; font-size: 14px; mso-line-height-alt: 16.8px;"><a href="http://www.example.com" target="_blank" style="text-decoration: none; color: #ffffff;" rel="noopener">Help Center</a></p>
																	</div>
																</div>
															</td>
														</tr>
													</table>
													<table class="social_block block-4" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
														<tr>
															<td class="pad" style="padding-bottom:10px;padding-left:20px;padding-right:10px;padding-top:10px;text-align:left;">
																<div class="alignment" align="left">
																	<table class="social-table" width="144px" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;">
																		<tr>
																			<td style="padding:0 4px 0 0;"><a href="https://www.example.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/facebook@2x.png" width="32" height="auto" alt="Facebook" title="facebook" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 4px 0 0;"><a href="https://www.example.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/twitter@2x.png" width="32" height="auto" alt="Twitter" title="twitter" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 4px 0 0;"><a href="https://www.example.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/linkedin@2x.png" width="32" height="auto" alt="Linkedin" title="linkedin" style="display: block; height: auto; border: 0;"></a></td>
																			<td style="padding:0 4px 0 0;"><a href="https://www.example.com/" target="_blank"><img src="https://app-rsrc.getbee.io/public/resources/social-networks-icon-sets/t-only-logo-white/instagram@2x.png" width="32" height="auto" alt="Instagram" title="instagram" style="display: block; height: auto; border: 0;"></a></td>
																		</tr>
																	</table>
																</div>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-33" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #131313;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; border-radius: 0; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<div class="spacer_block block-1" style="height:45px;line-height:45px;font-size:1px;">&#8202;</div>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
					<table class="row row-34" align="center" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff;">
						<tbody>
							<tr>
								<td>
									<table class="row-content stack" align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #ffffff; color: #000000; width: 680px; margin: 0 auto;" width="680">
										<tbody>
											<tr>
												<td class="column column-1" width="100%" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; padding-bottom: 5px; padding-top: 5px; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;">
													<table class="icons_block block-1" width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; text-align: center; line-height: 0;">
														<tr>
															<td class="pad" style="vertical-align: middle; color: #1e0e4b; font-family: 'Inter', sans-serif; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;"><!--[if vml]><table align="center" cellpadding="0" cellspacing="0" role="presentation" style="display:inline-block;padding-left:0px;padding-right:0px;mso-table-lspace: 0pt;mso-table-rspace: 0pt;"><![endif]-->
																<!--[if !vml]><!-->
																<table class="icons-inner" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block; padding-left: 0px; padding-right: 0px;" cellpadding="0" cellspacing="0" role="presentation"><!--<![endif]-->
																	<tr>
																		<td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 6px;"><a href="http://designedwithbeefree.com/" target="_blank" style="text-decoration: none;"><img class="icon" alt="Beefree Logo" src="https://d1oco4z2z1fhwp.cloudfront.net/assets/Beefree-logo.png" height="auto" width="34" align="center" style="display: block; height: auto; margin: 0 auto; border: 0;"></a></td>
																		<td style="font-family: 'Inter', sans-serif; font-size: 15px; font-weight: undefined; color: #1e0e4b; vertical-align: middle; letter-spacing: undefined; text-align: center; line-height: normal;"><a href="http://designedwithbeefree.com/" target="_blank" style="color: #1e0e4b; text-decoration: none;">Designed with Beefree</a></td>
																	</tr>
																</table>
															</td>
														</tr>
													</table>
												</td>
											</tr>
										</tbody>
									</table>
								</td>
							</tr>
						</tbody>
					</table>
				</td>
			</tr>
		</tbody>
	</table><!-- End -->
</body>

</html>
"""
attachment_path = input("Ingrese la ruta del archivo que desea adjuntar (o presione Enter para omitir): ")
Correo_html(subject, message, correos, attachment_path if attachment_path else None)
print("Correo enviado.")
