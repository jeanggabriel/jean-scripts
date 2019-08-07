import smtplib

tlssmtp = smtplib.SMTP(‘localhost’, 587)smtp.starttls()
smtp = smtplib.SMTP_SSL(‘localhost’, 465)
smtp = smtplib.SMTP(‘localhost’, 25)
smtp.login(‘usuário’, ‘senha’)
Enviando um email:msg = “””From: seudominio.com.br
To: outroemail@seudominio.com.br
Subject: SempreUpdateEmail de teste do SempreUpdate.”””
smtp.sendmail(‘seuemail@seudominio.com.br’, [‘outroemail@seudominio.com.br’], msg)
smtp.quit()