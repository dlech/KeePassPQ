# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\PyQt1\ui\MainWindow.ui'
#
# Created: Tue Jun  4 17:10:50 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(741, 455)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalTabWidget = QtGui.QTabWidget(self.centralWidget)
        self.verticalTabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.verticalTabWidget.setObjectName(_fromUtf8("verticalTabWidget"))
        self.verticalTabWidgetPage1 = QtGui.QWidget()
        self.verticalTabWidgetPage1.setObjectName(_fromUtf8("verticalTabWidgetPage1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalTabWidgetPage1)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalSplitter = QtGui.QSplitter(self.verticalTabWidgetPage1)
        self.horizontalSplitter.setOrientation(QtCore.Qt.Vertical)
        self.horizontalSplitter.setChildrenCollapsible(True)
        self.horizontalSplitter.setObjectName(_fromUtf8("horizontalSplitter"))
        self.widget = QtGui.QWidget(self.horizontalSplitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalSplitter = QtGui.QSplitter(self.widget)
        self.verticalSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.verticalSplitter.setObjectName(_fromUtf8("verticalSplitter"))
        self.sideBySideTextBrowser = QtGui.QTextBrowser(self.verticalSplitter)
        self.sideBySideTextBrowser.setVisible(False)
        self.sideBySideTextBrowser.setObjectName(_fromUtf8("sideBySideTextBrowser"))
        self.groupTreeWidget = QtGui.QTreeWidget(self.verticalSplitter)
        self.groupTreeWidget.setObjectName(_fromUtf8("groupTreeWidget"))
        self.entryListWidget = QtGui.QListWidget(self.verticalSplitter)
        self.entryListWidget.setObjectName(_fromUtf8("entryListWidget"))
        self.verticalLayout_3.addWidget(self.verticalSplitter)
        self.stackedTextBrowser = QtGui.QTextBrowser(self.horizontalSplitter)
        self.stackedTextBrowser.setObjectName(_fromUtf8("stackedTextBrowser"))
        self.verticalLayout.addWidget(self.horizontalSplitter)
        self.verticalTabWidget.addTab(self.verticalTabWidgetPage1, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.verticalTabWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 741, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOpen = QtGui.QMenu(self.menuFile)
        self.menuOpen.setObjectName(_fromUtf8("menuOpen"))
        self.menuOpen_Recent = QtGui.QMenu(self.menuFile)
        self.menuOpen_Recent.setObjectName(_fromUtf8("menuOpen_Recent"))
        self.menuSave_As = QtGui.QMenu(self.menuFile)
        self.menuSave_As.setObjectName(_fromUtf8("menuSave_As"))
        self.menuSynchronize = QtGui.QMenu(self.menuFile)
        self.menuSynchronize.setObjectName(_fromUtf8("menuSynchronize"))
        self.menuRecent_Files = QtGui.QMenu(self.menuSynchronize)
        self.menuRecent_Files.setObjectName(_fromUtf8("menuRecent_Files"))
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuShow_Entries_by_Tag = QtGui.QMenu(self.menuEdit)
        self.menuShow_Entries_by_Tag.setObjectName(_fromUtf8("menuShow_Entries_by_Tag"))
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menu_Window_Layout = QtGui.QMenu(self.menuView)
        self.menu_Window_Layout.setObjectName(_fromUtf8("menu_Window_Layout"))
        self.menu_Sort_By = QtGui.QMenu(self.menuView)
        self.menu_Sort_By.setObjectName(_fromUtf8("menu_Sort_By"))
        self.menuTAN_View_Options = QtGui.QMenu(self.menuView)
        self.menuTAN_View_Options.setObjectName(_fromUtf8("menuTAN_View_Options"))
        self.menu_Grouping_in_Entry_List = QtGui.QMenu(self.menuView)
        self.menu_Grouping_in_Entry_List.setObjectName(_fromUtf8("menu_Grouping_in_Entry_List"))
        self.menuTools = QtGui.QMenu(self.menuBar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))
        self.menu_Database_Tools = QtGui.QMenu(self.menuTools)
        self.menu_Database_Tools.setObjectName(_fromUtf8("menu_Database_Tools"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionNewDatabase = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_FileNew.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewDatabase.setIcon(icon)
        self.actionNewDatabase.setObjectName(_fromUtf8("actionNewDatabase"))
        self.actionCloseDatabase = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola_Derived/B16x16_File_Close.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCloseDatabase.setIcon(icon1)
        self.actionCloseDatabase.setObjectName(_fromUtf8("actionCloseDatabase"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_FileSave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionDatabaseSettings = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_Package_Development.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDatabaseSettings.setIcon(icon3)
        self.actionDatabaseSettings.setObjectName(_fromUtf8("actionDatabaseSettings"))
        self.actionChangeMasterKey = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_File_Locked.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChangeMasterKey.setIcon(icon4)
        self.actionChangeMasterKey.setObjectName(_fromUtf8("actionChangeMasterKey"))
        self.actionPrint = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_FilePrint.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon5)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionImport = QtGui.QAction(MainWindow)
        self.actionImport.setObjectName(_fromUtf8("actionImport"))
        self.actionExport = QtGui.QAction(MainWindow)
        self.actionExport.setObjectName(_fromUtf8("actionExport"))
        self.actionLock_Workspace = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Images/B16x16_LockWorkspace.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLock_Workspace.setIcon(icon6)
        self.actionLock_Workspace.setObjectName(_fromUtf8("actionLock_Workspace"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionOpen_File = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_Folder_Yellow_Open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_File.setIcon(icon7)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionOpen_Url = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola_Client/C01_Package_Network.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_Url.setIcon(icon8)
        self.actionOpen_Url.setObjectName(_fromUtf8("actionOpen_Url"))
        self.actionClear_List = QtGui.QAction(MainWindow)
        self.actionClear_List.setObjectName(_fromUtf8("actionClear_List"))
        self.actionSave_to_File = QtGui.QAction(MainWindow)
        self.actionSave_to_File.setObjectName(_fromUtf8("actionSave_to_File"))
        self.actionSave_to_URL = QtGui.QAction(MainWindow)
        self.actionSave_to_URL.setObjectName(_fromUtf8("actionSave_to_URL"))
        self.actionSave_copy_as = QtGui.QAction(MainWindow)
        self.actionSave_copy_as.setObjectName(_fromUtf8("actionSave_copy_as"))
        self.actionSynchronize_with_File = QtGui.QAction(MainWindow)
        self.actionSynchronize_with_File.setObjectName(_fromUtf8("actionSynchronize_with_File"))
        self.actionSynchronize_with_URL = QtGui.QAction(MainWindow)
        self.actionSynchronize_with_URL.setObjectName(_fromUtf8("actionSynchronize_with_URL"))
        self.actionClear_List_2 = QtGui.QAction(MainWindow)
        self.actionClear_List_2.setObjectName(_fromUtf8("actionClear_List_2"))
        self.actionAdd_Group = QtGui.QAction(MainWindow)
        self.actionAdd_Group.setObjectName(_fromUtf8("actionAdd_Group"))
        self.actionEdit_Group = QtGui.QAction(MainWindow)
        self.actionEdit_Group.setObjectName(_fromUtf8("actionEdit_Group"))
        self.actionDelete_Group = QtGui.QAction(MainWindow)
        self.actionDelete_Group.setObjectName(_fromUtf8("actionDelete_Group"))
        self.actionAdd_Entry = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_KGPG_Import.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Entry.setIcon(icon9)
        self.actionAdd_Entry.setObjectName(_fromUtf8("actionAdd_Entry"))
        self.actionEdit_View_Entry = QtGui.QAction(MainWindow)
        self.actionEdit_View_Entry.setObjectName(_fromUtf8("actionEdit_View_Entry"))
        self.actionDuplicate_Entry = QtGui.QAction(MainWindow)
        self.actionDuplicate_Entry.setObjectName(_fromUtf8("actionDuplicate_Entry"))
        self.actionDelete_Entry = QtGui.QAction(MainWindow)
        self.actionDelete_Entry.setObjectName(_fromUtf8("actionDelete_Entry"))
        self.actionShow_All_Entries = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_KGPG_Key3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShow_All_Entries.setIcon(icon10)
        self.actionShow_All_Entries.setObjectName(_fromUtf8("actionShow_All_Entries"))
        self.actionShow_All_Expired_Entries = QtGui.QAction(MainWindow)
        self.actionShow_All_Expired_Entries.setObjectName(_fromUtf8("actionShow_All_Expired_Entries"))
        self.action_No_tags_found = QtGui.QAction(MainWindow)
        self.action_No_tags_found.setEnabled(False)
        self.action_No_tags_found.setObjectName(_fromUtf8("action_No_tags_found"))
        self.actionFind = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_XMag.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFind.setIcon(icon11)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        self.actionSe_lect_All = QtGui.QAction(MainWindow)
        self.actionSe_lect_All.setObjectName(_fromUtf8("actionSe_lect_All"))
        self.actionChange_Language = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_Keyboard_Layout.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionChange_Language.setIcon(icon12)
        self.actionChange_Language.setObjectName(_fromUtf8("actionChange_Language"))
        self.actionShow_Toolbar = QtGui.QAction(MainWindow)
        self.actionShow_Toolbar.setCheckable(True)
        self.actionShow_Toolbar.setChecked(True)
        self.actionShow_Toolbar.setObjectName(_fromUtf8("actionShow_Toolbar"))
        self.actionShow_Entry_View = QtGui.QAction(MainWindow)
        self.actionShow_Entry_View.setCheckable(True)
        self.actionShow_Entry_View.setChecked(True)
        self.actionShow_Entry_View.setObjectName(_fromUtf8("actionShow_Entry_View"))
        self.action_Always_on_Top = QtGui.QAction(MainWindow)
        self.action_Always_on_Top.setCheckable(True)
        self.action_Always_on_Top.setObjectName(_fromUtf8("action_Always_on_Top"))
        self.action_Configure_Columns = QtGui.QAction(MainWindow)
        self.action_Configure_Columns.setObjectName(_fromUtf8("action_Configure_Columns"))
        self.actionUse_Simple_List_View_for_TAN_Only_Groups = QtGui.QAction(MainWindow)
        self.actionUse_Simple_List_View_for_TAN_Only_Groups.setCheckable(True)
        self.actionUse_Simple_List_View_for_TAN_Only_Groups.setChecked(True)
        self.actionUse_Simple_List_View_for_TAN_Only_Groups.setObjectName(_fromUtf8("actionUse_Simple_List_View_for_TAN_Only_Groups"))
        self.actionShowTANIndicies = QtGui.QAction(MainWindow)
        self.actionShowTANIndicies.setCheckable(True)
        self.actionShowTANIndicies.setChecked(True)
        self.actionShowTANIndicies.setObjectName(_fromUtf8("actionShowTANIndicies"))
        self.actionShow_Entries_of_Subgroups = QtGui.QAction(MainWindow)
        self.actionShow_Entries_of_Subgroups.setCheckable(True)
        self.actionShow_Entries_of_Subgroups.setObjectName(_fromUtf8("actionShow_Entries_of_Subgroups"))
        self.action_Generate_Password = QtGui.QAction(MainWindow)
        self.action_Generate_Password.setObjectName(_fromUtf8("action_Generate_Password"))
        self.actionGenerate_Password_List = QtGui.QAction(MainWindow)
        self.actionGenerate_Password_List.setObjectName(_fromUtf8("actionGenerate_Password_List"))
        self.action_Triggers = QtGui.QAction(MainWindow)
        self.action_Triggers.setObjectName(_fromUtf8("action_Triggers"))
        self.action_Plugins = QtGui.QAction(MainWindow)
        self.action_Plugins.setObjectName(_fromUtf8("action_Plugins"))
        self.action_Options = QtGui.QAction(MainWindow)
        self.action_Options.setObjectName(_fromUtf8("action_Options"))
        self.action_TAN_WIzard = QtGui.QAction(MainWindow)
        self.action_TAN_WIzard.setObjectName(_fromUtf8("action_TAN_WIzard"))
        self.actionDatabase_Maintenance = QtGui.QAction(MainWindow)
        self.actionDatabase_Maintenance.setObjectName(_fromUtf8("actionDatabase_Maintenance"))
        self.actionDelete_Duplicate_Entris = QtGui.QAction(MainWindow)
        self.actionDelete_Duplicate_Entris.setObjectName(_fromUtf8("actionDelete_Duplicate_Entris"))
        self.actionDelete_Empty_Groups = QtGui.QAction(MainWindow)
        self.actionDelete_Empty_Groups.setObjectName(_fromUtf8("actionDelete_Empty_Groups"))
        self.actionDelete_Unused_Custom_Icons = QtGui.QAction(MainWindow)
        self.actionDelete_Unused_Custom_Icons.setObjectName(_fromUtf8("actionDelete_Unused_Custom_Icons"))
        self.action_Help_Contents = QtGui.QAction(MainWindow)
        self.action_Help_Contents.setObjectName(_fromUtf8("action_Help_Contents"))
        self.actionHelp_Source = QtGui.QAction(MainWindow)
        self.actionHelp_Source.setObjectName(_fromUtf8("actionHelp_Source"))
        self.actionKeePass_Website = QtGui.QAction(MainWindow)
        self.actionKeePass_Website.setObjectName(_fromUtf8("actionKeePass_Website"))
        self.action_Donate = QtGui.QAction(MainWindow)
        self.action_Donate.setObjectName(_fromUtf8("action_Donate"))
        self.action_Check_for_Update = QtGui.QAction(MainWindow)
        self.action_Check_for_Update.setObjectName(_fromUtf8("action_Check_for_Update"))
        self.actionAbout_KeePass = QtGui.QAction(MainWindow)
        self.actionAbout_KeePass.setObjectName(_fromUtf8("actionAbout_KeePass"))
        self.actionCopyUserName = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_Personal.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopyUserName.setIcon(icon13)
        self.actionCopyUserName.setObjectName(_fromUtf8("actionCopyUserName"))
        self.actionCopy_Password = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/KeePass/Resources/Nuvola/B16x16_KGPG_Info.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy_Password.setIcon(icon14)
        self.actionCopy_Password.setObjectName(_fromUtf8("actionCopy_Password"))
        self.actiongroupEntryView = QtGui.QActionGroup(MainWindow)
        self.actiongroupEntryView.setObjectName(_fromUtf8("actiongroupEntryView"))
        self.action_Stacked = QtGui.QAction(self.actiongroupEntryView)
        self.action_Stacked.setCheckable(True)
        self.action_Stacked.setChecked(True)
        self.action_Stacked.setObjectName(_fromUtf8("action_Stacked"))
        self.actionSide_by_Side = QtGui.QAction(self.actiongroupEntryView)
        self.actionSide_by_Side.setCheckable(True)
        self.actionSide_by_Side.setObjectName(_fromUtf8("actionSide_by_Side"))
        self.actiongroupSortByType = QtGui.QActionGroup(MainWindow)
        self.actiongroupSortByType.setObjectName(_fromUtf8("actiongroupSortByType"))
        self.action_No_Sort = QtGui.QAction(self.actiongroupSortByType)
        self.action_No_Sort.setCheckable(True)
        self.action_No_Sort.setChecked(True)
        self.action_No_Sort.setObjectName(_fromUtf8("action_No_Sort"))
        self.actionTitle = QtGui.QAction(self.actiongroupSortByType)
        self.actionTitle.setCheckable(True)
        self.actionTitle.setObjectName(_fromUtf8("actionTitle"))
        self.actionUser_Name = QtGui.QAction(self.actiongroupSortByType)
        self.actionUser_Name.setCheckable(True)
        self.actionUser_Name.setObjectName(_fromUtf8("actionUser_Name"))
        self.actionPassword = QtGui.QAction(self.actiongroupSortByType)
        self.actionPassword.setCheckable(True)
        self.actionPassword.setObjectName(_fromUtf8("actionPassword"))
        self.actionURL = QtGui.QAction(self.actiongroupSortByType)
        self.actionURL.setCheckable(True)
        self.actionURL.setObjectName(_fromUtf8("actionURL"))
        self.actionNotes = QtGui.QAction(self.actiongroupSortByType)
        self.actionNotes.setCheckable(True)
        self.actionNotes.setObjectName(_fromUtf8("actionNotes"))
        self.actiongroupSortByOrder = QtGui.QActionGroup(MainWindow)
        self.actiongroupSortByOrder.setObjectName(_fromUtf8("actiongroupSortByOrder"))
        self.action_Ascending = QtGui.QAction(self.actiongroupSortByOrder)
        self.action_Ascending.setCheckable(True)
        self.action_Ascending.setObjectName(_fromUtf8("action_Ascending"))
        self.action_Descending = QtGui.QAction(self.actiongroupSortByOrder)
        self.action_Descending.setCheckable(True)
        self.action_Descending.setObjectName(_fromUtf8("action_Descending"))
        self.actiongroupShowTANIndicies = QtGui.QActionGroup(MainWindow)
        self.actiongroupShowTANIndicies.setObjectName(_fromUtf8("actiongroupShowTANIndicies"))
        self.actionShowTANIndiciesOn = QtGui.QAction(self.actiongroupShowTANIndicies)
        self.actionShowTANIndiciesOn.setCheckable(True)
        self.actionShowTANIndiciesOn.setObjectName(_fromUtf8("actionShowTANIndiciesOn"))
        self.actionShowTANIndiciesAuto = QtGui.QAction(self.actiongroupShowTANIndicies)
        self.actionShowTANIndiciesAuto.setCheckable(True)
        self.actionShowTANIndiciesAuto.setChecked(True)
        self.actionShowTANIndiciesAuto.setObjectName(_fromUtf8("actionShowTANIndiciesAuto"))
        self.actionShowTANIndiciesOff = QtGui.QAction(self.actiongroupShowTANIndicies)
        self.actionShowTANIndiciesOff.setCheckable(True)
        self.actionShowTANIndiciesOff.setObjectName(_fromUtf8("actionShowTANIndiciesOff"))
        self.menuOpen.addAction(self.actionOpen_File)
        self.menuOpen.addAction(self.actionOpen_Url)
        self.menuOpen_Recent.addSeparator()
        self.menuOpen_Recent.addAction(self.actionClear_List)
        self.menuSave_As.addAction(self.actionSave_to_File)
        self.menuSave_As.addAction(self.actionSave_to_URL)
        self.menuSave_As.addSeparator()
        self.menuSave_As.addAction(self.actionSave_copy_as)
        self.menuRecent_Files.addSeparator()
        self.menuRecent_Files.addAction(self.actionClear_List_2)
        self.menuSynchronize.addAction(self.actionSynchronize_with_File)
        self.menuSynchronize.addAction(self.actionSynchronize_with_URL)
        self.menuSynchronize.addSeparator()
        self.menuSynchronize.addAction(self.menuRecent_Files.menuAction())
        self.menuFile.addAction(self.actionNewDatabase)
        self.menuFile.addAction(self.menuOpen.menuAction())
        self.menuFile.addAction(self.menuOpen_Recent.menuAction())
        self.menuFile.addAction(self.actionCloseDatabase)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuSave_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDatabaseSettings)
        self.menuFile.addAction(self.actionChangeMasterKey)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.menuSynchronize.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionLock_Workspace)
        self.menuFile.addAction(self.actionExit)
        self.menuShow_Entries_by_Tag.addAction(self.action_No_tags_found)
        self.menuEdit.addAction(self.actionAdd_Group)
        self.menuEdit.addAction(self.actionEdit_Group)
        self.menuEdit.addAction(self.actionDelete_Group)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionAdd_Entry)
        self.menuEdit.addAction(self.actionEdit_View_Entry)
        self.menuEdit.addAction(self.actionDuplicate_Entry)
        self.menuEdit.addAction(self.actionDelete_Entry)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSe_lect_All)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionShow_All_Entries)
        self.menuEdit.addAction(self.actionShow_All_Expired_Entries)
        self.menuEdit.addAction(self.menuShow_Entries_by_Tag.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind)
        self.menu_Window_Layout.addAction(self.action_Stacked)
        self.menu_Window_Layout.addAction(self.actionSide_by_Side)
        self.menu_Sort_By.addAction(self.action_No_Sort)
        self.menu_Sort_By.addSeparator()
        self.menu_Sort_By.addAction(self.actionTitle)
        self.menu_Sort_By.addAction(self.actionUser_Name)
        self.menu_Sort_By.addAction(self.actionPassword)
        self.menu_Sort_By.addAction(self.actionURL)
        self.menu_Sort_By.addAction(self.actionNotes)
        self.menu_Sort_By.addSeparator()
        self.menu_Sort_By.addAction(self.action_Ascending)
        self.menu_Sort_By.addAction(self.action_Descending)
        self.menuTAN_View_Options.addAction(self.actionUse_Simple_List_View_for_TAN_Only_Groups)
        self.menuTAN_View_Options.addAction(self.actionShowTANIndicies)
        self.menu_Grouping_in_Entry_List.addAction(self.actionShowTANIndiciesOn)
        self.menu_Grouping_in_Entry_List.addAction(self.actionShowTANIndiciesAuto)
        self.menu_Grouping_in_Entry_List.addAction(self.actionShowTANIndiciesOff)
        self.menuView.addAction(self.actionChange_Language)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_Toolbar)
        self.menuView.addAction(self.actionShow_Entry_View)
        self.menuView.addAction(self.menu_Window_Layout.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.action_Always_on_Top)
        self.menuView.addSeparator()
        self.menuView.addAction(self.action_Configure_Columns)
        self.menuView.addAction(self.menu_Sort_By.menuAction())
        self.menuView.addAction(self.menuTAN_View_Options.menuAction())
        self.menuView.addAction(self.menu_Grouping_in_Entry_List.menuAction())
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionShow_Entries_of_Subgroups)
        self.menu_Database_Tools.addAction(self.actionDatabase_Maintenance)
        self.menu_Database_Tools.addSeparator()
        self.menu_Database_Tools.addAction(self.actionDelete_Duplicate_Entris)
        self.menu_Database_Tools.addAction(self.actionDelete_Empty_Groups)
        self.menu_Database_Tools.addAction(self.actionDelete_Unused_Custom_Icons)
        self.menuTools.addAction(self.action_Generate_Password)
        self.menuTools.addAction(self.actionGenerate_Password_List)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_TAN_WIzard)
        self.menuTools.addAction(self.menu_Database_Tools.menuAction())
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_Triggers)
        self.menuTools.addAction(self.action_Plugins)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_Options)
        self.menuHelp.addAction(self.action_Help_Contents)
        self.menuHelp.addAction(self.actionHelp_Source)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionKeePass_Website)
        self.menuHelp.addAction(self.action_Donate)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.action_Check_for_Update)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_KeePass)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionNewDatabase)
        self.toolBar.addAction(self.actionOpen_File)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAdd_Entry)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCopyUserName)
        self.toolBar.addAction(self.actionCopy_Password)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFind)
        self.toolBar.addAction(self.actionShow_All_Entries)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLock_Workspace)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionShow_Toolbar, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.toolBar.setVisible)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.action_Stacked, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.stackedTextBrowser.setVisible)
        QtCore.QObject.connect(self.actionSide_by_Side, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.sideBySideTextBrowser.setVisible)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupTreeWidget.headerItem().setText(0, _translate("MainWindow", "Group", None))
        self.menuFile.setTitle(_translate("MainWindow", "&File", None))
        self.menuOpen.setTitle(_translate("MainWindow", "&Open", None))
        self.menuOpen_Recent.setTitle(_translate("MainWindow", "Open &Recent", None))
        self.menuSave_As.setTitle(_translate("MainWindow", "Save &As", None))
        self.menuSynchronize.setTitle(_translate("MainWindow", "S&ynchronize", None))
        self.menuRecent_Files.setTitle(_translate("MainWindow", "&Recent Files", None))
        self.menuEdit.setTitle(_translate("MainWindow", "&Edit", None))
        self.menuShow_Entries_by_Tag.setTitle(_translate("MainWindow", "Show Entries &by Tag", None))
        self.menuView.setTitle(_translate("MainWindow", "&View", None))
        self.menu_Window_Layout.setTitle(_translate("MainWindow", "&Window Layout", None))
        self.menu_Sort_By.setTitle(_translate("MainWindow", "&Sort By", None))
        self.menuTAN_View_Options.setTitle(_translate("MainWindow", "TAN &View Options", None))
        self.menu_Grouping_in_Entry_List.setTitle(_translate("MainWindow", "&Grouping in Entry List", None))
        self.menuTools.setTitle(_translate("MainWindow", "&Tools", None))
        self.menu_Database_Tools.setTitle(_translate("MainWindow", "&Database Tools", None))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionNewDatabase.setText(_translate("MainWindow", "&New...", None))
        self.actionNewDatabase.setToolTip(_translate("MainWindow", "Create a New Database", None))
        self.actionNewDatabase.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionCloseDatabase.setText(_translate("MainWindow", "&Close", None))
        self.actionCloseDatabase.setToolTip(_translate("MainWindow", "Close Current Database", None))
        self.actionCloseDatabase.setShortcut(_translate("MainWindow", "Ctrl+W", None))
        self.actionSave.setText(_translate("MainWindow", "&SaveDatabase", None))
        self.actionSave.setToolTip(_translate("MainWindow", "Save Current Database", None))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S", None))
        self.actionDatabaseSettings.setText(_translate("MainWindow", "&Database Settings...", None))
        self.actionDatabaseSettings.setToolTip(_translate("MainWindow", "Open Database Settings Dialog", None))
        self.actionChangeMasterKey.setText(_translate("MainWindow", "Change &Master Key...", None))
        self.actionChangeMasterKey.setToolTip(_translate("MainWindow", "Change Master Key for Current Database", None))
        self.actionPrint.setText(_translate("MainWindow", "&Print...", None))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P", None))
        self.actionImport.setText(_translate("MainWindow", "&Import...", None))
        self.actionExport.setText(_translate("MainWindow", "&Export...", None))
        self.actionLock_Workspace.setText(_translate("MainWindow", "&Lock Workspace", None))
        self.actionLock_Workspace.setShortcut(_translate("MainWindow", "Ctrl+L", None))
        self.actionExit.setText(_translate("MainWindow", "E&xit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Exit KeePass", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Open &File...", None))
        self.actionOpen_File.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionOpen_Url.setText(_translate("MainWindow", "Open &Url...", None))
        self.actionOpen_Url.setShortcut(_translate("MainWindow", "Ctrl+Shift+O", None))
        self.actionClear_List.setText(_translate("MainWindow", "&Clear List", None))
        self.actionSave_to_File.setText(_translate("MainWindow", "Save to &File...", None))
        self.actionSave_to_URL.setText(_translate("MainWindow", "Save to &URL...", None))
        self.actionSave_copy_as.setText(_translate("MainWindow", "Save &Copy to File...", None))
        self.actionSynchronize_with_File.setText(_translate("MainWindow", "Synchronize with &File...", None))
        self.actionSynchronize_with_File.setShortcut(_translate("MainWindow", "Ctrl+R", None))
        self.actionSynchronize_with_URL.setText(_translate("MainWindow", "Synchronize with &URL...", None))
        self.actionSynchronize_with_URL.setShortcut(_translate("MainWindow", "Ctrl+Shift+R", None))
        self.actionClear_List_2.setText(_translate("MainWindow", "&Clear List", None))
        self.actionAdd_Group.setText(_translate("MainWindow", "Add &Group", None))
        self.actionEdit_Group.setText(_translate("MainWindow", "Ed&it Group", None))
        self.actionDelete_Group.setText(_translate("MainWindow", "Dele&te Group", None))
        self.actionDelete_Group.setShortcut(_translate("MainWindow", "Del", None))
        self.actionAdd_Entry.setText(_translate("MainWindow", "&Add Entry...", None))
        self.actionAdd_Entry.setShortcut(_translate("MainWindow", "Ctrl+I", None))
        self.actionEdit_View_Entry.setText(_translate("MainWindow", "&Edit/View Entry...", None))
        self.actionEdit_View_Entry.setShortcut(_translate("MainWindow", "Return", None))
        self.actionDuplicate_Entry.setText(_translate("MainWindow", "Dupli&cate Entry", None))
        self.actionDelete_Entry.setText(_translate("MainWindow", "&Delete Entry", None))
        self.actionDelete_Entry.setShortcut(_translate("MainWindow", "Del", None))
        self.actionShow_All_Entries.setText(_translate("MainWindow", "&Show All Entries", None))
        self.actionShow_All_Expired_Entries.setText(_translate("MainWindow", "Show All E&xpired Entries", None))
        self.action_No_tags_found.setText(_translate("MainWindow", "(No tags found)", None))
        self.actionFind.setText(_translate("MainWindow", "&Find...", None))
        self.actionFind.setShortcut(_translate("MainWindow", "Ctrl+F", None))
        self.actionSe_lect_All.setText(_translate("MainWindow", "Se&lect All", None))
        self.actionSe_lect_All.setShortcut(_translate("MainWindow", "Ctrl+A", None))
        self.actionChange_Language.setText(_translate("MainWindow", "Change &Language...", None))
        self.actionShow_Toolbar.setText(_translate("MainWindow", "Show &Toolbar", None))
        self.actionShow_Entry_View.setText(_translate("MainWindow", "Show &Entry View", None))
        self.action_Always_on_Top.setText(_translate("MainWindow", "&Always on Top", None))
        self.action_Configure_Columns.setText(_translate("MainWindow", "&Configure Columns...", None))
        self.actionUse_Simple_List_View_for_TAN_Only_Groups.setText(_translate("MainWindow", "Use &Simple List View for TAN-Only Groups", None))
        self.actionShowTANIndicies.setText(_translate("MainWindow", "Show TAN &Indicies in Entry Titles", None))
        self.actionShow_Entries_of_Subgroups.setText(_translate("MainWindow", "Show Entries of Su&bgroups", None))
        self.action_Generate_Password.setText(_translate("MainWindow", "&Generate Password...", None))
        self.actionGenerate_Password_List.setText(_translate("MainWindow", "Generate Password &List...", None))
        self.action_Triggers.setText(_translate("MainWindow", "&Triggers...", None))
        self.action_Plugins.setText(_translate("MainWindow", "&Plugins...", None))
        self.action_Options.setText(_translate("MainWindow", "&Options...", None))
        self.action_TAN_WIzard.setText(_translate("MainWindow", "&TAN WIzard...", None))
        self.actionDatabase_Maintenance.setText(_translate("MainWindow", "Database &Maintenance...", None))
        self.actionDelete_Duplicate_Entris.setText(_translate("MainWindow", "Delete &Duplicate Entries", None))
        self.actionDelete_Empty_Groups.setText(_translate("MainWindow", "Delete Empty &Groups", None))
        self.actionDelete_Unused_Custom_Icons.setText(_translate("MainWindow", "Delete Unused Custom &Icons", None))
        self.action_Help_Contents.setText(_translate("MainWindow", "&Help Contents", None))
        self.action_Help_Contents.setShortcut(_translate("MainWindow", "F1", None))
        self.actionHelp_Source.setText(_translate("MainWindow", "Help &Source...", None))
        self.actionKeePass_Website.setText(_translate("MainWindow", "KeePass &Website", None))
        self.action_Donate.setText(_translate("MainWindow", "&Donate...", None))
        self.action_Check_for_Update.setText(_translate("MainWindow", "&Check for Update", None))
        self.actionAbout_KeePass.setText(_translate("MainWindow", "About KeePass...", None))
        self.actionCopyUserName.setText(_translate("MainWindow", "CopyUserName", None))
        self.actionCopyUserName.setToolTip(_translate("MainWindow", "Copy User Name to Clipboard", None))
        self.actionCopyUserName.setShortcut(_translate("MainWindow", "Ctrl+B", None))
        self.actionCopy_Password.setText(_translate("MainWindow", "Copy Password", None))
        self.actionCopy_Password.setToolTip(_translate("MainWindow", "Copy Password to Clipboard", None))
        self.actionCopy_Password.setShortcut(_translate("MainWindow", "Ctrl+C", None))
        self.action_Stacked.setText(_translate("MainWindow", "&Stacked", None))
        self.actionSide_by_Side.setText(_translate("MainWindow", "Side &by Side", None))
        self.action_No_Sort.setText(_translate("MainWindow", "&No Sort", None))
        self.actionTitle.setText(_translate("MainWindow", "Title", None))
        self.actionUser_Name.setText(_translate("MainWindow", "User Name", None))
        self.actionPassword.setText(_translate("MainWindow", "Password", None))
        self.actionURL.setText(_translate("MainWindow", "URL", None))
        self.actionNotes.setText(_translate("MainWindow", "Notes", None))
        self.action_Ascending.setText(_translate("MainWindow", "&Ascending", None))
        self.action_Descending.setText(_translate("MainWindow", "&Descending", None))
        self.actionShowTANIndiciesOn.setText(_translate("MainWindow", "On", None))
        self.actionShowTANIndiciesAuto.setText(_translate("MainWindow", "Auto (&Recommended)", None))
        self.actionShowTANIndiciesOff.setText(_translate("MainWindow", "Off", None))

import ui.keepass_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

