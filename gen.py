#!/usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals

import os
import re
from operator import itemgetter
from xml.etree import cElementTree as ET

import pathlib2
import jinja2
import tabulate

SOURCE = pathlib2.Path(os.getcwd()) / 'source'
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader([
        (SOURCE / '_templates').as_posix(),
        (SOURCE / 'examples').as_posix(),
    ])
)
CLASS_TEMPLATE = env.get_template('class.txt')
PROPERTY_TEMPLATE = env.get_template('property.txt')
METHOD_TEMPLATE = env.get_template('method.txt')
INDEX_TEMPLATE = env.get_template('index.txt')
ADDITIONS = {
    'Core': {
        'class': {
            'UnitRect.rst',
            'UnitPoint.rst',
            'FileArray.rst',
            'AliasArray.rst',
        }
    }
}
EXCLUDE = [
    'Photoshop/global',
    'Photoshop/Point'
]


def getTable(data):
    table = [['**{}**'.format(_['name']), _['short_description']] for _ in data]
    return tabulate.tabulate(table, tablefmt='grid')


def getRefTable(data):
    data = sorted(data, key=itemgetter('name'))
    table = [[':ref:`{0}<{1}>` readonly'.format(_['name'], _['namespace']), _['short_description']] for _ in data]
    return tabulate.tabulate(table, tablefmt='grid')


def getProperties(element, elmtype):
    data = []
    for child in element.findall("elements[@type='{}']/property".format(elmtype)):
        p = dict(child.attrib)
        p['classname'] = element.attrib['name']
        p['return_type'] = getRefType(child.findall('datatype/type')[0].text)
        p['short_description'], p['description'] = getDescriptions(child)
        p['namespace'] = '{}.{}'.format(element.attrib['name'], p['name'])
        data.append(p)

    return data


def getMethods(element, elmtype):
    data = []
    for child in element.findall("elements[@type='{}']/method".format(elmtype)):
        p = dict(child.attrib)
        p['classname'] = element.attrib['name']
        types = child.findall('datatype/type')
        if types:
            p['return_type'] = getRefType(types[0].text)
        else:
            p['return_type'] = 'void'

        p['short_description'], p['description'] = getDescriptions(child)
        p['namespace'] = '{}.{}'.format(element.attrib['name'], p['name'])
        p['parameters'] = getParameters(child)
        p['param_table'] = getTable(p['parameters'])
        data.append(p)

    return data


def getParameters(element):
    data = []
    for child in element.findall('parameters/parameter'):
        p = dict(child.attrib)
        p['type'] = getRefType(child.findall('datatype/type')[0].text)
        p['short_description'], p['description'] = getDescriptions(child)
        data.append(p)

    return data


def sanitizeText(text):
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.replace('’', '\'')
    text = text.replace('—', '-')
    text = text.replace('&#160;', ' ')

    return text.encode('utf8')


def getRefType(data):
    prim = ('int', 'bool', 'any', 'uint', 'undefined', 'null')
    if data.lower() in prim:
        return data.lower()

    return ':ref:`{}`'.format(data)


def getDescriptions(element):
    desc = element.find('description')
    short = element.find('shortdesc')

    description = ''
    shortdescription = ''

    try:
        description = ''.join(desc.itertext()).strip().encode('ascii', 'replace').replace('\t', '').replace('\n', ' ')
    except AttributeError:
        pass

    try:
        shortdescription = ''.join(short.itertext()).strip().encode('ascii', 'replace').replace('\t', '').replace('\n', ' ')
    except AttributeError:
        pass

    return shortdescription, description


