!!!Use at your own risk!!!

This is purely experimental and I haven't had the chance to work on remote database access so for now you will need to provide a local database yourself.

  Modules: 
         bcrypt to hash master password and generate salt for AES_ENCRYPT in Database.
         keyring to store hashed master password.
         mysql-connector-python for MySQL Database.
         
To create MySQL Database run these commands:
  
    CREATE DATABASE pwmanager;
    CREATE TABLE profiles(id MEDIUMINT NOT NULL AUTO_INCREMENT PRIMARY KEY, service LONGBLOB, emailuser LONGBLOB, passwd LONGBLOB, salt LONGBLOB);
  
Create a user profile in MySQL and add the name and password into this block of code in generator-, manager-, and delete.py:
  
    db = mysql.connector.connect(
        host = "localhost",
        user = "<yourusername>",
        passwd = "<password>",
        database = "pwmanager"
    )

Open pw.py to create master password.

Open main.py to run program.

Enter your master password.

Choose "add", "view", "delete" or "exit".

  "add" to add a profile.
  "view" to view profiles.
  "delete" to delete profiles.
  "exit" to exit program.
  
    add calls the function add() from generator.py in subfolder "modes".
    Input your:

      service, app or website you want to add a profile for.

      email or username for the service, app or website you want to add.

      the length of the password that will be generated for the profile.
        password will be generated from lower- and uppercase characters,
        numbers and punctuation characters.

      The profile will be added to MySQL Database.
  
 You can now choose between the four options again
  
    view calls the function view() from manager.py in subfolder "modes".
    Input:

      The service, app, or website you are looking for.

      Database allows duplicates so you will see all accounts for that service, app or website.

      The profiles will be displayed.
  
  You can now choose between the four options again.
  
    delete calls the function delete() from delete.py in subfolder "modes".
    Input:

      If you want to delete a "single" profile or "all" profiles of a service, app or website.

      The profile you want to delete.

      If you chose single, you will be shown the profiles with their corresponding ID.
        Input the ID of the profile you want to delete.

      If you chose all, all profiles of the service, app or website you entered will be deleted.
  
  You can now choose between the four options again.
  
    exit will exit the program.
