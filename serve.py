#!/usr/bin/env python

import csv
from random import randint

from flask import Flask, url_for

__author__ = "niklaskoopmann"
__version__ = "0.0.1"
__status__ = "Development"

TARGET_PORT = 42069

print("Starting server...")


class Question:
    def __init__(self, question, answer, category):
        self.question = question
        self.answer = answer
        self.category = category

    def __str__(self):
        return "Category: " + self.category + "<br>Question: " + self.question + "<br>Answer: " + self.answer


print("  Importing questions...")

allCategories = []

questionsArtLiterature = []
questionsEntertainment = []
questionsFoodDrink = []
questionsGeneral = []
questionsGeography = []
questionsHistoryHolidays = []
questionsLanguage = []
questionsMathematics = []
questionsMusic = []
questionsPeoplePlaces = []
questionsReligionMythology = []
questionsScienceNature = []
questionsSportsLeisure = []
questionsTechnologyVideoGames = []
questionsToysGames = []

def fill_category_question_list()

with open('./questions/art_literature.csv', 'rt', encoding="utf-8") as csvfile:
    category_display_name = "Art & Literature"
    allCategories.append(category_display_name)
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        questionsArtLiterature.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/entertainment.csv', 'rt', encoding="utf-8") as csvfile:
    category_display_name = "Entertainment"
    allCategories.append(category_display_name)
    reader = csv.reader(csvfile, delimiter=";")
    for row in reader:
        questionsEntertainment.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/food_drink.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Food & Drink"
    allCategories.append(category_display_name)
    for row in reader:
        questionsFoodDrink.append(Question(row[0], row[1], category_display_name))

with open('./questions/general.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "General"
    allCategories.append(category_display_name)
    for row in reader:
        questionsGeneral.append(Question(row[0], row[1], category_display_name))

with open('./questions/geography.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Geography"
    allCategories.append(category_display_name)
    for row in reader:
        questionsGeography.append(Question(row[0], row[1], category_display_name))

with open('./questions/history_holidays.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "History & Holidays"
    allCategories.append(category_display_name)
    for row in reader:
        questionsHistoryHolidays.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/language.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Language"
    allCategories.append(category_display_name)
    for row in reader:
        questionsLanguage.append(Question(row[0], row[1], category_display_name))

with open('./questions/mathematics.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Mathematics"
    allCategories.append(category_display_name)
    for row in reader:
        questionsMathematics.append(Question(row[0], row[1], category_display_name))

with open('./questions/music.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Music"
    allCategories.append(category_display_name)
    for row in reader:
        questionsMusic.append(Question(row[0], row[1], category_display_name))

with open('./questions/people_places.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "People & Places"
    allCategories.append(category_display_name)
    for row in reader:
        questionsPeoplePlaces.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/religion_mythology.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Religion & Mythology"
    allCategories.append(category_display_name)
    for row in reader:
        questionsReligionMythology.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/science_nature.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Science & Nature"
    allCategories.append(category_display_name)
    for row in reader:
        questionsScienceNature.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/sports_leisure.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Sports & Leisure"
    allCategories.append(category_display_name)
    for row in reader:
        questionsSportsLeisure.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/technology_video_games.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Technology & Video Games"
    allCategories.append(category_display_name)
    for row in reader:
        questionsTechnologyVideoGames.append(
            Question(row[0], row[1], category_display_name))

with open('./questions/toys_games.csv', 'rt', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")
    category_display_name = "Toys & Games"
    allCategories.append(category_display_name)
    for row in reader:
        questionsToysGames.append(Question(row[0], row[1], category_display_name))

totalNumberOfQuestions = len(questionsArtLiterature)
totalNumberOfQuestions += len(questionsEntertainment)
totalNumberOfQuestions += len(questionsFoodDrink)
totalNumberOfQuestions += len(questionsGeneral)
totalNumberOfQuestions += len(questionsGeography)
totalNumberOfQuestions += len(questionsHistoryHolidays)
totalNumberOfQuestions += len(questionsLanguage)
totalNumberOfQuestions += len(questionsMathematics)
totalNumberOfQuestions += len(questionsMusic)
totalNumberOfQuestions += len(questionsPeoplePlaces)
totalNumberOfQuestions += len(questionsReligionMythology)
totalNumberOfQuestions += len(questionsScienceNature)
totalNumberOfQuestions += len(questionsSportsLeisure)
totalNumberOfQuestions += len(questionsTechnologyVideoGames)
totalNumberOfQuestions += len(questionsToysGames)

print("  Successfully imported", totalNumberOfQuestions, "questions!")
print("")
print("  Starting Flask server...")

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"


@app.route("/art-literature")
def art_literature():
    i = randint(0, len(questionsArtLiterature))
    return questionsArtLiterature[i].__str__()


@app.route("/entertainment")
def entertainment():
    i = randint(0, len(questionsEntertainment))
    return questionsEntertainment[i].__str__()


@app.route("/food-drink")
def food_drink():
    i = randint(0, len(questionsFoodDrink))
    return questionsFoodDrink[i].__str__()


@app.route("/general")
def general():
    i = randint(0, len(questionsGeneral))
    return questionsGeneral[i].__str__()


@app.route("/geography")
def geography():
    i = randint(0, len(questionsGeography))
    return questionsGeography[i].__str__()


@app.route("/history-holidays")
def history_holidays():
    i = randint(0, len(questionsHistoryHolidays))
    return questionsHistoryHolidays[i].__str__()


@app.route("/language")
def language():
    i = randint(0, len(questionsLanguage))
    return questionsLanguage[i].__str__()


@app.route("/mathematics")
def mathematics():
    i = randint(0, len(questionsMathematics))
    return questionsMathematics[i].__str__()


@app.route("/music")
def music():
    i = randint(0, len(questionsMusic))
    return questionsMusic[i].__str__()


@app.route("/people-places")
def people_places():
    i = randint(0, len(questionsPeoplePlaces))
    return questionsPeoplePlaces[i].__str__()


@app.route("/religion-mythology")
def religion_mythology():
    i = randint(0, len(questionsReligionMythology))
    return questionsReligionMythology[i].__str__()


@app.route("/science-nature")
def science_nature():
    i = randint(0, len(questionsScienceNature))
    return questionsScienceNature[i].__str__()


@app.route("/sports-leisure")
def sports_leisure():
    i = randint(0, len(questionsSportsLeisure))
    return questionsSportsLeisure[i].__str__()


@app.route("/technology-video-games")
def technology_video_games():
    i = randint(0, len(questionsTechnologyVideoGames))
    return questionsTechnologyVideoGames[i].__str__()


@app.route("/toys-games")
def toys_games():
    i = randint(0, len(questionsToysGames))
    return questionsToysGames[i].__str__()


@app.route("/about/categories")
def about_categories():
    return allCategories.__str__()


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=TARGET_PORT)  # serve on local network
    app.run(port=TARGET_PORT)  # serve on localhost
