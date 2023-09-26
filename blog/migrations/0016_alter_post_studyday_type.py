# Generated by Django 4.2.2 on 2023-09-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_studyday_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='studyday_type',
            field=models.CharField(choices=[('Tuesday 17:00', 'Tuesday 17:00'), ('Tuesday 18:00', 'Tuesday 18:00'), ('Wednesday 17:00', 'Wednesday 17:00'), ('Wednesday 18:00', 'Wednesday 18:00'), ('Friday 17:00', 'Friday 17:00'), ('Friday 18:00', 'Friday 18:00'), ('Saturday 10:00', 'Saturday 10:00'), ('Saturday 11:00', 'Saturday 11:00'), ('Saturday 13:00', 'Saturday 13:00'), ('Saturday 14:00', 'Saturday 14:00')], max_length=100),
        ),
    ]