from django.views.generic import TemplateView
from rest_framework.schemas.openapi import SchemaGenerator


class APIListView(TemplateView):
    template_name = "api.html"
    app_label = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        generator = SchemaGenerator()
        schema = generator.get_schema()

        paths = []
        for path in schema["paths"]:
            for method in schema["paths"][path]:
                item = {"path": path, "method": method}
                paths.append(item)

        app_label = self.kwargs.get("app_label", None)
        if app_label:
            paths = [x for x in paths if x["path"].startswith(f"/api/v1/{app_label}/")]

        context["items"] = paths

        print(context)

        return context
