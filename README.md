# 2024-dj-blog-clone-medium
Based on: https://github.com/hakanyalcinkayadev/Uctan-Uca-Projelerle-Sifirdan-Full-Stack-Python-ve-Django-Egitimi
MyGihub: https://github.com/gurnitha/2024-dj-blog-clone-medium


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


      






















