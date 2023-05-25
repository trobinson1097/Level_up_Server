from rest_framework import routers
from levelupapi.views import GameTypeView, EventView, GameView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user

router = routers.DefaultRouter(trailing_slash=False) 
# ^ tells the router to accept /gametypes instead of /gametypes/
router.register(r'game_types', GameTypeView, 'game_type')
router.register(r'events', EventView, 'event')
router.register(r'games', GameView, 'game')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('levelupreports.urls')),
]