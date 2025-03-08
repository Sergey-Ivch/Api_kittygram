from django.db import models


class Cat(models.Model):
    """
    Представляет породу кошек со своими характерными чертами.
    """

    breed = models.CharField(max_length=56, verbose_name= ("Breed Name"))
    life_expectancy = models.CharField(max_length=56,verbose_name= ("Life Expectancy"))
    cat_size = models.CharField(max_length=56, verbose_name=("Cat Size"))
    weight_of_the_cat = models.CharField(max_length=56, verbose_name=("Weight (kg)"))
    cat_size_1 = models.CharField(max_length=56, verbose_name=("Care Instructions"))
    care = models.CharField(max_length=56, verbose_name=("Care Instructions"))
    personality = models.CharField(max_length=56, verbose_name=("Personality"))
    activity = models.CharField(max_length=56, verbose_name=("Activity Level"))
    image = models.ImageField(
        'Картинка',
        upload_to='cat_images/', #Changed to a more semantic name.  Avoid "spicok" unless it has a specific meaning.
        blank=True,
        null=True, #Added null=True to allow no image. Best practice with blank=True.
        help_text=("Загрузите репрезентативное изображение породы.")
    )

    Wool = models.CharField(max_length=56, verbose_name=("Wool Type"))
    Molting = models.CharField(max_length=56, verbose_name=("Molting Level"))
    Attitude_towards_children = models.CharField(max_length=56, verbose_name=("Attitude Towards Children"))
    Attitude_towards_other_animals = models.CharField(max_length=56, verbose_name=("Attitude Towards Other Animals"))
    The_level_of_intelligence = models.CharField(max_length=56, verbose_name=("Intelligence Level"))
    The_need_for_attention = models.CharField(max_length=56, verbose_name=("Need for Attention"))
    Nutrition_features = models.CharField(max_length=56, verbose_name=("Nutritional Features"))


    class Meta:
        verbose_name = ("Порода кошек")  # Proper singular name for admin interface
        verbose_name_plural = ("Породы кошек")  # Proper plural name
        ordering = ['breed']  # Default ordering in admin interface and queries

    def __str__(self):
        return self.breed

