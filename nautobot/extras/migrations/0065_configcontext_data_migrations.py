# Generated by Django 3.2.16 on 2022-11-25 11:45

from django.db import migrations
from nautobot.extras.utils import migrate_role_data


def migrate_data_from_legacy_roles_to_new_roles(apps, schema):
    """Migrate ConfigContext data from legacy_roles to new_roles."""
    ConfigContext = apps.get_model("extras", "ConfigContext")
    DeviceRole = apps.get_model("dcim", "DeviceRole")
    Role = apps.get_model("extras", "Role")
    migrate_role_data(
        model_to_migrate=ConfigContext,
        from_role_field_name="legacy_roles",
        from_role_model=DeviceRole,
        to_role_field_name="new_roles",
        to_role_model=Role,
        is_m2m_field=True,
    )


def reverse_role_data_migrate(apps, schema):
    """Migrate ConfigContext data from new_roles to legacy_roles."""
    ConfigContext = apps.get_model("extras", "ConfigContext")
    DeviceRole = apps.get_model("dcim", "DeviceRole")
    Role = apps.get_model("extras", "Role")
    migrate_role_data(
        model_to_migrate=ConfigContext,
        from_role_field_name="new_roles",
        from_role_model=Role,
        to_role_field_name="legacy_roles",
        to_role_model=DeviceRole,
        is_m2m_field=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0064_alter_configcontext_and_add_new_role"),
    ]

    operations = [
        migrations.RunPython(migrate_data_from_legacy_roles_to_new_roles, reverse_role_data_migrate),
    ]
