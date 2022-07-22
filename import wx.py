import wx
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from numpy import random


class MainFrame(wx.Frame):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, title="Demo GUI", size=(1200, 580))

        # Add SplitterWindow panels
        self.split_win = wx.SplitterWindow(self)
        self.graph_panel = MatplotPanel(self.split_win)
        self.ctrl_menu = wx.Panel(self.split_win)
        self.split_win.SplitVertically(self.ctrl_menu, self.graph_panel, 200)

        #Select channel to tune.
        self.chText = wx.StaticText(self.ctrl_menu, -1, 'Select Object:', size = (100,20), pos = (10,200))
        self.chBox = wx.ComboBox(self.ctrl_menu,  choices =['Emma','2','3','4','5','6','7','8','Common'], size = (100,20), pos=(10,220))


        self.measBut = wx.Button(self.ctrl_menu, -1, "Press Me!", size=(80, 40), pos=(10, 410))
        self.measBut.Bind(wx.EVT_BUTTON, self.print_stuff)

    def measure(self, event):
        self.fig = Figure()

        self.ax1 = self.fig.add_subplot(111)
        self.ax1.set_title("Random Data")
        self.ax1.set_xlim([0,20])
        self.ax1.set_ylim([0,1])
        self.ax1.set_xlabel('Time')
        self.ax1.set_ylabel('Value')
        self.canvas = FigureCanvas(self.graph_panel, -1, self.fig)

        for n in range(4):
            self.ax1.plot(range(20), random.rand(20), 30)


    def set_path(self, event):

        fdlg = wx.FileDialog(self.ctrl_menu, "Select location to save data.", "", "", "CSV files(*.csv)|*.*", wx.FD_SAVE)

        if fdlg.ShowModal() == wx.ID_OK:
            self.save_path = fdlg.GetPath() + ".csv"
            self.file_path.SetValue(self.save_path)

    def print_stuff(self, event):
        print('This is cool!')


class MatplotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size=(50, 50))

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)

        t = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
        s = [0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 1.0, 2.0, 1.0, 0.0]

        self.axes.plot(t, s)
        self.canvas = FigureCanvas(self, -1, self.figure)


app = wx.App()
frame = MainFrame(None).Show()
app.MainLoop()