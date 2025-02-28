# import FreeCAD
# import FreeCADGui
# from PySide2 import QtGui, QtCore, QtWidgets

# class StageBar(QtWidgets.QWidget):
#     def __init__(self):
#         super(StageBar, self).__init__()
#         self.initUI()

#     def initUI(self):
#         layout = QtWidgets.QHBoxLayout()

#         self.geometryButton = QtWidgets.QPushButton("Geometry")
#         self.geometryButton.clicked.connect(self.showGeometry)
#         layout.addWidget(self.geometryButton)

#         self.structuresButton = QtWidgets.QPushButton("Structures")
#         self.structuresButton.clicked.connect(self.showStructures)
#         layout.addWidget(self.structuresButton)

#         self.materialsButton = QtWidgets.QPushButton("Materials")
#         self.materialsButton.clicked.connect(self.showMaterials)
#         layout.addWidget(self.materialsButton)

#         self.hydraulicButton = QtWidgets.QPushButton("Hydraulic Conditions")
#         self.hydraulicButton.clicked.connect(self.showHydraulic)
#         layout.addWidget(self.hydraulicButton)

#         self.meshingButton = QtWidgets.QPushButton("Meshing")
#         self.meshingButton.clicked.connect(self.showMeshing)
#         layout.addWidget(self.meshingButton)

#         self.stagedConstructionButton = QtWidgets.QPushButton("Staged Construction")
#         self.stagedConstructionButton.clicked.connect(self.showStagedConstruction)
#         layout.addWidget(self.stagedConstructionButton)

#         self.setLayout(layout)

#     def showGeometry(self):
#         self.updateToolbar("Geometry")


#     def showStructures(self):
#         self.updateToolbar("Structures")


#     def showMaterials(self):
#         self.updateToolbar("Materials")


#     def showHydraulic(self):
#         self.updateToolbar("Hydraulic")


#     def showMeshing(self):
#         self.updateToolbar("Meshing")


#     def showStagedConstruction(self):
#         self.updateToolbar("StagedConstruction")


#     def updateToolbar(self, stage):
#         mw = FreeCADGui.getMainWindow()

        
#         for toolbar in mw.findChildren(QtWidgets.QToolBar):
#             if toolbar.objectName() == "CustomToolbar":
#                 mw.removeToolBar(toolbar)

#         toolbar = QtWidgets.QToolBar("CustomToolbar")
#         toolbar.setObjectName("CustomToolbar")
#         mw.addToolBar(toolbar)

#         solidsToolbar = mw.findChild(QtWidgets.QToolBar, "Solids")
#         toolsToolbar = mw.findChild(QtWidgets.QToolBar, "Part tools")
#         booleanToolbar = mw.findChild(QtWidgets.QToolBar, "Boolean")

#         if solidsToolbar:
#             solidsToolbar.hide()
#         if toolsToolbar:
#             toolsToolbar.hide()
#         if booleanToolbar:
#             booleanToolbar.hide()

#         stageView = mw.findChild(QtWidgets.QDockWidget, "Stage")
#         if stageView:
#             stageView.hide()


#         actions = []
#         if stage == "Geometry":
#             FreeCADGui.activateWorkbench("PartWorkbench")
#             if solidsToolbar:
#                 solidsToolbar.show()
#             if toolsToolbar:
#                 toolsToolbar.show()
#             if booleanToolbar:
#                 booleanToolbar.show()
#             actions = ["Std_FillBox", "Std_Import3Dobject"]

#         elif stage == "Structures":
#             actions = ["Std_SoilStructureInteraction"]
#         elif stage == "Materials":
#             actions = ["Std_Materialproperties", "Std_SoilTests"]  
#         elif stage == "Hydraulic":
#             actions = ["Std_SoilWaterCouplingParametersInput"]  
#         elif stage == "Meshing":
#             actions = ["Std_AutofitSimulationDomain", "Std_MeshingOrder", "Std_GenerateParticles"]  
#         elif stage == "StagedConstruction": 
#             if stageView:
#                 stageView.show()
    
#             actions = ["Std_ExecuteSimulations",  "Std_ExportOutputToParaview",  "Std_ExportOutputToTabFormat", "Std_OpenParaView"] 

#         for action_name in actions:
#             action = mw.findChild(QtWidgets.QAction, action_name)
#             if action:
#                 toolbar.addAction(action)
        

# def createStageBar():
#     mw = FreeCADGui.getMainWindow()
#     dock = QtWidgets.QDockWidget("Stage Bar", mw)
#     stageBar = StageBar()
#     dock.setWidget(stageBar)
#     dock.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)

#     mw.addDockWidget(QtCore.Qt.TopDockWidgetArea, dock)

# if __name__ == "__main__":
#     createStageBar()
    


import FreeCADGui
from PySide2 import QtWidgets, QtCore

