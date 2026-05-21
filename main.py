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
currentAisle = -1   # 0 = not in an aisle

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

tomatoA = 0
noodlesA = 0
flourA =0
milkA = 0
eggA = 0
meatA = 0
vegmeatA = 0
cheeseA = 0
onionA = 0
waterA = 0
carrotA = 0
butterA = 0
oilA = 0
lettuceA = 0
cucumberA = 0
chocolateA = 0
sugarA = 0
saltA = 0
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

def buy_tomato(food: str) -> str:
    """Gets the radius of the given planet

    Args:
        planet_name - name of the planet to get radius of

    Returns:
        radius of the given planet
    """
    if currentAisle== -1:
        return "You are not in the store! Go to the store to look for your ingredient."
    elif currentAisle==tomatoA:
        if money0>0:
            money0 = money0-1
            tomato = tomato+1
            return "You found the tomato! You gained a tomato, and paid 1 gold"
        else:
            return "You have no money! Go earn some by working in the Cafe."
    else:
        return "You can't find the tomato in this Aisle. Go look in another one!"
        
def checkLoc(location):
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
    
    
def changeLoc(locatio):
    global atHome
    global atCafe
    global atStore
    h =atHome
    t= True
    f= False
    c=atCafe
    s=atStore
    if locatio=="home":
        if h==f:
            atHome=t
            print("You've came back home")
        else:
            print("You are already at home")
    elif locatio=="store":
        if s==f:
            atStore=t
            print("You've entered the Store, what do you want to buy?")
        else:
            print("You are already at the Store")
    elif locatio=="cafe":
        if c==f:
            atCafe=t
            print("You've entered the Cafe, time to work!")
        else:
            print("You are already at the Cafe")

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


def birth_date(matches: List[str]) -> List[str]:
    """Returns birth date of named person in matches

    Args:
        matches - match from pattern of person's name to find birth date of

    Returns:
        birth date of named person
    """
    return [get_birth_date(" ".join(matches))]

def buy_food(matches: List[str]) -> List[str]:
    if mat1==tomato:
        buy_tomato(" ".join(matches))

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
    ("when was % born".split(), birth_date),
    ("what is the polar radius of %".split(), polar_radius),
    ("when did % die".split(),death_date),
    ("how old is %".split(),age),
    ("how old was %".split(),age),
    ("where was % born".split(),birth_place),
    ("is % alive".split(),alive),
    ("is % still alive".split(),alive),
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