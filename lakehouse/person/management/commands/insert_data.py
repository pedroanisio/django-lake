from django.core.management.base import BaseCommand
from person.models import (
    Occupation, FieldOfStudy, Person, PersonFieldOfStudy, Alias, Concept, Contributions, 
    RelationshipType, DetailedRelationship, Publications, POSTags, NERtags, NER_POS_Link, Location, Event, Verb
)

class Command(BaseCommand):
    help = 'Insert initial data into the database'

    def handle(self, *args, **kwargs):
        # Insert data into Occupation table
        Occupation.objects.get_or_create(occupation_id=1, defaults={'occupation': 'Philosopher'})

        # Insert data into FieldOfStudy table
        FieldOfStudy.objects.get_or_create(field_id=1, defaults={'field_name': 'Linguistics'})
        FieldOfStudy.objects.get_or_create(field_id=2, defaults={'field_name': 'Pragmatics'})
        FieldOfStudy.objects.get_or_create(field_id=3, defaults={'field_name': 'Semantics'})

        # Insert data into Person table
        person, created = Person.objects.get_or_create(
            person_id=1, defaults={
                'full_name': 'Herbert Paul Grice', 'birth_date': '1913-03-13', 'death_date': '1988-08-28', 
                'nationality': 'British', 'gender': 'Male', 'occupation_id': 1, 'primary_field_id': 1
            }
        )

        # Insert data into PersonFieldOfStudy table for secondary fields
        PersonFieldOfStudy.objects.get_or_create(person=person, field_id=2)
        PersonFieldOfStudy.objects.get_or_create(person=person, field_id=3)

        # Insert data into Alias table
        Alias.objects.get_or_create(alias_id=1, defaults={'person': person, 'alias_name': 'H. P. Grice'})
        Alias.objects.get_or_create(alias_id=2, defaults={'person': person, 'alias_name': 'H. Paul Grice'})
        Alias.objects.get_or_create(alias_id=3, defaults={'person': person, 'alias_name': 'Paul Grice'})

        # Insert data into Concept table
        Concept.objects.get_or_create(concept_id=1, defaults={'name': 'Theory of Implicature', 'description': 'A theory created by H. P. Grice', 'field': 'Linguistics'})
        Concept.objects.get_or_create(concept_id=2, defaults={'name': 'Cooperative Principle', 'description': 'A principle including the Gricean maxims', 'field': 'Linguistics'})
        Concept.objects.get_or_create(concept_id=3, defaults={'name': 'Gricean Maxims', 'description': 'Maxims part of the Cooperative Principle', 'field': 'Linguistics'})
        Concept.objects.get_or_create(concept_id=4, defaults={'name': 'Pragmatics', 'description': 'Field in linguistics influenced by Grice', 'field': 'Linguistics'})
        Concept.objects.get_or_create(concept_id=5, defaults={'name': 'Semantics', 'description': 'Philosophical study of meaning influenced by Grice', 'field': 'Philosophy'})

        # Insert data into RelationshipType table
        RelationshipType.objects.get_or_create(relationship_type_id=1, defaults={'name': 'Created Concept'})
        RelationshipType.objects.get_or_create(relationship_type_id=2, defaults={'name': 'Influenced Field'})
        RelationshipType.objects.get_or_create(relationship_type_id=3, defaults={'name': 'Published As'})
        RelationshipType.objects.get_or_create(relationship_type_id=4, defaults={'name': 'Spouse Of'})
        RelationshipType.objects.get_or_create(relationship_type_id=5, defaults={'name': 'Parent Of'})

        # Insert data into Contributions table
        Contributions.objects.get_or_create(contribution_id=1, defaults={'person': person, 'concept_id': 1, 'contribution_detail': 'Developed the Theory of Implicature which explains how people understand indirect meaning in communication.'})
        Contributions.objects.get_or_create(contribution_id=2, defaults={'person': person, 'concept_id': 2, 'contribution_detail': 'Established the Cooperative Principle which includes the Gricean Maxims of Quantity, Quality, Relation, and Manner.'})
        Contributions.objects.get_or_create(contribution_id=3, defaults={'person': person, 'concept_id': 3, 'contribution_detail': 'Outlined the Gricean Maxims that are part of the Cooperative Principle.'})

        # Insert data into DetailedRelationship table
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=1, defaults={'source_id': 1, 'target_id': 1, 'relationship_type_id': 1, 'description': 'Created Theory of Implicature'})
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=2, defaults={'source_id': 1, 'target_id': 2, 'relationship_type_id': 1, 'description': 'Created Cooperative Principle'})
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=3, defaults={'source_id': 1, 'target_id': 3, 'relationship_type_id': 1, 'description': 'Created Gricean Maxims'})
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=4, defaults={'source_id': 1, 'target_id': 4, 'relationship_type_id': 2, 'description': 'Influenced Pragmatics'})
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=5, defaults={'source_id': 1, 'target_id': 5, 'relationship_type_id': 2, 'description': 'Influenced Semantics'})
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=6, defaults={'source_id': 1, 'target_id': 1, 'relationship_type_id': 3, 'description': 'Published as H. P. Grice'})
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=7, defaults={'source_id': 1, 'target_id': 1, 'relationship_type_id': 3, 'description': 'Published as H. Paul Grice'})
        DetailedRelationship.objects.get_or_create(detailed_relationship_id=8, defaults={'source_id': 1, 'target_id': 1, 'relationship_type_id': 3, 'description': 'Published as Paul Grice'})

        # Insert data into Publications table
        Publications.objects.get_or_create(publication_id=1, defaults={'person': person, 'publication_name': 'Studies in the Way of Words'})
        Publications.objects.get_or_create(publication_id=2, defaults={'person': person, 'publication_name': 'Logic and Conversation'})

        # Insert data into POSTags table
        POSTags.objects.get_or_create(postag_id=1, defaults={'word': 'Herbert', 'tag': 'NNP'})
        POSTags.objects.get_or_create(postag_id=2, defaults={'word': 'Paul', 'tag': 'NNP'})
        POSTags.objects.get_or_create(postag_id=3, defaults={'word': 'Grice', 'tag': 'NNP'})
        POSTags.objects.get_or_create(postag_id=4, defaults={'word': 'create', 'tag': 'VB'})
        POSTags.objects.get_or_create(postag_id=5, defaults={'word': 'theory', 'tag': 'NN'})

        # Insert data into NERtags table
        NERtags.objects.get_or_create(nertag_id=1, defaults={'entity': 'Herbert Paul Grice', 'type': 'PERSON'})
        NERtags.objects.get_or_create(nertag_id=2, defaults={'entity': 'Theory of Implicature', 'type': 'WORK_OF_ART'})
        NERtags.objects.get_or_create(nertag_id=3, defaults={'entity': 'Cooperative Principle', 'type': 'WORK_OF_ART'})

        # Insert data into NER_POS_Link table
        NER_POS_Link.objects.get_or_create(link_id=1, defaults={'nertag_id': 1, 'postag_id': 1})
        NER_POS_Link.objects.get_or_create(link_id=2, defaults={'nertag_id': 1, 'postag_id': 2})
        NER_POS_Link.objects.get_or_create(link_id=3, defaults={'nertag_id': 1, 'postag_id': 3})
        NER_POS_Link.objects.get_or_create(link_id=4, defaults={'nertag_id': 2, 'postag_id': 4})
        NER_POS_Link.objects.get_or_create(link_id=5, defaults={'nertag_id': 2, 'postag_id': 5})

        # Insert data into Location table
        harborne, created = Location.objects.get_or_create(location_id=1, defaults={'location_name': 'Harborne', 'parent_location': None})
        birmingham, created = Location.objects.get_or_create(location_id=2, defaults={'location_name': 'Birmingham', 'parent_location': harborne})
        uk, created = Location.objects.get_or_create(location_id=3, defaults={'location_name': 'United Kingdom', 'parent_location': None})
        clifton_college, created = Location.objects.get_or_create(location_id=4, defaults={'location_name': 'Clifton College', 'parent_location': uk})
        corpus_christi, created = Location.objects.get_or_create(location_id=5, defaults={'location_name': 'Corpus Christi College, Oxford', 'parent_location': uk})
        rossall_school, created = Location.objects.get_or_create(location_id=6, defaults={'location_name': 'Rossall School', 'parent_location': uk})
        merton_college, created = Location.objects.get_or_create(location_id=7, defaults={'location_name': 'Merton College', 'parent_location': uk})
        st_johns_college, created = Location.objects.get_or_create(location_id=8, defaults={'location_name': 'St John\'s College', 'parent_location': uk})
        royal_navy, created = Location.objects.get_or_create(location_id=9, defaults={'location_name': 'Royal Navy', 'parent_location': uk})
        uc_berkeley, created = Location.objects.get_or_create(location_id=10, defaults={'location_name': 'University of California, Berkeley', 'parent_location': None})

        # Insert data into Event table
        born_event, created = Event.objects.get_or_create(event_id=1, defaults={'event_name': 'Born in Harborne', 'location': harborne, 'start_date': '1913-03-13', 'related_person': person})
        educated_event, created = Event.objects.get_or_create(event_id=2, defaults={'event_name': 'Educated at Clifton College', 'location': clifton_college, 'related_person': person})
        studied_event, created = Event.objects.get_or_create(event_id=3, defaults={'event_name': 'Studied at Corpus Christi College, Oxford', 'location': corpus_christi, 'related_person': person})
        taught_event, created = Event.objects.get_or_create(event_id=4, defaults={'event_name': 'Taught at Rossall School', 'location': rossall_school, 'related_person': person})
        graduate_student_event, created = Event.objects.get_or_create(event_id=5, defaults={'event_name': 'Graduate student at Merton College', 'location': merton_college, 'start_date': '1936-01-01', 'end_date': '1938-01-01', 'related_person': person})
        lecturer_event, created = Event.objects.get_or_create(event_id=6, defaults={'event_name': 'Lecturer, Fellow, and Tutor at St John\'s College', 'location': st_johns_college, 'start_date': '1938-01-01', 'end_date': '1967-01-01', 'related_person': person})
        served_event, created = Event.objects.get_or_create(event_id=7, defaults={'event_name': 'Served in the Royal Navy', 'location': royal_navy, 'related_person': person})
        professor_event, created = Event.objects.get_or_create(event_id=8, defaults={'event_name': 'Professor at University of California, Berkeley', 'location': uc_berkeley, 'start_date': '1967-01-01', 'end_date': '1988-08-28', 'related_person': person})
        lecture_event, created = Event.objects.get_or_create(event_id=9, defaults={'event_name': 'John Locke lectures on Aspects of Reason', 'location': uk, 'start_date': '1979-01-01', 'related_person': person})

        # Insert data into Verb table
        verbs = {
            'be born': ['Born in Harborne'],
            'educate': ['Educated at Clifton College'],
            'study': ['Studied at Corpus Christi College, Oxford', 'Graduate student at Merton College'],
            'teach': ['Taught at Rossall School'],
            'serve': ['Served in the Royal Navy'],
            'lecture': ['Lecturer, Fellow, and Tutor at St John\'s College', 'John Locke lectures on Aspects of Reason'],
            'profess': ['Professor at University of California, Berkeley'],
            'give lectures': ['John Locke lectures on Aspects of Reason'],
            'publish': ['Studies in the Way of Words', 'Logic and Conversation']
        }
        for verb_name, event_names in verbs.items():
            verb, created = Verb.objects.get_or_create(verb_name=verb_name)
            for event_name in event_names:
                events = Event.objects.filter(event_name=event_name)
                for event in events:
                    event.verbs.add(verb)
            if verb_name in ['be born', 'educate', 'study', 'teach', 'serve', 'lecture', 'profess']:
                person.verbs.add(verb)
            if verb_name == 'publish':
                for publication in Publications.objects.filter(person=person):
                    person.verbs.add(verb)

        # Insert spouse
        spouse, created = Person.objects.get_or_create(
            person_id=2, defaults={'full_name': 'Kathleen Watson', 'nationality': 'British', 'gender': 'Female', 'occupation_id': 1, 'primary_field_id': 1}
        )

        # Insert spouse relationship
        DetailedRelationship.objects.get_or_create(
            detailed_relationship_id=9, defaults={'source_id': 1, 'target_id': 2, 'relationship_type_id': 4, 'description': 'Married to Herbert Paul Grice'}
        )

        self.stdout.write(self.style.SUCCESS('Successfully inserted initial data'))
