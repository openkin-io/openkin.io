# Generated by Django 5.0.3 on 2024-09-18 13:12

import app.models.world
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='The usual, English name of the location', verbose_name='name')),
                ('native_name', models.TextField(blank=True, help_text='The location name in the native language, if different from the name.', verbose_name='native_name')),
                ('wiki', models.URLField(blank=True, verbose_name='Wikipedia URL')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='longitude')),
                ('image_flag', models.URLField(blank=True, verbose_name='image_flag')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Filiation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_adoption', models.BooleanField(null=True)),
                ('date_of_adoption', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_union', models.DateField(null=True)),
                ('partnership_type', models.CharField(blank=True, help_text='partnership, marriage, etc.', max_length=255, verbose_name='partnership type')),
            ],
            options={
                'ordering': ['person', 'partner'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=750, verbose_name='name')),
                ('surname', models.CharField(blank=True, help_text='Also called last name, second name or family name.', max_length=750, verbose_name='surname')),
                ('given_name', models.CharField(blank=True, help_text='Also called first name or forename.', max_length=100, verbose_name='given name')),
                ('birth_name', models.CharField(blank=True, help_text='Name at birth, also known as maiden name; only use if different from name', max_length=750, verbose_name='birth name')),
                ('native_name', models.CharField(blank=True, help_text="The person's name in their own language, if different.", max_length=750, verbose_name='native name')),
                ('native_name_lang', models.CharField(blank=True, choices=[('af', 'Afrikaans'), ('ar', 'Arabic'), ('ar-dz', 'Algerian Arabic'), ('ast', 'Asturian'), ('az', 'Azerbaijani'), ('bg', 'Bulgarian'), ('be', 'Belarusian'), ('bn', 'Bengali'), ('br', 'Breton'), ('bs', 'Bosnian'), ('ca', 'Catalan'), ('ckb', 'Central Kurdish (Sorani)'), ('cs', 'Czech'), ('cy', 'Welsh'), ('da', 'Danish'), ('de', 'German'), ('dsb', 'Lower Sorbian'), ('el', 'Greek'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'Spanish'), ('es-ar', 'Argentinian Spanish'), ('es-co', 'Colombian Spanish'), ('es-mx', 'Mexican Spanish'), ('es-ni', 'Nicaraguan Spanish'), ('es-ve', 'Venezuelan Spanish'), ('et', 'Estonian'), ('eu', 'Basque'), ('fa', 'Persian'), ('fi', 'Finnish'), ('fr', 'French'), ('fy', 'Frisian'), ('ga', 'Irish'), ('gd', 'Scottish Gaelic'), ('gl', 'Galician'), ('he', 'Hebrew'), ('hi', 'Hindi'), ('hr', 'Croatian'), ('hsb', 'Upper Sorbian'), ('hu', 'Hungarian'), ('hy', 'Armenian'), ('ia', 'Interlingua'), ('id', 'Indonesian'), ('ig', 'Igbo'), ('io', 'Ido'), ('is', 'Icelandic'), ('it', 'Italian'), ('ja', 'Japanese'), ('ka', 'Georgian'), ('kab', 'Kabyle'), ('kk', 'Kazakh'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', 'Korean'), ('ky', 'Kyrgyz'), ('lb', 'Luxembourgish'), ('lt', 'Lithuanian'), ('lv', 'Latvian'), ('mk', 'Macedonian'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'Marathi'), ('ms', 'Malay'), ('my', 'Burmese'), ('nb', 'Norwegian Bokmål'), ('ne', 'Nepali'), ('nl', 'Dutch'), ('nn', 'Norwegian Nynorsk'), ('os', 'Ossetic'), ('pa', 'Punjabi'), ('pl', 'Polish'), ('pt', 'Portuguese'), ('pt-br', 'Brazilian Portuguese'), ('ro', 'Romanian'), ('ru', 'Russian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sq', 'Albanian'), ('sr', 'Serbian'), ('sr-latn', 'Serbian Latin'), ('sv', 'Swedish'), ('sw', 'Swahili'), ('ta', 'Tamil'), ('te', 'Telugu'), ('tg', 'Tajik'), ('th', 'Thai'), ('tk', 'Turkmen'), ('tr', 'Turkish'), ('tt', 'Tatar'), ('udm', 'Udmurt'), ('ug', 'Uyghur'), ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('uz', 'Uzbek'), ('vi', 'Vietnamese'), ('zh-hans', 'Simplified Chinese'), ('zh-hant', 'Traditional Chinese')], max_length=7, verbose_name='language of native name')),
                ('pronunciation', models.CharField(blank=True, help_text='The phonetic pronunciation of the native name.', max_length=100, verbose_name='pronunciation of native name')),
                ('other_names', models.TextField(blank=True, help_text='Other notable names for the person, if different from name and birth name.This can include stage names, nicknames, criminal aliases, etc.', verbose_name='other names')),
                ('honorific_prefix', models.CharField(blank=True, help_text='This is for honorifics of serious significance that are attached tothe name in formal address, such as knighthoods, "The Honourable", and "His/Her Excellency"; do not use it for routine things like "Dr." or "Ms."', max_length=100, verbose_name='honorific prefix')),
                ('honorific_suffix', models.CharField(blank=True, help_text='Similar to honorific prefix, this is for honorifics of serious significance.', max_length=100, verbose_name='honorific suffix')),
                ('image', models.URLField(blank=True, help_text="A person's image", verbose_name='image url')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('birth_place_object_id', models.PositiveIntegerField()),
                ('disappearance_date', models.DateField(blank=True, help_text='(For missing persons)', null=True, verbose_name='date of disappearance')),
                ('disappearance_place_object_id', models.PositiveIntegerField()),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='date of death')),
                ('death_place_object_id', models.PositiveIntegerField()),
                ('death_cause', models.TextField(blank=True, verbose_name='cause of death')),
                ('resting_place_object_id', models.PositiveIntegerField()),
                ('education', models.TextField(blank=True, help_text='e.g., degree, institution and graduation year, if relevant. If verylittle information is available or relevant, the alma mater parametermay be more appropriate. ', verbose_name='education')),
                ('alma_mater', models.TextField(blank=True, help_text='e.g. college, university, etc.', verbose_name='alma mater')),
                ('nationality', models.CharField(blank=True, help_text='Synonymous with citizenship. Do not put religion or ethnicity in this field.', max_length=100, verbose_name='nationality')),
                ('occupation', models.TextField(blank=True, verbose_name='occupation')),
                ('title', models.CharField(blank=True, help_text='e.g. Mayor of the city of New York', max_length=100, verbose_name='title')),
                ('notes', models.TextField(blank=True, verbose_name='notes')),
                ('birth_place_content_type', models.ForeignKey(limit_choices_to={'model__in': [app.models.world.Country, app.models.world.Region, app.models.world.SubRegion, app.models.world.Settlement, app.models.world.Place]}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='natives', to='contenttypes.contenttype')),
                ('death_place_content_type', models.ForeignKey(limit_choices_to={'model__in': [app.models.world.Country, app.models.world.Region, app.models.world.SubRegion, app.models.world.Settlement, app.models.world.Place]}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deceased', to='contenttypes.contenttype')),
                ('disappearance_place_content_type', models.ForeignKey(limit_choices_to={'model__in': [app.models.world.Country, app.models.world.Region, app.models.world.SubRegion, app.models.world.Settlement, app.models.world.Place]}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gone_missing', to='contenttypes.contenttype')),
                ('genetic_father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.person')),
                ('genetic_mother', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='app.person')),
                ('parents', models.ManyToManyField(through='app.Filiation', to='app.person')),
                ('partners', models.ManyToManyField(through='app.Partnership', to='app.person')),
                ('resting_place_content_type', models.ForeignKey(limit_choices_to={'model__in': [app.models.world.Country, app.models.world.Region, app.models.world.SubRegion, app.models.world.Settlement, app.models.world.Place]}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='partnership',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnerships', to='app.person'),
        ),
        migrations.AddField(
            model_name='partnership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person'),
        ),
        migrations.AddField(
            model_name='filiation',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person'),
        ),
        migrations.AddField(
            model_name='filiation',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='app.person'),
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='The usual, English name of the location', verbose_name='name')),
                ('native_name', models.TextField(blank=True, help_text='The location name in the native language, if different from the name.', verbose_name='native_name')),
                ('wiki', models.URLField(blank=True, verbose_name='Wikipedia URL')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='longitude')),
                ('region_type', models.CharField(blank=True, default='region', help_text='State, province, oblast, etc.', max_length=32, verbose_name='region type')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Siblingship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('became_siblings_at', models.DateField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.person')),
                ('sibling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='siblingships', to='app.person')),
            ],
            options={
                'ordering': ['person', 'sibling'],
            },
        ),
        migrations.AddField(
            model_name='person',
            name='siblings',
            field=models.ManyToManyField(through='app.Siblingship', to='app.person'),
        ),
        migrations.CreateModel(
            name='SubRegion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='The usual, English name of the location', verbose_name='name')),
                ('native_name', models.TextField(blank=True, help_text='The location name in the native language, if different from the name.', verbose_name='native_name')),
                ('wiki', models.URLField(blank=True, verbose_name='Wikipedia URL')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='longitude')),
                ('subregion_type', models.CharField(blank=True, default='subregion', help_text='County, district, etc.', max_length=32, verbose_name='subregion type')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.region')),
            ],
            options={
                'verbose_name': 'SubRegion',
                'verbose_name_plural': 'SubRegions',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='The usual, English name of the location', verbose_name='name')),
                ('native_name', models.TextField(blank=True, help_text='The location name in the native language, if different from the name.', verbose_name='native_name')),
                ('wiki', models.URLField(blank=True, verbose_name='Wikipedia URL')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='longitude')),
                ('settlement_type', models.CharField(blank=True, default='settlement', help_text='City, town, village, hamlet, municipality, reservation, etc.', max_length=32, verbose_name='settlement type')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.country')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.region')),
                ('subregion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.subregion')),
            ],
            options={
                'verbose_name': 'Municipality',
                'verbose_name_plural': 'Municipalities',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='The usual, English name of the location', verbose_name='name')),
                ('native_name', models.TextField(blank=True, help_text='The location name in the native language, if different from the name.', verbose_name='native_name')),
                ('wiki', models.URLField(blank=True, verbose_name='Wikipedia URL')),
                ('latitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='latitude')),
                ('longitude', models.DecimalField(blank=True, decimal_places=4, max_digits=7, null=True, verbose_name='longitude')),
                ('place_type', models.CharField(blank=True, help_text='Can be a natural place like a forest, a body of water, a mountain, etc.;or a man-made place like a landmark, a monument, a historic site, a building, etc.', max_length=70, verbose_name='place type')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.country')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.region')),
                ('settlement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.settlement')),
                ('subregion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.subregion')),
            ],
            options={
                'verbose_name': 'Place',
                'verbose_name_plural': 'Places',
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='partnership',
            constraint=models.UniqueConstraint(fields=('person', 'partner'), name='unique_partnership'),
        ),
        migrations.AddConstraint(
            model_name='filiation',
            constraint=models.UniqueConstraint(fields=('parent', 'child'), name='parent_child_unique'),
        ),
        migrations.AddConstraint(
            model_name='siblingship',
            constraint=models.UniqueConstraint(fields=('person', 'sibling'), name='unique_siblingship'),
        ),
    ]
