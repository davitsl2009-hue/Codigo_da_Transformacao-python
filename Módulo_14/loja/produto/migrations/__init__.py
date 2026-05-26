
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128, verbose_name='Nome do Produto')),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Preço')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade em Estoque')),
            ],
        ),
    ]