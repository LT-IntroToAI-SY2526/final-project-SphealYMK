###############################################################
#                COOKING SIM — BASE STRUCTURE (NOTES)
###############################################################

# -----------------------------
#  GLOBAL VARIABLES (BASE ONLY)
# -----------------------------
act1 = "J"
pat1 = "K"
mat1 = "L"
# Location flags
atHome = True
atStore = False
atCafe = False
inKitchen = False

# Store navigation
currentAisle = -1   # 0 = not in an aisle # -1 = not at Store

# Player stats
money0 = 1
inventory = {}
inventorySpace = 0   # decide max later

# Recipe system
currentRecipe = None
recipes = {}         # fill in later
gameWon = False

#foods in store
tomato = 0
noodles = 0
flour =0
milk = 0
egg = 0
meat = 0
vegmeat = 0
cheese = 0
onion = 0
water = 0
carrot = 0
butter = 0
oil = 0
lettuce = 0
cucumber = 0
chocolate = 0
sugar = 0
salt = 0


#ailes of ingredients
tomatoA = random.randint(1, 3)
noodlesA = random.randint(1, 3)
flourA = random.randint(1, 3)
milkA = random.randint(1, 3)
eggA = random.randint(1, 3)
meatA = random.randint(1, 3)
vegmeatA = random.randint(1, 3)
cheeseA = random.randint(1, 3)
onionA = random.randint(1, 3)
waterA = random.randint(1, 3)
carrotA = random.randint(1, 3)
butterA = random.randint(1, 3)
oilA = random.randint(1, 3)
lettuceA = random.randint(1, 3)
cucumberA = random.randint(1, 3)
chocolateA = random.randint(1, 3)
sugarA = random.randint(1, 3)
saltA = random.randint(1, 3)

#cafe ingredients
'Toppings: Whipped Cream, Chocolate Syrup, Carmel Syrup, Marshmallow, Plain(no additives),'
'Base: Coffee Bean, Vanilla Bean, Tonka Bean, Chikory Root, Hot Chocolate'
orders = [
    # Whipped Cream
    "I'd like a Whipped Cream Chicory",
    "I'd like a Whipped Cream Coffee",
    "I'd like a Whipped Cream Hot Chocolate",
    "I'd like a Whipped Cream Tonka",
    "I'd like a Whipped Cream Vanilla",

    # Chocolate Syruped
    "I'd like a Chocolate Syruped Chicory",
    "I'd like a Chocolate Syruped Coffee",
    "I'd like a Chocolate Syruped Hot Chocolate",
    "I'd like a Chocolate Syruped Tonka",
    "I'd like a Chocolate Syruped Vanilla",

    # Caramel Syrup
    "I'd like a Caramel Syrup Chicory",
    "I'd like a Caramel Syrup Coffee",
    "I'd like a Caramel Syrup Hot Chocolate",
    "I'd like a Caramel Syrup Tonka",
    "I'd like a Caramel Syrup Vanilla",

    # Marshmallow
    "I'd like a Marshmallow Chicory",
    "I'd like a Marshmallow Coffee",
    "I'd like a Marshmallow Hot Chocolate",
    "I'd like a Marshmallow Tonka",
    "I'd like a Marshmallow Vanilla",

    # Plain
    "I'd like a Plain Chicory",
    "I'd like a Plain Coffee",
    "I'd like a Plain Hot Chocolate",
    "I'd like a Plain Tonka",
    "I'd like a Plain Vanilla"
]

orderNames = [
    "Whipped Cream Chicory",
    "Whipped Cream Coffee",
    "Whipped Cream Hot Chocolate",
    "Whipped Cream Tonka",
    "Whipped Cream Vanilla",

    "Chocolate Syruped Chicory",
    "Chocolate Syruped Coffee",
    "Chocolate Syruped Hot Chocolate",
    "Chocolate Syruped Tonka",
    "Chocolate Syruped Vanilla",

    "Caramel Syrup Chicory",
    "Caramel Syrup Coffee",
    "Caramel Syrup Hot Chocolate",
    "Caramel Syrup Tonka",
    "Caramel Syrup Vanilla",

    "Marshmallow Chicory",
    "Marshmallow Coffee",
    "Marshmallow Hot Chocolate",
    "Marshmallow Tonka",
    "Marshmallow Vanilla",

    "Plain Chicory",
    "Plain Coffee",
    "Plain Hot Chocolate",
    "Plain Tonka",
    "Plain Vanilla"
]

