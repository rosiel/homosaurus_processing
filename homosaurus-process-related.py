#!/usr/bin/env/python3

##
# This script adds the prefLabel for related terms to the
# items in the Linked Data vocabulary, Homosaurus.
# It takes as input a jsonld file that is the full dump
# of the homosaurus vocabulary. For related entities (broader,
# narrower, top concept, and related), it adds the prefLabel
# based on a lookup in the same file. Then, when turned into
# MARC by Terry Reese's XSLT (or derivative), the resulting
# MARC Authority records will have the textual form of related
# terms instead of just their URIs.
##

import json

raw_data_filename = 'homosaurus.jsonld'
output_filename = raw_data_filename.replace('.jsonld','-processed.jsonld')


def getPrefName(item, data):
    target = [x for x in data['@graph'] if x['@id']==item['@id']]
    if len(target) < 1:
        print("Not found for @id {}".format(item['@id']))
        return item
    item['skos:prefLabel'] = target[0]['skos:prefLabel']
    return item


data = json.load(open(raw_data_filename, 'r'))
if not(data):
    print('Data did not load.')
    exit(1)
for term in data['@graph']:
    # Loop over the related categories.
    relators = ['skos:broader', 'skos:hasTopConcept', 'skos:narrower', 'skos:related']
    for relator in relators:
        # Check if that term has that relator property
        if relator in term:
            related = term[relator]
            if isinstance(related, dict):  # We have a single item.
                related = getPrefName(related, data)
            else:  # We have a list.
                for related_item in related:
                    related_item = getPrefName(related_item, data)

with open(output_filename, 'w') as f:
    json.dump(data, f)
