# Generated by Django 2.1.15 on 2019-12-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kubeops_api', '0051_auto_20191224_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='conditions',
            field=models.ManyToManyField(null=True, to='kubeops_api.Condition'),
        ),
        migrations.AlterField(
            model_name='node',
            name='conditions',
            field=models.ManyToManyField(null=True, to='kubeops_api.Condition'),
        ),
    ]
