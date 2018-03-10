'''A tool for listing images that will be built from a given docker-compose yaml file.
'''
import yaml
from optparse import OptionParser


def get_image_names(yaml_file):
    data = yaml.load(open(yaml_file))
    return [k for k, v in data['services'].iteritems() if v.get('build', None)]

if __name__ == '__main__':
    usage = '''\
    %prog

    To list names of images to be built from a compose yaml file.
    '''
    parser = OptionParser(usage=usage)

    parser.add_option(
        "-f", "--yaml-file", dest="yaml_file", help="Name of the Yaml file.")

    (cmd_options, _) = parser.parse_args()

    image_names = get_image_names(str(cmd_options.yaml_file))
    print(' '.join(str(e) for e in image_names))
