

from lxml import objectify, etree

from radioportal.models import *

# Docs for lxml: http://lxml.de/objectify.html#tree-generation-with-the-e-factory
# Docs for django ORM: https://docs.djangoproject.com/en/1.7/topics/db/queries/#retrieving-objects
# See radioportal/models.py for data structure

def generate_xml():
    E = objectify.ElementMaker(annotate=False)
    root = E.root(
        E.child1("value"),
        E.child2("anothervalue"),
    )

    root.shows = E.shows()

    for s in Show.objects.all():
        root.shows.append(E.show(s.name))

    root.child3 = E.child3("some other value")

    setattr(root, "child-4", E.child4("Mit Bindestrich"))

    return etree.tostring(root, pretty_print=True)


if __name__ == "__main__":
    print generate_xml()
    
