from .models import Products
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    type = filters.ChoiceFilter(choices=Products.TYPE_CHOICES)

    subcategory = filters.CharFilter(field_name='subcategories__id', lookup_expr='exact')
    category = filters.CharFilter(field_name='category__id',
                                  lookup_expr='exact')

    tag = filters.CharFilter(field_name='tags__id', lookup_expr='exact')

    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    sort = filters.OrderingFilter(
        fields=(
            ('create_date', 'newest'),
            ('-create_date', 'oldest'),
        ),
    )

    class Meta:
        model = Products
        fields = ['type', 'subcategory', 'category', 'tag', 'name', 'sort']
