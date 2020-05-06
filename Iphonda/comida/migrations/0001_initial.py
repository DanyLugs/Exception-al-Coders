
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('descripcion', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to='categoria/static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, unique=True)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='comida/static/images')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comida.Categoria')),
            ],
        ),
    ]
