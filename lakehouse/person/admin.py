from django.contrib import admin
from .models import (
    Occupation, FieldOfStudy, Person, PersonFieldOfStudy, Alias, Concept,
    Contributions, RelationshipType, DetailedRelationship, Publications,
    POSTags, NERtags, NER_POS_Link, Location, Event, Verb
)

class PersonFieldOfStudyInline(admin.TabularInline):
    model = PersonFieldOfStudy
    extra = 1

class AliasInline(admin.TabularInline):
    model = Alias
    extra = 1

class PublicationsInline(admin.TabularInline):
    model = Publications
    extra = 1

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'birth_date', 'death_date', 'nationality', 'gender', 'occupation', 'primary_field')
    search_fields = ('full_name', 'nationality')
    list_filter = ('nationality', 'gender', 'occupation', 'primary_field')
    inlines = [PersonFieldOfStudyInline, AliasInline, PublicationsInline]

class ConceptAdmin(admin.ModelAdmin):
    list_display = ('name', 'field')
    search_fields = ('name', 'field')
    list_filter = ('field',)

class ContributionsAdmin(admin.ModelAdmin):
    list_display = ('person', 'concept', 'contribution_detail')
    search_fields = ('person__full_name', 'concept__name')
    list_filter = ('concept',)

class DetailedRelationshipAdmin(admin.ModelAdmin):
    list_display = ('source', 'target', 'relationship_type', 'description')
    search_fields = ('source__full_name', 'target__name', 'relationship_type__name')
    list_filter = ('relationship_type',)

class POSTagsAdmin(admin.ModelAdmin):
    list_display = ('word', 'tag')
    search_fields = ('word',)
    list_filter = ('tag',)

class NERtagsAdmin(admin.ModelAdmin):
    list_display = ('entity', 'type')
    search_fields = ('entity',)
    list_filter = ('type',)

class NER_POS_LinkAdmin(admin.ModelAdmin):
    list_display = ('nertag', 'postag')
    search_fields = ('nertag__entity', 'postag__word')

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('occupation_id', 'occupation')
    search_fields = ('occupation',)
    ordering = ('occupation',)

class FieldOfStudyAdmin(admin.ModelAdmin):
    list_display = ('field_id', 'field_name')
    search_fields = ('field_name',)
    ordering = ('field_name',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_id', 'location_name', 'parent_location')
    search_fields = ('location_name',)
    list_filter = ('parent_location',)
    ordering = ('location_name',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id', 'event_name', 'location', 'start_date', 'end_date')
    search_fields = ('event_name', 'location__location_name')
    list_filter = ('location', 'start_date', 'end_date')
    ordering = ('start_date',)

class VerbAdmin(admin.ModelAdmin):
    list_display = ('verb_id', 'verb_name')
    search_fields = ('verb_name',)
    ordering = ('verb_name',)

admin.site.register(Occupation, OccupationAdmin)
admin.site.register(FieldOfStudy, FieldOfStudyAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Alias)
admin.site.register(Concept, ConceptAdmin)
admin.site.register(Contributions, ContributionsAdmin)
admin.site.register(RelationshipType)
admin.site.register(DetailedRelationship, DetailedRelationshipAdmin)
admin.site.register(Publications)
admin.site.register(POSTags, POSTagsAdmin)
admin.site.register(NERtags, NERtagsAdmin)
admin.site.register(NER_POS_Link, NER_POS_LinkAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Verb, VerbAdmin)
