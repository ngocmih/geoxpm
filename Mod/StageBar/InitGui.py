import FreeCADGui
import stagebar  # Import stagebar.py

class StageBarWorkbench(FreeCADGui.Workbench):
    MenuText = "Stage Bar"
    ToolTip = "Custom Workbench with StageBar"
    Icon = ""

    def Initialize(self):
        stagebar.createStageBar() 

    def GetClassName(self):
        return "Gui::PythonWorkbench"

# Đăng ký Workbench vào FreeCAD
# FreeCADGui.addWorkbench(StageBarWorkbench())

# Gọi `createStageBar()` ngay khi FreeCAD khởi động
stagebar.createStageBar()

