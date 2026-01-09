# Portfolio Tech Theme

A modern, responsive portfolio website built with Django, featuring a sleek tech-inspired design with neon accents and glassmorphism effects.

![Portfolio Preview](https://via.placeholder.com/800x400/0c0a1a/00f5ff?text=Portfolio+Tech+Theme)

## 🚀 Features

- **Modern Tech Design**: Neon cyan and violet color scheme with glassmorphism effects
- **Responsive Layout**: Fully responsive design that works on all devices
- **Dynamic Content**: Admin panel for easy content management
- **Contact Form**: Functional contact form with email notifications
- **Project Showcase**: Display projects with screenshots and links
- **Blog System**: Built-in blog with categories
- **Experience Timeline**: Professional experience display
- **Education Section**: Academic background showcase
- **Skills Visualization**: Progress bars for technical skills
- **Social Media Integration**: Links to GitHub, LinkedIn, and other platforms

## 🛠️ Tech Stack

- **Backend**: Django 5.2.8
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0, JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **Styling**: Custom CSS with CSS Variables, Font Awesome icons
- **Deployment**: Gunicorn, WhiteNoise for static files
- **Email**: SMTP integration for contact forms

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mdzihad42/portfolio_tech_theme.git
   cd portfolio_tech_theme
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   # On Windows
   env\Scripts\activate
   # On macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/` (if superuser created)

## 📁 Project Structure

```
portfolio_tech_theme/
├── zihad_02_Portfolio/          # Main Django project
│   ├── __init__.py
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL configuration
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
├── portfolio/                   # Main app
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URL configuration
│   ├── admin.py                # Admin panel configuration
│   ├── templates/              # HTML templates
│   │   └── portfolio/
│   │       ├── base.html       # Base template
│   │       ├── home.html       # Home page
│   │       ├── about.html      # About page
│   │       ├── projects.html   # Projects page
│   │       ├── contact.html    # Contact page
│   │       └── ...
│   └── static/                 # Static files (CSS, JS, images)
├── media/                      # User uploaded files
├── staticfiles/                # Collected static files
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🚀 Deployment

### Using Gunicorn

1. **Install Gunicorn** (already in requirements.txt)
2. **Run with Gunicorn**
   ```bash
   gunicorn zihad_02_Portfolio.wsgi:application --bind 0.0.0.0:8000
   ```

### Environment Variables

Create a `.env` file in the root directory for sensitive settings:

```
SECRET_KEY=your-secret-key-here
DEBUG=False
DATABASE_URL=your-database-url
EMAIL_HOST=your-email-host
EMAIL_HOST_USER=your-email-user
EMAIL_HOST_PASSWORD=your-email-password
```

## 📧 Email Configuration

The contact form uses Gmail SMTP. Update the settings in `zihad_02_Portfolio/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## 🎨 Customization

### Colors and Styling

The design uses CSS custom properties (variables) defined in `base.html`. You can customize:

- Primary colors: `--primary-color`, `--secondary-color`
- Backgrounds: `--bg-primary`, `--bg-secondary`
- Gradients: `--primary-gradient`, `--secondary-gradient`

### Content Management

Use the Django admin panel to add/edit:
- Hero section content
- About information
- Projects and screenshots
- Experience and education
- Blog posts
- Skills

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**MD Zihad Hossain**
- Email: mdzidad01793561142@gmail.com
- Phone: +880 1793 561142
- LinkedIn: [MD Zihad Hossain](https://www.linkedin.com/in/md-zihad-hossain-580074387/)
- GitHub: [mdzihad42](https://github.com/mdzihad42)
- Twitter: [@ZihadMd60133](https://x.com/ZihadMd60133)
- Location: Dhaka, Bangladesh

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/) - The web framework
- [Bootstrap](https://getbootstrap.com/) - CSS framework
- [Font Awesome](https://fontawesome.com/) - Icons
- [Google Fonts](https://fonts.google.com/) - Typography

---

⭐ **Star this repo if you found it helpful!**
