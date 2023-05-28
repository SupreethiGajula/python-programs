import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('gajulasupreethi1317@gmail.com','vbplqfhjjdllszwr')
server.sendmail('gajulasupreethi1317@gmail.com','supgajula1312@gmail.com','mail sent from python vscode')
print('mail sent')