from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='absence/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('signup/', views.student_signup, name='signup'),
    path('', views.home, name='home'),
    path('my-absences/', views.my_absences, name='my_absences'),
    path('submit/', views.submit_absence, name='submit_absence'),
    path('review/', views.review_list, name='review_list'),
    path('review/<int:form_id>/', views.review_form, name='review_form'),
]

# ✅ Append static files config properly
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)