# Ingredient list (fill in later)
# ingredients = {
#     "ingredientName": { "aisle": ?, "price": ? },
# }

# -----------------------------
#  ACTIONS TO IMPLEMENT (BASE)
# -----------------------------

# goToStore
# goToHome
# goToKitchen
# cookItem
# goToAisle
# buyItem
# storeItem
# work

# -----------------------------
#  PA-LIST COMMANDS (BASE)
# -----------------------------
# ("go to store".split(), goToStore)
# ("go home".split(), goToHome)
# ("go to kitchen".split(), goToKitchen)
# ("cook %".split(), cookItem)
# ("go to aisle %".split(), goToAisle)
# ("buy %".split(), buyItem)
# ("store %".split(), storeItem)
# ("work".split(), work)

###############################################################
# END — FILL IN TOMORROW

import re, string, calendar, requests, time
from wikipedia import WikipediaPage
import wikipedia
from bs4 import BeautifulSoup
from match import match
from typing import List, Callable, Tuple, Any, Match
from dateutil import parser
import random



def clean_text(text: str) -> str:
    """Cleans given text removing non-ASCII characters and duplicate spaces & newlines

    Args:
        text - text to clean

    Returns:
        cleaned text
    """
    only_ascii = "".join([char if char in string.printable else " " for char in text])
    no_dup_spaces = re.sub(" +", " ", only_ascii)
    no_dup_newlines = re.sub("\n+", "\n", no_dup_spaces)
    return no_dup_newlines


def get_match(
    text: str,
    pattern: str,
    error_text: str = "Page doesn't appear to have the property you're expecting",
) -> Match:
    """Finds regex matches for a pattern

    Args:
        text - text to search within
        pattern - pattern to attempt to find within text
        error_text - text to display if pattern fails to match

    Returns:
        text that matches
    """
    p = re.compile(pattern, re.DOTALL | re.IGNORECASE)
    match = p.search(text)

    if not match:
        raise AttributeError(error_text)
    return match

def update_mat1(item):
    global mat1
    y = item
    mat1 = y

# def check_mat1(item):

def buy_tomato():
    global tomato
    global money0
    global tomatoA
    global currentAisle
    if currentAisle== -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle== 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle==tomatoA:
        if money0>0:
            money0 = money0-1
            tomato = tomato+1
            print("You found the tomato! You gained a tomato, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the tomato in this Aisle. Go look in another one!")

def buy_noodles():
    global noodles
    global money0
    global noodlesA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == noodlesA:
        if money0 > 0:
            money0 -= 1
            noodles += 1
            print("You found the noodles! You gained noodles, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the noodles in this Aisle. Go look in another one!")


def buy_flour():
    global flour
    global money0
    global flourA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == flourA:
        if money0 > 0:
            money0 -= 1
            flour += 1
            print("You found the flour! You gained flour, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the flour in this Aisle. Go look in another one!")


def buy_milk():
    global milk
    global money0
    global milkA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == milkA:
        if money0 > 0:
            money0 -= 1
            milk += 1
            print("You found the milk! You gained milk, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the milk in this Aisle. Go look in another one!")


def buy_egg():
    global egg
    global money0
    global eggA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == eggA:
        if money0 > 0:
            money0 -= 1
            egg += 1
            print("You found the egg! You gained an egg, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the egg in this Aisle. Go look in another one!")


def buy_meat():
    global meat
    global money0
    global meatA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == meatA:
        if money0 > 0:
            money0 -= 1
            meat += 1
            print("You found the meat! You gained meat, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the meat in this Aisle. Go look in another one!")


