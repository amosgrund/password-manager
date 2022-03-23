def view():
    print("What service are you looking for?")
    service = input()

    import mysql.connector
    from requests import get
    
    db = mysql.connector.connect(
        host = "192.168.178.57",
        user = "pw",
        passwd = "password",
        database = "pwmanager"
    )

    mycursor = db.cursor()

    sql = "SELECT emailuser, replace(cast(AES_DECRYPT(passwd, '4afe1ecv') AS CHAR(255)), salt, '') FROM profiles WHERE service = '{}'".format(service)

    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)