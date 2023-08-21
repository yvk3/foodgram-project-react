from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientAmount, Recipe,
                     ShoppingCart, Tag)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """Модель админа для ингредиентов."""
    list_display = ('name', 'measurement_unit')
    list_filter = ('name',)


class IngredientsInline(admin.TabularInline):
    model = IngredientAmount
    extra = 1


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Модель теги."""
    list_display = ('id', 'name', 'color', 'slug')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Модель админа для рецептов."""
    list_display = ('name', 'author', 'text', 'added_to_favorite')
    list_filter = ('author', 'name', 'tags')
    inlines = (IngredientsInline,)

    @staticmethod
    def added_to_favorite(obj):
        return obj.favorite.count()


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    """Модель админа для избранного."""
    list_display = ('id', 'recipe', 'user')


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    """Модель админа корзины."""
    list_display = ('id', 'recipe', 'user')


@admin.register(IngredientAmount)
class IngredientAmountAdmin(admin.ModelAdmin):
    list_display = ('id', 'ingredient', 'recipe', 'amount')