def buy_vegmeat():
    global vegmeat
    global money0
    global vegmeatA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == vegmeatA:
        if money0 > 0:
            money0 -= 1
            vegmeat += 1
            print("You found the vegmeat! You gained vegmeat, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the vegmeat in this Aisle. Go look in another one!")


def buy_cheese():
    global cheese
    global money0
    global cheeseA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == cheeseA:
        if money0 > 0:
            money0 -= 1
            cheese += 1
            print("You found the cheese! You gained cheese, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the cheese in this Aisle. Go look in another one!")


def buy_onion():
    global onion
    global money0
    global onionA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == onionA:
        if money0 > 0:
            money0 -= 1
            onion += 1
            print("You found the onion! You gained an onion, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the onion in this Aisle. Go look in another one!")


def buy_water():
    global water
    global money0
    global waterA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == waterA:
        if money0 > 0:
            money0 -= 1
            water += 1
            print("You found the water! You gained water, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the water in this Aisle. Go look in another one!")


def buy_carrot():
    global carrot
    global money0
    global carrotA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == carrotA:
        if money0 > 0:
            money0 -= 1
            carrot += 1
            print("You found the carrot! You gained a carrot, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the carrot in this Aisle. Go look in another one!")


def buy_butter():
    global butter
    global money0
    global butterA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == butterA:
        if money0 > 0:
            money0 -= 1
            butter += 1
            print("You found the butter! You gained butter, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the butter in this Aisle. Go look in another one!")


def buy_oil():
    global oil
    global money0
    global oilA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == oilA:
        if money0 > 0:
            money0 -= 1
            oil += 1
            print("You found the oil! You gained oil, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the oil in this Aisle. Go look in another one!")


def buy_lettuce():
    global lettuce
    global money0
    global lettuceA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == lettuceA:
        if money0 > 0:
            money0 -= 1
            lettuce += 1
            print("You found the lettuce! You gained lettuce, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the lettuce in this Aisle. Go look in another one!")


def buy_cucumber():
    global cucumber
    global money0
    global cucumberA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == cucumberA:
        if money0 > 0:
            money0 -= 1
            cucumber += 1
            print("You found the cucumber! You gained a cucumber, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the cucumber in this Aisle. Go look in another one!")


def buy_chocolate():
    global chocolate
    global money0
    global chocolateA
    global currentAisle    
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == chocolateA:
        if money0 > 0:
            money0 -= 1
            chocolate += 1
            print("You found the chocolate! You gained chocolate, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the chocolate in this Aisle. Go look in another one!")


def buy_sugar():
    global sugar
    global money0
    global sugarA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == sugarA:
        if money0 > 0:
            money0 -= 1
            sugar += 1
            print("You found the sugar! You gained sugar, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the sugar in this Aisle. Go look in another one!")


def buy_salt():
    global salt
    global money0
    global saltA
    global currentAisle
    if currentAisle == -1:
        print("You are not in the store! Go to the store to look for your ingredient.")
    elif currentAisle == 0:
        print("You are not in an aisle right now. Go to an aisle first!")
    elif currentAisle == saltA:
        if money0 > 0:
            money0 -= 1
            salt += 1
            print("You found the salt! You gained salt, and paid 1 gold")
        else:
            print("You have no money! Go earn some by working in the Cafe.")
    else:
        print("You can't find the salt in this Aisle. Go look in another one!")

def checkLoc(location)-> str:
    global atHome
    global atCafe
    global atStore
    h =atHome
    c=atCafe
    s=atStore
    if location=="home":
        return h
    if location=="store":
        return s
    if location=="cafe":
        return c
    
    return True
    
    
def changeLoc(locatio):
    global atHome
    global atCafe
    global atStore
    global currentAisle
    h =atHome
    t= True
    f= False
    c=atCafe
    s=atStore
    cA=currentAisle
    if locatio=="home":
        if h==f:
            currentAisle= -1
            print("You've come back home")
            atHome=t
            atStore=f
            atCafe=f
        else:
            print("You are already at home")
    elif locatio=="store":
        if s==f:
            currentAisle= 0
            print("You've entered the Store, what do you want to buy?")
            atStore=t
            atHome=f
            atCafe=f            
        else:
            print("You are already at the Store")
    elif locatio=="cafe":
        if c==f:
            currentAisle= -1
            print("You've entered the Cafe, time to work!")
            atCafe=t
            atHome=f
            atStore=f
        else:
            print("You are already at the Cafe")
    else:
        print("Not a Valid location, Please enter: 'Go to (Cafe, Home, or Store)")

