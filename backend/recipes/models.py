from django.core import validators
from django.db import models
from django.db.models import Exists, OuterRef
from users.models import User


class Ingredient(models.Model):
    """Модель ингредиентов."""
    name = models.CharField(
        blank=False,
        max_length=150,
        verbose_name='Название ингредиента',
    )
    measurement_unit = models.CharField(
        blank=False,
        max_length=150,
        verbose_name='Единица измерения',
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return f'{self.name}, {self.measurement_unit}'


class Tag(models.Model):
    """Тег модель."""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название тега',
        validators=(
            validators.RegexValidator(
                regex=r'[а-яА-Я]',
                message='Проверьте вводимый формат',
            ),
        ),
        help_text='Название тега, только русские буквы.',
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        verbose_name='Цвет тега (HEX code)',
        help_text='Цвет тега (HEX code), пример - #49B64E',
        validators=(
            validators.RegexValidator(
                regex="^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                message='Проверьте вводимый формат',
            ),
        )
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='Слаг тега',
        validators=(
            validators.MinLengthValidator(3, 'Не менее трех символов'),
        )
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class RecipeQuerySet(models.QuerySet):
    """Модель поиска рецептов."""

    def filter_tags(self, tags):
        if tags:
            return self.filter(tags__slug__in=tags).distinct()
        return self

    def add_user_annotations(self, user_id):
        return self.annotate(
            is_favorited=Exists(
                Favorite.objects.filter(
                    recipe__pk=OuterRef('pk'),
                    user_id=user_id,
                )
            ),
            is_in_shopping_cart=Exists(
                ShoppingCart.objects.filter(
                    recipe__pk=OuterRef('pk'),
                    user_id=user_id,
                )
            ),
        )


class Recipe(models.Model):
    """Модель рецептов."""
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта',
    )
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название рецепта',
    )
    image = models.ImageField(
        blank=True,
        upload_to='recipes/',
        verbose_name='Фотография',
    )
    text = models.TextField(
        verbose_name='Опишите порядок приготовления',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='IngredientAmount',
        related_name='recipes',
        verbose_name='Ингредиенты для блюда',
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='recipes',
        verbose_name='Тег',
    )
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name='Время приготовления',
        help_text='время приготовления в минутах',
        validators=(
            validators.MinValueValidator(
                1, 'Время приготовления не может быть меньше "1"'),
        )
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    objects = RecipeQuerySet.as_manager()

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    """Модель количество ингредиентов."""
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='ingredients_amount',
        verbose_name='Ингредиент',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amount',
        verbose_name='Рецепт',
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name='Количество ингредиента в рецепте',
        default=1,
        validators=(
            validators.MinValueValidator(1, 'Минимальное значение: 1'),
            validators.MaxValueValidator(9999, 'Максимальное значение: 9999'),
            validators.RegexValidator(
                '^[0-9]+$',
                (
                    'Количество ингредиента может быть '
                    'целым числом от 1 до 9999'
                )
            ),
        ),
    )

    class Meta:
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'

    def __str__(self):
        return f'{self.ingredient}: {self.amount}'


class Favorite(models.Model):
    """Модель избранное."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Рецепт',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'


class ShoppingCart(models.Model):
    """Модель для листа покупок."""
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Рецепт',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь',
    )

    class Meta:
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
        # constraints = [
        #     UniqueConstraint(
        #         fields=['user', 'recipe'],
        #         name='unique_shopingcart'
        #     )
        # ]
