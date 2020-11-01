import subprocess
import sys
import re
import os
import pyfiglet


target_file = sys.argv[1] #Getting Subdomains
project_name = sys.argv[2] #Project Name
command2 = "mkdir "+project_name+"_jsfiles"
p2 = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE)


def banner():

	out = pyfiglet.figlet_format("Nature_JScraper")
	print(out)
	print("                                                                 v0.01")
	print("                                                                 by br33z3")




# -------------------------------------------------------------
# -----------------------notify--------------------------------

def notify( msg ):

	# https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e
	token  = CHANGEME
	chatid = CHANGEME
	command = "curl -s -X POST"+" \"https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chatid+"&text="+msg+"\""
	p4 = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)

# -----------------------notify--------------------------------
# -------------------------------------------------------------


# -------------------------------------------------------------
# -----------------------waybackurls---------------------------
def waybackurls():

	command = "cat "+target_file+" |"+"waybackurls"
	p1 = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
	output = p1.stdout.read()
	print("[+] All WayBackUrls Found")
#	file_name = project_name+"_waybackurls"
#	file = open(file_name, "a")
#	file.write(output.decode())
#	file.close()
#	print("[+] All WayBackUrls Writed To "+file_name)
	return output
# -----------------------waybackurls---------------------------
# -------------------------------------------------------------



# -------------------------------------------------------------
# -----------------------Convert_List--------------------------
def Convert( outputx ): 
    li = list(outputx.split("\n"))
    print("[+] Files Converted to List in WayBackUrls") 
    return li
# -----------------------Convert_List--------------------------
# -------------------------------------------------------------



# -------------------------------------------------------------
# -----------------------string_parse--------------------------

def string_parse( waybackurls_output ):

	res = list(filter(lambda x: '.js' in x, waybackurls_output))
	print("[+] Extracted JavaScript Files in WayBackUrls\n\n")
	for p in range(len(res)):
		print(res[p])
	return res

# -----------------------string_parse--------------------------
# -------------------------------------------------------------


# ------------------------------------------------------------------
# -----------------------Download JS Files--------------------------

def download_files( files ):

	length = len(files)
	print("\n\n[+] Downloading All JavaScript Files in WayBackUrls")
	pwd = os.getcwd()
	for i in range(length):
		command = "wget "+"\""+files[i]+"\""+" -P "+pwd+"/"+project_name+"_jsfiles -q"
		os.system(command)
	print("[+] All WayBackUrls JavaScript Files Downloaded Successfully")


# -----------------------Download JS Files--------------------------
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# -----------------------get JS Function----------------------------

def getJS():

	print("[+] Finding Current JavaScript Files\n\n")
	getJS_list = []
	file_getJS = open(target_file, "r")
	for line in file_getJS:
		add = "http://"+line
		add_2 = "https://"+line
		add = add.rstrip("\n")
		add_2 = add_2.rstrip("\n")	
		getJS_list.append(add)
		getJS_list.append(add_2)

	
	pwd = os.getcwd()
	for x in range(len(getJS_list)):
		i = 0
		command2 = "getJS --url "+getJS_list[x]+" --complete"
		p2 = subprocess.Popen(command2,shell=True,stdout=subprocess.PIPE)
		output = p2.stdout.read()
		output = output.decode().strip() # Find all JavaScript Files
		lima = list(output.split("\n"))  # From raw input to list
		for m in range(len(lima)):
			print(lima[m])

		for i in range(len(lima)):
			command = "wget "+"\""+lima[i]+"\""+" -P "+pwd+"/"+project_name+"_jsfiles -q"
			os.system(command)
	print("\n\n[+] Downloading All Current JavaScript Files")
	print("[+] Finished Downloading All Current JavaScript Files")
	

# -----------------------get JS Function----------------------------
# ------------------------------------------------------------------

# -------------------------------------------------------------------
# -----------------------LinkFinder----------------------------------

def LinkFinder():

	print("\n[***]Searching For Interesting and Juicy Endpoints,api-keys inside all JavaScript Files")
	command3 = "python linkfinder.py -i '"+project_name+"_jsfiles/*.js'"+" -o results.html"
	p3 = subprocess.Popen(command3,shell=True,stdout=subprocess.PIPE)
	print("[***]Search Done Results Saved to results.html")

# -----------------------LinkFinder---------------------------------
# ------------------------------------------------------------------



if __name__ == "__main__":
	banner()
	print("\n\n[+] Finding All WayBackUrls")
	wbu_output = waybackurls() #Execute WayBackUrls
	wbu_output_list = Convert(wbu_output.decode()) #Convert String Output to List
	js_files = string_parse( wbu_output_list ) #Parse List and extract js Files
	download_files(js_files)
	getJS()
	LinkFinder()
	notify("Scan is Over")
	
	