class StageBar(QtWidgets.QWidget):

    def __init__(self, toolbar, parent=None):
        super(StageBar, self).__init__(parent)
        self.toolbar = toolbar  # Nhận QToolBar từ `QSplitter`
        self.initUI()

    def initUI(self):
        layout = QtWidgets.QHBoxLayout(self)

        buttons = {
            "Geometry": self.showGeometry,
            "Structures": self.showStructures,
            "Materials": self.showMaterials,
            "Hydraulic Conditions": self.showHydraulic,
            "Meshing": self.showMeshing,
            "Staged Construction": self.showStagedConstruction
        }

        for name, method in buttons.items():
            button = QtWidgets.QPushButton(name)
            button.clicked.connect(method)
            layout.addWidget(button)

        self.setLayout(layout)

    def showGeometry(self):
        self.updateToolbar("Geometry")

    def showStructures(self):
        self.updateToolbar("Structures")

    def showMaterials(self):
        self.updateToolbar("Materials")

    def showHydraulic(self):
        self.updateToolbar("Hydraulic")

    def showMeshing(self):
        self.updateToolbar("Meshing")

    def showStagedConstruction(self):
        self.updateToolbar("StagedConstruction")

    def updateToolbar(self, stage):
        """Cập nhật toolbar trong splitter thay vì MainWindow"""
        self.toolbar.clear()

        mw = FreeCADGui.getMainWindow()

        # Ẩn các toolbar mặc định của FreeCAD nếu cần
        for name in ["Solids", "Part tools", "Boolean"]:
            tb = mw.findChild(QtWidgets.QToolBar, name)
            if tb:
                tb.hide()

        stageView = mw.findChild(QtWidgets.QDockWidget, "Stage")
        if stageView:
            stageView.hide()
           
        actions = {
            "Geometry": ["Std_FillBox", "Std_Import3Dobject"],
            "Structures": ["Std_SoilStructureInteraction"],
            "Materials": ["Std_Materialproperties", "Std_SoilTests"],
            "Hydraulic": ["Std_SoilWaterCouplingParametersInput"],
            "Meshing": ["Std_AutofitSimulationDomain", "Std_MeshingOrder", "Std_GenerateParticles"],
            "StagedConstruction": ["Std_ExecuteSimulations", "Std_ExportOutputToParaview", 
                                   "Std_ExportOutputToTabFormat", "Std_OpenParaView"]
        }
        action_list = [] 
        if stage in actions:
            for action_name in actions[stage]:
                action = mw.findChild(QtWidgets.QAction, action_name)
                if action:
                    self.toolbar.addAction(action)
                    action_list.append(action_name) 

        if stage == "Geometry":
            FreeCADGui.activateWorkbench("PartWorkbench")
            for name in ["Solids", "Part tools", "Boolean"]:
                tb = mw.findChild(QtWidgets.QToolBar, name)
                if tb:
                    tb.show()

        elif stage == "StagedConstruction" and stageView:
            stageView.show()
        

def createStageBar():
    """Tạo QSplitter chứa StageBar, Toolbar và mdiArea"""
    mw = FreeCADGui.getMainWindow()
    
    # Tạo QSplitter để chứa Toolbar (trái) và mdiArea (phải)
    splitter = QtWidgets.QSplitter(QtCore.Qt.Horizontal, mw)

     # **Thêm viền cho thanh chia giữa**
    splitter.setStyleSheet("""
        QSplitter::handle {
            background-color: gray; /* Màu nền */
            border: 2px solid black; /* Viền màu đen */
            width: 2px; /* Độ dày của thanh */
        }
    """)

    # Tạo toolbar nằm trong splitter (bên trái)
    toolbar = QtWidgets.QToolBar("CustomToolbar", mw)
    toolbar.setObjectName("CustomToolbar")
    toolbar.setOrientation(QtCore.Qt.Vertical)
    splitter.addWidget(toolbar)

    # Tạo StageBar và liên kết với toolbar
    stageBar = StageBar(toolbar)

    # Dock StageBar ở trên
    dock = QtWidgets.QDockWidget("Stage Bar", mw)
    dock.setWidget(stageBar)
    mw.addDockWidget(QtCore.Qt.TopDockWidgetArea, dock)

    # Thêm mdiArea vào splitter (bên phải)
    mdiArea = mw.findChild(QtWidgets.QMdiArea)
    if mdiArea:
        splitter.addWidget(mdiArea)

    # Điều chỉnh tỷ lệ hiển thị
    splitter.setStretchFactor(0, 2)  # Toolbar chiếm ít không gian
    splitter.setStretchFactor(1, 4)  # mdiArea chiếm phần lớn

    # **Ghi đè setCentralWidget để sử dụng QSplitter thay vì mdiArea**
    mw.setCentralWidget(splitter)


if __name__ == "__main__":
    createStageBar()


