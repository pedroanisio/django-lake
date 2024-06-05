from django.contrib import admin
from .models import Occupation, FieldOfStudy, Person, PersonFieldOfStudy, Alias, Concept, Contributions, RelationshipType, DetailedRelationship, Publications, POSTags, NERtags, NER_POS_Link

admin.site.register(Occupation)
admin.site.register(FieldOfStudy)
admin.site.register(Person)
admin.site.register(PersonFieldOfStudy)
admin.site.register(Alias)
admin.site.register(Concept)
admin.site.register(Contributions)
admin.site.register(RelationshipType)
admin.site.register(DetailedRelationship)
admin.site.register(Publications)
admin.site.register(POSTags)
admin.site.register(NERtags)
admin.site.register(NER_POS_Link)
