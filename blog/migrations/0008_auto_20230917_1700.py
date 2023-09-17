# Generated by Django 3.2.20 on 2023-09-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_save_comment_savepoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.TextField()),
                ('image', models.ImageField(upload_to="{% uplode_image 'contact_image' %}")),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ImageField(upload_to="{% uplode_image 'menber_face' %}"),
        ),
    ]