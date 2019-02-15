from django.contrib import admin
# from survey_app.models import survey
from survey_app.models import survey
from survey_app.models import UserProfileInfo

# Register your models here.
admin.site.register(survey)
admin.site.register(UserProfileInfo)
