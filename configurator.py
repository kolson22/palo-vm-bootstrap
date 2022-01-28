#!/usr/bin/env python3

try:
    import os
    import argparse
    import pycdlib
    from jinja2 import Template
except ImportError:
    print("you need to make sure pycdlib and argparse are installed")

# get the arguments from the cli
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--address",
                    help="The IP address of the outside of the firewall",
                    required=True)
parser.add_argument("-m", "--mask",
                    help="The subnet mask, ex: 255.255.255.0",
                    required=True)
parser.add_argument("-g", "--gateway",
                    help="The default gateway of the outside",
                    required=True)
parser.add_argument("-n", "--name",
                    help="The hostname of the firewall",
                    required=True)
parser.add_argument("-i", "--id",
                    help="The vm series id registration")
parser.add_argument("-v", "--value",
                    help="The vm series value for registration")
parser.add_argument("-k", "--key",
                    help="The vm auth token")
args = parser.parse_args()

# open the template file to build the configuration
with open('./templates/palo.jinja2') as template_file:
    template = Template(template_file.read())

# make a rendered configuration with the args as variables
config_output = template.render(
    address=args.address,
    mask=args.mask,
    gateway=args.gateway,
    hostname=args.name,
    id=args.id,
    value=args.value,
    key=args.key,
)

folders = [
        'config',
        'content',
        'software',
        'license',
        'plugins'
        ]

# write the rendered configuration to the day0 config file
config_file = open("init-cfg.txt", "w")
config_file.write(config_output)
config_file.write("\n")
config_file.close()

# create the iso object and place the files in there
iso = pycdlib.PyCdlib()
iso.new(joliet=3, vol_ident=args.name.upper())
for folder in folders:
    iso.add_directory('/' + folder.upper(), joliet_path="/" + folder)
iso.add_file("init-cfg.txt", joliet_path="/config/init-cfg.txt")
iso.write(args.name + '.iso')
iso.close()

os.remove('init-cfg.txt')
print("Successfully created the boostrap iso: ./" + args.name + '.iso')
