# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import sys

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QTreeWidgetItem
from PyQt4.QtCore import Qt

from .Ui_MainWindow import Ui_MainWindow

import clr
clr.AddReference("KeePassLib")

from KeePassLib import PwDefs

class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (QWidget)
        """
        super().__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_actionOpen_File_triggered(self):
        """
        Slot documentation goes here.
        """
        try:
            file = QFileDialog.getOpenFileName(
                None,
                self.trUtf8("Open Database File"),
                "C:\\temp",
                self.trUtf8("KeePass KDBX Files (*.kdbx);;All Files (*.*)"))
            
            if file == "" :
                # user selected "Cancel"
                return
            
            from KeePassLib.Serialization import  IOConnectionInfo
            fileConnection = IOConnectionInfo.FromPath(file)
            
            from KeePassLib.Keys import CompositeKey
            from KeePassLib.Keys import KcpPassword
            passoword = KcpPassword("test")
            compositeKey = CompositeKey()
            compositeKey.AddUserKey(passoword)
            
            from KeePassLib import PwDatabase
            database = PwDatabase()
            database.Open(fileConnection,  compositeKey,  None)
                    
            print("Successfully opened %s" % file)
        except:           
            e = sys.exc_info()[1]
            msgBox = QMessageBox()
            #TODO: show application name as title 
            msgBox.setWindowTitle("KeePassPQ")
            msgBox.setText(e.Message)
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.exec()
            
        self.load_db(database)
            
    def load_db(self,  pwDatabase):
        rootGroup = pwDatabase.RootGroup
        self.groupTreeWidget.clear()
        treeWidgetItem = self.recusive_add_group(self.groupTreeWidget,  rootGroup)
        self.groupTreeWidget.addTopLevelItem(treeWidgetItem)
        self.groupTreeWidget.currentItemChanged.connect(self.load_group_entries)       
        
    def recusive_add_group(self,  parentTreeWidgetItem,  pwGroup):
        treeWidgetItem = QTreeWidgetItem(parentTreeWidgetItem)
        treeWidgetItem.setText(0,  pwGroup.Name)
        treeWidgetItem.setData(1,  Qt.UserRole,  pwGroup)
        
        for childGroup in pwGroup.Groups:
            self.recusive_add_group(treeWidgetItem,  childGroup)
                
        treeWidgetItem.setExpanded(True)
        
        return treeWidgetItem
        
        
    @pyqtSlot(QTreeWidgetItem,  QTreeWidgetItem)
    def load_group_entries(self,  newItem,  oldItem):
        self.entryListWidget.clear()
        pwGroup = newItem.data(1,  Qt.UserRole)
        for entry in pwGroup.Entries:
            self.entryListWidget.addItem(entry.Strings.Get(PwDefs.TitleField).ReadString())
        
        
