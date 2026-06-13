from django.db import models

class MonthPlan(models.Model):
    month = models.CharField(max_length=7)
    plan_sales = models.BigIntegerField(default=0)
    plan_leads = models.IntegerField(default=0)
    work_days = models.IntegerField(default=26)
    passed_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-month']
        verbose_name = 'План месяца'
        verbose_name_plural = 'Планы месяцев'

    def __str__(self):
        return f"План {self.month}"


class DailyRecord(models.Model):
    month_plan = models.ForeignKey(MonthPlan, on_delete=models.CASCADE, related_name='daily_records')
    day_number = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    sales = models.BigIntegerField(default=0)
    leads = models.IntegerField(default=0)
    deals = models.IntegerField(default=0)
    spend = models.BigIntegerField(default=0)
    comment = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['day_number']
        verbose_name = 'Дневная запись'
        verbose_name_plural = 'Дневные записи'

    def __str__(self):
        return f"День {self.day_number} ({self.date})"