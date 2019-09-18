import os
import subprocess
import json

with open('config.json') as config_file:
    data = json.load(config_file)

generate_command = data["cli"]["generate_app_cli"]
#sample_app_path = data["sample_app_path"]

#sdk_folder = "./sdk/"
def generate_sample_app(sdk_path, app_name, app_path):

    #temp solution to bypass the Android generating release key when create sample app
    #by removing the lines of code in tools/tasks/generate-custom-config
    file_to_remove_line = sdk_path + "/tools/tasks/generate-custom-config.js"
    remove_lines_in_file(file_to_remove_line, "86", "91")

    generate_command = sdk_path + "/" + data["cli"]["generate_app_cli"] + " " + app_name + " " + app_path + " > logs/generate_sample_app.log"
    #print (generate_command)
    cp = subprocess.run(generate_command, shell=True
        , stdout=subprocess.PIPE
        , stderr=subprocess.PIPE
        )
    if cp.returncode == 0:
        print ("Sample app is created at %s" % app_path + "/" + app_name)
        return "Done"
    else:
        print ("There seems some errors in the sample app generation process. Code: %s" % cp.returncode)
        return "Error"



def remove_lines_in_file(file, line_start, line_end):
    remove_command = "sed " + "-i.bak " + "'" + line_start + "," + line_end + "d' " + file
    #print (remove_command)
    subprocess.run(remove_command, shell=True
            , stdout=subprocess.PIPE
            , stderr=subprocess.PIPE
            )

