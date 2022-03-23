import random
import string
import bcrypt

def add():
    print("What service/app/website do you want to add?")
    service = input()
    print("What is the email/username for", service + "?")
    emailuser = input()
    print("How long should the password be?")
    passwordlength = int(input())

    passwordcharacters = string.ascii_letters + string.digits + string.punctuation

    passwd = ''.join(random.choice(passwordcharacters) for i in range(passwordlength))
    
    import mysql.connector
    from requests import get

    db = mysql.connector.connect(
        host = "192.168.178.57",
        user = "pw",
        passwd = "password",
        database = "pwmanager"
    )

    salt = bcrypt.gensalt(rounds = 15).decode('utf-8')

    mycursor = db.cursor()
    sql = "INSERT INTO profiles(service, emailuser, passwd, salt) VALUES ('{}', '{}', AES_ENCRYPT(CONCAT('{}', '{}'), '4afe1ecv'), '{}')".format(service, emailuser, passwd, salt, salt)

    #print(sql)

    try:
        mycursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    print("Profile added to database!")
    db.close()