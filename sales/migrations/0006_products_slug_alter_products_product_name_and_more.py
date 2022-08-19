# Generated by Django 4.0.1 on 2022-07-09 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_rename_products_sold_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(choices=[('big bottle coke', '60cl coke'), ('big bottle fanta', '60cl fanta'), ('big bottle sprite', '60cl sprite'), ('small pet coke', '35cl coke'), ('small pet fanta', '35cl fanta'), ('small pet sprite', '35cl sprite'), ('lucuzade', 'lucuzade'), ('big pulpy', 'big pulpy'), ('small pulpy', 'small pulpy'), ('big lacasera', 'big lacasera'), ('small lacasera', 'small lacasera'), ('pepsi pet', 'pepsi pet'), ('team lemon', 'team lemon'), ('limca', 'limca'), ('chapman', 'chapman'), ('mama coke', 'mama coke'), ('berryblast', 'berryblast'), ('big eva', 'big eva'), ('small eva', 'small eva'), ('big algor', 'big algor'), ('small algor', 'small algor'), ('star radlar', 'star radlar'), ('fayrouz', 'fayrouz'), ('can coke', 'can coke'), ('can sprite', 'can sprite'), ('dubic malt', 'dubic malt'), ('malta guiness', 'malta guiness'), ('heineken', 'heineken'), ('exotic', 'exotic'), ('black bullet', 'black bullet'), ('fearless', 'fearless'), ('predator', 'predator'), ('zero pet', 'zero pet'), ('action bitter', 'action bitter'), ('coke crate', 'coke crate'), ('small crate', 'small crate'), ('pepsi crate', 'pepsi crate'), ('team soda', 'team soda'), ('nutri milk', 'nutri milk'), ('big ice block', 'big ice block'), ('big ice block', 'big ice block'), ('sachet water', 'pure water'), ('small ice block', 'small ice block'), ('big ice block', 'big ice block'), ('algor small water', 'algor 50cl')], max_length=30),
        ),
        migrations.AlterField(
            model_name='sold',
            name='product_name',
            field=models.CharField(choices=[('big bottle coke', '60cl coke'), ('big bottle fanta', '60cl fanta'), ('big bottle sprite', '60cl sprite'), ('small pet coke', '35cl coke'), ('small pet fanta', '35cl fanta'), ('small pet sprite', '35cl sprite'), ('lucuzade', 'lucuzade'), ('big pulpy', 'big pulpy'), ('small pulpy', 'small pulpy'), ('big lacasera', 'big lacasera'), ('small lacasera', 'small lacasera'), ('pepsi pet', 'pepsi pet'), ('team lemon', 'team lemon'), ('limca', 'limca'), ('chapman', 'chapman'), ('mama coke', 'mama coke'), ('berryblast', 'berryblast'), ('big eva', 'big eva'), ('small eva', 'small eva'), ('big algor', 'big algor'), ('small algor', 'small algor'), ('star radlar', 'star radlar'), ('fayrouz', 'fayrouz'), ('can coke', 'can coke'), ('can sprite', 'can sprite'), ('dubic malt', 'dubic malt'), ('malta guiness', 'malta guiness'), ('heineken', 'heineken'), ('exotic', 'exotic'), ('black bullet', 'black bullet'), ('fearless', 'fearless'), ('predator', 'predator'), ('zero pet', 'zero pet'), ('action bitter', 'action bitter'), ('coke crate', 'coke crate'), ('small crate', 'small crate'), ('pepsi crate', 'pepsi crate'), ('team soda', 'team soda'), ('nutri milk', 'nutri milk'), ('big ice block', 'big ice block'), ('big ice block', 'big ice block'), ('sachet water', 'pure water'), ('small ice block', 'small ice block'), ('big ice block', 'big ice block'), ('algor small water', 'algor 50cl')], max_length=30),
        ),
    ]
