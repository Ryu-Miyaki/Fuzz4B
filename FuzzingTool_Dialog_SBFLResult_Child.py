import wx
import FuzzingTool
# from FuzzingTool_Dialog_SBFLResult import FuzzingTool_Dialog_SBFLResult
from itertools import groupby

# Implementing Dialog_SBFLResult
class FuzzingTool_Dialog_SBFLResult_Child(wx.Dialog):
	def __init__(self, parent, sbfl_result):
		wx.Dialog.__init__ (self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,700 ), style = wx.RESIZE_BORDER)
		self.sbfl_result = sbfl_result
		
		self.SetSizeHints(wx.Size(500, 500), wx.DefaultSize)

		bSizer_SBFLResult = wx.BoxSizer(wx.VERTICAL)
		self.Notebook_SBFLResult = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer_SBFLResult.Add( self.Notebook_SBFLResult, 1, wx.EXPAND |wx.ALL, 5 )
		self.Button_OK = wx.Button( self, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer_SBFLResult.Add( self.Button_OK, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		index = 0
		for key, g in groupby(self.sbfl_result, key = lambda m: m["Sourcefile"]):
			group = []
			group.append(list(g))

			panel = wx.Panel(self.Notebook_SBFLResult, wx.ID_ANY)
			self.Notebook_SBFLResult.InsertPage(index, panel, key)
			
			bSizer = wx.BoxSizer(wx.VERTICAL)
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
			grid.SetColLabelValue(2, u"Suspicious Value")
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
			index += 1
			bSizer.Add(grid, 1, wx.EXPAND |wx.ALL, 5)
			panel.SetSizer(bSizer)
			panel.Layout()
			bSizer.Fit(panel)

		self.SetSizer(bSizer_SBFLResult)
		self.Layout()
		
		self.Centre(wx.BOTH)

		self.Button_OK.Bind( wx.EVT_BUTTON, self.Button_OKOnButtonClick )


	# Handlers for Dialog_SBFLResult events.
	def Button_OKOnButtonClick( self, event ):
		# TODO: Implement Button_OKOnButtonClick
		self.EndModal(True)


