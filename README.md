# Homosaurus Processing Tools for Cataloguers

## Files and Workflow

### homosaurus.jsonld

A JSON-LD dump of the entire homosaurus v3 vocabulary from 2024-07-10. You can download an updated copy here: https://homosaurus.org/v3. Note: You could skip the following "processing" step if you use the XML dump (I didn't realize at the time, but it contains the prefLabels for the related terms.). 

### homosaurus-process-related.py

A python script that finds all related term fields (broader, narrower, top concept, and related) and adds the skos:prefLabel (looked up in the same file). If you don't do this, the related terms only contain URIs. (Or, skip this by using the XML dump. As of July 2024 the XML file contains this already)

### homosaurus-processed.jsonld

This is the result of running homosaurus-process-related.py on homosaurus.jsonld. 

### homosaurus_xml_all.xsl

An adaptation of Terry Reese's homosaurus_xml.xsl transform that accommodates an entire vocabulary dump, rather than an individual record. Set up a translation in MarcEdit following the steps in [his Youtube Video](https://www.youtube.com/watch?v=FJsdQI3pZPQ) but select this transform. Then use your translation to transform homosaurus-processed.jsonld to MARC Authority. 


## Support

Rosie Le Faive
github.com/rosiel
