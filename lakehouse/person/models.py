from django.db import models

class Occupation(models.Model):
    occupation_id = models.AutoField(primary_key=True)
    occupation = models.CharField(max_length=255)

    def __str__(self):
        return self.occupation

class FieldOfStudy(models.Model):
    field_id = models.AutoField(primary_key=True)
    field_name = models.CharField(max_length=255)

    def __str__(self):
        return self.field_name

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=255)
    parent_location = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='child_locations')

    def __str__(self):
        return self.location_name

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    related_person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    verbs = models.ManyToManyField('Verb', related_name='events')

    def __str__(self):
        return self.event_name

# Model representing a verb such as 'create', 'influence', etc.
# This model stores verbs in their base form (infinitive) without tense inflection
# to ensure consistency across different uses and contexts.
class Verb(models.Model):
    verb_id = models.AutoField(primary_key=True)  # Auto-incremented primary key
    verb_name = models.CharField(max_length=255)  # Name of the verb in its base form

    def __str__(self):
        return self.verb_name


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    primary_field = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)
    verbs = models.ManyToManyField('Verb', related_name='persons', blank=True)

    def __str__(self):
        return self.full_name

class PersonFieldOfStudy(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    field = models.ForeignKey(FieldOfStudy, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('person', 'field')

    def __str__(self):
        return f'{self.person.full_name} - {self.field.field_name}'

class Alias(models.Model):
    alias_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    alias_name = models.CharField(max_length=255)

    def __str__(self):
        return self.alias_name

class Concept(models.Model):
    concept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    field = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Contributions(models.Model):
    contribution_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE)
    contribution_detail = models.TextField()
    verbs = models.ManyToManyField('Verb', related_name='contributions', blank=True)

    def __str__(self):
        return f'{self.person.full_name} - {self.concept.name}'

class RelationshipType(models.Model):
    relationship_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DetailedRelationship(models.Model):
    detailed_relationship_id = models.AutoField(primary_key=True)
    source = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='source_person')
    target = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='target_concept')
    relationship_type = models.ForeignKey(RelationshipType, on_delete=models.CASCADE)
    description = models.TextField()
    verbs = models.ManyToManyField('Verb', related_name='detailed_relationships', blank=True)

    def __str__(self):
        return f'{self.source.full_name} - {self.relationship_type.name} - {self.target.name}'

class Publications(models.Model):
    publication_id = models.AutoField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    publication_name = models.CharField(max_length=255)

    def __str__(self):
        return self.publication_name
    
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title

class Lecture(models.Model):
    lecture_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='lectures')

    def __str__(self):
        return self.title

class ArticleEvent(models.Model):
    article_event_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article.title} - {self.event.event_name}'


class POSTags(models.Model):
    postag_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255)
    tag = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.word} - {self.tag}'

class NERtags(models.Model):
    nertag_id = models.AutoField(primary_key=True)
    entity = models.CharField(max_length=255)
    type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.entity} ({self.type})'

class NER_POS_Link(models.Model):
    link_id = models.AutoField(primary_key=True)
    nertag = models.ForeignKey(NERtags, on_delete=models.CASCADE)
    postag = models.ForeignKey(POSTags, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nertag.entity} - {self.postag.word}'
