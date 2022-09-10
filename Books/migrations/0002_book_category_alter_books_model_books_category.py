# Generated by Django 4.1.1 on 2022-09-10 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='books_model',
            name='books_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.book_category'),
        ),
    ]