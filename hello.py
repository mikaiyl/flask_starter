from flask import Flask, render_template
from tinydb import TinyDB
from random import randrange

app = Flask(__name__)
app.db = TinyDB('db.json')


@app.route('/all')
def hello_world():
    return render_template('all.html', recipe_list=app.db.all())


@app.route('/')
def rand_recipe():
    recipe = app.db.all()[randrange(len(app.db))]
    return render_template('recipe.html', recipe=recipe) # noqa


@app.route('/recipe/')
@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe = app.db.all()[int(recipe_id)]
    print(recipe)
    return render_template('recipe.html', recipe=recipe) # noqa
