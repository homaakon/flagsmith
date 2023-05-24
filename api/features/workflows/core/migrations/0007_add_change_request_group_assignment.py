# Generated by Django 3.2.18 on 2023-05-18 15:10

from django.db import migrations, models
import django.db.models.deletion
import django_lifecycle.mixins
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0034_add_user_permission_group_membership_through_model'),
        ('workflows_core', '0006_auto_20230518_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeRequestGroupAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('change_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows_core.changerequest', related_name="group_assignments")),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userpermissiongroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(django_lifecycle.mixins.LifecycleModelMixin, models.Model),
        ),
    ]