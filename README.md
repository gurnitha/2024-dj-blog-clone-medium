# 2024-dj-blog-clone-medium
Based on: https://github.com/hakanyalcinkayadev/Uctan-Uca-Projelerle-Sifirdan-Full-Stack-Python-ve-Django-Egitimi
MyGihub: https://github.com/gurnitha/2024-dj-blog-clone-medium


## 1. SETUP


#### 1. Initial setup after creating remote repository

        modified:   .gitignore
        modified:   README.md


#### 2. Created venv and install Django v5.0

        λ python -m venv venv31250 --prompt dj-cln-medium
        λ venv31250\Scripts\activate.bat
        (dj-cln-medium) λ pip install django
        ...
        (dj-cln-medium) λ python.exe -m pip install --upgrade pip
        ...
        Successfully installed pip-23.3.2


#### 3. Created django project 'config'

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 4. Created django app 'page'

        modified:   README.md
        new file:   apps/page/__init__.py
        new file:   apps/page/admin.py
        new file:   apps/page/apps.py
        new file:   apps/page/migrations/__init__.py
        new file:   apps/page/models.py
        new file:   apps/page/tests.py
        new file:   apps/page/views.py


#### 5. Registered page to config/settings.py and run check

        (dj-cln-medium) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   apps/page/apps.py
        modified:   config/settings.py


#### 6. Created home page using templates, views, and urls

        modified:   README.md
        new file:   apps/page/templates/page/home_page.html
        new file:   apps/page/urls.py
        modified:   apps/page/views.py
        modified:   config/urls.py

        :)


#### 7. Added html template to home page

        modified:   README.md
        modified:   apps/page/templates/page/home_page.html


#### 8. Setup and loaded static files

        modified:   README.md
        modified:   apps/page/templates/page/home_page.html
        modified:   config/settings.py
        new file:   config/static/css/bootstrap.min.css
        new file:   config/static/css/bootstrap.min.css.map
        new file:   config/static/css/style.css
        new file:   config/static/js/bootstrap.bundle.min.js
        new file:   config/static/js/bootstrap.bundle.min.js.map


#### 9. Template inheritance

        modified:   README.md
        new file:   apps/page/templates/page/_footer.html
        new file:   apps/page/templates/page/_hero.html
        new file:   apps/page/templates/page/_navbar.html
        new file:   apps/page/templates/page/_other_posts.html
        new file:   apps/page/templates/page/_trending.html
        new file:   apps/page/templates/page/base.html
        deleted:    apps/page/templates/page/home_page.html
        new file:   apps/page/templates/page/index.html
        modified:   apps/page/views.py

        :)


## 2. USERS


#### 1. Create app 'accounts'

        modified:   README.md
        new file:   apps/accounts/__init__.py
        new file:   apps/accounts/admin.py
        new file:   apps/accounts/apps.py
        new file:   apps/accounts/migrations/__init__.py
        new file:   apps/accounts/models.py
        new file:   apps/accounts/tests.py
        new file:   apps/accounts/views.py


#### 2. Register accounts to config/settings.py

        (dj-cln-medium) λ python manage.py check
        System check identified no issues (0 silenced).

        modified:   README.md
        modified:   apps/accounts/apps.py
        modified:   config/settings.py

        :)


#### 3. Register a new user

        modified:   README.md
        new file:   apps/accounts/forms.py
        new file:   apps/accounts/templates/accounts/base.html
        new file:   apps/accounts/templates/accounts/register.html
        new file:   apps/accounts/urls.py
        modified:   apps/accounts/views.py
        modified:   apps/page/templates/page/_navbar.html
        modified:   config/settings.py
        modified:   config/urls.py

        NOTE: Successful register a new user

        :)


#### 3. Register a new user

        modified:   apps/accounts/views.py
        new file:   apps/page/templates/page/_messages.html
        modified:   apps/page/templates/page/base.html

        NOTE: Successfully showed flash messages


#### 4. Showing error messages to unsuccessful registered user

        new file:   apps/accounts/templates/accounts/_messages.html
        modified:   apps/accounts/templates/accounts/register.html
        modified:   apps/accounts/views.py
        new file:   apps/page/templates/page/_messages.html
        modified:   apps/page/templates/page/base.html
        modified:   config/settings.py

        :)


#### 5. Logged in a registered user

        new file:   apps/accounts/templates/accounts/login.html
        modified:   apps/accounts/urls.py
        modified:   apps/accounts/views.py

        :)


#### 6. Logged out a logged in user

        modified:   README.md
        modified:   apps/accounts/urls.py
        modified:   apps/accounts/views.py

        Note: Register, login, and logout all with flash messages.

        :)


#### 7. Added menu for login, logout

        modified:   README.md
        modified:   apps/page/templates/page/_navbar.html


#### 8. Added conditional to show/hide some menus to logged in and un-login user

        modified:   README.md
        modified:   apps/page/templates/page/_navbar.html

        :)
      






















