from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('auth/', include('apps.account.urls_auth')),
    path('users/', include('apps.account.urls')),

    path('categories/', include('apps.titles.urls.category')),
    path('titles/', include('apps.titles.urls.titles')),
    path('genres/', include('apps.titles.urls.genre')),
]
