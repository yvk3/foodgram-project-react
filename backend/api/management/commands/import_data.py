import os
from csv import reader

from django.conf import settings
from django.core.management import BaseCommand
from recipes.models import Ingredient

DATA_PATH = os.path.join(settings.BASE_DIR, 'data')
INGREDIENTS_DATA = os.path.join(DATA_PATH, 'ingredients.csv')

class Command(BaseCommand):
    """Импорт ингредиентов из csv файла в базу"""

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Старт команды'))
        with (
            open(INGREDIENTS_DATA, 'r', encoding='UTF-8') as ingredients,
        ):
            for fields in reader(ingredients):
                if len(fields) == 2:
                    name, measurement_unit = fields
                    Ingredient.objects.get_or_create(
                        name=name,
                        measurement_unit=measurement_unit,
                    )
        self.stdout.write(self.style.SUCCESS('Данные загружены'))
