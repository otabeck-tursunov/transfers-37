from .models import Country
from django.db.models import Count, ExpressionWrapper, PositiveSmallIntegerField


def get_countries(request):
    countries = Country.objects.annotate(
        clubs_count=ExpressionWrapper(
            Count('club'),
            output_field=PositiveSmallIntegerField()
        )
    ).order_by('-clubs_count')

    left_countries = []
    right_countries = []
    for i in range(len(countries)):
        if i % 2 == 0:
            left_countries.append(countries[i])
        else:
            right_countries.append(countries[i])

    context = {
        'left_countries': left_countries,
        'right_countries': right_countries,
    }
    return context
