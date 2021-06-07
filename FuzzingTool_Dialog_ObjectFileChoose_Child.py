import wx
import FuzzingTool
import pyperclip

# Implementing Dialog_ObjectFileChoose
class FuzzingTool_Dialog_ObjectFileChoose_Child( wx.Dialog ):
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.bSizer_ObjectFileChoose = wx.BoxSizer( wx.VERTICAL )

		self.Text_ObjectFileChoose = wx.StaticText( self, wx.ID_ANY, u"Please generate object (.o) files by afl-gcc or afl-g++ with the following options.\n※You should save all the source code and generated object files\n    under the directory where you compiled them.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_ObjectFileChoose.Wrap( -1 )

		self.bSizer_ObjectFileChoose.Add( self.Text_ObjectFileChoose, 0, wx.ALL, 5 )

		self.Text_Option_g = wx.StaticText( self, wx.ID_ANY, u"● -g", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_Option_g.Wrap( -1 )

		self.bSizer_ObjectFileChoose.Add( self.Text_Option_g, 0, wx.ALL, 5 )

		self.Text_Option_coverage = wx.StaticText( self, wx.ID_ANY, u"● --coverage", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_Option_coverage.Wrap( -1 )

		self.bSizer_ObjectFileChoose.Add( self.Text_Option_coverage, 0, wx.ALL, 5 )

		self.Text_Option_c = wx.StaticText( self, wx.ID_ANY, u"● -c", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_Option_c.Wrap( -1 )

		self.bSizer_ObjectFileChoose.Add( self.Text_Option_c, 0, wx.ALL, 5 )

		bSizer_CompileCommandandCopyButton = wx.BoxSizer( wx.HORIZONTAL )

		self.Text_CompileCommand = wx.StaticText( self, wx.ID_ANY, u"e.g. afl-gcc -g --coverage -c sourcefile.c", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_CompileCommand.Wrap( -1 )

		bSizer_CompileCommandandCopyButton.Add( self.Text_CompileCommand, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Button_Copy = wx.Button( self, wx.ID_ANY, u"Copy", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		bSizer_CompileCommandandCopyButton.Add( self.Button_Copy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.bSizer_ObjectFileChoose.Add( bSizer_CompileCommandandCopyButton, 1, wx.EXPAND, 5 )

		bSizer_CompilationDir = wx.BoxSizer( wx.HORIZONTAL )

		self.Text_CompilationDir = wx.StaticText( self, wx.ID_ANY, u"Directory where you compiled files", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Text_CompilationDir.Wrap( -1 )

		bSizer_CompilationDir.Add( self.Text_CompilationDir, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.DirPicker_CompilationCommand = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		bSizer_CompilationDir.Add( self.DirPicker_CompilationCommand, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


		self.bSizer_ObjectFileChoose.Add( bSizer_CompilationDir, 1, wx.EXPAND, 5 )

		bSizer_OKorCanncel = wx.StdDialogButtonSizer()
		self.bSizer_OKorCanncelOK = wx.Button( self, wx.ID_OK )
		bSizer_OKorCanncel.AddButton( self.bSizer_OKorCanncelOK )
		self.bSizer_OKorCanncelCancel = wx.Button( self, wx.ID_CANCEL )
		bSizer_OKorCanncel.AddButton( self.bSizer_OKorCanncelCancel )
		bSizer_OKorCanncel.Realize()

		self.bSizer_ObjectFileChoose.Add( bSizer_OKorCanncel, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.SetSizer( self.bSizer_ObjectFileChoose )
		self.Layout()
		self.bSizer_ObjectFileChoose.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Button_Copy.Bind( wx.EVT_BUTTON, self.Button_CopyOnButtonClick )
		self.DirPicker_CompilationCommand.Bind( wx.EVT_DIRPICKER_CHANGED, self.DirPicker_CompilationCommandOnDirChanged )
		self.bSizer_OKorCanncelCancel.Bind( wx.EVT_BUTTON, self.bSizer_OKorCanncelOnCancelButtonClick )
		self.bSizer_OKorCanncelOK.Bind( wx.EVT_BUTTON, self.bSizer_OKorCanncelOnOKButtonClick )

		self.bSizer_OKorCanncelOK.Disable()

		self.added_bsizer_list = []
		self.added_text_list = []
		self.added_filepicker_list = []
		self.otherobjectfilepicker_count = 0
		self.compilationdir_choosed = False

	# Handlers for Dialog_ObjectFileChoose events.
	def Button_CopyOnButtonClick( self, event ):
		# TODO: Implement Button_CopyOnButtonClick
		pyperclip.copy(self.Text_CompileCommand.GetLabel().split(' ', )[1])

	def DirPicker_CompilationCommandOnDirChanged( self, event ):
		# TODO: Implement DirPicker_CompilationCommandOnDirChanged
		if self.added_text_list != []:
			for text in self.added_text_list:
				text.Destroy()
			self.added_text_list.clear()
		if self.added_filepicker_list != []:
			for filepicker in self.added_filepicker_list:
				filepicker.Destroy()
			self.added_filepicker_list.clear()
		if self.added_bsizer_list != []:
			for bSizer in self.added_bsizer_list:
				self.bSizer_ObjectFileChoose.Remove(bSizer)
			self.added_bsizer_list.clear()
		
		if self.compilationdir_choosed == False:
			bSizer_AddObjectFile = wx.BoxSizer( wx.HORIZONTAL )
			self.Text_AddObjectFile = wx.StaticText( self, wx.ID_ANY, u"Add more object files", wx.DefaultPosition, wx.DefaultSize, 0 )
			self.Text_AddObjectFile.Wrap( -1 )
			bSizer_AddObjectFile.Add( self.Text_AddObjectFile, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			self.Button_Add = wx.Button( self, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
			bSizer_AddObjectFile.Add( self.Button_Add, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
			self.bSizer_ObjectFileChoose.Insert( self.bSizer_ObjectFileChoose.GetItemCount() - 1, bSizer_AddObjectFile, 1, wx.EXPAND, 5 )
			self.Button_Add.Bind( wx.EVT_BUTTON, self.Button_AddOnButtonClick )
		
		bSizer = wx.BoxSizer(wx.HORIZONTAL)
		text = wx.StaticText(self, wx.ID_ANY, u"Object file including main()", wx.DefaultPosition, wx.DefaultSize, 0)
		text.Wrap(-1)
		bSizer.Add(text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		filepicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		filepicker.SetInitialDirectory(self.DirPicker_CompilationCommand.GetPath())
		bSizer.Add(filepicker, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		self.bSizer_ObjectFileChoose.Insert(self.bSizer_ObjectFileChoose.GetItemCount() - 2, bSizer, 1, wx.EXPAND, 5)
		filepicker.Bind(wx.EVT_FILEPICKER_CHANGED, self.FilePicker_ObjectFilewithmainOnFileChanged)
		
		self.added_bsizer_list.append(bSizer)
		self.added_text_list.append(text)
		self.added_filepicker_list.append(filepicker)
			
		self.Layout()
		self.bSizer_ObjectFileChoose.Fit( self )
		
		self.compilationdir_choosed = True
		self.otherobjectfilepicker_count = 0
		self.bSizer_OKorCanncelOK.Disable()

	def FilePicker_ObjectFilewithmainOnFileChanged( self, event ):
		# TODO: Implement FilePicker_ObjectFilewithmainOnFileChanged
		self.bSizer_OKorCanncelOK.Enable()

	def Button_AddOnButtonClick( self, event ):
		# TODO: Implement Button_AddOnButtonClick
		if self.otherobjectfilepicker_count == 0:
			self.Add_Objectfilepicker()
		elif self.added_filepicker_list[self.otherobjectfilepicker_count].GetPath() != "":
			self.caution.SetLabel("")
			self.Add_Objectfilepicker()
		else:
			self.caution.SetLabel("Please select a file. ")
			self.Layout()
			self.bSizer_ObjectFileChoose.Fit(self)

	def Add_Objectfilepicker(self):
		self.otherobjectfilepicker_count += 1
		bSizer = wx.BoxSizer(wx.HORIZONTAL)
		text = wx.StaticText(self, wx.ID_ANY, u"Object file" + str(self.otherobjectfilepicker_count), wx.DefaultPosition, wx.DefaultSize, 0)
		text.Wrap(-1)
		bSizer.Add(text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		filepicker = wx.FilePickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE)
		filepicker.SetInitialDirectory(self.DirPicker_CompilationCommand.GetPath())
		bSizer.Add(filepicker, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		self.caution = wx.StaticText(self, wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
		self.caution.Wrap(-1)
		bSizer.Add(self.caution, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
		self.bSizer_ObjectFileChoose.Insert(self.bSizer_ObjectFileChoose.GetItemCount() - 2, bSizer, 1, wx.EXPAND, 5)
		self.Layout()
		self.bSizer_ObjectFileChoose.Fit(self)

		self.added_bsizer_list.append(bSizer)
		self.added_text_list.append(text)
		self.added_text_list.append(self.caution)
		self.added_filepicker_list.append(filepicker)

	def bSizer_OKorCanncelOnCancelButtonClick( self, event ):
		# TODO: Implement bSizer_OKorCanncelOnCancelButtonClick
		self.EndModal(False)

	def bSizer_OKorCanncelOnOKButtonClick( self, event ):
		# TODO: Implement bSizer_OKorCanncelOnOKButtonClick
		self.compilationdir = self.DirPicker_CompilationCommand.GetPath()
		self.objectfile_list = [filepicker.GetPath() for filepicker in self.added_filepicker_list if filepicker.GetPath() != ""]
		self.EndModal(True)
