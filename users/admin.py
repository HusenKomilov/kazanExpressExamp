from django.conf import settings
from django.contrib import admin
# from django4_recaptcha_admin_login import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import decorators, get_user_model
from django.utils.translation import gettext_lazy as _
from users.models import Role
from users.forms import UserAdminChangeForm, UserAdminCreationForm
from django.utils.safestring import mark_safe

User = get_user_model()
# admin.site.register(Role)
if settings.DJANGO_ADMIN_FORCE_ALLAUTH:
    # Force the `admin` sign in process to go through the `django-allauth` workflow:
    # https://django-allauth.readthedocs.io/en/stable/advanced.html#admin
    admin.site.login = decorators.login_required(admin.site.login)  # type: ignore[method-assign]

admin.site.register(Role)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password",)}),
        (_("Personal info"), {"fields": ("first_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    'role',
                    "image",
                ),
            },
        ),

    )
    list_display = ["first_name", "is_superuser", "get_role", "image"]
    search_fields = ["name"]

    def get_role(self, obj):
        return [a.title for a in obj.role.all()]
