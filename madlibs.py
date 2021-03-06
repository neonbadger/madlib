from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


character_list = ['tom cruise', 'george clooney', 'benedict cumberbatch', 'joseph gordon-levitt',
                  'leonardo dicaprio', 'emma watson', 'james bond', 'lady gaga', 'katniss everdeen']

color_list = ['red', 'blue', 'yellow', 'green', 'black', 'purple', 'pink',
              'neon', 'iridescent', 'gold', 'marigold', 'lavender', 'cerulean blue']

adj_list = ['fierce', 'grumpy', 'sad', 'happy', 'shallow']


@app.route('/')
def start_here():
    """Homepage."""

    return render_template("home.html")


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_game_form():

    answer = request.args.get("game")

    if answer == "yes":
        return render_template('game.html', characters=character_list,
                                colors=color_list, adjectives=adj_list)
    else:
        return render_template('goodbye.html')



@app.route('/madlib', methods=['POST', 'GET'])
def show_madlib():

    if request.method == "GET":
        character = request.args.get('character')
        color = request.args.get('color')
        noun = request.args.get('noun')
        adjs = request.args.getlist('adj')

    elif request.method == "POST":
        character = request.form.get('character')
        color = request.form.get('color')
        noun = request.form.get('noun')
        adjs = request.form.getlist('adj')

    which_template = choice(['madlib.html', 'altmadlib.html'])

    return render_template(which_template, character=character,
                            color=color, noun=noun, adjs=adjs)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
