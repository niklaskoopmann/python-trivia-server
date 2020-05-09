#!/usr/bin/env python

import csv
import json
from random import randint

from flask import Flask, jsonify, url_for

__author__ = "niklaskoopmann"
__version__ = "0.0.1"
__status__ = "Development"

TARGET_PORT = 42069
all_categories = []
total_number_of_questions = 0

print("Starting server...")


class Question:
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer
        self.category = category

    def __str__(self):
        return "Category: " + self.category + "<br>Question: " + self.question + "<br>Answer: " + self.answer


print("  Importing questions...")


def fill_category_question_list(internal_name, display_name):
    global total_number_of_questions
    all_categories.append((internal_name, display_name))
    out_list = []
    with open("./questions/" + internal_name + ".csv", "rt", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            out_list.append(Question(row[0], row[1], display_name))
            total_number_of_questions += 1
    return out_list


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


print("  Successfully imported", total_number_of_questions, "questions!")
print("")
print("  Starting Flask server...")

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/art-literature")
def art_literature():
    i = randint(0, len(questions_art_literature))
    return questions_art_literature[i].__str__()


@app.route("/entertainment")
def entertainment():
    i = randint(0, len(questions_entertainment))
    return questions_entertainment[i].__str__()


@app.route("/food-drink")
def food_drink():
    i = randint(0, len(questions_food_drink))
    return questions_food_drink[i].__str__()


@app.route("/general")
def general():
    i = randint(0, len(questions_general))
    return questions_general[i].__str__()


@app.route("/geography")
def geography():
    i = randint(0, len(questions_geography))
    return questions_geography[i].__str__()


@app.route("/history-holidays")
def history_holidays():
    i = randint(0, len(questions_history_holidays))
    return questions_history_holidays[i].__str__()


@app.route("/language")
def language():
    i = randint(0, len(questions_language))
    return questions_language[i].__str__()


@app.route("/mathematics")
def mathematics():
    i = randint(0, len(questions_mathematics))
    return questions_mathematics[i].__str__()


@app.route("/music")
def music():
    i = randint(0, len(questions_music))
    return questions_music[i].__str__()


@app.route("/people-places")
def people_places():
    i = randint(0, len(questions_people_places))
    return questions_people_places[i].__str__()


@app.route("/religion-mythology")
def religion_mythology():
    i = randint(0, len(questions_religion_mythology))
    return questions_religion_mythology[i].__str__()


@app.route("/science-nature")
def science_nature():
    i = randint(0, len(questions_science_nature))
    return questions_science_nature[i].__str__()


@app.route("/sports-leisure")
def sports_leisure():
    i = randint(0, len(questions_sports_leisure))
    return questions_sports_leisure[i].__str__()


@app.route("/technology-video-games")
def technology_video_games():
    i = randint(0, len(questions_technology_video_games))
    return questions_technology_video_games[i].__str__()


@app.route("/toys-games")
def toys_games():
    i = randint(0, len(questions_toys_games))
    return questions_toys_games[i].__str__()


@app.route("/about/categories")
def about_categories():
    categories_dict = {"categories": []}
    for c in all_categories:
        categories_dict["categories"].append(
            {"internal": c[0], "display": c[1]})
    return jsonify(categories_dict)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=TARGET_PORT)  # serve on local network
    app.run(port=TARGET_PORT)  # serve on localhost
