# Generated by Django 4.2.3 on 2023-10-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_remove_collaboraterequest_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaboraterequest',
            name='requester',
        ),
        migrations.AddField(
            model_name='collaboraterequest',
            name='email',
            field=models.EmailField(default='test@email.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collaboraterequest',
            name='name',
            field=models.CharField(default='test', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collaboraterequest',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
