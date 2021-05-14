"""Forms"""

from dataclasses import dataclass

from django import forms
from django.core.exceptions import ValidationError


@dataclass
class Meal:
    """Meal"""

    key: str
    name: str
    people_served: int = 1
    contains_meat: bool = False
    contains_dairy: bool = False
    contains_other_animal_products: bool = False


MEALS = [
    Meal("whole-chicken", "Whole Chicken", 4, contains_meat=True),
    Meal("half-chicken", "Half Chicken", 2, contains_meat=True),
    Meal("roast-cauliflower", "Roast Cauliflower", 2),
    Meal("large-veg-pizza", "Large Vegetarian Pizza", 3, contains_dairy=True),
    Meal(
        "large-meat-pizza",
        "Large Pepperoni Pizza",
        3,
        contains_meat=True,
        contains_dairy=True,
    ),
    Meal("small-veg-pizza", "Small Vegetarian Pizza", 1, contains_dairy=True),
    Meal(
        "small-meat-pizza",
        "Small Pepperoni Pizza",
        1,
        contains_meat=True,
        contains_dairy=True,
    ),
    Meal("greek-salad", "Greek Salad", 1, contains_dairy=True),
    Meal("scrambled-eggs", "Scrambled Eggs", 2, contains_other_animal_products=True),
    Meal("garden-salad", "Garden Salad"),
    Meal("tomato-soup", "Tomato Soup"),
]


class OrderMealForm(forms.Form):
    """Order meal form."""

    meal = forms.ChoiceField(
        choices=[(None, "---")]
        + [(meal.key, f"{meal.name} (serves {meal.people_served})") for meal in MEALS]
    )
    num_people = forms.IntegerField(min_value=1, max_value=6, initial=1)
    vegetarian = forms.BooleanField(required=False)
    vegan = forms.BooleanField(required=False)
    lactose_intolerant = forms.BooleanField(required=False)

    def clean(self):
        """Validate a meal order."""

        super().clean()

        meals_by_key = {meal.key: meal for meal in MEALS}
        meal = meals_by_key[self.cleaned_data["meal"]]

        if self.cleaned_data["vegetarian"] and meal.contains_meat:
            self.add_error(
                "meal",
                ValidationError(
                    "Meal not suitable for vegetarians.", code="vegetarian"
                ),
            )

        if self.cleaned_data["lactose_intolerant"] and meal.contains_dairy:
            self.add_error(
                "meal",
                ValidationError(
                    "Meal not suitable for lactose intolerant people.",
                    code="lactose_intolerant",
                ),
            )

        if (
            self.cleaned_data["vegan"]
            and meal.contains_meat
            or meal.contains_dairy
            or meal.contains_other_animal_products
        ):
            self.add_error(
                "meal", ValidationError("Meal not suitable for vegans.", code="vegan")
            )

        if self.cleaned_data["num_people"] % meal.people_served:
            self.add_error(
                "num_people",
                ValidationError(
                    "Invalid number of people for the selected meal.", code="num_people"
                ),
            )
