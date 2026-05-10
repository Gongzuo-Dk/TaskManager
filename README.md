# TaskManager

A full-featured task management web application built with Django and PostgreSQL.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Django](https://img.shields.io/badge/Django-6.0-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

## Live Demo

🔗 [TaskManager on Railway](https://web-production-f102b.up.railway.app/)

## About

TaskManager is a personal productivity app that lets users manage their daily tasks with smart filtering, category organization, and priority tagging. Built as a portfolio project to demonstrate backend development skills with Django, PostgreSQL, and deployment.

## Features

- **Authentication** — Register, login, logout, and password change
- **Task CRUD** — Create, edit, delete, and complete tasks
- **Smart filtering** — Tasks automatically grouped into Overdue, Today, Next 7 Days, Later, and No Date sections
- **Category system** — Create custom categories and pin them to the sidebar for quick access
- **Priority tagging** — Tag tasks as High, Medium, or Low priority
- **Search** — Search tasks by title, content, category, or priority
- **User profiles** — Upload a custom avatar
- **Ownership protection** — Users can only access and modify their own data

## Tech Stack

- **Backend** — Python, Django
- **Database** — PostgreSQL
- **Frontend** — Bootstrap 5, custom CSS
- **Deployment** — Railway
- **Auth** — Django's built-in authentication system

## Project Structure

```
TaskManager/          # Project settings and root URLs
task_manager/         # Core app — tasks, categories, views
accounts/             # Auth app — user profiles, signals
templates/            # Project-level base template and error pages
static/               # CSS, JS, images
```

## Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/Gongzuo-Dk/TaskManager.git
cd TaskManager  

```

**2. Create and activate virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Create a `.env` file in the project root**
```
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

**5. Set up the database**

Make sure PostgreSQL is running and the database exists, then:
```bash
python manage.py migrate
```

**6. Create a superuser**
```bash
python manage.py createsuperuser
```

**7. Run the development server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## Key Implementation Details

- **Signals** — `post_save` signal automatically creates a `Profile` whenever a new `User` is registered
- **Context processors** — Pinned categories are injected into every template globally without passing them from each view individually
- **Ownership checks** — Every view that modifies data verifies `task.user == request.user` before proceeding
- **Environment variables** — All secrets and environment-specific config managed via `python-decouple`
- **Static files** — Served in production via WhiteNoise

## Screenshots

> _Add screenshots here_

