python -m venv venv
.\venv\Scripts\activate
pip install django

django-admin startproject questbooking
cd questbooking
python manage.py startapp quest

Добавить quest в settings в INSALLED_APPS
Туда же добавить 

LOGIN_REDIRECT_URL = 'base'
LOGIN_URL = '/login/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


Написать файлик для создания бд(main.py)
Убрать из sql кода все лишнее:

ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

Курглые скобки после current_timestamp() чтобы стало current_timestamp

Все timestamp заменить на datetime(но current_timestamp отсается как есть)

Все поля с id заменить на такие:
`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT

Запустить main.py
Полученную базу данных положить в папку проекта рядом с manage.py

С settings.py поменять название базы данных 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'quest.db',
    }
}

Выполнить команду
python manage.py inspectdb | out-file "models.py" -encoding utf8 
Так сложно чтобы не было той ошибки на нулевые байты
Полученный файл models.py поместить на место models.py в папке приложения quest

Если запомнить не удается, то python manage.py inspectdb и скопировать вывод из терминала


Теперь менять models.py
У всех полей, у которых был current_timestamp добавить в скобках auto_now_add=True

Все поля с id заменить на ForeignKey
До:
    user_id = models.IntegerField()
После:
    user = models.ForeignKey('User', on_delete=models.CASCADE)



Юзера сделать наследником AbstractUser из django.contrib.auth.models
Добавить ему 
username = models.CharField(max_length=20, blank=True)
REQUIRED_FIELDS = ['full_name', 'phone', 'email', 'password', 'username']
USERNAME_FIELD = 'login'
У Login добавить unique=True

Убрать весь класс мета Юзеру

В настройках указать
AUTH_USER_MODEL = 'quest.User' 

Можно даже название на CustomUser не менять


Всем моедлям сделать метод str

python manage.py makemigrations
python manage.py migrate

Дальше создать суперпользователя
python manage.py createsuperuser
Но первый пользователь будет с id 1, что не соответствует базе данных
Поэтому надо трижды запустить эту команду и ввести пользователей по порядку из sql файла
Потом зайти в админку и у первых двух пользователей убрать галочку superuser status и staff status

Дальше как обычно написать авторизацию и регистрацию - темплейты, base, views, urls и forms
В главные url Добавить эти url и urls на медию
Потом написать функцию index и добавить ее в urls с name='base'
И проверить, что все работает

Пустая страница для незарегистрированного тут даже не нужна

Добавить форму на букинг и две вьюшки - на просмотр и на создание
