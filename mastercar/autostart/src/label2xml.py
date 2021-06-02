from xml.etree.ElementTree import Element, ElementTree
import os
import json

label_prefix = 'barracks'
label_file = '{}.txt'.format(label_prefix)
new_label = 'train_{}.txt'.format(label_prefix)
Label_DIR = 'Label/{}'.format(label_prefix)


def dict_to_xml(tag, d, sub_elem=None):
    elem = Element(tag)
    for key, value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    if sub_elem:
        for e in sub_elem:
            elem.append(e)
    return elem


with open(label_file, 'r') as f:
    with open(new_label, 'w+') as new:
        while True:
            line = f.readline()
            if not line:
                break
            items = line.strip().split('\t')
            objects = items[1:]
            dir_name = os.path.dirname(items[0])
            file_name = items[0].split('/')[-1]
            object_list = []
            for item in objects:
                dict_label = json.loads(item)

                name = dict_label['value']
                [xmin, ymin], [xmax, ymax] = dict_label['coordinate']
                bbox = dict_to_xml('bndbox',
                                   {'xmin': int(xmin), 'xmax': int(xmax), 'ymin': int(ymin), 'ymax': int(ymax)})

                object_ = dict_to_xml('object', {'name': name, 'difficult': 0}, [bbox])
                object_list.append(object_)
            anno = dict_to_xml('annotation', {"tmp": "tmp"}, object_list)
            tree = ElementTree(anno)
            # tree = ElementTree(object_)
            if not os.path.exists(Label_DIR):
                os.makedirs(Label_DIR)
            assert os.path.exists(Label_DIR)
            xml_label_path = os.path.join(Label_DIR, file_name[:-4]) + '.xml'
            # xml_path = '1.xml'
            xml_path = os.path.join(Label_DIR, file_name[:-4] + '.xml')
            tree.write(xml_path, encoding='utf-8')
            new.write(items[0])
            new.write(' ')
            new.write(xml_label_path)
            new.write('\n')


