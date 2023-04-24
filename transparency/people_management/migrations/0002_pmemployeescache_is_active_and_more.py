# Generated by Django 4.1.3 on 2023-04-18 08:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('people_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmemployeescache',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='pmemployeescache',
            name='is_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pmemployeescache',
            name='month',
            field=models.PositiveIntegerField(null=True, verbose_name='Mês'),
        ),
        migrations.AddField(
            model_name='pmemployeescache',
            name='publication_date_nomination',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Data da publicação - Nomeação'),
        ),
        migrations.AddField(
            model_name='pmemployeescache',
            name='publication_date_retirement',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Data da publicação - Aposentadoria'),
        ),
        migrations.AddField(
            model_name='pmemployeescache',
            name='updated',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='pmemployeescache',
            name='year',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pmemployeescache',
            name='ordinance_number_nomination',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Número da Portaria - Nomeação'),
        ),
        migrations.AlterField(
            model_name='pmemployeescache',
            name='ordinance_number_retirement',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Número da Portaria - Aposentadoria'),
        ),
        migrations.AlterField(
            model_name='pmemployeescache',
            name='ordinance_year_nomination',
            field=models.CharField(blank=True, max_length=4, verbose_name='Ano da Portaria - Nomeação'),
        ),
        migrations.AlterField(
            model_name='pmemployeescache',
            name='ordinance_year_retirement',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='Ano da Portaria - Aposentadoria'),
        ),
        migrations.AlterField(
            model_name='pmemployeescache',
            name='stability',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterUniqueTogether(
            name='pmemployeescache',
            unique_together={('registration', 'month', 'year')},
        ),
        migrations.CreateModel(
            name='PMTraineesCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nome')),
                ('level', models.CharField(default='', max_length=100, verbose_name='Nível')),
                ('specialty', models.CharField(blank=True, max_length=100, null=True, verbose_name='Especialidade')),
                ('deadline', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Prazo')),
                ('month', models.PositiveIntegerField(null=True, verbose_name='Mês')),
                ('year', models.PositiveIntegerField(null=True, verbose_name='Ano')),
                ('is_mandatory', models.BooleanField(default=False)),
                ('updated', models.BooleanField(default=False, null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'month', 'year')},
            },
        ),
        migrations.CreateModel(
            name='PMPensionersCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name_founder', models.CharField(default='', max_length=100, verbose_name='Instituidor da pensão')),
                ('effective_role', models.CharField(blank=True, max_length=100, null=True)),
                ('name_pensioner', models.CharField(default='', max_length=100, verbose_name='Pensionista')),
                ('ordinance_number_pension', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número da portaria')),
                ('ordinance_year_pension', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ano da portaria')),
                ('publication_date_pension', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Data da publicação')),
                ('month', models.PositiveIntegerField(null=True, verbose_name='Mês')),
                ('year', models.PositiveIntegerField(null=True)),
                ('updated', models.BooleanField(default=False, null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name_pensioner', 'month', 'year')},
            },
        ),
        migrations.CreateModel(
            name='PMEmployeesGratifComisCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('registration', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Matrícula')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nome')),
                ('bond', models.CharField(default='', max_length=100, verbose_name='Vínculo')),
                ('comission_role', models.CharField(blank=True, max_length=100, null=True, verbose_name='Gratificação')),
                ('workplace', models.CharField(default='', max_length=100, verbose_name='Lotação')),
                ('ordinance_number_nomination', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número do ato (Nomeação)')),
                ('ordinance_year_nomination', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ano do ato (Nomeação)')),
                ('publication_date_nomination', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Data da publicação - Nomeação')),
                ('month', models.PositiveIntegerField(null=True, verbose_name='Mês')),
                ('year', models.PositiveIntegerField(null=True)),
                ('is_member', models.BooleanField(default=False)),
                ('updated', models.BooleanField(default=False, null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('registration', 'month', 'year')},
            },
        ),
        migrations.CreateModel(
            name='PMCollaboratorsCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nome')),
                ('cathegory', models.CharField(default='', max_length=100, verbose_name='Categoria')),
                ('workplace', models.CharField(max_length=100)),
                ('act_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número do ato (Nomeação/Designação)')),
                ('act_year', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ano do ato (Nomeação/Designação)')),
                ('month', models.PositiveIntegerField(null=True, verbose_name='Mês')),
                ('year', models.PositiveIntegerField(null=True)),
                ('updated', models.BooleanField(default=False, null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('name', 'month', 'year')},
            },
        ),
        migrations.CreateModel(
            name='PMAssignedEmployeesCache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('registration', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Matrícula')),
                ('name', models.CharField(default='', max_length=100, verbose_name='Nome')),
                ('original_role', models.CharField(blank=True, max_length=100, null=True)),
                ('current_role', models.CharField(blank=True, max_length=100, null=True)),
                ('comission_role', models.CharField(blank=True, max_length=100, null=True)),
                ('ordinance_number_assignment', models.CharField(blank=True, max_length=20, null=True, verbose_name='Número da portaria')),
                ('ordinance_year_assignment', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ano da portaria')),
                ('publication_date_assignment', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Data da publicação')),
                ('workplace', models.CharField(max_length=100)),
                ('original_organ', models.CharField(max_length=100)),
                ('target_organ', models.CharField(max_length=100)),
                ('onus_mp', models.BooleanField(default=False)),
                ('from_mp', models.BooleanField(default=False)),
                ('deadline', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Prazo')),
                ('month', models.PositiveIntegerField(null=True, verbose_name='Mês')),
                ('year', models.PositiveIntegerField(null=True)),
                ('updated', models.BooleanField(default=False, null=True)),
                ('created_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('registration', 'month', 'year')},
            },
        ),
    ]
