from django.contrib import admin
from django.urls import path
from django.urls.conf import include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructors/', include('apps.instructor.urls') ),
    path('members/', include('apps.member.urls')),
    path('payments/', include('apps.payment.urls')),
    path('users/', include('apps.user.urls')),
    path('workouts/', include('apps.workout.urls')),
]
