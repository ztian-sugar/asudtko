from install_sdk import *
import os
import json
import argparse

with open('config.json') as config_file:
    data = json.load(config_file)

sdk_install_path = data["SDK_install_path"]
sample_app_path = data["sample_app_path"]

parser = argparse.ArgumentParser(description='')
parser.add_argument('sdkFile', type=str, help='SDK file with path')
args = parser.parse_args()

sdk_file = args.sdkFile


# 1. install sdk file to

if sdk_file == '':
    print ("SDK file needs to pass in CLI.")
else:
    print ("+++Start SDK installation process...")
    install = install_sdk(sdk_file)
    if install == "Done":
        print ("+++Complete SDK installation process.")
        os.remove(sdk_file)
    elif install == "Error":
        print ("!!!SDK installation process have errors, please check")



