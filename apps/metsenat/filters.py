from django_filters.rest_framework import DjangoFilterBackend
class AllDjangoFilterBackend(DjangoFilterBackend):
    '''
    Filters DRF views by any of the objects properties.
    '''

    def get_filter_class(self, view, queryset=None):
        '''
        Return the django-filters `FilterSet` used to filter the queryset.
        '''
        filter_class = getattr(view, 'filter_class', None)
        filter_fields = getattr(view, 'filter_fields', None)

        if filter_class or filter_fields:
            return super().get_filter_class(self, view, queryset)

        class AutoFilterSet(self.default_filter_set):
            class Meta:
                model = queryset.model
                fields = []
                #fields = [field for field in queryset.model._meta.get_fields()]
                #exclude = ''

        return AutoFilterSet