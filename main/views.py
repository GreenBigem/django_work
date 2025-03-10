from django.core.validators import validate_email
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Accounts, Operations


def index(request):
    return render(request, 'index/index.html')

def finance(request):
    #User.objects.get(username=the_username).pk
    all_user_accounts = Accounts.objects.filter(user_id = 1)
    all_user_operations = get_all_operations(request)
    return render(request, 'index/finance.html', {'all_user_accounts': all_user_accounts, 'all_user_operations' : all_user_operations})

def account_create(request):
    if request.method == 'POST':
        HttpResponse(f'{request.POST.get('name')}')
        new_account = Accounts(name = request.POST.get('name'))

        new_account.user_id = 1
        new_account.save()
        return redirect(finance)
    else: return HttpResponse(f'Аккаунт не удалось создать')

def accounts(request):
    all_user_accounts = get_object_or_404(Accounts, user_id = 1)
    return all_user_accounts

def operation_create(request):
    if request.method == 'POST':
        new_operation = Operations(
            name = request.POST.get('name'),
            date = request.POST.get('date'),
            account=request.POST.get('account'),
            # account = Accounts.objects.get(name='dsad'),
            value = request.POST.get('value'),
            odbiorca = request.POST.get('odbiorca'),
            type = 'INC'
        )

        new_operation.user_id = 1
        new_operation.save()
        return redirect(finance)
    else: return HttpResponse(f'Операцию не удалось создать')

def get_all_operations(request):
    all_user_operations = Operations.objects.all()
    return all_user_operations

def operation_delete(request, id):
    if True:
        Operations.objects.filter(id=id).delete()
        return redirect(finance)
    else: return HttpResponse(f'Операцию не удалось удалить')
