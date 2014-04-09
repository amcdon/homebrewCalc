import modules.calculators as Calc
import time
import math


ogCalculator = Calc.OriginalGravityCalculator()
srmCalculator = Calc.SRMCalculator()
ibuCalculator = Calc.IBUCalculator()

def app():
    while True:
        helper = raw_input("What would you like to do today?  For help type 'Help' ")

        if helper.lower() == 'help':
            print ("Please enter a command for what you would like to do. Options include: Calculate Original Gravity, Calculate SRM")
            time.sleep(1)

        elif helper.lower() in ('calculate original gravity', 'calculate og', 'calc og'):
            time.sleep(1)
            return calcOG()

        elif helper.lower() in ('calculate srm', 'calc srm'):
            time.sleep(1)
            return calcSRM()

        elif helper.lower() in ('calculate ibu', 'calc ibu'):
            time.sleep(1)
            return calcIBU()

def calcOG():
    method = raw_input("How will you be brewing today? ")
    volume = float(raw_input("What is your batch volume? "))
    ingredient_place_holder = 1
    total_og = 0.0

    if method.lower() in ("all-grain", "all grain", "ag"):
        ingredients = float(raw_input("How many fermentable ingredients are in your recipe? "))
        brewhouse_eff = float(raw_input("What is your brew house efficiency? "))

        while ingredient_place_holder <= ingredients:
            weight = float(raw_input("Ingredient " + str(ingredient_place_holder) + " weight in pounds. "))
            ppg = float(raw_input("Ingredient " + str(ingredient_place_holder) + " points per pound per gallon. "))
            total_og += ogCalculator.allGrain(weight, ppg, brewhouse_eff, volume)
            ingredient_place_holder += 1

        return ogCalculator.og(total_og)


    elif method.lower() in ("partial-mash", "partial mash", "pm"):
        ingredients = float(raw_input("How many fermentable ingredients are in your recipe? "))
        brewhouse_eff = float(raw_input("What is your brew house efficiency? "))

        while ingredient_place_holder <= ingredients:
            helper = raw_input("Is ingredient " + str(ingredient_place_holder) + " extract or malt? ")

            if helper == "extract":
                weight = float(raw_input("Ingredient " + str(ingredient_place_holder) + " weight in pounds. "))
                ppg = float(raw_input("Ingredient " + str(ingredient_place_holder) + " points per pound per gallon(PPG). "))
                total_og += ogCalculator.extractOG(weight, ppg, volume)
                ingredient_place_holder += 1

            elif helper == "malt":
                weight = float(raw_input("Ingredient " + str(ingredient_place_holder) + " weight in pounds. "))
                ppg = float(raw_input("Ingredient " + str(ingredient_place_holder) + " points per pound per gallon(PPG). "))
                total_og += ogCalculator.allGrain(weight, ppg, brewhouse_eff, volume)
                ingredient_place_holder += 1

            else:
                print "You did not enter a valid option."

        return ogCalculator.og(total_og)

    elif method.lower() in ("extract"):
        ingredients = float(raw_input("How many fermentable ingredients are in your recipe? "))

        while ingredient_place_holder <= ingredients:
            weight = float(raw_input("Ingredient " + str(ingredient_place_holder) + " weight in pounds. "))
            ppg = float(raw_input("Ingredient " + str(ingredient_place_holder) + " points per pound per gallon(PPG). "))
            total_og += ogCalculator.extractOG(weight, ppg, volume)
            ingredient_place_holder += 1

        return ogCalculator.og(total_og)

    else:
        print "You did not enter a valid method."


def calcSRM():
    ingredients = int(raw_input("How many ingredients are in your grain bill? "))
    volume = float(raw_input("What is your batch volume? "))
    ingredient_place_holder = 1
    total_srm = 0.0

    while ingredient_place_holder <= ingredients:
        weight = float(raw_input("Ingredient " + str(ingredient_place_holder) + " weight: "))
        lov = float(raw_input("Ingredient " + str(ingredient_place_holder) + " Lovibond: "))
        total_srm += srmCalculator.srmEstimator(weight,lov,volume)
        ingredient_place_holder += 1

    return total_srm

def calcIBU():
    import modules.utilization_library as util

    ingredients = int(raw_input("How many different hop additions will you be making? "))
    volume = float(raw_input("What will be your starting boil volume? "))
    original_gravity = round(float(raw_input("What is the original gravity? ")), 2)
    ingredient_place_holder = 1
    total_ibu = 0.0

    while ingredient_place_holder <= ingredients:
        weight = float(raw_input("Hop " + str(ingredient_place_holder) + " weight in ounces? "))
        alpha_acid = float(raw_input("Hop " + str(ingredient_place_holder) + " alpha acid percentage? "))
        boil_time = int(raw_input("how long will hop " + str(ingredient_place_holder) + " be in the boil? "))
        aau = ibuCalculator.calcAAU(weight, alpha_acid)
        utilization = util.utilization[boil_time][original_gravity]
        total_ibu += ibuCalculator.calcIBU(aau, utilization, volume)
        ingredient_place_holder += 1
    return total_ibu


print app()