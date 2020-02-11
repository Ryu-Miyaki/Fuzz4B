import wx
from FuzzingTool_Frame_StartupScreen_Child import FuzzingTool_Frame_StartupScreen_Child

if __name__ == '__main__':
    app=wx.App(False)
    lang=wx.Locale(language=wx.LANGUAGE_ENGLISH_US)
    frame=FuzzingTool_Frame_StartupScreen_Child(None)
    frame.Show(True)
    app.SetTopWindow(frame)
    app.MainLoop()