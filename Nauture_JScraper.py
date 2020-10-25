import subprocess
import sys
import re
import os


target_file = sys.argv[1] #Getting Subdomains
project_name = sys.argv[2] #Project Name
command2 = "mkdir "+project_name+"_jsfiles"
p2 = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE)

# -------------------------------------------------------------
# -----------------------waybackurls---------------------------
def waybackurls():
	command = "cat "+target_file+" |"+"waybackurls"
	p1 = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	output = p1.stdout.read()
	return output
# -----------------------waybackurls---------------------------
# -------------------------------------------------------------



# -------------------------------------------------------------
# -----------------------Convert_List--------------------------
def Convert( outputx ): 
    li = list(outputx.split("\n")) 
    return li
# -----------------------Convert_List--------------------------
# -------------------------------------------------------------



# -------------------------------------------------------------
# -----------------------string_parse--------------------------

def string_parse( waybackurls_output ):

	res = list(filter(lambda x: '.js' in x, waybackurls_output))
	return res

# -----------------------string_parse--------------------------
# -------------------------------------------------------------


# ------------------------------------------------------------------
# -----------------------Download JS Files--------------------------

def download_files( files ):

	pwd = os.getcwd()
	length = len(files)
	for i in range(length):
		command = "wget "+files[i]+" -P "+pwd+"/"+project_name+"_jsfiles"
		os.system(command)


# -----------------------Download JS Files--------------------------
# ------------------------------------------------------------------

if __name__ == "__main__":

    wbu_output = waybackurls() #Execute WayBackUrls
    wbu_output_list = Convert(wbu_output.decode()) #Convert String Output to List
    js_files = string_parse( wbu_output_list ) #Parse List and extract js Files
    download_files(js_files)






