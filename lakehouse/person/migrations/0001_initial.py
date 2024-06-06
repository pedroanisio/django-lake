# Generated by Django 5.0.6 on 2024-06-06 00:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concept',
            fields=[
                ('concept_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('field', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FieldOfStudy',
            fields=[
                ('field_id', models.AutoField(primary_key=True, serialize=False)),
                ('field_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NERtags',
            fields=[
                ('nertag_id', models.AutoField(primary_key=True, serialize=False)),
                ('entity', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('occupation_id', models.AutoField(primary_key=True, serialize=False)),
                ('occupation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='POSTags',
            fields=[
                ('postag_id', models.AutoField(primary_key=True, serialize=False)),
                ('word', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipType',
            fields=[
                ('relationship_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('occupation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.occupation')),
                ('primary_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.fieldofstudy')),
            ],
        ),
        migrations.CreateModel(
            name='Contributions',
            fields=[
                ('contribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('contribution_detail', models.TextField()),
                ('concept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.concept')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('alias_id', models.AutoField(primary_key=True, serialize=False)),
                ('alias_name', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='NER_POS_Link',
            fields=[
                ('link_id', models.AutoField(primary_key=True, serialize=False)),
                ('nertag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.nertags')),
                ('postag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.postags')),
            ],
        ),
        migrations.CreateModel(
            name='Publications',
            fields=[
                ('publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('publication_name', models.CharField(max_length=255)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
        ),
        migrations.CreateModel(
            name='DetailedRelationship',
            fields=[
                ('detailed_relationship_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_concept', to='person.concept')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_person', to='person.person')),
                ('relationship_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.relationshiptype')),
            ],
        ),
        migrations.CreateModel(
            name='PersonFieldOfStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.fieldofstudy')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='person.person')),
            ],
            options={
                'unique_together': {('person', 'field')},
            },
        ),
    ]
