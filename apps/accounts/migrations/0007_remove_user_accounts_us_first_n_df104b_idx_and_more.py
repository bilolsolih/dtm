# Generated by Django 4.2.7 on 2023-12-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_options_alter_user_birthdate_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='user',
            name='accounts_us_first_n_df104b_idx',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nickname',
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(default='Banzay', max_length=128, verbose_name='Ism Sharif'),
            preserve_default=False,
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['full_name'], name='accounts_us_full_na_88336b_idx'),
        ),
    ]
