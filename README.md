# Palo VM-series Bootstrap

## Getting Started

``` bash
pip install -r requirements.txt
```

Modify the './templates/palo.jinja2' file to match the configuration you like'


## How to use once configured

``` bash
python3 configurator.py -a 10.0.0.1 -m 255.255.255.0 -g 10.0.0.254 -n test-firewall
```

- "-a" or "--address" is for the outside IP address of GigabitEthernet0/0
- "-m" or "--mask" is for the subnet mask for GigabitEthernet0/0
- "-g" or "--gateway" is the gateway for the outside interface
- "-n" or "--name" is the hostname of the firewall
- "-i" or "--id" is the id for the registration (optional)
- "-v" or "--value" is the value for the registration (optional)
- "-k" or "--key" for the auth token of the VM (optional)

## Next Steps
- [x] jinja templating to generate the configuration
- [x] folder structure created to be placed in the iso
- [ ] testing the iso on a lab Palo VM
