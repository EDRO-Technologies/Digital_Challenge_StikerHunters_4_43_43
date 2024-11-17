import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('title', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('contact', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='image/organizator')),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='partners',
            field=models.ForeignKey(blank=True, max_length=150, null=True, on_delete=django.db.models.deletion.CASCADE, to='Events.organizer'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.OneToOneField(max_length=100, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=80)),
                ('second_name', models.CharField(max_length=80)),
                ('surname', models.CharField(max_length=80)),
                ('birth', models.DateField(auto_now_add=True)),
                ('is_organizer', models.BooleanField(default=False, help_text='Я организатор')),
                ('category', models.CharField(max_length=100)),
                ('special', models.CharField(max_length=100)),
                ('github', models.URLField()),
                ('image', models.ImageField(null=True, upload_to='image/event/')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Events.event')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