def go_somewhere(place):
    if not checkLoc(place):
        changeLoc(place)

# def get_birth_date(name: str) -> str:
#     """Gets birth date of the given person

#     Args:
#         name - name of the person

#     Returns:
#         birth date of the given person
#     """
#     infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
#     pattern = r"(?:Born\D*)(?P<birth>\d{4}-\d{2}-\d{2})"
#     error_text = (
#         "Page infobox has no birth information (at least none in xxxx-xx-xx format)"
#     )
#     match = get_match(infobox_text, pattern, error_text)

#     return match.group("birth")

# def get_death_date(name: str) -> str:
#     """Gets birth date of the given person

#     Args:
#         name - name of the person

#     Returns:
#         birth death of the given person
#     """
#     #infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
#     infobox_text = re.sub(r"\(.*?\)", "", infobox_text)
#     pattern = r"Died[^A-Za-z]*([A-Za-z]+\s+\d{1,2},?\s+\d{4})"

#     error_text = (
#         "Page infobox has no death information (at least none in xxxx-xx-xx format)"
#     )
#     match = re.search(pattern, infobox_text)
#     if not match:
#         return "Alive"
#     raw_date = match.group(1)

#     dt = parser.parse(raw_date)
#     return dt.strftime("%Y-%m-%d")

# def get_age(name: str) -> str:
#     #infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))

#     # 1. Check for death age: (aged XX)
#     death_age_match = re.search(r"\(aged\s+(\d+)\)", infobox_text)
#     if death_age_match:
#         age = death_age_match.group(1)
#         return f"Dead at age {age}"

#     # 2. Check for living age: (age XX)
#     living_age_match = re.search(r"\(age\s+(\d+)\)", infobox_text)
#     if living_age_match:
#         age1 = living_age_match.group(1)
#         return f"{age1} years old"
#     # 3. No age found
#     return "Unknown"

# def get_aliveness(name:str) -> str:
#     #infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))
#     death_age_match1 = re.search(r"\(aged\s+(\d+)\)", infobox_text)
#     if death_age_match1:
#         return f"The Person is currently Dead"

#     # 2. Check for living age: (age XX)
#     living_age_match1 = re.search(r"\(age\s+(\d+)\)", infobox_text)
#     if living_age_match1:
#         return f"The person is currently alive"
#     # 3. No age found
#     return "Unknown"
# def get_birth_place(name: str) -> str:
#     #infobox_text = clean_text(get_first_infobox_text(get_page_html(name)))

#     pattern = r"Born.*?\d{4}[^\w]*([A-Za-z .'-]+,[A-Za-z .'-]+)"
#     match = re.search(pattern, infobox_text)

#     if match:
#         return match.group(1).strip()

