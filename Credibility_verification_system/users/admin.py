from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Statement, Verdict
from django.template.loader import render_to_string
from django.urls import reverse
from weasyprint import HTML
from django.http import HttpResponse

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name','gender','country' ,'password')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Names', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name','username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)

class StatementAdmin(admin.ModelAdmin):
    list_display = ('statement', 'created_at', 'verdict', 'probability_percentage')

    def verdict(self, obj):
        verdict_obj = Verdict.objects.filter(statement_id=obj.id).first()
        return verdict_obj.Statement_verdict if verdict_obj else None

    def probability_percentage(self, obj):
        verdict_obj = Verdict.objects.filter(statement_id=obj.id).first()
        return "{:.2%}".format(verdict_obj.predicted_probability) if verdict_obj else None

    verdict.short_description = 'Verdict'
    probability_percentage.short_description = 'Probability (%)'
    
    actions = ['export_statements_as_pdf']

    def export_statements_as_pdf(self, request, queryset):
        html_content = render_to_string('admin/export_statements_pdf.html', {'statements': queryset})
        pdf_file = HTML(string=html_content).write_pdf()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="exported_statements.pdf"'
        response.write(pdf_file)
        return response

    export_statements_as_pdf.short_description = "Export statements as PDF"

admin.site.register(Statement, StatementAdmin)

class VerdictAdmin(admin.ModelAdmin):
    list_display = ('form_id', 'statement_id', 'Statement_verdict', 'predicted_probability')

admin.site.register(Verdict, VerdictAdmin)