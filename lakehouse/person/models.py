from django.db import models

class Occupation(models.Model):
    occupation_id = models.AutoField(primary_key=True)
    occupation = models.CharField(max_length=255)

class FieldOfStudy(models.Model):
    field_id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=255)

class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    primary_field = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)

class PersonFieldOfStudy(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    field = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('person', 'field')

class Alias(models.Model):
    alias_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=255)

class Concept(models.Model):
    concept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    field = models.CharField(max_length=255)

class Contributions(models.Model):
    contribution_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    contribution_detail = models.TextField()

class RelationshipType(models.Model):
    relationship_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class DetailedRelationship(models.Model):
    detailed_relationship_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='source_person')
    target = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='target_concept')
    relationship_type = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)
    description = models.TextField()

class Publications(models.Model):
    publication_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    publication_name = models.CharField(max_length=255)

class POSTags(models.Model):
    postag_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255)
    tag = models.CharField(max_length=10)

class NERtags(models.Model):
    nertag_id = models.AutoField(primary_key=True)
    entity = models.CharField(max_length=255)
    type = models.CharField(max_length=50)

class NER_POS_Link(models.Model):
    link_id = models.AutoField(primary_key=True)
    nertag = models.ForeignKey(NERtags, on_delete=models.CASCADE)
    postag = models.ForeignKey(POSTags, on_delete=models.CASCADE)
