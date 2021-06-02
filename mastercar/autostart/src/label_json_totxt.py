import json
import os
ROOT_DIR = ''
DIR = 'barracks'
FILES = os.listdir(DIR)
LABEL_FILE = '{}.txt'.format(DIR)
IMG_FILES = [item for item in FILES if item[-3:] == 'png' or item[-3:] == 'jpg']
JSON_FILES = [item for item in FILES if item[-4:] == 'json']
# img_suffix = IMG_FILES[0][-3:]

def check_img_exist():
    for file in JSON_FILES:
        file_prefix = file[:-4]
        if file_prefix + 'jpg' not in IMG_FILES and file_prefix + 'png' not in IMG_FILES:
            os.remove(os.path.join(DIR, file))
            JSON_FILES.remove(file)
            print('no img {}'.format(file_prefix))

def json2txt():
    with open(LABEL_FILE, 'w') as f:
        for file in JSON_FILES:
            img_prefix = file[:-4]
            if img_prefix + 'jpg' in IMG_FILES:
                img_name = img_prefix + 'jpg'
            else:
                img_name = img_prefix + 'png'
            img_with_path = os.path.join(ROOT_DIR, os.path.join(DIR, img_name))
            f.write(img_with_path)
            f.write('\t')
            with open(os.path.join(DIR, file), 'r') as json_f:
                # json_item = json_f.readline()
                label_dict = json.load(json_f)
                items = label_dict['shapes']
                for item in items:
                    label = item["label"]
                    all_items_str = json.dumps({'value': label,
                                      'coordinate': item['points']})
                    f.write(all_items_str)
                    f.write('\t')
                    # just for test
                    break
                    # end test
            f.write('\n')

if __name__ == '__main__':
    check_img_exist()
    json2txt()