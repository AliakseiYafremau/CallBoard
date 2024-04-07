import django_filters
from django_filters import FilterSet, OrderingFilter
from django import forms
from .models import Comment


class CommentFilter(FilterSet):
    data_of_creation = django_filters.DateTimeFilter(
        field_name='data_of_creation',
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        lookup_expr='date'
    )

    data_of_creation__gt = django_filters.DateTimeFilter(
        field_name='data_of_creation',
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        lookup_expr='date__gt'
    )

    data_of_creation__lt = django_filters.DateTimeFilter(
        field_name='data_of_creation',
        widget=forms.DateTimeInput(attrs={'type': 'date'}),
        lookup_expr='date__lt'
    )

    o = OrderingFilter(
        fields=(
            ('user__username', 'Username'),
            ('data_of_creation', 'Date'),
        ),
    )

    class Meta:
        model = Comment
        fields = {
            'text': ['icontains'],
        }