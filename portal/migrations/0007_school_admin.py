# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_teacher_email_verification'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='admin',
            field=models.ForeignKey(default=0, to='portal.Teacher'),
            preserve_default=False,
        ),
    ]