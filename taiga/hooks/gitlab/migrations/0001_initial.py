# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.db import migrations
from django.core.files import File

import uuid


def create_github_system_user(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    User = get_user_model()
    db_alias = schema_editor.connection.alias
    random_hash = uuid.uuid4().hex
    user = User.objects.using(db_alias).create(
        username="gitlab-{}".format(random_hash),
        email="gitlab-{}@taiga.io".format(random_hash),
        full_name="GitLab",
        is_active=False,
        is_system=True,
        bio="",
    )
    f = open("taiga/hooks/gitlab/migrations/logo.png", "rb")
    user.photo.save("logo.png", File(f))
    user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_theme')
    ]

    operations = [
        migrations.RunPython(create_github_system_user),
    ]
