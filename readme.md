# DJANGO-WITH-ME

A small Django project (learning / demo) containing a Django project (`myproject`) and an app called `paras`.

This README explains how to set up the project on Windows (PowerShell), run it locally, and where to find important files.

## Quick summary
- Framework: Django
- Database: SQLite (`db.sqlite3`)
- App: `paras`
- Templates: `templates/` (contains `index.html`)
- Media: `media/` (images)

## Prerequisites
- Python 3.8+ (use the version you prefer)
- Git (optional, for cloning and version control)

This repository already includes a virtual environment in `env/`. You may use that, or create a fresh virtual environment.

## Setup (PowerShell)

Below are commands you can run in Windows PowerShell. Adjust paths and Python executable as needed.

1. (Optional) If you want a fresh virtual environment instead of the included `env/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. If you're using the included `env/`, activate it:

```powershell
.\env\Scripts\Activate.ps1
```

3. Install dependencies

If the project has a `requirements.txt`, run:

```powershell
pip install -r requirements.txt
```

If there is no `requirements.txt`, at minimum install Django (version pinned in the provided virtualenv):

```powershell
pip install django
```

4. Apply database migrations

```powershell
python manage.py migrate
```

5. Create a superuser (optional, to access the admin)

```powershell
python manage.py createsuperuser
```

6. Run the development server

```powershell
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Project layout (important files)

- `manage.py` — Django management wrapper
- `db.sqlite3` — SQLite database file (development)
- `myproject/` — Django project settings and WSGI/ASGI
	- `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`
- `paras/` — Django app (models, views, urls, admin)
- `templates/` — HTML templates (e.g., `index.html`)
- `static/` — static files (CSS in `static/css/style.css`)
- `media/` — user-uploaded files, images

## Common commands

- Check current status:

```powershell
git status
```

- Create and switch to a new branch:

```powershell
git checkout -b feature/my-branch
# or
git switch -c feature/my-branch
```

- Run tests (if any):

```powershell
python manage.py test
```

## Notes & troubleshooting

- If you see import errors, make sure the correct virtual environment is activated.
- If the DB schema is out-of-sync, run `python manage.py migrate` and `python manage.py makemigrations` as needed.
- If static files are not loading in production, remember to run `collectstatic` and configure your web server.

## Contribution

If you plan to contribute:

1. Create a branch: `git checkout -b feature/your-change`
2. Make changes and run tests
3. Commit and push: `git push -u origin feature/your-change`
4. Open a PR describing your change

## License

Choose and add a license (e.g., MIT) or contact the repository owner for license details.

---

If you want, I can:
- add a `requirements.txt` with the current environment's packages,
- create a `.gitignore` (if missing) for `env/`, `db.sqlite3`, `__pycache__/`, and `media/`,
- or commit this README directly into the repository. Tell me which you'd like me to do next.
a