#     pattern2 = r"Born[\s\S]*?\(age \d+\)\s*([A-Za-z .'-]+,[A-Za-z .'-]+)(?=Afghanistan|Albania|Algeria|Andorra|Angola|Antigua|Argentina|Armenia|Australia|Austria|Azerbaijan|Baden|Bahamas|Bahrain|Bangladesh|Barbados|Bavaria|Belarus|Belgium|Belize|Benin|Bolivia|Bosnia|Botswana|Brazil|Brunei|Brunswick|Bulgaria|Burkina|Burma|Burundi|Cabo|Cambodia|Cameroon|Canada|Cayman|Central|Chad|Chile|China|Colombia|Comoros|Congo|Cook|Costa|Cote|Croatia|Cuba|Cyprus|Czechia|Czechoslovakia|Democratic|Denmark|Djibouti|Dominica|Dominican|Duchy|East|Ecuador|Egypt|El|Equatorial|Eritrea|Estonia|Eswatini|Ethiopia|Federal|Fiji|Finland|France|Gabon|Gambia|Georgia|Germany|Ghana|Grand|Greece|Grenada|Guatemala|Guinea|Guyana|Haiti|Hanover|Hanseatic|Hawaii|Hesse|Holy|Honduras|Hungary|Iceland|India|Indonesia|Iran|Iraq|Ireland|Israel|Italy|Jamaica|Japan|Jordan|Kazakhstan|Kenya|Kingdom|Kiribati|Korea|Kosovo|Kuwait|Kyrgyzstan|Laos|Latvia|Lebanon|Lesotho|Lew|Liberia|Libya|Liechtenstein|Lithuania|Luxembourg|Madagascar|Malawi|Malaysia|Maldives|Mali|Malta|Marshall|Mauritania|Mauritius|Mecklenburg-Schwerin|Mecklenburg-Strelitz|Mexico|Micronesia|Moldova|Monaco|Mongolia|Montenegro|Morocco|Mozambique|Namibia|Nassau|Nauru|Nepal|Netherlands|New|Nicaragua|Niger|Nigeria|Niue|North|Norway|Oldenburg|Oman|Orange|Pakistan|Palau|Panama|Papal|Papua|Paraguay|Peru|Philippines|Piedmont-Sardinia|Poland|Portugal|Qatar|Republic|Romania|Russia|Rwanda|Saint|Samoa|San|Sao|Saudi|Schaumburg-Lippe|Senegal|Serbia|Seychelles|Sierra|Singapore|Slovakia|Slovenia|Solomon|Somalia|South|Spain|Sri|Sudan|Suriname|Sweden|Switzerland|Syria|Tajikistan|Tanzania|Texas|Thailand|Timor-Leste|Togo|Tonga|Trinidad|Tunisia|Turkey|Turkmenistan|Tuvalu|Two|Uganda|Ukraine|Union|United|Uruguay|Uzbekistan|Vanuatu|Venezuela|Vietnam|Württemberg|Yemen|Zambia|Zimbabwe)"
#     pattern3 = r"Birthplace[\s\S]*?\(age \d+\)\s*([A-Za-z .'-]+,[A-Za-z .'-]+)(?=Afghanistan|Albania|Algeria|Andorra|Angola|Antigua|Argentina|Armenia|Australia|Austria|Azerbaijan|Baden|Bahamas|Bahrain|Bangladesh|Barbados|Bavaria|Belarus|Belgium|Belize|Benin|Bolivia|Bosnia|Botswana|Brazil|Brunei|Brunswick|Bulgaria|Burkina|Burma|Burundi|Cabo|Cambodia|Cameroon|Canada|Cayman|Central|Chad|Chile|China|Colombia|Comoros|Congo|Cook|Costa|Cote|Croatia|Cuba|Cyprus|Czechia|Czechoslovakia|Democratic|Denmark|Djibouti|Dominica|Dominican|Duchy|East|Ecuador|Egypt|El|Equatorial|Eritrea|Estonia|Eswatini|Ethiopia|Federal|Fiji|Finland|France|Gabon|Gambia|Georgia|Germany|Ghana|Grand|Greece|Grenada|Guatemala|Guinea|Guyana|Haiti|Hanover|Hanseatic|Hawaii|Hesse|Holy|Honduras|Hungary|Iceland|India|Indonesia|Iran|Iraq|Ireland|Israel|Italy|Jamaica|Japan|Jordan|Kazakhstan|Kenya|Kingdom|Kiribati|Korea|Kosovo|Kuwait|Kyrgyzstan|Laos|Latvia|Lebanon|Lesotho|Lew|Liberia|Libya|Liechtenstein|Lithuania|Luxembourg|Madagascar|Malawi|Malaysia|Maldives|Mali|Malta|Marshall|Mauritania|Mauritius|Mecklenburg-Schwerin|Mecklenburg-Strelitz|Mexico|Micronesia|Moldova|Monaco|Mongolia|Montenegro|Morocco|Mozambique|Namibia|Nassau|Nauru|Nepal|Netherlands|New|Nicaragua|Niger|Nigeria|Niue|North|Norway|Oldenburg|Oman|Orange|Pakistan|Palau|Panama|Papal|Papua|Paraguay|Peru|Philippines|Piedmont-Sardinia|Poland|Portugal|Qatar|Republic|Romania|Russia|Rwanda|Saint|Samoa|San|Sao|Saudi|Schaumburg-Lippe|Senegal|Serbia|Seychelles|Sierra|Singapore|Slovakia|Slovenia|Solomon|Somalia|South|Spain|Sri|Sudan|Suriname|Sweden|Switzerland|Syria|Tajikistan|Tanzania|Texas|Thailand|Timor-Leste|Togo|Tonga|Trinidad|Tunisia|Turkey|Turkmenistan|Tuvalu|Two|Uganda|Ukraine|Union|United|Uruguay|Uzbekistan|Vanuatu|Venezuela|Vietnam|Württemberg|Yemen|Zambia|Zimbabwe)"
#     match2 = re.search(pattern2, infobox_text)
#     match3 = re.search(pattern3, infobox_text)
#     if match2:
#         birthplace = match2.group(1).strip()
#         return birthplace
#     if match3:
#         birthplace2 = match2.group(1).strip()
#         return birthplace2

