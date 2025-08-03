from django.shortcuts import render, redirect
from .models import News, NewsCategory
from .forms import RegForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.views import View

# Create your views here.
def home_page(request):
    news_category = NewsCategory.objects.all()
    news = News.objects.all()
    context = {
        'news_category': news_category,
        'news': news
    }
    return render(request, 'home.html', context)

class Register(View):
    template_name = 'registration/register.html'

    # Этап 1 - получение формы
    def get(self, request):
        context = {'form': RegForm}
        return render(request, self.template_name, context)

    # этап 2 - отправка формы в БД
    def post(self, request):
        form = RegForm(request.POST)

        if form.is_valid():
            # Достали данные которые ввел пользователь
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')

            #Создаем нового пользователя в БД
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password)
            user.save()

            # Аутентифицируем пользователя
            login(request, user)

            # Переводим на главную страницу
            return redirect('/')
