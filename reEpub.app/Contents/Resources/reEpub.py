import os, os.path
import zipfile
import sys

def reassemble (dir, rootdir):    
    if not dir == "pewpew.py" and not dir == "epubs":
        print ""
        print "zipping up: "+dir
        new_epub = zipfile.ZipFile(os.path.join(rootdir,(dir+".epub")),"w")
        new_epub.writestr("mimetype", "application/epub+zip", zipfile.ZIP_STORED)
        for subdir, dirs, files in os.walk(os.path.join(rootdir,dir), False):
            for name in files:
               
                target = os.path.join(subdir, name)
                new_target = target[len(os.path.join(dir,"")):]
                if not new_target == "mimetype":
                    print "writing "+new_target+" to "+dir+".epub"
                    new_epub.write(target,new_target)
        new_epub.close()

if (len(sys.argv) > 1):
    for filename in sys.argv[1:]:
        rootdir = os.path.dirname(os.path.realpath(filename))
        if os.path.exists(filename):
            reassemble(filename, rootdir)
        
    
    

