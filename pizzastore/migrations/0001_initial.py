# Generated by Django 2.2.6 on 2019-10-09 14:11

from django.db import migrations, models
import django.db.models.aggregates
import django.db.models.deletion
import django_queryset_constraint.constraints
import django_queryset_constraint.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PizzaTopping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddConstraint(
            model_name='topping',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, name='Anchovies'), name='Anchovies are not a valid topping for anything'),
        ),
        migrations.AddField(
            model_name='pizzatopping',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzastore.Pizza'),
        ),
        migrations.AddField(
            model_name='pizzatopping',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizzastore.Topping'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(through='pizzastore.PizzaTopping', to='pizzastore.Topping'),
        ),
        migrations.AddConstraint(
            model_name='pizzatopping',
            constraint=django_queryset_constraint.constraints.QuerysetConstraint(name='At most 5 toppings', queryset=django_queryset_constraint.utils.M(app_label=None, finalized=True, model_name=None, operations=[{'args': ('objects',), 'kwargs': {}, 'type': '__getattribute__'}, {'args': ('values',), 'kwargs': {}, 'type': '__getattribute__'}, {'args': ('pizza',), 'kwargs': {}, 'type': '__call__'}, {'args': ('annotate',), 'kwargs': {}, 'type': '__getattribute__'}, {'args': (), 'kwargs': {'num_toppings': django.db.models.aggregates.Count('topping')}, 'type': '__call__'}, {'args': ('filter',), 'kwargs': {}, 'type': '__getattribute__'}, {'args': (), 'kwargs': {'num_toppings__gt': 5}, 'type': '__call__'}])),
        ),
        migrations.AddConstraint(
            model_name='pizzatopping',
            constraint=django_queryset_constraint.constraints.QuerysetConstraint(name='No pineapple', queryset=django_queryset_constraint.utils.M(app_label=None, finalized=True, model_name=None, operations=[{'args': ('objects',), 'kwargs': {}, 'type': '__getattribute__'}, {'args': ('filter',), 'kwargs': {}, 'type': '__getattribute__'}, {'args': (), 'kwargs': {'topping__name': 'Pineapple'}, 'type': '__call__'}])),
        ),
        migrations.AlterUniqueTogether(
            name='pizzatopping',
            unique_together={('pizza', 'topping')},
        ),
    ]
