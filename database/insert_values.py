import mysql.connector
import os
import csv

trivia_database = mysql.connector.connect(
    host="192.168.2.100",
    user="root",
    passwd="123456",
    database="trivia_questions",
    auth_plugin="mysql_native_password"
)

current_script_directory = os.path.dirname(os.path.realpath(__file__))

print(trivia_database)

with os.scandir(current_script_directory + "/../questions/") as files:
    for questions_file in files:
        print(questions_file.name)
        index = 0
        with open(current_script_directory + "/../questions/" + questions_file.name, "rt", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                print(row)
                print("INSERT INTO " + os.path.splitext(questions_file.name)[0] + " VALUES (%s, %s, %s)", (index, row[0], row[1]))
                trivia_database.cursor().execute("INSERT INTO " + os.path.splitext(questions_file.name)[0] + " VALUES (%s, %s, %s)", (index, row[0], row[1]))
                #trivia_database.cursor().execute("INSERT INTO " + os.path.splitext(questions_file.name)[0] + " VALUES (" + str(index) + ", \'" + row[0] + "\', \'" + row[1] + "\')")
                index += 1

trivia_database.commit()
