from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Cooksignupfunc, Cookloginfunc, Cooklogoutfunc, Cooklistfunc, Cookdetailfunc, CookCreate, CookDelete, CookEdit, AccountRegistration

urlpatterns = [
    path('registration', AccountRegistration.as_view(), name='registration'),
    path('admin/', admin.site.urls),
    path('signup/', Cooksignupfunc, name= 'signup'),
    path('', Cookloginfunc, name = 'login'),
    path('logout/', Cooklogoutfunc, name = 'logout'),
    path('list/', Cooklistfunc, name = 'list'),
    path('detail/<int:pk>/', Cookdetailfunc, name = 'detail'),
    path('create/', CookCreate.as_view(), name='create'),
    path('delete/<int:pk>/', CookDelete.as_view(), name='delete'),
    path('edit/<int:pk>/', CookEdit.as_view(), name='edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)