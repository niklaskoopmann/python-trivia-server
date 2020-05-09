# python-trivia-server
:snake: :question: :outbox_tray:

A basic Flask server to provide random trivia questions from different categories.
It's still work in progress :wrench: at every front but already serves from a CSV database of 45k questions with an endpoint per category.
Thanks to u/007craft for publishing their huge set of trivia questions! :wave:

## TO DO

### Feedback to server
- implement POST requests
- features:
  - regex checking for validity of questions (warn if failed)
  - correct questions and answers
  - suggest re-categorization
  - suggest sub-categorization (map categories!)
- for now: blindly accept suggestions (can't get much worse anyway)

### Database
- Make it grow!
  - use rest of questions in Excel sheet
  - find new questions online
    - open trivia database
    - Wer wird Millionär? / Who wants to be a Millionaire?
- Centralize it in a MySQL database. (Docker?)

### Frontend
- on start: label wedges with custom categories
- display "wheel" with six wedge colours on screen
- click wedge to get random question
- if applicable: hide multiple choice answers with optional show

### Documentation
- add comments to script

## Mapping to Trivial Pursuit categories
| Trivial Pursuit (DE)     | python-trivia-server                                |
|--------------------------|-----------------------------------------------------|
| Kunst und Literatur      | art-literature, language                            |
| Erdkunde                 | geography                                           |
| Sport und Vergnügen      | sports-leisure, food-drink                          |
| Geschichte               | history-holidays, religion-mythology                |
| Unterhaltung             | entertainment, music, people-places, toys-games     |
| Wissenschaft und Technik | mathematics, science-nature, technology-video-games |
