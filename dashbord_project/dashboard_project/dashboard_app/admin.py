from django.contrib import admin
from .models import MonthPlan, DailyRecord

class DailyRecordInline(admin.TabularInline):
    model = DailyRecord
    extra = 0

@admin.register(MonthPlan)
class MonthPlanAdmin(admin.ModelAdmin):
    list_display = ['month', 'plan_sales', 'plan_leads', 'work_days', 'updated_at']
    inlines = [DailyRecordInline]

@admin.register(DailyRecord)
class DailyRecordAdmin(admin.ModelAdmin):
    list_display = ['month_plan', 'day_number', 'date', 'sales', 'leads', 'deals']