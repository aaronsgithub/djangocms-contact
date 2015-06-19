SECRET_KEY = "test key"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

INSTALLED_APPS = [
    "djangocms_contact",
    "tests",
]

MIDDLEWARE_CLASSES = [
]

ARE_THE_SETTINGS_BEING_DETECTED = True
