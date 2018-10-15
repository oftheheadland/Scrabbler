from flask import Flask, render_template, request, jsonify, make_response
from json import dumps
from collections import Counter
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

#TODO: sanitize input, only take letters
#TODO: if given more than 12? letters, display a message, don't send ajax
#TODO: better UI/UX
@app.route('/scrabble/', methods=['POST'])
def scrabble():
    print(request.form.get('letters', 0))
    letters = list(request.form.get('letters', 0).lower())
    charSet = Counter(letters)

    matches = []
    with open('scrabble.txt', 'r') as f:
        input = f.readlines()

    # traverse words in list, remove \n then check if the word can be made from the letters given. return an array of matched words.
    for word in input:
        word = word.replace('\n', '').lower()
        # if first letter isn't in the character list, skip it
        if word[0] not in charSet:
            continue

        if not Counter(word) - charSet:
            matches.append(word)
        

    return make_response(dumps(matches))


if __name__ == '__main__':
    app.run(debug=True)
