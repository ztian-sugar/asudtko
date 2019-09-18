from zipfile import ZipFile
import os
import subprocess

with open('config.json') as config_file:
    data = json.load(config_file)

sdk_install_path = data["SDK_install_path"]
install_command = data["cli"]["generate_app_cli"]
#sample_app_path = data["sample_app_path"]

def unzip(file):
    path = "./"
    zf = ZipFile(file, 'r')
    zf.extractall(path)
    zf.close()

#sdk_folder = "./sdk/"
def install_sdk():
    if os.path.exists("sdk/"):
        install = install_command + sdk_install_path
        subprocess.popen(install)
        print ("SDK is installed at %s" % sdk_install_path)
        os.rmdir("sdk")
    else:
        print ("NO sdk extract folder.")