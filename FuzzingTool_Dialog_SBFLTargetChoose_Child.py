import wx
import FuzzingTool

# Implementing Dialog_SBFLTargetChoose
class FuzzingTool_Dialog_SBFLTargetChoose_Child(wx.Dialog):
	def __init__( self, parent, compilation_dir="./"):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.bSizer_SBFLTargetChoose = wx.BoxSizer( wx.VERTICAL )

		self.Text_SBFLTargetChoose = wx.StaticText( self, wx.ID_ANY, u"Please select source files that may contain fault locations.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_SBFLTargetChoose.Wrap( -1 )

		self.bSizer_SBFLTargetChoose.Add( self.Text_SBFLTargetChoose, 0, wx.ALL, 5 )

		bSizer_FilePickerandText = wx.BoxSizer( wx.HORIZONTAL )

		self.Text_SBFLTarget = wx.StaticText( self, wx.ID_ANY, u"Source file 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_SBFLTarget.Wrap( -1 )

		bSizer_FilePickerandText.Add( self.Text_SBFLTarget, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.FilePicker_SBFLTarget = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer_FilePickerandText.Add( self.FilePicker_SBFLTarget, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Text_Caution = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_Caution.Wrap( -1 )

		bSizer_FilePickerandText.Add( self.Text_Caution, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.bSizer_SBFLTargetChoose.Add( bSizer_FilePickerandText, 1, wx.EXPAND, 5 )

		self.Button_Add = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.bSizer_SBFLTargetChoose.Add( self.Button_Add, 0, wx.ALL, 5 )

		bSizer_OKorCancel = wx.StdDialogButtonSizer()
		self.bSizer_OKorCancelOK = wx.Button( self, wx.ID_OK )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelOK )
		self.bSizer_OKorCancelCancel = wx.Button( self, wx.ID_CANCEL )
		bSizer_OKorCancel.AddButton( self.bSizer_OKorCancelCancel )
		bSizer_OKorCancel.Realize()

		self.bSizer_SBFLTargetChoose.Add( bSizer_OKorCancel, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( self.bSizer_SBFLTargetChoose )
		self.Layout()
		self.bSizer_SBFLTargetChoose.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.FilePicker_SBFLTarget.Bind( wx.EVT_FILEPICKER_CHANGED, self.FilePicker_SBFLTargetOnFileChanged )
		self.Button_Add.Bind( wx.EVT_BUTTON, self.Button_AddOnButtonClick )
		self.bSizer_OKorCancelCancel.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnCancelButtonClick )
		self.bSizer_OKorCancelOK.Bind( wx.EVT_BUTTON, self.bSizer_OKorCancelOnOKButtonClick )
		
		self.bSizer_OKorCancelOK.Disable()
		self.compilation_dir = compilation_dir
		self.FilePicker_SBFLTarget.SetInitialDirectory(self.compilation_dir)
		self.filepicker_list = [self.FilePicker_SBFLTarget]
		self.filepicker_index = 0
		self.caution = self.Text_Caution

	# Handlers for Dialog_SBFLTargetChoose events.
	def FilePicker_SBFLTargetOnFileChanged( self, event ):
		# TODO: Implement FilePicker_SBFLTargetOnFileChanged
		self.bSizer_OKorCancelOK.Enable()

	def Button_AddOnButtonClick( self, event ):
		# TODO: Implement Button_AddOnButtonClick
		if self.filepicker_list[self.filepicker_index].GetPath() != "":
			self.caution.SetLabel("")
			self.Add_Filepicker()
		else:
			self.caution.SetLabel("Please select a file.")
			self.Layout()
			self.bSizer_SBFLTargetChoose.Fit(self)

	def Add_Filepicker(self):
		self.filepicker_index += 1
		bSizer = wx.BoxSizer(wx.HORIZONTAL)
		Text = wx.StaticText(self, wx.ID_ANY, u"Source file " + str(self.filepicker_index + 1), wx.DefaultPosition, wx.DefaultSize, 0)
		Text.Wrap(-1)
		bSizer.Add(Text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		FilePicker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
		FilePicker.SetInitialDirectory(self.compilation_dir)
		bSizer.Add(FilePicker, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		self.caution = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
		self.caution.Wrap(-1)
		bSizer.Add(self.caution, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		self.bSizer_SBFLTargetChoose.Insert(self.bSizer_SBFLTargetChoose.GetItemCount() - 2, bSizer, 1, wx.EXPAND, 5)
		self.Layout()
		self.bSizer_SBFLTargetChoose.Fit(self)
		self.filepicker_list.append(FilePicker)

	def bSizer_OKorCancelOnCancelButtonClick( self, event ):
		# TODO: Implement bSizer_OKorCancelOnCancelButtonClick
		self.EndModal(False)

	def bSizer_OKorCancelOnOKButtonClick( self, event ):
		# TODO: Implement bSizer_OKorCancelOnOKButtonClick
		self.file_list = [filepicker.GetPath() for filepicker in self.filepicker_list if filepicker.GetPath() != ""]
		self.EndModal(True)
