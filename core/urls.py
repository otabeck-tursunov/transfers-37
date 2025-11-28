from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:pk>/details/', ClubDetailsView.as_view(), name='club-details'),
    path('about/', AboutView.as_view(), name='about'),
    path('latest-transfers/', LatestTransfersView.as_view(), name='latest-transfers'),
    path('players/', PlayersView.as_view(), name='players'),
    path('u-20-players/', U20PlayersView.as_view(), name='u-20-players'),
    path('statistics/', StatisticsView.as_view(), name='stats'),
    path('top-150-accurate-predictions/', Top150AccuratePredictions.as_view(), name='top-150-accurate-predictions'),
    path('top-50-clubs-by-expenditure/', Top50ClubsByExpenditure.as_view(), name='top-50-clubs-by-expenditure'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
