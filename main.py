###############################################################
#                COOKING SIM — BASE STRUCTURE (NOTES)
###############################################################

# -----------------------------
#  GLOBAL VARIABLES (BASE ONLY)
# -----------------------------

# Location flags
atHome = True
atStore = False
atCafe = False
inKitchen = False

# Store navigation
currentAisle = 0   # 0 = not in an aisle

# Player stats
money = 0
inventory = {}
inventorySpace = 0   # decide max later

# Recipe system
currentRecipe = None
recipes = {}         # fill in later
gameWon = False

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