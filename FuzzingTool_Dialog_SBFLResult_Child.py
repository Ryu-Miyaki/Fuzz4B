import wx
import FuzzingTool
# from FuzzingTool_Dialog_SBFLResult import FuzzingTool_Dialog_SBFLResult
from itertools import groupby
import wx.lib.plot as plot
import csv

# Implementing Dialog_SBFLResult
class FuzzingTool_Dialog_SBFLResult_Child(wx.Dialog):
	def __init__(self, parent, sbfl_result):
		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.RESIZE_BORDER)
		self.sbfl_result = sbfl_result
		
		self.SetSizeHints(wx.Size(500, 500), wx.DefaultSize)

		self.ShowTable = True

		bSizer_SBFLResult = wx.BoxSizer(wx.VERTICAL)
		self.Notebook_SBFLResult = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer_SBFLResult.Add( self.Notebook_SBFLResult, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer_Buttons = wx.BoxSizer(wx.HORIZONTAL)
		self.Button_Switch = wx.Button( self, wx.ID_ANY, u"Display the result in graphs", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Button_CSVOutput = wx.Button( self, wx.ID_ANY, u"Download csv", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Button_Exit = wx.Button( self, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_Buttons.Add(self.Button_Switch, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		bSizer_Buttons.Add(self.Button_CSVOutput, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		bSizer_Buttons.Add(self.Button_Exit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		bSizer_SBFLResult.Add( bSizer_Buttons, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.MakeNotebookPages(self.ShowTable)

		self.SetSizer(bSizer_SBFLResult)
		self.Layout()
		
		self.Centre(wx.BOTH)

		self.Button_Switch.Bind( wx.EVT_BUTTON, self.Button_SwitchOnButtonClick )
		self.Button_CSVOutput.Bind( wx.EVT_BUTTON, self.Button_CSVOutputOnButtonClick )
		self.Button_Exit.Bind( wx.EVT_BUTTON, self.Button_ExitOnButtonClick )


	# Handlers for Dialog_SBFLResult events.
	def Button_SwitchOnButtonClick( self, event ):
		self.ShowTable = not self.ShowTable

		nowPage = self.Notebook_SBFLResult.GetSelection()

		self.Notebook_SBFLResult.DeleteAllPages()
		
		if self.ShowTable:
			self.Button_Switch.SetLabel("Display the result in graphs")
		else:
			self.Button_Switch.SetLabel("Display the result in tables")

		self.MakeNotebookPages(self.ShowTable)
		
		self.Layout()
		self.Notebook_SBFLResult.SetSelection(nowPage)


	def Button_CSVOutputOnButtonClick( self, event ):
		# TODO: Implement Button_ExitOnButtonClick
		dialog = wx.FileDialog(self, u"Select a file", "./", "SBFLResult.csv", "*.csv", wx.FD_SAVE)
		if dialog.ShowModal() == wx.ID_OK:
			with open(dialog.GetPath(), 'w', encoding = 'utf-8', newline = '') as file:
				csvWriter = csv.DictWriter(file, ["Sourcefile", "Number", "Statement", "Suspicious"])
				csvWriter.writeheader()
				csvWriter.writerows(self.sbfl_result)
		dialog.Destroy()

	def Button_ExitOnButtonClick( self, event ):
		# TODO: Implement Button_ExitOnButtonClick
		self.EndModal(True)

	def MakeNotebookPages( self, showtable ):
		index = 0
		for key, g in groupby(self.sbfl_result, key = lambda m: m["Sourcefile"]):
			group = []
			group.append(list(g))

			panel = wx.Panel(self.Notebook_SBFLResult, wx.ID_ANY)
			self.Notebook_SBFLResult.InsertPage(index, panel, key)
			
			bSizer = wx.BoxSizer(wx.VERTICAL)

			if showtable:
				result = self.MakeSBFLResultGrid(panel, group)
			else:
				result = self.MakeSBFLResultGraph(panel, group)
			
			bSizer.Add(result, 1, wx.EXPAND |wx.ALL, 5)
			panel.SetSizer(bSizer)
			panel.Layout()
			bSizer.Fit(panel)

	def MakeSBFLResultGrid( self, panel, group ):
		grid = wx.grid.Grid(panel, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 300), wx.HSCROLL|wx.VSCROLL)
	
		grid.CreateGrid(len(group[0]), 3)
		grid.EnableEditing(False)
		grid.EnableGridLines(True)
		grid.EnableDragGridSize(False)
		grid.SetMargins(0, 0)
	
		grid.AutoSizeColumns()
		grid.EnableDragColMove(False)
		grid.EnableDragColSize(False)
		grid.SetColLabelSize(30)
		grid.SetColLabelValue(0, u"Line No.")
		grid.SetColLabelValue(1, u"Source code")
		grid.SetColLabelValue(2, u"Suspicious value")
		grid.SetColLabelValue(3, wx.EmptyString)
		grid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
	
		grid.EnableDragRowSize(False)
		grid.SetRowLabelSize(0)
		grid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
	
		grid.SetLabelBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_GRAYTEXT))
		grid.SetLabelFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
		grid.SetLabelTextColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))
	
		grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
		
		rows = 0
		for member in group[0]:
			grid.SetCellValue(rows, 0, str(member["Number"]))
			grid.SetCellValue(rows, 1, member["Statement"])
			grid.SetCellValue(rows, 2, str(member["Suspicious"]))
			if 0.25 <= member["Suspicious"] and member["Suspicious"] < 0.50:
				grid.SetCellBackgroundColour(rows, 1, wx.Colour("#ffff00"))
				grid.SetCellBackgroundColour(rows, 2, wx.Colour("#ffff00"))
			elif 0.50 <= member["Suspicious"] and member["Suspicious"] < 0.75:
				grid.SetCellBackgroundColour(rows, 1, wx.Colour("#ffa500"))
				grid.SetCellBackgroundColour(rows, 2, wx.Colour("#ffa500"))
			elif 0.75 <= member["Suspicious"]:
				grid.SetCellBackgroundColour(rows, 1, wx.Colour("#ff0000"))
				grid.SetCellBackgroundColour(rows, 2, wx.Colour("#ff0000"))
			rows += 1
		grid.AutoSizeColumns()
		return grid

	def MakeSBFLResultGraph( self, panel, group):
		xy_val = []
		for member in group[0]:
			xy_val.append((member["Number"], member["Suspicious"]))
		graph = plot.PlotCanvas(panel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL)
		line = plot.PolyLine(xy_val)
		graphic = plot.PlotGraphics([line], group[0][0]["Sourcefile"], "Line No.", "Suspicious value")
		graph.ySpec = (0, 1)
		graph.Draw(graphic)
		return graph

