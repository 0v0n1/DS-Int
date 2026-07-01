class plan:
    def breakfast(self):
        pass

class KetoDiet(plan):
    def breakfast(self):
        return "Fruits"

class VeganDiet(plan):
    def breakfast(self):
        return "Salad"

class YetAnotherDiet(plan):
    def breakfast(self):
        return "Cereal"

def printIt(plan):
    print(f"breakfast: {plan.breakfast()}")

keto = KetoDiet()
vegan = VeganDiet()
yet_another = YetAnotherDiet()
printIt(keto)
printIt(vegan)
printIt(yet_another)