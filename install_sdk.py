from zipfile import ZipFile, ZipInfo
import os
import subprocess
import json
import shutil


with open('config.json') as config_file:
    data = json.load(config_file)

sdk_install_path = data["SDK_install_path"]

#Subclassing "ZipFile". Because Python ZipFile removes execute permissions from binaries
#The reason for this can be found in the _extract_member() method in zipfile.py,
#it only calls shutil.copyfileobj() which will write the output file without any execute bits.
#The easiest way to solve this is by subclassing ZipFile and changing extract()
class MyZipFile(ZipFile):

    def extract(self, member, path=None, pwd=None):
        if not isinstance(member, ZipInfo):
            member = self.getinfo(member)

        if path is None:
            path = os.getcwd()

        ret_val = self._extract_member(member, path, pwd)
        attr = member.external_attr >> 16
        if attr != 0:
            os.chmod(ret_val, attr)
        return ret_val

    def extractall(self, path=None, members=None, pwd=None):
        if members is None:
            members = self.namelist()

        if path is None:
            path = os.getcwd()
        else:
            path = os.fspath(path)

        for zipinfo in members:
            self.extract(zipinfo, path, pwd)


def install_sdk(file):
    path = "./" + file[:-4]

    zf = MyZipFile(file, 'r')
    zf.extractall(path)
    zf.close()

    if os.path.exists(path):
        install_command = path + "/install"
        if os.path.exists(install_command):
            #subprocess.Popen(['chmod', '-R', '+x', path])
            cp = subprocess.run(install_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            #print (cp.returncode)
            if cp.returncode == 0:
                shutil.rmtree(path)
                print ("SDK is installed at %s" % sdk_install_path)
                return "Done"
            else:
                print ("There seems some errors in the installation process.")
                return "Error"
    else:
        print ("NO sdk extract folder.")
        return "Error"
