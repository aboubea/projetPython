from django.conf.urls import url
from . import views
from .views import StudentCreateView

urlpatterns = [
    url('/lycee', views.index, name='index'),
    url('lycee/<int:cursus_id>', views.detail, name='detail'),
    url('lycee/student/<int:student_id>', views.detail_student, name='detail_student'),
    url('lycee/student/create', StudentCreateView.as_view(), name='create_student'),
]
