from django.contrib import admin
from .models import Cat
from .resources import CatResource
from import_export.admin import ImportExportModelAdmin # type: ignore


@admin.register(Cat)
class CatAdmin(ImportExportModelAdmin):
    """
    Настройка администратора для модели Cat, включая функции импорта/экспорта.
    """
    resource_class = CatResource
    list_display = (
        'id', 
        'breed', 
        'life_expectancy', 
        'cat_size', 
        'weight_of_the_cat', 
        'cat_size_1', 
        'care', 
        'personality', 
        'activity', 
        'image', 
        'Wool', 
        'Molting', 
        'Attitude_towards_children', 
        'Attitude_towards_other_animals', 
        'The_level_of_intelligence', 
        'The_need_for_attention', 
        'Nutrition_features'
    )
    
    search_fields = ('breed', 'personality')