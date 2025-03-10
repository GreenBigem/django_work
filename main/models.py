from django.db import models
from django.conf import settings
from django.utils import timezone

class Accounts(models.Model):
    user_id = models.IntegerField()
    # user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    create_date = models.DateField(default=timezone.now)
    initial_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Operations(models.Model):
    date = models.DateField(default=timezone.now)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)
    odbiorca = models.CharField(max_length=100, default='Третье лицо')


    TYPE_CHOICES = [
        ('INC', 'Доход'), # Income
        ('EXP', 'Расход'), # Expense
        ('TRA', 'Перевод'), # Transfer
    ]

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name

class Income_Types(models.Model):

    TYPE_CHOICES = [
        ('PRE', 'Аванс (Prepayment)'),
        ('BON', 'Премия (Bonus)'),
        ('ANO', 'Иное (Another)'),
    ]

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)

class Expense_Types(models.Model):

    TYPE_CHOICES = [
        ('SAL', 'Зарплата'), # Salary
        ('BON', 'Премия'), # Bonus
        ('CPA', 'Выплата подрядчику'), # Payment to the contractor
        ('PMA', 'Покупка материалов'), # Purchase of materials
        ('PEQ', 'Покупка оборудования'), # Purchase of equipment
        ('REP', 'Представительские'), # Representative expenses
    ]

    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
