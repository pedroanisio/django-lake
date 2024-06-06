from django.shortcuts import render
from .models import Person, Location, Event, Publications, Alias, Concept, Contributions, DetailedRelationship, RelationshipType, Verb

def grice_details_view(request):
    person = Person.objects.get(full_name='Herbert Paul Grice')
    locations = Location.objects.all()
    events = Event.objects.filter(related_person=person)
    publications = Publications.objects.filter(person=person)
    aliases = Alias.objects.filter(person=person)
    concepts = Concept.objects.all()
    contributions = Contributions.objects.filter(person=person)
    detailed_relationships = DetailedRelationship.objects.filter(source=person)
    relationship_types = RelationshipType.objects.all()
    verbs = Verb.objects.all()
    
    context = {
        'person': person,
        'locations': locations,
        'events': events,
        'publications': publications,
        'aliases': aliases,
        'concepts': concepts,
        'contributions': contributions,
        'detailed_relationships': detailed_relationships,
        'relationship_types': relationship_types,
        'verbs': verbs
    }
    
    return render(request, 'person/grice_details.html', context)
