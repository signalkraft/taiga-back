# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20151005_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authdata',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='auth_data'),
        ),
    ]
