import datetime
from django.db.models import ExpressionWrapper, F, PositiveSmallIntegerField, FloatField, Sum
from django.db.models.functions import ExtractYear, Abs
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import *


class HomeView(View):
    def get(self, request):
        return render(request, 'index.html')


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()

        country = request.GET.get('country')
        if country:
            clubs = clubs.filter(country__name=country)

        context = {
            'clubs': clubs
        }
        return render(request, 'clubs.html', context)


class ClubDetailsView(View):
    def get(self, request, pk):
        club = get_object_or_404(Club, id=pk)
        players = club.player_set.order_by('-price')
        context = {
            'club': club,
            'players': players
        }
        return render(request, 'club-details.html', context)


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class LatestTransfersView(View):
    def get(self, request):
        transfers = Transfer.objects.filter().order_by('-price')
        # season=Season.objects.last()
        context = {
            'transfers': transfers
        }
        return render(request, 'latest-transfers.html', context)


class PlayersView(View):
    def get(self, request):
        players = Player.objects.all()
        context = {
            'players': players,
        }
        return render(request, 'players.html', context)


class U20PlayersView(View):
    def get(self, request):
        now_year = int(datetime.datetime.now().year)
        players = Player.objects.annotate(
            age=ExpressionWrapper(
                now_year - ExtractYear('birth_date'),
                output_field=PositiveSmallIntegerField()
            )
        ).filter(age__lte=20).order_by('-price')
        context = {
            'players': players
        }
        return render(request, 'u-20-players.html', context)


class StatisticsView(View):
    def get(self, request):
        context = {
            'last_season': Season.objects.last()
        }
        return render(request, 'stats.html', context)


class Top150AccuratePredictions(View):
    def get(self, request):
        top_accurate_transfers = Transfer.objects.annotate(
            moa=Abs(
                (1 - F('price') / F('price_tft')) * 100
            )
        ).order_by('moa')[:150]
        context = {
            'top_accurate_transfers': top_accurate_transfers
        }
        return render(request, 'stats/top-150-accurate-predictions.html', context)


class Top50ClubsByExpenditure(View):
    def get(self, request):
        clubs = Club.objects.annotate(
            total_expense=Sum('import_transfers__price')
        ).order_by('-total_expense')[:50]
        context = {
            'last_season': Season.objects.last(),
            'clubs': clubs
        }
        return render(request, 'stats/top-50-clubs-by-expenditure.html', context)
