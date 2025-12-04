# Development Guide

## Before Starting Server

### Activate the Virtual Environment

On macOS:

```bash
source venv/bin/activate
```

## Creating a New App

1. Create the app using Django's management command:

```bash
python manage.py startapp appname
```

2. Move the newly created app into the `apps` folder.

3. Update the app configuration:

   - Open `apps/appname/apps.py`
   - Change the `name` field to `apps.appname`

4. Register the app in Django settings:
   - Open `club_config/settings.py`
   - Add `apps.appname` to the `INSTALLED_APPS` list
