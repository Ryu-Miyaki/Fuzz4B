"""Subclass of Dialog_InputTestcaseandRun, which is generated by wxFormBuilder."""

import wx
import FuzzingTool
from FuzzingTool_Dialog_InputTestcaseandRun import FuzzingTool_Dialog_InputTestcaseandRun
import os
import subprocess
import pyperclip

# Implementing Dialog_InputTestcaseandRun
class FuzzingTool_Dialog_InputTestcaseandRun_Child( FuzzingTool_Dialog_InputTestcaseandRun ):
	def __init__( self, parent, program, crashtestcase, originaltestcase, minimizedtestcase):
		FuzzingTool.Dialog_InputTestcaseandRun.__init__( self, parent )
		self.program=program
		self.crashtestcase=crashtestcase
		self.originaltestcase=originaltestcase
		self.minimizedtestcase=minimizedtestcase
		if self.minimizedtestcase=="":
			self.RadioBtn_MinimizedTestcase.Enable(False)

		self.UseGDB=False
		self.inputtestcase=self.crashtestcase
		self.WriteCommand()

	# Handlers for Dialog_InputTestcaseandRun events.
	def Button_CopyOnButtonClick( self, event ):
		# TODO: Implement Button_CopyOnButtonClick
		pyperclip.copy(self.TextCtrl_CommandforInputTestcaseandRun.GetValue())

	def CheckBox_UseGDBorNotOnCheckBox( self, event ):
		# TODO: Implement CheckBox_UseGDBorNotOnCheckBox
		self.UseGDB=not self.UseGDB
		self.WriteCommand()

	def RadioBtn_CrashTestcaseOnRadioButton( self, event ):
		# TODO: Implement RadioBtn_CrashTestcaseOnRadioButton
		self.inputtestcase=self.crashtestcase
		self.WriteCommand()

	def RadioBtn_OriginalTestcaseOnRadioButton( self, event ):
		# TODO: Implement RadioBtn_OriginalTestcaseOnRadioButton
		self.inputtestcase=self.originaltestcase
		self.WriteCommand()

	def RadioBtn_MinimizedTestcaseOnRadioButton( self, event ):
		# TODO: Implement RadioBtn_MinimizedTestcaseOnRadioButton
		self.inputtestcase=self.minimizedtestcase
		self.WriteCommand()

	def Button_RunGDBOnButtonClick( self, event ):
		# TODO: Implement Button_RunGDBOnButtonClick
		if self.inputtestcase==self.crashtestcase:
			subprocess.call(["gnome-terminal","--","gdb",self.program,"-x","./gdb_config_files/crash/gdb_"+os.path.basename(self.crashtestcase)])
		elif self.inputtestcase==self.originaltestcase:
			subprocess.call(["gnome-terminal","--","gdb",self.program,"-x","./gdb_config_files/original/gdb_"+os.path.basename(self.originaltestcase)])
		elif self.inputtestcase==self.minimizedtestcase:
			subprocess.call(["gnome-terminal","--","gdb",self.program,"-x","./gdb_config_files/minimized/gdb_"+os.path.basename(self.minimizedtestcase)])

	def Button_ExitOnButtonClick( self, event ):
		# TODO: Implement Button_ExitOnButtonClick
		self.EndModal(True)

	def WriteCommand(self):
		self.TextCtrl_CommandforInputTestcaseandRun.Clear()
		if self.UseGDB==True:
			if self.inputtestcase==self.crashtestcase:
				self.TextCtrl_CommandforInputTestcaseandRun.WriteText("gdb "+self.program+" -x "+os.getcwd()+"/gdb_config_files/crash/gdb_"+os.path.basename(self.crashtestcase))
			elif self.inputtestcase==self.originaltestcase:
				self.TextCtrl_CommandforInputTestcaseandRun.WriteText("gdb "+self.program+" -x "+os.getcwd()+"/gdb_config_files/original/gdb_"+os.path.basename(self.originaltestcase))
			elif self.inputtestcase==self.minimizedtestcase:
				self.TextCtrl_CommandforInputTestcaseandRun.WriteText("gdb "+self.program+" -x "+os.getcwd()+"/gdb_config_files/minimized/gdb_"+os.path.basename(self.minimizedtestcase))
		else:
			self.TextCtrl_CommandforInputTestcaseandRun.WriteText(self.program+" < "+self.inputtestcase)
