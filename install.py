import os


os.system("git clone https://github.com/GerbenJavado/LinkFinder.git")
os.system("cp LinkFinder/README.md .")
os.system("python LinkFinder/setup.py install")
os.system("pip2 install argparse")
os.system("pip2 install jsbeautifier")
os.system("pip3 install pyfiglet")
os.system("rm -rf build/ README.md dist/ LinkFinder.egg-info/")
os.system("mv LinkFinder/linkfinder.py LinkFinder/template.html .")
os.system("rm -rf LinkFinder")
