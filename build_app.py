import os
import subprocess
import json

with open('config.json') as config_file:
    data = json.load(config_file)

#build_qa_android_cli = data["cli"]["build_qa_android_cli"]
init_native_cli = data["cli"]["init_native_cli"]

def buildApp(sample_app_path, sample_app_name, scheme, platform):
    scheme = scheme.lower()
    platform = platform.lower()
    build_cli_para = "build_" + scheme + "_" + platform + "_cli"
    build_command = sample_app_path + "/" + data["cli"][build_cli_para] + " > logs/build.log"
    init_native_command = sample_app_path + "/" + init_native_cli + " > logs/init_native.log"

    if platform == "android":
        build_file = sample_app_path + "/build/" + platform + "/" + sample_app_name + "CRM.apk"
    elif platform == "ios":
        build_file = sample_app_path + "/build/" + platform + "/" + sample_app_name + "CRM.ipa"
    else:
        print ("We only support Android and iOS build for now.")
        return "Error"

    cp_init = subprocess.run(init_native_command, shell=True
            , stdout=subprocess.PIPE
            , stderr=subprocess.PIPE
            )
    if cp_init.returncode == 0:
        print ("Native init is done.")
        cp_build = subprocess.run(build_command, shell=True
                , stdout=subprocess.PIPE
                , stderr=subprocess.PIPE
                )
        if cp_build.returncode == 0 and os.path.exists(build_file):
            print ("Build is done. Build file is at %s" % build_file)
            return "Done"
        else:
            print ("There seems some errors in building file. Code: %s" % cp_build.returncode)
            return "Error"
    else:
        print ("There seems some errors in the native init process. Code: %s" % cp_init.returncode)
        return "Error"