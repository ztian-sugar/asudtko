from install_sdk import *
from generate_app import *
from build_app import *
from install_native_build import *
import os
import json
import argparse

with open('config.json') as config_file:
    data = json.load(config_file)

sdk_install_path = data["SDK_install_path"]
sample_app_install_path = data["sample_app_install_path"]
android_device = data["android_emulator"]

parser = argparse.ArgumentParser(description='')
parser.add_argument('sdkFile', type=str, help='SDK file with path')
args = parser.parse_args()

sdk_file = args.sdkFile
sdk_path = sdk_install_path + "/" + sdk_file[17:-4]
sample_app_name = sdk_file[17:25].replace('.', '')
sample_app_path = sample_app_install_path + "/" + sample_app_name
android_build_file = sample_app_path + "/build/android/" + sample_app_name + "CRM.apk"
ios_build_file = sample_app_path + "/build/ios/" + sample_app_name + "CRM.ipa"

'''
#-- 1. install sdk file

if sdk_file == '':
    print ("SDK file needs to pass in CLI.")
else:
    print ("+++Start SDK installation process...")
    install = installSdk(sdk_file)
    if install == "Done":
        print ("+++Complete SDK installation process.")
        os.remove(sdk_file)
    elif install == "Error":
        print ("!!!SDK installation process has error, please check.")


#-- 2. generate sample app

if sample_app_name != '' and os.path.exists(sample_app_install_path) and os.path.exists(sdk_path):
    print ("+++Start sample app generation...")
    sample = generateSampleApp(sdk_path, sample_app_name, sample_app_install_path)
    if sample == "Done":
        print ("+++Complete sample app generation.")
    elif sample == "Error":
        print ("!!!Sample app generation has error, please check.")
else:
    print ("Something is wrong.")


#-- 3. build native android app from sample code

if sample_app_name != '' and os.path.exists(sample_app_path):
    print ("+++Start native init and Android app building...")
    qa_android = buildApp(sample_app_path, sample_app_name, "qa", "android")
    #qa_ios = buildApp(sample_app_path, sample_app_name, "qa", "ios")
    if qa_android == "Done":
            print ("+++Complete native init and Android app building.")
    elif qa_android == "Error":
            print ("!!!Native init or Android app building has error, please check.")
else:
    print ("Something is wrong.")

'''
#-- 4. install native build app to device/emulator

if android_device != '' and os.path.exists(android_build_file):
    print ("+++Start installing and launching android app on device...")
    launch = installNative(android_build_file, android_device)
    if launch == "Done":
        print ("+++Complete installing and launching app on device.")
    else:
        print ("!!!There are errors during installing and launching app on device")
else:
    print ("Something is wrong.")
