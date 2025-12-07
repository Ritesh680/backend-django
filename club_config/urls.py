"""
URL configuration for club_config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import os
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
]

# Dynamically include URLs from all apps in the apps folder
apps_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "apps")
if os.path.exists(apps_dir):
    for app in os.listdir(apps_dir):
        app_path = os.path.join(apps_dir, app)
        urls_path = os.path.join(app_path, "urls.py")
        # Only include directories that have a urls.py file and are not __pycache__
        if (
            os.path.isdir(app_path)
            and app != "__pycache__"
            and not app.startswith("__")
            and os.path.exists(urls_path)
        ):
            try:
                urlpatterns.append(path("api/", include(f"apps.{app}.urls")))
            except Exception:
                # Skip apps that can't be imported (e.g., missing urls module)
                pass
