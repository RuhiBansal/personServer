# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_person_deathyear'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='deathYear',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
    ]
