from .models import Cat # Замените MyModel
from import_export import resources # type: ignore


class CatResource(resources.ModelResource):
    """
    Resource for importing and exporting Cat model data using django-import-export.
    """

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
        ) # Specify fields to import/export. Include all relevant fields.
        import_id_fields = ('id',)  # Fields used to identify existing instances during import
        skip_unchanged = True  # Skip rows where data hasn't changed during import
        report_skipped = True  # Report skipped rows during import
        clean_model_instances = True # Clean the model instance before saving
        use_bulk = True #Use bulk_create/bulk_update for performance boost
        batch_size = 1000 #Process objects in batches during import for better memory management.