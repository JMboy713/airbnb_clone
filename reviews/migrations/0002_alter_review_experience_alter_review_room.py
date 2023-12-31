# Generated by Django 4.2.6 on 2023-10-26 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_alter_room_amenities_alter_room_category_and_more'),
        ('experiences', '0002_experience_category_alter_perk_description_and_more'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='experience',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='review',
            name='room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='rooms.room'),
        ),
    ]
