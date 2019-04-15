import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
usuario = open("usuario").read()
senha = open("senha").read()
server.login(usuario,senha)
server.sendmail(usuario,usuario,"ola manolo")
server.quit()
