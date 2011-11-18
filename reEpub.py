import os, os.path
import zipfile
import sys
import time
import re
from PyQt4 import QtCore,QtGui
from mainUi import Ui_MainWindow

class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)
        self.targetproceses = 0
        self.currentprocess = 0 
    
    def dragEnterEvent(self, e):
        if e.mimeData().hasUrls:
            e.accept()
        else:
            e.ignore()
            
    def get_file_count(self, directory):
        counter = 0
        for subdir, dirs, files in os.walk(directory, False):
            for name in files:
                counter = counter +1
        return counter
    
    def get_process_count(self, directory):
        files = self.get_file_count(directory)
        processes = files
        if os.path.exists(directory+".epub"):
            processes = processes + 1
        if os.path.exists(os.path.join(directory, "mimetype")):
            processes = processes + 1
        return processes+1
    
    def update_progress (self, parseText):
        if self.currentprocess < self.targetproceses:
            self.currentprocess = self.currentprocess + 1
        perc = (float(self.currentprocess)/float(self.targetproceses))*100
        self.ui.progressBarRunning.setProperty("value", perc)
        self.ui.labelProgress.setText(parseText)
        #print parseText
    
    def reassemble (self, directory, rootdir):
        self.ui.labelProgress.setText(os.path.basename(directory)+": checking...")
        self.targetproceses = self.get_process_count (os.path.join(rootdir,directory))
        self.currentprocess = 0
        if os.path.exists(os.path.join(rootdir,(directory+".epub"))):
            if self.ui.radioButtonArchive.isChecked():
                self.update_progress(os.path.basename(directory)+": archiving original...")
                os.rename(os.path.join(rootdir,(directory+".epub")), os.path.join(rootdir,(directory+"-"+str(int(time.time()))[5:]+".epub")))
                self.update_progress(os.path.basename(directory)+": creating new EPUB file")
            else:
                self.targetproceses = self.targetproceses - 1
                self.update_progress(os.path.basename(directory)+": overwriting EPUB file")
        else:
            self.targetproceses = self.targetproceses - 1
            self.update_progress(os.path.basename(directory)+": overwriting EPUB file")
        new_epub = zipfile.ZipFile(os.path.join(rootdir,(directory+".epub")),"w")
        
        self.update_progress(os.path.basename(directory)+": adding mimetype")
        new_epub.writestr("mimetype", "application/epub+zip", zipfile.ZIP_STORED)
        for subdir, dirs, files in os.walk(os.path.join(rootdir,directory), False):
            for name in files:
                target = os.path.join(subdir, name)
                new_target = target[len(os.path.join(directory,"")):]
                if not new_target == "mimetype":
                    #print "writing "+new_target+" to "+directory+".epub"
                    self.update_progress(os.path.basename(directory)+": adding "+new_target +" to EPUB")
                    new_epub.write(target,new_target, zipfile.ZIP_DEFLATED)
        
        self.update_progress(os.path.basename(directory)+": Done")
        new_epub.close()
        
    def dropEvent(self, e):
        for indrag in e.mimeData().urls():
            target = str(indrag.toLocalFile())
            if target[len(target)-1] == "/":
                target = target[:len(target)-1]
            rootdir = os.path.dirname(os.path.realpath(target))
            #print indrag
            #print target
            #print rootdir
            if os.path.exists(target):
                #print "bungholio"
                self.reassemble(target, rootdir)

def main():
    app = QtGui.QApplication(sys.argv)
    
    window=Main()
    window.show()
    if (len(sys.argv) > 1):
        for filename in sys.argv[1:]:
            rootdir = os.path.dirname(os.path.realpath(filename))
            if os.path.exists(filename):
                window.reassemble(filename, rootdir)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
