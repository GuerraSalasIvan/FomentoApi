# Generated by Django 4.2.9 on 2024-03-07 22:09

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rol', models.PositiveSmallIntegerField(choices=[(1, 'administrador'), (2, 'cliente'), (3, 'entrenador')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Colores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('Blanco', 'Blanco'), ('Negro', 'Negro'), ('Amarillo', 'Amarillo'), ('Rojo', 'Rojo'), ('Azul', 'Azul'), ('Rosa', 'Rosa'), ('Morado', 'Morado'), ('Verde', 'Verde'), ('Gris', 'Gris'), ('Marron', 'Marron'), ('Gris', 'Gris'), ('Naranja', 'Naranja'), ('---', 'Sin asignar')], default='---', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Deportes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deporte', models.CharField(choices=[('FUT', 'Futbol'), ('BSK', 'Baloncesto'), ('PDL', 'Padel'), ('---', 'Sin_Asignar')], default='---', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('capacidad', models.IntegerField(default=1)),
                ('media_equipo', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('color_eq_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_eq_1', to='app.colores')),
                ('color_eq_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_eq_2', to='app.colores')),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.deportes', verbose_name='deporte')),
            ],
        ),
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liga', models.CharField(choices=[('2ªReg', 'Segunda Regional'), ('1ºReg', 'Primera Regional'), ('DivHonor', 'Division de honor'), ('Nacional', 'Nacional'), ('---', 'Sin asignar')], default='---', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edad', models.IntegerField()),
                ('media', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('sexo', models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino'), ('---', 'Sin_Asignar')], default='---', max_length=3)),
                ('rol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Votacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField(default=0)),
                ('comentario', models.CharField(max_length=400)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipos')),
                ('usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('capacidad', models.IntegerField()),
                ('calle', models.CharField(max_length=150)),
                ('lat', models.FloatField(verbose_name='latitud')),
                ('lng', models.FloatField(verbose_name='longitud')),
                ('deporte', models.ManyToManyField(to='app.deportes', verbose_name='deporte')),
                ('equipo', models.ManyToManyField(to='app.equipos', verbose_name='equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Rel_Usu_Equi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipos', verbose_name='equipos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuarios', verbose_name='usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Rel_Equi_Ubi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipos', verbose_name='equipos')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion', verbose_name='ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='Rel_Dep_Ubi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deporte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.deportes', verbose_name='deporte')),
                ('equipos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.equipos', verbose_name='equipos')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil_Publico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('deportes_fav', models.TextField()),
                ('hitos_publicos', models.TextField()),
                ('lugar_fav', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion', verbose_name='lugar_fav')),
                ('usuarios', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('puntos_local', models.IntegerField(default=0)),
                ('puntos_visitante', models.IntegerField(default=0)),
                ('color_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_local', to='app.colores')),
                ('color_visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color_visitante', to='app.colores')),
                ('equipo_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_local', to='app.equipos')),
                ('equipo_visitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipo_visitiante', to='app.equipos')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion', verbose_name='ubicacion')),
            ],
        ),
        migrations.AddField(
            model_name='equipos',
            name='liga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.liga', verbose_name='Liga'),
        ),
        migrations.AddField(
            model_name='equipos',
            name='usuario',
            field=models.ManyToManyField(related_name='usuario_equipo', through='app.Rel_Usu_Equi', to='app.usuarios'),
        ),
        migrations.AddField(
            model_name='equipos',
            name='usuario_valoracion',
            field=models.ManyToManyField(related_name='votacion_usuario', through='app.Votacion', to='app.usuarios'),
        ),
        migrations.CreateModel(
            name='Entrenador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.ManyToManyField(to='app.equipos', verbose_name='equipo')),
                ('rol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Detalles_Ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incidentes', models.BooleanField()),
                ('cubierto', models.BooleanField()),
                ('ubicacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.ubicacion', verbose_name='ubicacion')),
            ],
        ),
    ]