def main(root, filename):
    xml = ET.parse((SOURCE / filename).as_posix())
    classes = []
    enumerations = []

    if root in ADDITIONS:
        classes += ADDITIONS[root].get('class', [])
        enumerations += ADDITIONS[root].get('enumeration', [])

    # for classdef in xml.findall("./package/classdef[@name='ColorSamplers']"):
    for classdef in xml.findall("./package/classdef[@dynamic]"):
        data = {
            'name': classdef.attrib['name'],
            'properties': getProperties(classdef, 'instance'),
            'methods': getMethods(classdef, 'instance'),
            'static_properties': getProperties(classdef, 'class'),
            'static_methods': getMethods(classdef, 'class'),
            'event_methods': getMethods(classdef, 'event'),
            'constructors': getMethods(classdef, 'constructor'),
        }
        data['short_description'], data['description'] = getDescriptions(classdef)

        if '{}/{}'.format(root, data['name']) in EXCLUDE:
            continue

        data['properties_table'] = getRefTable(data['properties'])
        data['methods_table'] = getRefTable(data['methods'])
        data['static_properties_table'] = getRefTable(data['static_properties'])
        data['static_methods_table'] = getRefTable(data['static_methods'])
        data['event_methods_table'] = getRefTable(data['event_methods'])
        data['constructors_table'] = getRefTable(data['constructors'])

        for key, value in data.iteritems():
            if isinstance(value, list):
                for _ in data[key]:
                    _['module'] = root

        content = sanitizeText(CLASS_TEMPLATE.render(**data))

        # Write class file
        outfile = SOURCE / root / '{}.rst'.format(data['name'])
        if not outfile.parent.exists():
            outfile.parent.mkdir(parents=True)
        outfile.write_bytes(content)
        classes.append(outfile.name)

        # Write out Property/Method files
        for property in data['properties'] + data['static_properties']:
            content = sanitizeText(PROPERTY_TEMPLATE.render(**property))

            # Write class file
            outfile = SOURCE / root / data['name'] / '{}.rst'.format(property['name'])
            if not outfile.parent.exists():
                outfile.parent.mkdir(parents=True)
            outfile.write_bytes(content)

        for method in data['methods'] + data['static_methods'] + data['event_methods'] + data['constructors']:
            content = sanitizeText(METHOD_TEMPLATE.render(**method))

            # Write class file
            outfile = SOURCE / root / data['name'] / '{}.rst'.format(method['name'])
            if not outfile.parent.exists():
                outfile.parent.mkdir(parents=True)
            outfile.write_bytes(content)

    # (SOURCE / root / 'index.rst').write_text(INDEX_TEMPLATE.render(name=root.capitalize(), classes=classes))

    for classdef in xml.findall("./package/classdef[@enumeration='true']"):
        data = {
            'name': classdef.attrib['name'],
            'description': classdef.find('shortdesc').text,
            'properties': getProperties(classdef, 'instance'),
            'methods': getMethods(classdef, 'instance'),
            'static_properties': getProperties(classdef, 'class'),
            'static_methods': getMethods(classdef, 'class'),
            'event_methods': getMethods(classdef, 'event'),
            'constructors': getMethods(classdef, 'constructor'),
        }
        data['properties_table'] = getRefTable(data['properties'])
        data['methods_table'] = getRefTable(data['methods'])
        data['static_properties_table'] = getRefTable(data['static_properties'])
        data['static_methods_table'] = getRefTable(data['static_methods'])
        data['event_methods_table'] = getRefTable(data['event_methods'])
        data['constructors_table'] = getRefTable(data['constructors'])

        content = sanitizeText(CLASS_TEMPLATE.render(**data))

        # Write class file
        outfile = SOURCE / root / '{}.rst'.format(data['name'])
        if not outfile.parent.exists():
            outfile.parent.mkdir(parents=True)
        outfile.write_bytes(content)
        enumerations.append(outfile.name)

        # Write out Property/Method files
        for property in data['properties'] + data['static_properties']:
            content = sanitizeText(PROPERTY_TEMPLATE.render(**property))

            # Write class file
            outfile = SOURCE / root / data['name'] / '{}.rst'.format(property['name'])
            if not outfile.parent.exists():
                outfile.parent.mkdir(parents=True)
            outfile.write_bytes(content)

        for method in data['methods'] + data['static_methods'] + data['event_methods'] + data['constructors']:
            content = sanitizeText(METHOD_TEMPLATE.render(**method))

            # Write class file
            outfile = SOURCE / root / data['name'] / '{}.rst'.format(method['name'])
            if not outfile.parent.exists():
                outfile.parent.mkdir(parents=True)
            outfile.write_bytes(content)

    (SOURCE / root / 'index.rst').write_text(INDEX_TEMPLATE.render(name=root.capitalize(), classes=sorted(classes), enumerations=sorted(enumerations)))


def genJavaScript(root, filename):
    f = SOURCE / filename
    content = f.read_bytes()
    classes = [
        f.stem,
        '=' * len(f.stem),
        '',
        '',
        ''
    ]
    classtoc = []

    for match in re.finditer('@class\s(\w+)', content):
        docline = '.. js:autoclass:: {}\n   :members:\n\n'.format(match.groups()[0])
        classes.append(docline)
        classtoc.append('      * :js:class:`{}`'.format(match.groups()[0]))

    classes = classes[:3] + classtoc + classes[3:]

    rstcontent = '\n'.join(classes)

    output = SOURCE / root / '{}.rst'.format(f.stem)
    output.write_text(rstcontent)


if __name__ == '__main__':
    main('Photoshop', 'omv.xml')
    main('Core', 'javascript.xml')
    main('ScriptUI', 'scriptui.xml')
    genJavaScript('CEP', 'CSInterface.js')
