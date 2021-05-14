"""Test the order meal form."""

# pylint: disable=undefined-variable

import pytest

from blog_demo_django_app.forms import MEALS, OrderMealForm


def error_codes_from_form(form):
    """Get all error codes from a form."""

    for _, field_error_data in form.errors.as_data().items():
        yield from [e.code for e in field_error_data]


@pytest.mark.parametrize("meal", [meal.key for meal in MEALS if not meal.contains_meat])
def test_valid_for_vegetarian(meal):
    """Test meals which are valid for vegetarians."""

    form = OrderMealForm(data={"vegetarian": True, "meal": meal, "num_people": 1})
    assert "vegetarian" not in error_codes_from_form(form)


@pytest.mark.parametrize("meal", [meal.key for meal in MEALS if meal.contains_meat])
def test_invalid_for_vegetarian(meal):
    """Test meals which are invalid for vegetarians."""

    form = OrderMealForm(data={"vegetarian": True, "meal": meal, "num_people": 1})
    assert "vegetarian" in error_codes_from_form(form)


@pytest.mark.parametrize(
    "meal", [meal.key for meal in MEALS if not meal.contains_dairy]
)
def test_valid_for_lactose_intolerant(meal):
    """Test meals which are valid for lactose intolerant people."""

    form = OrderMealForm(
        data={"lactose_intolerant": True, "meal": meal, "num_people": 1}
    )
    assert "lactose_intolerant" not in error_codes_from_form(form)


@pytest.mark.parametrize("meal", [meal.key for meal in MEALS if meal.contains_dairy])
def test_invalid_for_lactose_intolerant(meal):
    """Test meals which are invalid for lactose intolerant people."""

    form = OrderMealForm(
        data={"lactose_intolerant": True, "meal": meal, "num_people": 1}
    )
    assert "lactose_intolerant" in error_codes_from_form(form)


@pytest.mark.parametrize(
    "meal",
    [
        meal.key
        for meal in MEALS
        if not meal.contains_meat
        and not meal.contains_dairy
        and not meal.contains_other_animal_products
    ],
)
def test_valid_for_vegan(meal):
    """Test meals which are valid for vegans."""

    form = OrderMealForm(data={"vegan": True, "meal": meal, "num_people": 1})
    assert "vegan" not in error_codes_from_form(form)


@pytest.mark.parametrize(
    "meal",
    [
        meal.key
        for meal in MEALS
        if meal.contains_meat
        or meal.contains_dairy
        or meal.contains_other_animal_products
    ],
)
def test_invalid_for_vegan(meal):
    """Test meals which are invalid for vegans."""

    form = OrderMealForm(data={"vegan": True, "meal": meal, "num_people": 1})
    assert "vegan" in error_codes_from_form(form)


def valid_meal_num_people_combos():
    """Get valid meal-number of people combinations."""

    for meal in MEALS:
        for num_people in range(1, 7):
            if num_people % meal.people_served == 0:
                yield (meal.key, num_people)


@pytest.mark.parametrize("meal, num_people", valid_meal_num_people_combos())
def test_valid_num_people(meal, num_people):
    """Test valid numbers of people."""

    form = OrderMealForm(data={"num_people": num_people, "meal": meal})
    assert "num_people" not in error_codes_from_form(form)


def invalid_meal_num_people_combos():
    """Get invalid meal-number of people combinations."""

    for meal in MEALS:
        for num_people in range(1, 7):
            if num_people % meal.people_served:
                yield (meal.key, num_people)


@pytest.mark.parametrize("meal, num_people", invalid_meal_num_people_combos())
def test_invalid_num_people(meal, num_people):
    """Test invalid numbers of people."""

    form = OrderMealForm(data={"num_people": num_people, "meal": meal})
    assert "num_people" in error_codes_from_form(form)
