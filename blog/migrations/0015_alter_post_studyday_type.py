# Generated by Django 4.2.2 on 2023-09-26 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_comment_savepoint_alter_post_studyday_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='studyday_type',
            field=models.CharField(choices=[('tuesday_17', 'Tuesday 17:00'), ('tuesday_18', 'Tuesday 18:00'), ('wednesday_17', 'Wednesday 17:00'), ('wednesday_18', 'Wednesday 18:00'), ('friday_17', 'Friday 17:00'), ('friday_18', 'Friday 18:00'), ('saturday_10', 'Saturday 10:00'), ('saturday_11', 'Saturday 11:00'), ('saturday_13', 'Saturday 13:00'), ('saturday_14', 'Saturday 14:00')], max_length=100),
        ),
    ]