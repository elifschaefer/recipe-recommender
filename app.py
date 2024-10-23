import requests
API_KEY='21b084b4b9fb4e0ca397f0ad02c202af'

def get_recipes(ingredients):
    url=f'https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&apiKey={API_KEY}'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    ingredients ='apple, banana'
    recipes = get_recipes(ingredients)
    print(recipes)
