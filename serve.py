#!/usr/bin/env python

import csv
import json
import mysql.connector
from random import randint

from flask import Flask, jsonify, url_for, request
from flasgger import Swagger, swag_from
from flask_cors import CORS

__author__ = "niklaskoopmann"
__version__ = "0.0.3"
__status__ = "Development"

TARGET_PORT = 60433
DATABASE_IP = "192.168.2.100"

all_categories = []
total_number_of_questions = 0

print("Starting server...")


class Question:
    def __init__(self, id, question, answer, category_internal, category_display):
        self.id = id
        self.question = question
        self.answer = answer
        self.category_internal = category_internal
        self.category_display = category_display
        # to do: rework population of all_categories
        if not (category_internal, category_display) in all_categories:
            all_categories.append((category_internal, category_display))

    def __init__(self):
        self

    def __str__(self):
        question_dict = {"category_internal": self.category_internal,
                         "category_display": self.category_display,
                         "question": self.question,
                         "answer": self.answer,
                         "id": self.id}
        return jsonify(question_dict)


print("  Connecting to database at", DATABASE_IP)

trivia_database = mysql.connector.connect(
    host=DATABASE_IP,
    user="root",
    passwd="123456",
    database="trivia_questions",
    auth_plugin="mysql_native_password"
)

trivia_db_cursor = trivia_database.cursor(buffered=True)

print("  Database connection established")
#print("  Importing questions...")

"""
def fill_category_question_list(internal_name, display_name):
    global total_number_of_questions
    all_categories.append((internal_name, display_name))
    out_list = []
    with open("./questions/" + internal_name + ".csv", "rt", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            out_list.append(
                Question(0, row[0], row[1], internal_name, display_name))
            total_number_of_questions += 1
    return out_list
"""


def get_random_question(category_internal, category_display):
    trivia_db_cursor.execute("SELECT * FROM trivia_questions." +
                             category_internal + " ORDER BY RAND() LIMIT 1;")
    question_data_tuple = trivia_db_cursor.fetchone()
    return Question(question_data_tuple[0], question_data_tuple[1], question_data_tuple[2], category_internal, category_display).__str__()


"""
questions_art_literature = fill_category_question_list(
    "art_literature", "Art & Literature")
questions_entertainment = fill_category_question_list(
    "entertainment", "Entertainment")
questions_food_drink = fill_category_question_list(
    "food_drink", "Food & Drink")
questions_general = fill_category_question_list("general", "General")
questions_geography = fill_category_question_list("geography", "Geography")
questions_history_holidays = fill_category_question_list(
    "history_holidays", "History & Holidays")
questions_language = fill_category_question_list("language", "Language")
questions_mathematics = fill_category_question_list(
    "mathematics", "Mathematics")
questions_music = fill_category_question_list("music", "Music")
questions_people_places = fill_category_question_list(
    "people_places", "People & Places")
questions_religion_mythology = fill_category_question_list(
    "religion_mythology", "Religion & Mythology")
questions_science_nature = fill_category_question_list(
    "science_nature", "Science & Nature")
questions_sports_leisure = fill_category_question_list(
    "sports_leisure", "Sports & Leisure")
questions_technology_video_games = fill_category_question_list(
    "technology_video_games", "Technology & Video Games")
questions_toys_games = fill_category_question_list(
    "toys_games", "Toys & Games")

"""

#print("  Successfully imported", total_number_of_questions, "questions!")
print("")
print("  Starting Flask server...")

app = Flask(__name__)
CORS(app)
app.config['SWAGGER'] = {
    'title': 'My API',
    'uiversion': 3,
    "specs_route": "/swagger/"
}
swagger = Swagger(app)


@app.route("/")
def home():
    # return some api documentation here?
    return "Hello World!"


@app.route("/art-literature")
def art_literature():
    return get_random_question("art_literature", "Art & Literature")


@app.route("/entertainment")
def entertainment():
    return get_random_question("entertainment", "Entertainment")


@app.route("/food-drink")
def food_drink():
    return get_random_question("food_drink", "Food & Drink")


@app.route("/general")
def general():
    return get_random_question("general", "General")


@app.route("/geography")
def geography():
    return get_random_question("geography", "Geography")


@app.route("/history-holidays")
def history_holidays():
    return get_random_question("history_holidays", "History & Holidays")


@app.route("/language")
def language():
    return get_random_question("language", "Language")


@app.route("/mathematics")
def mathematics():
    return get_random_question("mathematics", "Mathematics")


@app.route("/music")
def music():
    return get_random_question("music", "Music")


@app.route("/people-places")
def people_places():
    return get_random_question("people_places", "People & Places")


@app.route("/religion-mythology")
def religion_mythology():
    return get_random_question("religion_mythology", "Religion & Mythology")


@app.route("/science-nature")
def science_nature():
    return get_random_question("science_nature", "Science & Nature")


@app.route("/sports-leisure")
def sports_leisure():
    return get_random_question("sports_leisure", "Sports & Leisure")


@app.route("/technology-video-games")
def technology_video_games():
    return get_random_question("technology_video_games", "Technology & Video Games")


@app.route("/toys-games")
def toys_games():
    return get_random_question("toys_games", "Toys & Games")


@app.route("/about/categories")
def about_categories():
    categories_dict = {"categories": []}
    for c in all_categories:
        categories_dict["categories"].append(
            {"internal": c[0], "display": c[1]})
    return jsonify(categories_dict)


@app.route("/about/stats")
def about_stats():
    trivia_db_cursor.execute(
        "SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'trivia_questions';")
    cat_stats_list = trivia_db_cursor.fetchall()
    cat_stats_dict = []
    for stat in cat_stats_list:
        cat_stats_dict.append(
            {"internal_name": stat[0], "question_count": stat[1]})
    return jsonify(cat_stats_dict)


@app.route("/update-question", methods = ["POST"])
def update_question():
    """
      post endpoint
      ---      
      tags:
        - Flast Restful APIs
      parameters:
        - name: body
          in: body
          required: true
      responses:
        400:
          description: Error Request body could not be processed
        200:
          description: Question updated              
      """
    updated_question = Question()
    try:
        updated_question.id = request.json["id"]
        updated_question.question = request.json["question"]
        updated_question.category_internal = request.json["category_internal"]
        updated_question.category_display = request.json["category"]
        updated_question.answer = request.json["answer"]
    except:
        return "Request body could not be processed", 400

    return "Question updated", 200


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=TARGET_PORT)  # serve on local network
    app.run(port=TARGET_PORT, debug=True)  # serve on localhost
