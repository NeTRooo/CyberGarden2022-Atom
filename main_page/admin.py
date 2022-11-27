from django.contrib import admin
from .models import UserInfo

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

#  
#  Register model
#  

admin.site.register(UserInfo, UserInfoAdmin)