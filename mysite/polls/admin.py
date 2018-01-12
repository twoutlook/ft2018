from import_export import resources
from django.contrib import admin

# from .models import Question

# admin.site.register(Question)
# from django.contrib import admin

from .models import Choice, Question
from .models import Yazhu


# wny .108 not show FtDev on admin yet?
from .models import FtDev


from import_export.admin import ImportExportModelAdmin


class FtDevResource(resources.ModelResource):
    class Meta:
        model = FtDev

class FtDevAdmin(ImportExportModelAdmin):
    resource_class = FtDevResource


admin.site.register(FtDev,FtDevAdmin)





class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class YazhuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['work_date','work_prod','work_mach']}),
        ('不良', {'fields': ['rej01','rej02','rej03'], 'classes': ['collapse']}),
    ]


admin.site.register(Yazhu, YazhuAdmin)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text','question_description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
