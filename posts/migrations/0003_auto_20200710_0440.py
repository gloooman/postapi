# Generated by Django 3.0.7 on 2020-07-10 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200710_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratio',
            name='opinion',
            field=models.CharField(choices=[('like', 'Like'), ('dislike', 'Dislike'), (None, 'No opinion')], default=None, max_length=7, null=True),
        ),
    ]
