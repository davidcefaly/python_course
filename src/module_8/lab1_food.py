class Food:
    base_hearts = 1

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)

    @classmethod
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts

    @classmethod
    def from_nothing(cls, hearts):
        food = cls([])
        food.hearts = hearts
        return food


def main():
    heart = "\u00f0\u0178\u2019\u2022"

    skewer = Food(["Mushroom", "Hearty Mushroom"])
    print(f"This Mushroom Skewer heals {skewer.hearts} hearts! {heart}")

    Food.base_hearts = 2
    skewer = Food(["Mushroom", "Hearty Mushroom"])
    print(f"This Mushroom Skewer heals {skewer.hearts} hearts! {heart}")

    skewer = Food.from_nothing(hearts=2)
    print(f"This Mushroom Skewer heals {skewer.hearts} hearts! {heart}")


main()