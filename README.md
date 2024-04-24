## wxVTK Demo

This is a demonstration of integrating VTK (Visualization Toolkit) with wxPython using the xVTKRenderWindowInteractor widget. The demo includes a simple application to plot and manipulate a 3D mesh using wxPython's GUI components.

### Prerequisites

Make sure you have the following libraries installed:

- wxPython
- VTK
- PyVista

### Usage

#### To run the demo:

1. Clone the repository:

```bash
git clone http://github.com/a-elrawy/wxvtk-demo
cd wxvtk-demo
```
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the demo:

```bash
python main.py
```


### Functionality

- The application window includes a menu bar with a "File" menu, allowing users to quit the application.
- It features a "Plot" button that initializes the plotting of a 3D mesh.
- Users can adjust the size of the mesh using a slider.
- The mesh is plotted using VTK and PyVista, with the rendering integrated into the wxPython window using `wxVTKRenderWindowInteractor`.
