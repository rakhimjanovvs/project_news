from django.shortcuts import render, redirect, get_object_or_404
from .models import News, NewsCategory
from django.urls import reverse
from .forms import RegForm, CommentForm, NewsForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
        print(request.POST)
        form = RegForm(request.POST)
        print(form.errors)
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

        context = {'form': form}
        return render(request, self.template_name, context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    login(request)
    return redirect('/')


def news_detail(request, pk):
    news_item = get_object_or_404(News, pk=pk)
    comments = news_item.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.news = news_item
                comment.author = request.user
                comment.save()
                return redirect('news_detail', pk=news_item.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'news/news_detail.html', {
        'news': news_item,
        'comments': comments,
        'form': form
    })


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})


def news_by_category(request, pk):
    category = get_object_or_404(NewsCategory, pk=pk)
    news_list = News.objects.filter(news_category=category).order_by('-added_date')
    return render(request, 'news/news_by_category.html', {
        'category': category,
        'news_list': news_list
    })