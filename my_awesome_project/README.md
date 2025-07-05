# My_awesome_project

A modern Django project generated with [modern-django-starter](https://github.com/CasualEngineerZombie/modern-django-starter).

## Features

- **Django 5.1** - Latest Django framework
- **HTMX** - Dynamic HTML updates without JavaScript
- **Alpine.js** - Lightweight JavaScript framework
- **TailwindCSS + DaisyUI** - Utility-first CSS framework with beautiful components
- **Django Allauth** - Comprehensive authentication system
- **HyperScript** - Easy DOM manipulation
- **PostgreSQL 16** - Advanced database system
- **Docker Support** - Containerized development and deployment
- **Django REST Framework** - Powerful API development
- **Celery** - Asynchronous task processing
- **Sentry** - Error tracking and performance monitoring
- **Vite** - Modern frontend build pipeline

## Quick Start

### Using Docker (Recommended)

1. **Clone and setup**:
   ```bash
   cd my_awesome_project
   cp .env.example .env
   # Edit .env with your configuration
   ```

2. **Build and run**:
   ```bash
   docker-compose up -d
   ```

3. **Run migrations**:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create superuser**:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Visit your application**:
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

### Manual Setup

1. **Create virtual environment**:
   ```bash
   cd my_awesome_project
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment configuration**:
   ```bash
   cp .env.example .env
   # Edit .env with your database and other settings
   ```

4. **Database setup**:
   ```bash
   # Make sure PostgreSQL is running
   createdb my_awesome_project
   ```

5. **Frontend setup**:
   ```bash
   npm install
   npm run dev  # In a separate terminal
   ```

6. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

7. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**:
   ```bash
   python manage.py runserver
   ```

## Development

### Project Structure

```
my_awesome_project/
├── my_awesome_project/          # Main project package
│   ├── settings/        # Settings modules
│   ├── urls.py         # URL configuration
│   ├── wsgi.py         # WSGI application
│   └── asgi.py         # ASGI application
├── apps/               # Django applications
│   ├── core/          # Core application
│   └── accounts/      # User accounts
├── templates/         # HTML templates
├── static/           # Static files (CSS, JS, images)
├── media/           # User uploaded files
├── requirements/    # Requirements files
├── Dockerfile       # Docker configuration
├── docker-compose.yml
├── package.json     # Frontend dependencies
├── vite.config.js   # Vite configuration
└── manage.py       # Django management script
```

### Available Commands

- `python manage.py runserver` - Start development server
- `python manage.py migrate` - Run database migrations
- `python manage.py makemigrations` - Create new migrations
- `python manage.py createsuperuser` - Create admin user
- `python manage.py collectstatic` - Collect static files
- `python manage.py test` - Run tests

### Frontend Development

- `npm run dev` - Start Vite development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

### Background Tasks

Start Celery worker:
```bash
celery -A my_awesome_project worker -l info
```

Start Celery beat (for scheduled tasks):
```bash
celery -A my_awesome_project beat -l info
```

### Code Quality

Run code formatting and linting:
```bash
black .
isort .
flake8
```

Run tests:
```bash
pytest
```

## Deployment


### Environment Variables

Copy `.env.example` to `.env` and configure:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (False in production)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` - Database configuration
- `SENTRY_DSN` - Sentry error tracking DSN

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `pytest`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

- Documentation: [Django Documentation](https://docs.djangoproject.com/)
- Issues: [Project Issues](https://github.com/CasualEngineerZombie/modern-django-starter/issues)
- HTMX: [HTMX Documentation](https://htmx.org/docs/)
- Alpine.js: [Alpine.js Documentation](https://alpinejs.dev/)
- TailwindCSS: [TailwindCSS Documentation](https://tailwindcss.com/docs)