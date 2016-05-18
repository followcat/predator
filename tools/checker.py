import glob
import utils.builtin
import os.path

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-y", "--yamlfile",
    dest="yamlname", help="urls yaml file", metavar="FILE")
parser.add_option("-i", "--inputpath",
    dest="inputpath", help="input path")
(options, args) = parser.parse_args()

if __name__ == '__main__':
    yaml_path, yaml_file = os.path.split(options.yamlname)
    inputpath = options.inputpath
    y = utils.builtin.load_yaml(yaml_path, yaml_file)
    count_wrong = 0
    count_passage = 0
    for id_str in y:
        yaml_name = id_str + '.yaml'
        md_name = id_str + '.md'
        try:
            data = utils.builtin.load_yaml(inputpath, yaml_name)
        except IOError:
            continue
        exep = data['experience']
        school = data['school']
        count_passage += 1
        for each in exep:
            try:
                company_exep = each[2].split("|")[1]
            except IndexError:
                continue
            with open(os.path.join(inputpath, md_name)) as fp:
                text = fp.read() 
            if school[1:].lstrip().rstrip() not in text.decode('utf-8') and\
            company_exep.lstrip().rstrip() not in text.decode('utf-8'):
                count_wrong += 1
                print id_str
                break
        if count_wrong == 3:
            break

    print count_wrong
    print count_passage


