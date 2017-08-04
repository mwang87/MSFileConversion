#!/usr/bin/python

import sys
import os
import subprocess
#import ming_parallel_library


PATH_TO_MSCONVERT = "pwiz_standalone\msconvert.exe"

def list_all_in_dir(directory):
    everything = [ os.path.join(directory,f) for f in os.listdir(directory) ]
    everything.sort()
    return everything

def main():
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    list_of_files = list_all_in_dir(input_path)

    allowed_extensions = [".mzXML", ".mzML", ".raw.", ".d", ".raw", ".RAW", ".wiff"]


    all_cmds = []

    for filename in list_of_files:
        if os.path.splitext(filename)[1] in allowed_extensions:
            relative_path = os.path.relpath(filename, input_path)
            target_filename = os.path.join(output_path, relative_path)
            target_directory = os.path.dirname(target_filename)
            #cmd = PATH_TO_MSCONVERT + " " + filename + ' --filter "peakPicking true 1-" ' + " --32 " + " --mzXML " + " -o " + target_directory + " --outfile " + target_filename
            cmd = PATH_TO_MSCONVERT + " " + filename + ' --filter "peakPicking true 1-" ' + " --32 " + " --mzML " + " -o " + target_directory + " --outfile " + os.path.splitext(target_filename)[0] + ".mzML"
            all_cmds.append(cmd)

    for cmd in all_cmds:
        try:
            print("Executing", cmd)
            subprocess.call(cmd, shell=True)
        except KeyboardInterrupt:
            raise
        except:
            print("Error executing", cmd)
    #ming_parallel_library.run_parallel_shellcommands(all_cmds, 4)

if __name__ == "__main__":
    main()
