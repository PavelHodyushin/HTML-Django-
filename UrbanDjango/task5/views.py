from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = request.POST.get('name')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            age = request.POST.get('age')
            return HttpResponse(f'Добро пожаловать, {username}')
            form.save()
    else:
        form = UserRegistrationForm()
    return render(request, 'fifth_task/registration_page.html', {'form': form})

users = ['user1', 'user2', 'user3','user4', 'user5', 'user6']

def sign_up_by_html(request):

    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')

        print(f"Имя: {username}")
        print(f"Почтовый адрес: {email}")
        print(f"Возраст: {age}")
        print(f"password: {password}")
        print(f"repeat_password: {repeat_password}")



        if password != repeat_password:
            return HttpResponse('Пароли не совпадают! Заполните форму повторно')
        else:
            for i in users:
                if i == username:
                    return HttpResponse('Пользователь с таким login уже существует!')
        return HttpResponse(f'Успешная регистрация! Приветствуем, {username}')


    return render(request, 'fifth_task/registration_page.html')
