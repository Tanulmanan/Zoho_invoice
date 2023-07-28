from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .errors import error_badrequest, error_forbidden, error_notfound, error_servererror
from .views import APIListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("qux.auth.urls")),
    path("account/tokens/", include("qux.token.urls")),
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    path("api/", APIListView.as_view(), name="api"),
   path("api/invoice_generation/", include("apps.invoice_generation.urls.apiurls")),
]

# Error handlers
handler400 = "project.errors.error_badrequest"
handler403 = "project.errors.error_forbidden"
handler404 = "project.errors.error_notfound"
handler500 = "project.errors.error_servererror"
errorpaths = [
    path("errors/400", error_badrequest),
    path("errors/403", error_forbidden),
    path("errors/404", error_notfound),
    path("errors/500", error_servererror),
]

if settings.DEBUG:
    urlpatterns += errorpaths
