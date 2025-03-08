from rest_framework import serializers
import base64
from .models import Cat
from django.core.files.base import ContentFile


class Base64ImageField(serializers.ImageField):
    """
    Пользовательское поле сериализатора для обработки изображений в кодировке Base64.
    """

    def to_internal_value(self, data):
        # Если полученный объект строка, и эта строка 
        # начинается с 'data:image'...
        if isinstance(data, str) and data.startswith('data:image'):
            try:
                # ...начинаем декодировать изображение из base64.
                # Сначала нужно разделить строку на части.
                format, imgstr = data.split(';base64,')  
                # И извлечь расширение файла.
                ext = format.split('/')[-1]  
                # Затем декодировать сами данные и поместить результат в файл,
                # которому дать название по шаблону.
                data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
            except (ValueError, TypeError, IndexError):
                raise serializers.ValidationError(("Invalid Base64 image data"))
        return super().to_internal_value(data)


class CatSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Cat.
    """

    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Cat
        fields = (
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
        read_only_fields = ('id',)
    
    def validate_breed(self, value):
        """
        Custom validation for the breed field.
        """
        if not isinstance(value, str) or len(value) > 56:  # Example validation
            raise serializers.ValidationError(("Название должно быть строкой и содержать не более 128 символов."))
        return value