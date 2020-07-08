# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Dec 12 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Frame_StartupScreen
###########################################################################

class Frame_StartupScreen ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 780,662 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 780,662 ), wx.DefaultSize )

		self.Menubar_Menubar = wx.MenuBar( 0 )
		self.Menu_FuzzingMenu = wx.Menu()
		self.MenuItem_StartFuzzing = wx.MenuItem( self.Menu_FuzzingMenu, wx.ID_ANY, u"Start", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_FuzzingMenu.Append( self.MenuItem_StartFuzzing )

		self.MenuItem_StopFuzzing = wx.MenuItem( self.Menu_FuzzingMenu, wx.ID_ANY, u"Stop", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_FuzzingMenu.Append( self.MenuItem_StopFuzzing )
		self.MenuItem_StopFuzzing.Enable( False )

		self.Menubar_Menubar.Append( self.Menu_FuzzingMenu, u"Fuzzing" )

		self.Menu_View = wx.Menu()
		self.MenuItem_TextFormString = wx.MenuItem( self.Menu_View, wx.ID_ANY, u"Display Special Characters in UTF-8", wx.EmptyString, wx.ITEM_CHECK )
		self.Menu_View.Append( self.MenuItem_TextFormString )
		self.MenuItem_TextFormString.Check( True )

		self.MenuItem_TextFormBytes = wx.MenuItem( self.Menu_View, wx.ID_ANY, u"Display Special Characters as binary data", wx.EmptyString, wx.ITEM_CHECK )
		self.Menu_View.Append( self.MenuItem_TextFormBytes )

		self.MenuItem_PathFormRelative = wx.MenuItem( self.Menu_View, wx.ID_ANY, u"Display relative path", wx.EmptyString, wx.ITEM_CHECK )
		self.Menu_View.Append( self.MenuItem_PathFormRelative )

		self.Menubar_Menubar.Append( self.Menu_View, u"View" )

		self.Menu_DegugMenu = wx.Menu()
		self.MenuItem_MinimizeFuzz = wx.MenuItem( self.Menu_DegugMenu, wx.ID_ANY, u"Reduce fuzz", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_DegugMenu.Append( self.MenuItem_MinimizeFuzz )
		self.MenuItem_MinimizeFuzz.Enable( False )

		self.MenuItem_InputTestcaseandRun = wx.MenuItem( self.Menu_DegugMenu, wx.ID_ANY, u"Run program with fuzz", wx.EmptyString, wx.ITEM_NORMAL )
		self.Menu_DegugMenu.Append( self.MenuItem_InputTestcaseandRun )
		self.MenuItem_InputTestcaseandRun.Enable( False )

		self.Menubar_Menubar.Append( self.Menu_DegugMenu, u"Debug" )

		self.SetMenuBar( self.Menubar_Menubar )

		bSizer_StartupScreen_GridandText = wx.BoxSizer( wx.HORIZONTAL )

		bSizer_Texts = wx.BoxSizer( wx.VERTICAL )

		self.Text_ChoisedRow = wx.StaticText( self, wx.ID_ANY, u"Selected No. ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_ChoisedRow.Wrap( -1 )

		bSizer_Texts.Add( self.Text_ChoisedRow, 0, wx.ALL, 5 )

		bSizer_CrashTestcase = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Fuzz which caused crash" ), wx.VERTICAL )

		self.TextCtrl_CrashTestcase = wx.TextCtrl( bSizer_CrashTestcase.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer_CrashTestcase.Add( self.TextCtrl_CrashTestcase, 1, wx.ALL, 5 )


		bSizer_Texts.Add( bSizer_CrashTestcase, 1, 0, 5 )

		bSizer_OriginalTestcase = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Original fuzz" ), wx.VERTICAL )

		self.TextCtrl_OriginalTestcase = wx.TextCtrl( bSizer_OriginalTestcase.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer_OriginalTestcase.Add( self.TextCtrl_OriginalTestcase, 1, wx.ALL, 5 )


		bSizer_Texts.Add( bSizer_OriginalTestcase, 1, 0, 5 )

		bSizer_MinimizedTestcase = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Reduced fuzz" ), wx.VERTICAL )

		self.TextCtrl_MinimizedTestcase = wx.TextCtrl( bSizer_MinimizedTestcase.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,150 ), wx.TE_MULTILINE|wx.TE_READONLY )
		bSizer_MinimizedTestcase.Add( self.TextCtrl_MinimizedTestcase, 1, wx.ALL, 5 )


		bSizer_Texts.Add( bSizer_MinimizedTestcase, 1, 0, 5 )


		bSizer_StartupScreen_GridandText.Add( bSizer_Texts, 0, wx.EXPAND, 5 )

		self.Grid_Testcases = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.HSCROLL|wx.VSCROLL )

		# Grid
		self.Grid_Testcases.CreateGrid( 1, 3 )
		self.Grid_Testcases.EnableEditing( False )
		self.Grid_Testcases.EnableGridLines( True )
		self.Grid_Testcases.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.Grid_Testcases.EnableDragGridSize( False )
		self.Grid_Testcases.SetMargins( 0, 0 )

		# Columns
		self.Grid_Testcases.AutoSizeColumns()
		self.Grid_Testcases.EnableDragColMove( False )
		self.Grid_Testcases.EnableDragColSize( False )
		self.Grid_Testcases.SetColLabelSize( 30 )
		self.Grid_Testcases.SetColLabelValue( 0, u"Fuzz which caused crash" )
		self.Grid_Testcases.SetColLabelValue( 1, u"Original fuzz" )
		self.Grid_Testcases.SetColLabelValue( 2, u"Reduced fuzz" )
		self.Grid_Testcases.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.Grid_Testcases.AutoSizeRows()
		self.Grid_Testcases.EnableDragRowSize( False )
		self.Grid_Testcases.SetRowLabelSize( 80 )
		self.Grid_Testcases.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance
		self.Grid_Testcases.SetLabelBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )
		self.Grid_Testcases.SetLabelTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )

		# Cell Defaults
		self.Grid_Testcases.SetDefaultCellTextColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.Grid_Testcases.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer_StartupScreen_GridandText.Add( self.Grid_Testcases, 0, wx.ALL, 5 )


		self.SetSizer( bSizer_StartupScreen_GridandText )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.Frame_StartupScreenOnClose )
		self.Bind( wx.EVT_MENU, self.MenuItem_StartFuzzingOnMenuSelection, id = self.MenuItem_StartFuzzing.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItem_StopFuzzingOnMenuSelection, id = self.MenuItem_StopFuzzing.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItem_TextFormStringOnMenuSelection, id = self.MenuItem_TextFormString.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItem_TextFormBytesOnMenuSelection, id = self.MenuItem_TextFormBytes.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItem_PathFormRelativeOnMenuSelection, id = self.MenuItem_PathFormRelative.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItem_MinimizeFuzzOnMenuSelection, id = self.MenuItem_MinimizeFuzz.GetId() )
		self.Bind( wx.EVT_MENU, self.MenuItem_InputTestcaseandRunOnMenuSelection, id = self.MenuItem_InputTestcaseandRun.GetId() )
		self.Grid_Testcases.Bind( wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.Grid_TestcasesOnGridLabelLeftClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Frame_StartupScreenOnClose( self, event ):
		event.Skip()

	def MenuItem_StartFuzzingOnMenuSelection( self, event ):
		event.Skip()

	def MenuItem_StopFuzzingOnMenuSelection( self, event ):
		event.Skip()

	def MenuItem_TextFormStringOnMenuSelection( self, event ):
		event.Skip()

	def MenuItem_TextFormBytesOnMenuSelection( self, event ):
		event.Skip()

	def MenuItem_PathFormRelativeOnMenuSelection( self, event ):
		event.Skip()

	def MenuItem_MinimizeFuzzOnMenuSelection( self, event ):
		event.Skip()

	def MenuItem_InputTestcaseandRunOnMenuSelection( self, event ):
		event.Skip()

	def Grid_TestcasesOnGridLabelLeftClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_AskCompileforAFL
###########################################################################

class Dialog_AskCompileforAFL ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_AskCompileforAFL = wx.BoxSizer( wx.VERTICAL )

		self.Text_AskCompileforAFL = wx.StaticText( self, wx.ID_ANY, u"Did you compile your program by afl-gcc or afl-g++?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_AskCompileforAFL.Wrap( -1 )

		bSizer_AskCompileforAFL.Add( self.Text_AskCompileforAFL, 0, wx.ALL, 5 )

		bSizer_YesorNo = wx.StdDialogButtonSizer()
		self.bSizer_YesorNoYes = wx.Button( self, wx.ID_YES )
		bSizer_YesorNo.AddButton( self.bSizer_YesorNoYes )
		self.bSizer_YesorNoNo = wx.Button( self, wx.ID_NO )
		bSizer_YesorNo.AddButton( self.bSizer_YesorNoNo )
		bSizer_YesorNo.Realize();

		bSizer_AskCompileforAFL.Add( bSizer_YesorNo, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_AskCompileforAFL )
		self.Layout()
		bSizer_AskCompileforAFL.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.bSizer_YesorNoNo.Bind( wx.EVT_BUTTON, self.bSizer_YesorNoOnNoButtonClick )
		self.bSizer_YesorNoYes.Bind( wx.EVT_BUTTON, self.bSizer_YesorNoOnYesButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bSizer_YesorNoOnNoButtonClick( self, event ):
		event.Skip()

	def bSizer_YesorNoOnYesButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_CompileforAFLCommand
###########################################################################

class Dialog_CompileforAFLCommand ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_CompileforAFLCommand = wx.BoxSizer( wx.VERTICAL )

		self.Text_PleaseCompileforAFL = wx.StaticText( self, wx.ID_ANY, u"Please compile your program for AFL by one of the following commands.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_PleaseCompileforAFL.Wrap( -1 )

		bSizer_CompileforAFLCommand.Add( self.Text_PleaseCompileforAFL, 0, wx.ALL, 5 )

		self.Text_CompileCommandforC = wx.StaticText( self, wx.ID_ANY, u"C program: afl-gcc -o <file> <source_code>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_CompileCommandforC.Wrap( -1 )

		bSizer_CompileforAFLCommand.Add( self.Text_CompileCommandforC, 0, wx.ALL, 5 )

		self.Text_CompileCommandforCplusplus = wx.StaticText( self, wx.ID_ANY, u"C++ program: afl-g++ -o <file> <source_code>", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_CompileCommandforCplusplus.Wrap( -1 )

		bSizer_CompileforAFLCommand.Add( self.Text_CompileCommandforCplusplus, 0, wx.ALL, 5 )

		self.Text_ExplanationParameter = wx.StaticText( self, wx.ID_ANY, u"<file>: executable file <source_code>: path of source code", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_ExplanationParameter.Wrap( -1 )

		bSizer_CompileforAFLCommand.Add( self.Text_ExplanationParameter, 0, wx.ALL, 5 )

		self.Button_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_CompileforAFLCommand.Add( self.Button_OK, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer_CompileforAFLCommand )
		self.Layout()
		bSizer_CompileforAFLCommand.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Button_OK.Bind( wx.EVT_BUTTON, self.Button_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Button_OKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_ProgramChoose
###########################################################################

class Dialog_ProgramChoose ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_ProgramChoose = wx.BoxSizer( wx.VERTICAL )

		self.Text_ChooseProgram = wx.StaticText( self, wx.ID_ANY, u"Please select an executable file for fuzzing.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_ChooseProgram.Wrap( -1 )

		bSizer_ProgramChoose.Add( self.Text_ChooseProgram, 0, wx.ALL, 5 )

		self.FilePicker_ChooseProgram = wx.FilePickerCtrl( self, wx.ID_ANY, u"./", u"Select a file", wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer_ProgramChoose.Add( self.FilePicker_ChooseProgram, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer_OKorCancel = wx.StdDialogButtonSizer()
		self.bSizer_OKorCancelOK = wx.Button( self, wx.ID_OK )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelOK )
		self.bSizer_OKorCancelCancel = wx.Button( self, wx.ID_CANCEL )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelCancel )
		bSizer_OKorCancel.Realize();

		bSizer_ProgramChoose.Add( bSizer_OKorCancel, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_ProgramChoose )
		self.Layout()
		bSizer_ProgramChoose.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.FilePicker_ChooseProgram.Bind( wx.EVT_FILEPICKER_CHANGED, self.FilePicker_ChooseProgramOnFileChanged )
		self.bSizer_OKorCancelCancel.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnCancelButtonClick )
		self.bSizer_OKorCancelOK.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnOKButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def FilePicker_ChooseProgramOnFileChanged( self, event ):
		event.Skip()

	def bSizer_OKorCancelOnCancelButtonClick( self, event ):
		event.Skip()

	def bSizer_OKorCancelOnOKButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_InputChoose
###########################################################################

class Dialog_InputChoose ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_InputChoose = wx.BoxSizer( wx.VERTICAL )

		self.Text_ChooseInput = wx.StaticText( self, wx.ID_ANY, u"Please select a directory including seed input files.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_ChooseInput.Wrap( -1 )

		bSizer_InputChoose.Add( self.Text_ChooseInput, 0, wx.ALL, 5 )

		self.DirPicker_ChooseInput = wx.DirPickerCtrl( self, wx.ID_ANY, u"./", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer_InputChoose.Add( self.DirPicker_ChooseInput, 0, wx.ALL, 5 )

		bSizer_OKorCancel = wx.StdDialogButtonSizer()
		self.bSizer_OKorCancelOK = wx.Button( self, wx.ID_OK )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelOK )
		self.bSizer_OKorCancelCancel = wx.Button( self, wx.ID_CANCEL )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelCancel )
		bSizer_OKorCancel.Realize();

		bSizer_InputChoose.Add( bSizer_OKorCancel, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_InputChoose )
		self.Layout()
		bSizer_InputChoose.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.bSizer_OKorCancelCancel.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnCancelButtonClick )
		self.bSizer_OKorCancelOK.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnOKButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bSizer_OKorCancelOnCancelButtonClick( self, event ):
		event.Skip()

	def bSizer_OKorCancelOnOKButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_AskStartFuzzing
###########################################################################

class Dialog_AskStartFuzzing ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 357,161 ), style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_AskStartFuzzing = wx.BoxSizer( wx.VERTICAL )

		self.Text_AskStartFuzzing = wx.StaticText( self, wx.ID_ANY, u"Let's start fuzzing with the following configuration.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_AskStartFuzzing.Wrap( -1 )

		bSizer_AskStartFuzzing.Add( self.Text_AskStartFuzzing, 0, wx.ALL, 5 )

		self.Text_FuzzingProgram = wx.StaticText( self, wx.ID_ANY, u"Program you selected: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_FuzzingProgram.Wrap( -1 )

		bSizer_AskStartFuzzing.Add( self.Text_FuzzingProgram, 0, wx.ALL, 5 )

		self.Text_FuzzingInput = wx.StaticText( self, wx.ID_ANY, u"Seed input: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_FuzzingInput.Wrap( -1 )

		bSizer_AskStartFuzzing.Add( self.Text_FuzzingInput, 0, wx.ALL, 5 )

		bSizer_OKorCancel = wx.StdDialogButtonSizer()
		self.bSizer_OKorCancelOK = wx.Button( self, wx.ID_OK )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelOK )
		self.bSizer_OKorCancelCancel = wx.Button( self, wx.ID_CANCEL )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelCancel )
		bSizer_OKorCancel.Realize();

		bSizer_AskStartFuzzing.Add( bSizer_OKorCancel, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_AskStartFuzzing )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.bSizer_OKorCancelCancel.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnCancelButtonClick )
		self.bSizer_OKorCancelOK.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnOKButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bSizer_OKorCancelOnCancelButtonClick( self, event ):
		event.Skip()

	def bSizer_OKorCancelOnOKButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_AskStopFuzzing
###########################################################################

class Dialog_AskStopFuzzing ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_AskStopFuzzing = wx.BoxSizer( wx.VERTICAL )

		self.Text_AskStopFuzzing = wx.StaticText( self, wx.ID_ANY, u"Do you want to stop fuzzing?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_AskStopFuzzing.Wrap( -1 )

		bSizer_AskStopFuzzing.Add( self.Text_AskStopFuzzing, 0, wx.ALL, 5 )

		bSizer_YesorNo = wx.StdDialogButtonSizer()
		self.bSizer_YesorNoYes = wx.Button( self, wx.ID_YES )
		bSizer_YesorNo.AddButton( self.bSizer_YesorNoYes )
		self.bSizer_YesorNoNo = wx.Button( self, wx.ID_NO )
		bSizer_YesorNo.AddButton( self.bSizer_YesorNoNo )
		bSizer_YesorNo.Realize();

		bSizer_AskStopFuzzing.Add( bSizer_YesorNo, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_AskStopFuzzing )
		self.Layout()
		bSizer_AskStopFuzzing.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.bSizer_YesorNoNo.Bind( wx.EVT_BUTTON, self.bSizer_YesorNoOnNoButtonClick )
		self.bSizer_YesorNoYes.Bind( wx.EVT_BUTTON, self.bSizer_YesorNoOnYesButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bSizer_YesorNoOnNoButtonClick( self, event ):
		event.Skip()

	def bSizer_YesorNoOnYesButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_ErrorLog
###########################################################################

class Dialog_ErrorLog ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_ErrorLog = wx.BoxSizer( wx.VERTICAL )

		self.Text_CausedError = wx.StaticText( self, wx.ID_ANY, u"Error!!", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_CausedError.Wrap( -1 )

		bSizer_ErrorLog.Add( self.Text_CausedError, 0, wx.ALL, 5 )

		self.Text_ErrorCode = wx.StaticText( self, wx.ID_ANY, u"ErrorCode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_ErrorCode.Wrap( -1 )

		bSizer_ErrorLog.Add( self.Text_ErrorCode, 0, wx.ALL, 5 )

		self.Text_Solution = wx.StaticText( self, wx.ID_ANY, u"Solution", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_Solution.Wrap( -1 )

		bSizer_ErrorLog.Add( self.Text_Solution, 0, wx.ALL, 5 )

		self.Button_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_ErrorLog.Add( self.Button_OK, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer_ErrorLog )
		self.Layout()
		bSizer_ErrorLog.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Button_OK.Bind( wx.EVT_BUTTON, self.Button_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Button_OKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_MinimizeFuzz
###########################################################################

class Dialog_MinimizeFuzz ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_MinimizeFuzz = wx.BoxSizer( wx.VERTICAL )

		self.Text_ChoisedFuzz = wx.StaticText( self, wx.ID_ANY, u"Fuzz you selected: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_ChoisedFuzz.Wrap( -1 )

		bSizer_MinimizeFuzz.Add( self.Text_ChoisedFuzz, 0, wx.ALL, 5 )

		bSizer_SpinCtrlandText = wx.BoxSizer( wx.HORIZONTAL )

		self.Text_timeout = wx.StaticText( self, wx.ID_ANY, u"Timeout (in seconds)\nZero means disabling timeout.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_timeout.Wrap( -1 )

		bSizer_SpinCtrlandText.Add( self.Text_timeout, 0, wx.ALL, 5 )

		self.spinCtrlDouble_timeout = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 3, 0.5 )
		self.spinCtrlDouble_timeout.SetDigits( 1 )
		bSizer_SpinCtrlandText.Add( self.spinCtrlDouble_timeout, 0, wx.ALL, 5 )


		bSizer_MinimizeFuzz.Add( bSizer_SpinCtrlandText, 1, wx.EXPAND, 5 )

		self.Text_AskMinimizeFuzz = wx.StaticText( self, wx.ID_ANY, u"Do you want to reduce this fuzz?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_AskMinimizeFuzz.Wrap( -1 )

		bSizer_MinimizeFuzz.Add( self.Text_AskMinimizeFuzz, 0, wx.ALL, 5 )

		bSizer_YesorNo = wx.StdDialogButtonSizer()
		self.bSizer_YesorNoYes = wx.Button( self, wx.ID_YES )
		bSizer_YesorNo.AddButton( self.bSizer_YesorNoYes )
		self.bSizer_YesorNoNo = wx.Button( self, wx.ID_NO )
		bSizer_YesorNo.AddButton( self.bSizer_YesorNoNo )
		bSizer_YesorNo.Realize();

		bSizer_MinimizeFuzz.Add( bSizer_YesorNo, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer_MinimizeFuzz )
		self.Layout()
		bSizer_MinimizeFuzz.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.bSizer_YesorNoNo.Bind( wx.EVT_BUTTON, self.bSizer_YesorNoOnNoButtonClick )
		self.bSizer_YesorNoYes.Bind( wx.EVT_BUTTON, self.bSizer_YesorNoOnYesButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def bSizer_YesorNoOnNoButtonClick( self, event ):
		event.Skip()

	def bSizer_YesorNoOnYesButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_FuzzAlreadyMinimized
###########################################################################

class Dialog_FuzzAlreadyMinimized ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_FuzzAlreadyMinimized = wx.BoxSizer( wx.VERTICAL )

		self.Text_FuzzAlreadyMinimized = wx.StaticText( self, wx.ID_ANY, u"This fuzz has been reduced already.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_FuzzAlreadyMinimized.Wrap( -1 )

		bSizer_FuzzAlreadyMinimized.Add( self.Text_FuzzAlreadyMinimized, 0, wx.ALL, 5 )

		self.Button_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_FuzzAlreadyMinimized.Add( self.Button_OK, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer_FuzzAlreadyMinimized )
		self.Layout()
		bSizer_FuzzAlreadyMinimized.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Button_OK.Bind( wx.EVT_BUTTON, self.Button_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Button_OKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_InputTestcaseandRun
###########################################################################

class Dialog_InputTestcaseandRun ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_InputTestcaseandRun = wx.BoxSizer( wx.VERTICAL )

		self.Text_YouCanInputTestcasetoProgram = wx.StaticText( self, wx.ID_ANY, u"You can run the program with the fuzz by executing the following command.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_YouCanInputTestcasetoProgram.Wrap( -1 )

		bSizer_InputTestcaseandRun.Add( self.Text_YouCanInputTestcasetoProgram, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer_CommandandCopyButton = wx.BoxSizer( wx.HORIZONTAL )

		self.TextCtrl_CommandforInputTestcaseandRun = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,-1 ), wx.TE_READONLY )
		bSizer_CommandandCopyButton.Add( self.TextCtrl_CommandforInputTestcaseandRun, 0, wx.ALL, 5 )

		self.Button_Copy = wx.Button( self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer_CommandandCopyButton.Add( self.Button_Copy, 0, wx.ALL, 5 )


		bSizer_InputTestcaseandRun.Add( bSizer_CommandandCopyButton, 0, wx.EXPAND, 5 )

		self.CheckBox_UseGDBorNot = wx.CheckBox( self, wx.ID_ANY, u"Display the command that invokes GDB", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_InputTestcaseandRun.Add( self.CheckBox_UseGDBorNot, 0, wx.ALL, 5 )

		self.Text_InputTestcase = wx.StaticText( self, wx.ID_ANY, u"Fuzz for the program", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_InputTestcase.Wrap( -1 )

		bSizer_InputTestcaseandRun.Add( self.Text_InputTestcase, 0, wx.ALL, 5 )

		self.RadioBtn_CrashTestcase = wx.RadioButton( self, wx.ID_ANY, u"Fuzz which caused crash", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_InputTestcaseandRun.Add( self.RadioBtn_CrashTestcase, 0, wx.ALL, 5 )

		self.RadioBtn_OriginalTestcase = wx.RadioButton( self, wx.ID_ANY, u"Original fuzz", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_InputTestcaseandRun.Add( self.RadioBtn_OriginalTestcase, 0, wx.ALL, 5 )

		self.RadioBtn_MinimizedTestcase = wx.RadioButton( self, wx.ID_ANY, u"Reduced fuzz", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_InputTestcaseandRun.Add( self.RadioBtn_MinimizedTestcase, 0, wx.ALL, 5 )

		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Note: If you select the \"Display relative path\" in View menu \nand tack the checks out of the checkbox, \nyou should fix the current directory correctly, \notherwise the command doesn't work correctly.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )

		bSizer_InputTestcaseandRun.Add( self.m_staticText23, 0, wx.ALL, 5 )

		bSizer_Buttons = wx.BoxSizer( wx.HORIZONTAL )

		self.Button_RunGDB = wx.Button( self, wx.ID_ANY, u"Invoke GDB and feed fuzz to the program", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_Buttons.Add( self.Button_RunGDB, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Button_Exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_Buttons.Add( self.Button_Exit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		bSizer_InputTestcaseandRun.Add( bSizer_Buttons, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer_InputTestcaseandRun )
		self.Layout()
		bSizer_InputTestcaseandRun.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Button_Copy.Bind( wx.EVT_BUTTON, self.Button_CopyOnButtonClick )
		self.CheckBox_UseGDBorNot.Bind( wx.EVT_CHECKBOX, self.CheckBox_UseGDBorNotOnCheckBox )
		self.RadioBtn_CrashTestcase.Bind( wx.EVT_RADIOBUTTON, self.RadioBtn_CrashTestcaseOnRadioButton )
		self.RadioBtn_OriginalTestcase.Bind( wx.EVT_RADIOBUTTON, self.RadioBtn_OriginalTestcaseOnRadioButton )
		self.RadioBtn_MinimizedTestcase.Bind( wx.EVT_RADIOBUTTON, self.RadioBtn_MinimizedTestcaseOnRadioButton )
		self.Button_RunGDB.Bind( wx.EVT_BUTTON, self.Button_RunGDBOnButtonClick )
		self.Button_Exit.Bind( wx.EVT_BUTTON, self.Button_ExitOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Button_CopyOnButtonClick( self, event ):
		event.Skip()

	def CheckBox_UseGDBorNotOnCheckBox( self, event ):
		event.Skip()

	def RadioBtn_CrashTestcaseOnRadioButton( self, event ):
		event.Skip()

	def RadioBtn_OriginalTestcaseOnRadioButton( self, event ):
		event.Skip()

	def RadioBtn_MinimizedTestcaseOnRadioButton( self, event ):
		event.Skip()

	def Button_RunGDBOnButtonClick( self, event ):
		event.Skip()

	def Button_ExitOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_ReplicateCrashCommand
###########################################################################

class Dialog_ReplicateCrashCommand ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_CommandandOKButton = wx.BoxSizer( wx.VERTICAL )

		self.Text_YouCanReplicateCrashbyThisCommand = wx.StaticText( self, wx.ID_ANY, u"以下のコマンドを端末に入力することでクラッシュを再現できます", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_YouCanReplicateCrashbyThisCommand.Wrap( -1 )

		bSizer_CommandandOKButton.Add( self.Text_YouCanReplicateCrashbyThisCommand, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer_CommandandCopyButton = wx.BoxSizer( wx.HORIZONTAL )

		self.TextCtrl_ReplicateCrashCommand = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_READONLY )
		bSizer_CommandandCopyButton.Add( self.TextCtrl_ReplicateCrashCommand, 0, wx.ALL, 5 )

		self.Button_Copy = wx.Button( self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer_CommandandCopyButton.Add( self.Button_Copy, 0, wx.ALL, 5 )


		bSizer_CommandandOKButton.Add( bSizer_CommandandCopyButton, 1, wx.EXPAND, 5 )

		self.RadioBtn_UseGDB = wx.RadioButton( self, wx.ID_ANY, u"GDBを使用する", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_CommandandOKButton.Add( self.RadioBtn_UseGDB, 0, wx.ALL, 5 )

		self.RadioBtn_NotUseGDB = wx.RadioButton( self, wx.ID_ANY, u"GDBを使用しない", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_CommandandOKButton.Add( self.RadioBtn_NotUseGDB, 0, wx.ALL, 5 )

		self.Button_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_CommandandOKButton.Add( self.Button_OK, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer_CommandandOKButton )
		self.Layout()
		bSizer_CommandandOKButton.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Button_Copy.Bind( wx.EVT_BUTTON, self.Button_CopyOnButtonClick )
		self.RadioBtn_UseGDB.Bind( wx.EVT_RADIOBUTTON, self.RadioBtn_UseGDBOnRadioButton )
		self.RadioBtn_NotUseGDB.Bind( wx.EVT_RADIOBUTTON, self.RadioBtn_NotUseGDBOnRadioButton )
		self.Button_OK.Bind( wx.EVT_BUTTON, self.Button_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Button_CopyOnButtonClick( self, event ):
		event.Skip()

	def RadioBtn_UseGDBOnRadioButton( self, event ):
		event.Skip()

	def RadioBtn_NotUseGDBOnRadioButton( self, event ):
		event.Skip()

	def Button_OKOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class Dialog_ComparewithOriginalCommand
###########################################################################

class Dialog_ComparewithOriginalCommand ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer_CommandandOKButton = wx.BoxSizer( wx.VERTICAL )

		self.Text_YouCanComparewithOriginalbyThisCommand = wx.StaticText( self, wx.ID_ANY, u"以下のコマンドを端末に入力することでクラッシュを再現できます", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_YouCanComparewithOriginalbyThisCommand.Wrap( -1 )

		bSizer_CommandandOKButton.Add( self.Text_YouCanComparewithOriginalbyThisCommand, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer_CommandandCopyButton = wx.BoxSizer( wx.HORIZONTAL )

		self.TextCtrl_ComparewithOriginalCommand = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), wx.TE_READONLY )
		bSizer_CommandandCopyButton.Add( self.TextCtrl_ComparewithOriginalCommand, 0, wx.ALL, 5 )

		self.Button_Copy = wx.Button( self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		bSizer_CommandandCopyButton.Add( self.Button_Copy, 0, wx.ALL, 5 )


		bSizer_CommandandOKButton.Add( bSizer_CommandandCopyButton, 1, wx.EXPAND, 5 )

		self.RadioBtn_UseGDB = wx.RadioButton( self, wx.ID_ANY, u"GDBを使用する", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_CommandandOKButton.Add( self.RadioBtn_UseGDB, 0, wx.ALL, 5 )

		self.RadioBtn_NotUseGDB = wx.RadioButton( self, wx.ID_ANY, u"GDBを使用しない", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_CommandandOKButton.Add( self.RadioBtn_NotUseGDB, 0, wx.ALL, 5 )

		self.Button_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_CommandandOKButton.Add( self.Button_OK, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( bSizer_CommandandOKButton )
		self.Layout()
		bSizer_CommandandOKButton.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Button_Copy.Bind( wx.EVT_BUTTON, self.Button_CopyOnButtonClick )
		self.RadioBtn_UseGDB.Bind( wx.EVT_RADIOBUTTON, self.RadioBtn_UseGDBOnRadioButton )
		self.RadioBtn_NotUseGDB.Bind( wx.EVT_RADIOBUTTON, self.RadioBtn_NotUseGDBOnRadioButton )
		self.Button_OK.Bind( wx.EVT_BUTTON, self.Button_OKOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def Button_CopyOnButtonClick( self, event ):
		event.Skip()

	def RadioBtn_UseGDBOnRadioButton( self, event ):
		event.Skip()

	def RadioBtn_NotUseGDBOnRadioButton( self, event ):
		event.Skip()

	def Button_OKOnButtonClick( self, event ):
		event.Skip()


