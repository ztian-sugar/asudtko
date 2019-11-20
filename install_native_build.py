import os
import subprocess
from time import sleep


def getPackageName(app_file):
    get_package_name_command = "aapt d badging " + app_file + " |grep package | cut -d\\' -f 2"
    #print (get_package_name_command)
    package_name = subprocess.run(get_package_name_command, shell=True
                 , stdout=subprocess.PIPE
                 , stderr=subprocess.PIPE)
    return package_name.stdout.decode("utf-8")[:-1]


def installNative(app_file, device):
    #--- building bash command
    install_command = "adb install -r " + app_file
    package_name = getPackageName(app_file)
    launch_app_command = "adb shell monkey -p " + package_name + " 1"
    start_device_command = "nohup emulator -avd " + device
    shutdown_device_command = "adb emu kill"

    #--- start device/emulator
    print ("launch device...")
    device = subprocess.Popen(start_device_command, shell=True
           , stdout=subprocess.PIPE
           , stderr=subprocess.PIPE)
    sleep(5)
    print ("...device launched")
    #--- install app
    print ("install app...")
    install = subprocess.run(install_command, shell=True
            , stdout=subprocess.PIPE
            , stderr=subprocess.PIPE)
    sleep(5)
    print ("...app installed")
    #--- launch app
    print ("launch app...")
    launch = subprocess.run(launch_app_command, shell=True
           , stdout=subprocess.PIPE
           , stderr=subprocess.PIPE)
    sleep(5)
    print ("...app launched")
    #--- shutdown device/emulator
    print ("shutdown device...")
    shutdown = subprocess.run(shutdown_device_command, shell=True
             , stdout=subprocess.PIPE
             , stderr=subprocess.PIPE)
    sleep(5)
    print ("...device is down")

    return "Done"
