# Homosaurus Processing Tools for Cataloguers

## Files and Workflow

### homosaurus-v3.xml

An XML download of the entire homosaurus v3 vocabulary from 2024-07-15. You can download an updated copy here: https://homosaurus.org/v3

### homosaurus_xml_all.xsl

An adaptation of Terry Reese's homosaurus_xml.xsl transform that accommodates an entire vocabulary download, rather than an individual record. 

Modifications:
* process a file of <record>s within a <record> tag.
* does not expect the <graph> tag that is an artefact of using MARCEdit to transform the JSONLD to XML. 
* ignore hasTopConcept, as Homosaurus currently uses it on every Concept to point to itself.
* normalize-space(.) on the comment string, as it's broken over several lines in the XML dump and the indentation gets carried into MARC as weird spacing issues.

To use wtih the download of XML, set up a translation in MarcEdit following the steps in [his Youtube Video](https://www.youtube.com/watch?v=FJsdQI3pZPQ). Select this transform. When selecting the "Original format", select "Other". Save the translation. Then use your translation to transform homosaurus-v3.xml to MARC Authority.

Alternately, use an XSLT processor with this transform to convert homosaurus-v3.xml into MARCXML.

### homosaurus_as_marc.mrc

The result of running the above transform, in MARCEdit, on homosaurus-v3.xml. A set of MARC Authority records.


## Support

Rosie Le Faive
github.com/rosiel
