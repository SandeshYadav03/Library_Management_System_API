# Generated by Django 4.1.1 on 2022-09-10 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_book_category_alter_books_model_books_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books_model',
            name='books_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='Books.book_category'),
        ),
    ]