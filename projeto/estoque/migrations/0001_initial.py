# Generated by Django 2.2.24 on 2021-12-14 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estoque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('nf', models.PositiveIntegerField(blank=True, null=True, verbose_name='nota fiscal')),
                ('movimento', models.CharField(blank=True, choices=[('e', 'entrada'), ('s', 'saida')], max_length=1)),
                ('funcionario', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ProtocoloEntrega',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('estoque_atualizado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProtocoloEntregaItens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
                ('protocolo_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='protocolo_entrega', to='estoque.ProtocoloEntrega')),
            ],
        ),
        migrations.CreateModel(
            name='EstoqueItens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('saldo', models.PositiveIntegerField(blank=True)),
                ('estoque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estoques', to='estoque.Estoque')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='EstoqueEntrada',
            fields=[
            ],
            options={
                'verbose_name': 'estoque entrada',
                'verbose_name_plural': 'estoque entrada',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
        migrations.CreateModel(
            name='EstoqueSaida',
            fields=[
            ],
            options={
                'verbose_name': 'estoque saída',
                'verbose_name_plural': 'estoque saída',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
    ]
