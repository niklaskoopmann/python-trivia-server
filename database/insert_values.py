import mysql.connector
import os

trivia_database = mysql.connector.connect(
    host="172.17.0.2",
    user="root",
    passwd="123456",
    database="trivia_questions"
)

print(trivia_database)

with os.scandir("../questions/") as files:
    for questions_file in files:
        index = 0
        with open("./" + questions_file.name, "rt", encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile, delimiter=";")
            for row in reader:
                trivia_database.cursor().execute("INSERT INTO " + os.path.splitext(questions_file.name)[0] + " VALUES (" + index + ", " + row[0] + ", " + row[1] + ")")
                index += 1
