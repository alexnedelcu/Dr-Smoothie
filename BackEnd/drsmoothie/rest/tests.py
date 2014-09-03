"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from .models import *

class NutrientTestCase(TestCase):
    def setUp(self):
        Nutrient.objects.create(id=“nys26”,name=“Vitamin C”, unit=“mg”, decimals=“12”)
        Nutrient.objects.create(id=“nys226”,name=“Vitamin D”, unit=“mg”, decimals=“12”)

    def test_nutrient_works(self):
        VitaminC = Nutrient.objects.get(name=“Vitamin C”)
        VitaminD = Nutrient.objects.get(name=“Vitamin D”)
        self.assertEqual(VitaminC.name, “Vitamin C”)
        self.assertEqual(VitaminD.name, “Vitamin D”)

class IngrdientTypeTestCase(TestCase):
    def setUp(self):
        IngredientType.objects.create(id=“001”, type=“Fruit”)
        IngredientType.objects.create(id=“002”, type=“Nuts”)

    def test_ingredient_works(self):
        Fruit = IngredientType.objects.get(id=“001”)
        Nuts = IngredientType.objects.get(name=“002”)
        self.assertEqual(Fruits.type, “Fruit”)
        self.assertEqual(Nuts.type, “Nuts”)

class IngrdientTestCase(TestCase):
    def setUp(self):
        Ingredient.objects.create(id=“001”,name=“Mango”, type=“Fruit”)
        Ingredient.objects.create(id=“002”,name=“Banana”, type=“Fruit”)

    def test_ingredient_works(self):
        Mango = Ingredient.objects.get(id=“001”)
        Banana = Ingredient.objects.get(name=“002”)
        self.assertEqual(Mango.name, “Mango”)
        self.assertEqual(Banana.name, “Banana”)

class PortionTestCase(TestCase):
    def setUp(self):
        Portion.objects.create(id=“001”, description=“Fruit”)
        Portion.objects.create(id=“002”, description =“Nuts”)

    def test_ingredient_works(self):
        Fruit = Portion.objects.get(id=“001”)
        Nuts = Portion.objects.get(name=“002”)
        self.assertEqual(Fruits.description, “Fruit”)
        self.assertEqual(Nuts.description, “Nuts”)

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(id=“nys26”)
        User.objects.create(id=“002”, description =“Nuts”)

    def test_ingredient_works(self):
        nys26 = Uder.objects.get(id=“nys26”)
        nys226 = Portion.objects.get(name=“nys226”)
        self.assertEqual(nys26.id, “nys26”)
        self.assertEqual(nys226.id, “nys226”)

class RecipeTestCase(TestCase):
    def setUp(self):
        Recipe.objects.create(name=“Nish Shah”, user=“nys26”)
        Recipe.objects.create(name=“Nish2 Shah”, user=“nys226”)

    def test_ingredient_works(self):
        nys26 = Recipe.objects.get(id=“nys26”)
        nys226 = Recipe.objects.get(id=“nys226”)
        self.assertEqual(nys26.name, “nys26”)
        self.assertEqual(nys226.name, “nys226”)



