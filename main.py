import wx
import vtk
from vtk.wx.wxVTKRenderWindowInteractor import wxVTKRenderWindowInteractor # widget to combine VTK and wxPython
import pyvista as pv

class VTKFrame(wx.Frame):
    def __init__(self, parent, ident):
        # create wx.Frame and wxVTKRenderWindowInteractor to put in it
        wx.Frame.__init__(self, parent, ident, "DRE wxVTK demo", size=(700,700))
        
        # create a menu
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        quitMenu = menu.Append(-1, "&Quit", "Quit")
        self.Bind(wx.EVT_MENU, self.onQuit, quitMenu)

        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        # Add button to plot a mesh
        self.button = wx.Button(self, 2, "Plot", (0, 0), (35, 35))
        self.Bind(wx.EVT_BUTTON, self.onPlot, self.button)
        
        self.rwi = wxVTKRenderWindowInteractor(self, -1) 

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.button, 1, wx.ALIGN_CENTER)
        sizer.Add(self.rwi, 2)
        self.SetSizer(sizer)
        self.Layout()
        
    def onQuit(self, event):
        for ren in self.listRen:
            ren.RemoveAllViewProps() 
        del ren 
        self.rwi.GetRenderWindow().Finalize() 
        del self.rwi 
        self.Destroy()
    
    def createBox(self, value, pl):
        # Create the box based on the value of the slider
        value = value/10
        bounds = [0, value, 0, value, 0, value]
        box = pv.Box(bounds)

        return pl.add_mesh(box, name="box", show_edges=True)
    
    def onSlider(self, event):
        value = event.GetInt()
        self.updateBox(value)

    def updateBox(self, value):
        if hasattr(self, 'actor'):
            self.ren.RemoveActor(self.actor)
        self.actor = self.createBox(value, self.plotter)
        self.ren.AddActor(self.actor)
        self.rwi.GetRenderWindow().Render()

    def onPlot(self, event):
        self.rwi.Enable(1)
        self.ren = vtk.vtkRenderer()
        self.rwi.GetRenderWindow().AddRenderer(self.ren)
        self.plotter = pv.Plotter()

        # Add wx slider to control the value of the mesh
        if hasattr(self, 'slider'):
            self.slider.Destroy()
        self.slider = wx.Slider(self, 3, 10, 0, 10, (0, 0), (100,50), style= wx.SL_HORIZONTAL) # create a slider with range 0-50 
        self.Bind(wx.EVT_SLIDER, self.onSlider, self.slider)

        # Add the slider to the window
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.slider, 3, wx.ALIGN_CENTER_VERTICAL)
        self.SetSizer(sizer)
        self.Layout()

        # Initialize the mesh
        self.updateBox(10)
        # Refresh the window
        self.rwi.GetRenderWindow().Render()


# start the wx loop
app = wx.PySimpleApp()
frame = VTKFrame(None, -1)
frame.Show()
app.MainLoop()