#     return "They are still alive! Live in the moment..."
# below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


# def birth_date(matches: List[str]) -> List[str]:
#     """Returns birth date of named person in matches

#     Args:
#         matches - match from pattern of person's name to find birth date of

#     Returns:
#         birth date of named person
#     """
#     return [get_birth_date(" ".join(matches))]

def buy_food(matches: List[str]) -> List[str]:
    if mat1=="tomato":
        buy_tomato()
    if mat1 == "noodles":
        buy_noodles()
    if mat1 == "flour":
        buy_flour()
    if mat1 == "milk":
        buy_milk()
    if mat1 == "egg":
        buy_egg()
    if mat1 == "meat":
        buy_meat()
    if mat1 == "vegmeat":
        buy_vegmeat()
    if mat1 == "cheese":
        buy_cheese()
    if mat1 == "onion":
        buy_onion()
    if mat1 == "water":
        buy_water()
    if mat1 == "carrot":
        buy_carrot()
    if mat1 == "butter":
        buy_butter()
    if mat1 == "oil":
        buy_oil()
    if mat1 == "lettuce":
        buy_lettuce()
    if mat1 == "cucumber":
        buy_cucumber()
    if mat1 == "chocolate":
        buy_chocolate()
    if mat1 == "sugar":
        buy_sugar()
    if mat1 == "salt":
        buy_salt()


# tomato = 0
# noodles = 0
# flour =0
# milk = 0
# egg = 0
# meat = 0
# vegmeat = 0
# cheese = 0
# onion = 0
# water = 0
# carrot = 0
# butter = 0
# oil = 0
# lettuce = 0
# cucumber = 0
# chocolate = 0
# sugar = 0
# salt = 0
def check_aisle() -> str:
    global currentAisle
    x=currentAisle
    return x

def change_aisle(number):
    global atStore
    global currentAisle
    y=atStore
    x=number
    if atStore==True:
        currentAisle=x
    else:
        print("You are not at the store right now!")

def make_coffee():
    global atCafe

# def polar_radius(matches: List[str]) -> List[str]:
#     """Returns polar radius of planet in matches

#     Args:
#         matches - match from pattern of planet to find polar radius of

#     Returns:
#         polar radius of planet
#     """
#     return [get_polar_radius(matches[0])]


# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# type aliases to make pa_list type more readable, could also have written:
# pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [...]
Pattern = List[str]
Action = Callable[[List[str]], List[Any]]

# The pattern-action list for the natural language query system. It must be declared
# here, after all of the function definitions
pa_list: List[Tuple[Pattern, Action]] = [
    ("buy %".split(), buy_food),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        print(act)
        print(pat)
        print(mat)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers"]

    return ["I don't understand"]


def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully"""
    print("Welcome to the wikipedia chatbot!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


# uncomment the next line once you've implemented everything are ready to try it out
#query_loop()
