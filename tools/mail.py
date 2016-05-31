import smtplib
import email.mime.text

mail_host = ""      # "smtp.xxx.com"
mail_user = ""      # "xxx@xxx.com"
mail_pass = ""      # "xxx"
mail_postfix = ""   # "xxx.com"
mailto_list = [""]  # ["xxx@xxx.com"]

def send_mail(to_list, sub, content):
    me = "hello"+"<"+mail_user+"@"+mail_postfix+">"
    msg = email.mime.text.MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "hello world"):
        print "Success"
    else:
        print "Failed"
