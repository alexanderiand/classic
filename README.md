## Classic blog site

> **classic** - classic blog site
>> Implemented everything that is inherent in the site:
> - Main page, with all publications
> - Categories of publications
> - View single article, article by category, view article by tag
> - Top publications
> - Tag cloud
> - Search
> - Search result
> - Registration, authorization, exit, user rights
> - Pagination
> - Admin (Django)
> - url: `http:localhost:8000/admin`
> - customized
> - the ability to add, view, edit, and delete categories
> - the ability to add, view, edit, and delete publications
> - the ability to add, view, edit, and delete tags
> - Caching

## Deploy

**Installing dependencies from requirements.txt**

`pip install -r requirements.txt`

**Migrations**

`python3 manage.py migrate `

**Create a site administrator**

`python3 manage.py createsuperuser`

`username: `

`email: `

`password:  `

**Run server**

`python3 manage.py runserver`

## Tech Stack

+ Python
+ Django
+ PostgreSQL
+ html, css (bootstrap), and js