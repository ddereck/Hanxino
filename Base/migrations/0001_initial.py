# Generated by Django 5.0.3 on 2024-05-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='discotheques/')),
            ],
        ),
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='artiste/')),
                ('nom', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('audio', models.FileField(upload_to='audios/')),
            ],
        ),
        migrations.CreateModel(
            name='Carrousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carrousels/')),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='concerts/')),
                ('date', models.DateField()),
                ('titre', models.CharField(max_length=100)),
                ('lieu', models.CharField(max_length=100)),
                ('heure', models.TimeField()),
                ('description', models.TextField()),
                ('prix', models.DecimalField(decimal_places=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ville', models.TextField(max_length=12)),
                ('quartier', models.TextField(max_length=15)),
                ('tel1', models.CharField(max_length=12)),
                ('tel2', models.CharField(max_length=12)),
                ('mail', models.EmailField(max_length=254)),
                ('remail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Discographie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='albums/')),
                ('detail', models.ImageField(upload_to='albums/')),
                ('titre', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=0, max_digits=8)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='evenements/')),
                ('cover', models.ImageField(upload_to='affiches/')),
                ('titre', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('lieu', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Morceau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('video', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_evenement', models.CharField(max_length=100)),
                ('nom_prenom', models.CharField(max_length=100)),
                ('montant_paye', models.DecimalField(decimal_places=2, max_digits=10)),
                ('email_acheteur', models.EmailField(max_length=254)),
                ('date_paiement', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prochainconcert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='concerts/')),
                ('date', models.DateTimeField()),
                ('titre', models.CharField(max_length=100)),
                ('prix', models.DecimalField(decimal_places=0, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeConcert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
                ('image', models.ImageField(upload_to='mediaconcerts/')),
                ('description', models.TextField()),
                ('duree', models.DurationField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ResumeConcert1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField()),
                ('image', models.ImageField(upload_to='mediaconcerts/')),
                ('description', models.TextField()),
                ('duree', models.DurationField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Youtubevd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='youtubevd/')),
                ('description', models.TextField()),
                ('video', models.URLField()),
            ],
        ),
    ]