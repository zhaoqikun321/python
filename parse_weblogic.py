# Create your views here.
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import sys

config_file = 'weblogic.xml'
config_file2 = 'config.xml'

def attr_gbk(elem, name):
    return elem.attrib.get(name).encode("GBK")


def attr_int(elem, name):
    return int(elem.attrib.get(name))


def attr_bool(elem, name):
    return bool(elem.attrib.get(name))


def attr(elem, *args):
    if len(args) > 1:
        result = []
        for name in args:
            result.append(attr(elem, name))
        return result

    [name] = args
    value = elem.attrib.get(name)
    if not value:
        return value
    elif isinstance(value, str):
        return value.encode("GBK")
    elif value.isdigit():
        return int(value)
    elif value.lower() in ["true", "false"]:
        return value.lower() == "true"
    else:
        return value


def fix_attribs(elem):
    dict_ = {}
    for key in elem.attrib:
        dict_.update({key: attr(elem, key)})
    return dict_


def build_dict(elem):
    if elem is not None:
        dict_ = {}


        for subelem in elem:
            #print (subelem.tag)
            if subelem.tag in dict_:
                if not isinstance(dict_[subelem.tag], list):
                    dict_[subelem.tag] = [dict_[subelem.tag]]
                dict_[subelem.tag].append(build_dict(subelem))
            else:
                dict_.update({subelem.tag: build_dict(subelem)})
            if subelem.text and subelem.text.strip():
                dict_.update({subelem.tag: {"_text": subelem.text}})
        dict_.update(fix_attribs(elem))
        return dict_
    else:
        return fix_attribs(elem)


if '__main__'==__name__:
    tree = ET.parse(config_file)
    root = tree.getroot()
    weblogic_configs = build_dict(root)
    tree = ET.parse(config_file2)
    root = tree.getroot()
    config_configs = build_dict(root)
    all_configs = {config_file: weblogic_configs, config_file2: config_configs}
    print(all_configs)