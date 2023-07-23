def main():
    fruit = input("Which fruit would you like to check? ").lower()

    if calorie_check(fruit):
        print (f"{fruit}: {calorie_check(fruit)} kcal")

def calorie_check(fruit):

    fruits = {
        'apple': 130,
        'avocado': 50,
        'banana': 110,
        'cantaloupe': 50,
        'grapefruit': 60,
        'grapes': 90,
        'honeydew lemon': 50,
        'kiwifruit': 90,
        'lemon': 15,
        'lime': 20,
        'nectarine': 60,
        'orange': 80,
        'peach': 60,
        'pear': 100,
        'pineapples': 50,
        'plums': 70,
        'strawberries': 50,
        'sweet cherries': 100,
        'tangerine': 50,
        'watermelon': 80
        }
    
    if fruit in fruits:
        return fruits[fruit]

main()