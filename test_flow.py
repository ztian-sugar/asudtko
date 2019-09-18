from install_sdk import *
from generate_app import *
import os
import json
import argparse

with open('config.json') as config_file:
    data = json.load(config_file)

sdk_install_path = data["SDK_install_path"]
sample_app_install_path = data["sample_app_install_path"]

parser = argparse.ArgumentParser(description='')
parser.add_argument('sdkFile', type=str, help='SDK file with path')
args = parser.parse_args()

sdk_file = args.sdkFile
sdk_path = sdk_install_path + "/" + sdk_file[17:-4]
sample_app_name = sdk_file[17:25].replace('.', '')
sample_app_path = sample_app_install_path + "/" + sample_app_name


# 1. install sdk file

if sdk_file == '':
    print ("SDK file needs to pass in CLI.")
else:
    print ("+++Start SDK installation process...")
    install = install_sdk(sdk_file)
    if install == "Done":
        print ("+++Complete SDK installation process.")
        os.remove(sdk_file)
    elif install == "Error":
        print ("!!!SDK installation process has error, please check.")


# 2. generate sample app

if sample_app_name != '' and os.path.exists(sample_app_install_path) and os.path.exists(sdk_path):
    print ("+++Start sample app generation...")
    sample = generate_sample_app(sdk_path, sample_app_name, sample_app_install_path)
    if sample == "Done":
        print ("+++Complete sample app generation.")
    elif sample == "Error":
        print ("!!!Sample app generation has error, please check.")
else:
    print ("Something is wrong.")
