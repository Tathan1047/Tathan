from django.contrib import admin

from apps.student.models import Student, Documenttype


class AdminStudent(admin.ModelAdmin):
    list_display = ['code_student', 'name_student', 'lastname_student'
                    'document_type',
                    ]


class AdminDocumenttype(admin.ModelAdmin):
    list_display = []




