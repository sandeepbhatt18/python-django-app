from django.urls import path
from . import views

app_name = 'survey_app'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('surveyform/',views.SurveyForm,name='surveyform'),
    path('tracking/',views.tracking,name='tracking'),
    path('analysis/',views.analysis,name='analysis'),

]
