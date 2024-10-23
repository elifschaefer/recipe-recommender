import requests
from flask import Flask

API_KEY='21b084b4b9fb4e0ca397f0ad02c202af'

def get_recipes(ingredients):
    url=f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={API_KEY}'
    response = requests.get(url)
    return response.json()

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!!!"

@app.route('/recipes')
def hello_recipes():
    ingredients ='apple, banana'
    recipes = get_recipes(ingredients)
    #print(recipes)
    return recipes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)




