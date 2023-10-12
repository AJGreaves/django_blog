# Generated by Django 4.2.3 on 2023-10-12 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('about', '0003_collaboraterequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaboraterequest',
            name='email',
        ),
        migrations.RemoveField(
            model_name='collaboraterequest',
            name='name',
        ),
        migrations.AddField(
            model_name='collaboraterequest',
            name='requester',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='collaborator', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
