from django.contrib import admin
from .models import *


#  
#  configuring the display
#  

# usr_id, name, email, programming_lang, mast
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('usr_id', 'name', 'mast')
    list_display_links = ('usr_id', 'name')
    search_fields = ('usr_id', 'programming_lang')
    list_editable = ('mast',)
    list_filter = ('mast',)

class QuizAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_text', 'questioner_name')
    list_display_links = ('question_id', 'question_text', 'questioner_name')
    search_fields = ('question_id', 'question_text', 'questioner_name')

#  
#  Register model
#  

admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Quiz, QuizAdmin)