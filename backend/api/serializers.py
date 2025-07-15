from rest_framework.fields import empty
from rest_framework.serializers import ModelSerializer

class ReadOnlyModelSerializer(ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        for field in fields:
            fields[field].read_only = True
        return fields
    
class CustomKwargsMixin(ModelSerializer):
    def __init__(self, instance=None, data=..., *args, custom_kwargs=None, **kwargs):
        #for some fucking reason works only with BaseManager as instance and many=True, so us filter()
        #custom_kwargs SHOULD NOT BE EMPTY
        self.custom_kwargs: dict = custom_kwargs
        super().__init__(instance, data, **kwargs)