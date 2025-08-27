# Taxi Service (Forms)

Невеликий Django-проєкт для керування автопарком таксі: виробники, авто, водії. Форми створені на базі **crispy-forms + Bootstrap 4**. Деплой на **Render**, БД — **PostgreSQL (Neon)**.

## 🔗 Live Demo
https://taxi-service-andriy125.onrender.com

## ✨ Основні можливості
- CRUD для **Manufacturer** та **Car** (кнопки створення/редагування/видалення на списках і деталках).
- Аутентифікація користувачів (Django auth).
- Охайні форми завдяки **django-crispy-forms** і **crispy-bootstrap4**.
- Готовий фікстчер з тестовими даними та суперкористувачем.
## 🧪 Тестовий користувач

Для швидкої перевірки функціоналу можна увійти під тестовим акаунтом:

- **Login:** `user`  
- **Password:** `user12345`

## Фото

<img width="1855" height="942" alt="image" src="https://github.com/user-attachments/assets/ad210e35-f59b-4bc3-a548-205a57cadfd6" />

## 🚀 Швидкий старт локально
```bash
git clone https://github.com/Andriy125/py-taxi-service-forms.git
cd py-taxi-service-forms
python -m venv .venv && . .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt

# Змінні оточення (приклад див. .env.sample)
export SECRET_KEY="change_me_please"
export DJANGO_SETTINGS_MODULE="taxi_service.settings.dev"

python manage.py migrate
python manage.py loaddata taxi_service_db_data.json
python manage.py runserver



