#***************************************************************************
#*   Copyright (c) 2013 Juergen Riegel <FreeCAD@juergen-riegel.net>        *
#*                                                                         *
#*   This program is free software; you can redistribute it and/or modify  *
#*   it under the terms of the GNU Lesser General Public License (LGPL)    *
#*   as published by the Free Software Foundation; either version 2 of     *
#*   the License, or (at your option) any later version.                   *
#*   for detail see the LICENCE text file.                                 *
#*                                                                         *
#*   This program is distributed in the hope that it will be useful,       *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
#*   GNU Library General Public License for more details.                  *
#*                                                                         *
#*   You should have received a copy of the GNU Library General Public     *
#*   License along with this program; if not, write to the Free Software   *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
#*   USA                                                                   *
#*                                                                         *
#***************************************************************************
"""Initialization of the Material Workbench graphical interface."""

import FreeCAD as App
import FreeCADGui as Gui
import os


class MaterialWorkbench(Gui.Workbench):
    """Part workbench object."""

    def __init__(self):
        self.__class__.Icon = os.path.join(App.getResourceDir(),
                                           "Mod", "Material",
                                           "Resources", "icons",
                                           "MaterialWorkbench.svg")
        self.__class__.MenuText = "Material"
        self.__class__.ToolTip = "Material workbench"

    def Initialize(self):
        # load the module
        import MatGui

    def GetClassName(self):
        return "MatGui::Workbench"


#Gui.addWorkbench(MaterialWorkbench())      //NATAES Ngoc - 1.2025

FreeCAD.__unit_test__ += [ "TestMaterialsGui" ]
