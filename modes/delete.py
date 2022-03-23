def delete():

    import mysql.connector

    db = mysql.connector.connect(
        host = "localhost",
        user = "<yourusername>",
        passwd = "<password>",
        database = "pwmanager"
    )

    mycursor = db.cursor()

    while True:
        print("Do you want to delete a single profile or all profiles with the same name? (single/all)")
        choice = input()
        if choice == "single":
            print("What profile do you want to delete?")
            service = input()

            sql = "SELECT * FROM profiles WHERE service = '{}'".format(service)

            mycursor.execute(sql)

            myresult = mycursor.fetchall()

            for x in myresult:
                print(x)

            print("Which of these profiles would you like to delete? (enter profile's ID)")
            chosenid = input()

            newsql = "DELETE FROM profiles WHERE id = '{}'".format(chosenid)

            try:
                mycursor.execute(newsql)
                db.commit()
            except:
                db.rollback()

            print("Profile", service, " with ID:", chosenid, "deleted!")
            db.close()

            break

        elif choice == "all":
            print("What profiles do you want to delete?")
            services = input()

            sql = "DELETE FROM profiles WHERE service = '{}'".format(services)

            try:
                mycursor.execute(sql)
                db.commit()
            except:
                db.rollback()

            print("All profiles for", services, "deleted!")
            db.close()

            break

        else:
            print("That's not a valid input. Try again or go back to main menu: (retry/back)")
            elsechoice = input()
            if elsechoice == "retry":
                continue
            else:
                break
