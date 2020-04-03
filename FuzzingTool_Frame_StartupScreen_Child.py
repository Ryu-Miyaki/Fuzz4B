"""Subclass of Frame_StartupScreen, which is generated by wxFormBuilder."""

import wx
import FuzzingTool
import subprocess
import os
import sys
import re
from FuzzingTool_Frame_StartupScreen import FuzzingTool_Frame_StartupScreen
from FuzzingTool_Dialog_AskCompileforAFL_Child import FuzzingTool_Dialog_AskCompileforAFL_Child
from FuzzingTool_Dialog_CompileforAFLCommand_Child import FuzzingTool_Dialog_CompileforAFLCommand_Child
from FuzzingTool_Dialog_ProgramChoose_Child import FuzzingTool_Dialog_ProgramChoose_Child
from FuzzingTool_Dialog_InputChoose_Child import FuzzingTool_Dialog_InputChoose_Child
from FuzzingTool_Dialog_AskStartFuzzing_Child import FuzzingTool_Dialog_AskStartFuzzing_Child
from FuzzingTool_Dialog_AskStopFuzzing_Child import FuzzingTool_Dialog_AskStopFuzzing_Child
from FuzzingTool_Dialog_ErrorLog_Child import FuzzingTool_Dialog_ErrorLog_Child
from FuzzingTool_Dialog_MinimizeFuzz_Child import FuzzingTool_Dialog_MinimizeFuzz_Child
from FuzzingTool_Dialog_FuzzAlreadyMinimized_Child import FuzzingTool_Dialog_FuzzAlreadyMinimized_Child
from FuzzingTool_Dialog_InputTestcaseandRun_Child import FuzzingTool_Dialog_InputTestcaseandRun_Child

from enum import Enum
class State(Enum):
	Initial=0
	StopFuzzing=1
	FuzzingNow=2

class TextForm(Enum):
	String=0
	Bytes=1

class PathForm(Enum):
	Absolute=0
	Relative=1

CRASH_TESTCASE=0
ORIGINAL_TESTCASE=1
MINIMIZED_TESTCASE=2

import pyinotify
class EventHandler(pyinotify.ProcessEvent):
	def my_init(self,grid):
		self.grid=grid
		self.rows=0
		self.pathform=PathForm.Absolute

	def process_IN_CREATE(self, event):
		if event.pathname.find('README')!=-1:
			pass
		else:
			if self.rows!=0:
				self.grid.AppendRows(1)
			
			if self.pathform==PathForm.Absolute:
				wx.CallAfter(self.grid.SetCellValue,self.rows,CRASH_TESTCASE,event.pathname)
			elif self.pathform==PathForm.Relative:
				wx.CallAfter(self.grid.SetCellValue,self.rows,CRASH_TESTCASE,event.pathname.replace(os.getcwd(),"."))

			id=re.search("src:"+r'\d\d\d\d\d\d',os.path.basename(event.pathname))
			id=id.group()
			originaltestcase=subprocess.check_output(['find','./out/queue','-type','d','-name','.state','-prune','-o','-type','f','-name',id.replace("src","id")+'*','-print'])
			originaltestcase=originaltestcase.decode()
			originaltestcase=originaltestcase.rstrip("\n")
			originaltestcase=os.getcwd()+originaltestcase.lstrip(".")

			if self.pathform==PathForm.Absolute:
				wx.CallAfter(self.grid.SetCellValue,self.rows,ORIGINAL_TESTCASE,originaltestcase)
			elif self.pathform==PathForm.Relative:
				wx.CallAfter(self.grid.SetCellValue,self.rows,ORIGINAL_TESTCASE,originaltestcase.replace(os.getcwd(),"."))


			gdbfile=open("./gdb_config_files/crash/gdb_"+os.path.basename(event.pathname),'w')
			gdbfile.write("start < \'"+event.pathname+"\'")
			gdbfile.close()
			gdbfile=open("./gdb_config_files/original/gdb_"+os.path.basename(originaltestcase),'w')
			gdbfile.write("start < \'"+originaltestcase+"\'")
			gdbfile.close()
		
			wx.CallAfter(self.grid.AutoSize)
			self.rows=self.rows+1
		
# Implementing Frame_StartupScreen
class FuzzingTool_Frame_StartupScreen_Child( FuzzingTool_Frame_StartupScreen ):
	def __init__( self, parent ):
		FuzzingTool_Frame_StartupScreen.__init__( self, parent )
		self.state=State.Initial
		self.textform=TextForm.String
		self.pathform=PathForm.Absolute
		self.program=""
		self.input_path=""
		self.choised_row=-1

		self.Grid_Testcases.AutoSize()

		self.handler=EventHandler(grid=self.Grid_Testcases)

	
	def Frame_StartupScreenOnClose( self, event ):
		if self.state==State.FuzzingNow:
			self.fuzzer.terminate()
			self.wm.rm_watch(list(self.wdd.values()))
			self.notifier.stop()
		self.Destroy()
	
	def ChangeState(self,state):
		self.state=state
		if self.state==State.StopFuzzing:
			self.MenuItem_StartFuzzing.Enable(True)
			self.MenuItem_StopFuzzing.Enable(False)
			self.fuzzer.terminate()
			self.wm.rm_watch(list(self.wdd.values()))
			self.notifier.stop()

		elif self.state==State.FuzzingNow:
			self.MenuItem_StartFuzzing.Enable(False)
			self.MenuItem_StopFuzzing.Enable(True)

			if os.path.exists("./reduced_testcases"):
				subprocess.call(["rm","-r","./reduced_testcases"])
			
			if os.path.exists("./gdb_config_files"):
				subprocess.call(["rm","-r","./gdb_config_files"])
			
			subprocess.call(["mkdir","gdb_config_files"])
			subprocess.call(["mkdir","gdb_config_files/crash"])
			subprocess.call(["mkdir","gdb_config_files/original"])
			subprocess.call(["mkdir","gdb_config_files/minimized"])

			if self.handler.rows!=0:
				self.Grid_Testcases.ClearGrid()
				for i in range(1,self.handler.rows):
					self.Grid_Testcases.DeleteRows()
				self.handler.rows=0
				self.choised_row=-1
				self.Grid_Testcases.AutoSize()
			
			self.Text_ChoisedRow.SetLabel("Selected No. ")

			self.TextCtrl_CrashTestcase.Clear()
			self.TextCtrl_OriginalTestcase.Clear()
			self.TextCtrl_MinimizedTestcase.Clear()

			self.EnableDebugMenu(False)
			
			subprocess.call(['resize','-s','25','80'],stdout=subprocess.DEVNULL)
			
			if os.path.exists("./out")==True:
				subprocess.call(['rm','-r','./out'])
			
			self.fuzzer=subprocess.Popen(["afl-fuzz","-i",self.input_path,"-o","./out",self.program],stdout=None)

			while(os.path.exists("./out/crashes")!=True):
				pass
			self.wm=pyinotify.WatchManager()
			self.notifier=pyinotify.ThreadedNotifier(self.wm,self.handler)
			self.notifier.start()
			self.wdd = self.wm.add_watch('./out/crashes', pyinotify.IN_CREATE)

	def MenuItem_StartFuzzingOnMenuSelection( self, event ):
		dialog=FuzzingTool_Dialog_AskCompileforAFL_Child(None)
		if dialog.ShowModal()==False:
			dialog.Destroy()
			dialog=FuzzingTool_Dialog_CompileforAFLCommand_Child(None)
			dialog.ShowModal()
			dialog.Destroy()
		else:
			dialog.Destroy()
			dialog=FuzzingTool_Dialog_ProgramChoose_Child(None)
			if dialog.ShowModal()==False:
				dialog.Destroy()
			else:
				self.program=dialog.program
				dialog.Destroy()
				dialog=FuzzingTool_Dialog_InputChoose_Child(None)
				if dialog.ShowModal()==False:
					dialog.Destroy()
				else:
					self.input_path=dialog.input_path
					dialog.Destroy()
					dialog=FuzzingTool_Dialog_AskStartFuzzing_Child(parent=None,program=self.program,input_path=self.input_path)
					if dialog.ShowModal()==False:
						if dialog.errorcode=="":
							dialog.Destroy()
						else:
							errorcode=dialog.errorcode
							dialog.Destroy()
							dialog=FuzzingTool_Dialog_ErrorLog_Child(None,errorcode=errorcode.strip('[-] PROGRAM ABORT: '))
							if dialog.ShowModal()==True:
								dialog.Destroy()
					else:
						dialog.Destroy()
						self.ChangeState(State.FuzzingNow)

	def MenuItem_StopFuzzingOnMenuSelection( self, event ):
		dialog=FuzzingTool_Dialog_AskStopFuzzing_Child(None)
		if dialog.ShowModal()==False:
			dialog.Destroy()
		else:
			dialog.Destroy()
			self.ChangeState(State.StopFuzzing)

	def MenuItem_TextFormStringOnMenuSelection( self, event ):
		self.textform=TextForm.String
		self.MenuItem_TextFormString.Check(True)
		self.MenuItem_TextFormBytes.Check(False)
		if self.choised_row!=-1:
			self.TextCtrl_CrashTestcase.Clear()
			self.TextCtrl_OriginalTestcase.Clear()
			self.TextCtrl_MinimizedTestcase.Clear()

			self.WriteFuzz(CRASH_TESTCASE)
			self.WriteFuzz(ORIGINAL_TESTCASE)
			self.WriteFuzz(MINIMIZED_TESTCASE)
	
	def MenuItem_TextFormBytesOnMenuSelection( self, event ):
		self.textform=TextForm.Bytes
		self.MenuItem_TextFormString.Check(False)
		self.MenuItem_TextFormBytes.Check(True)
		if self.choised_row!=-1:
			self.TextCtrl_CrashTestcase.Clear()
			self.TextCtrl_OriginalTestcase.Clear()
			self.TextCtrl_MinimizedTestcase.Clear()

			self.WriteFuzz(CRASH_TESTCASE)
			self.WriteFuzz(ORIGINAL_TESTCASE)
			self.WriteFuzz(MINIMIZED_TESTCASE)

	def MenuItem_PathFormRelativeOnMenuSelection( self, event ):
		if self.pathform==PathForm.Absolute:
			self.pathform=PathForm.Relative
			self.handler.pathform=PathForm.Relative
			self.MenuItem_PathFormRelative.Check(True)
		elif self.pathform==PathForm.Relative:
			self.pathform=PathForm.Absolute
			self.handler.pathform=PathForm.Absolute
			self.MenuItem_PathFormRelative.Check(False)
		if self.state!=State.Initial:
			for i in range(self.Grid_Testcases.GetNumberRows()):
				crashtestcase=self.Grid_Testcases.GetCellValue(i,CRASH_TESTCASE)
				crashtestcase=self.ChangePath(crashtestcase)
				self.Grid_Testcases.SetCellValue(i,CRASH_TESTCASE,crashtestcase)
				originaltestcase=self.Grid_Testcases.GetCellValue(i,ORIGINAL_TESTCASE)
				originaltestcase=self.ChangePath(originaltestcase)
				self.Grid_Testcases.SetCellValue(i,ORIGINAL_TESTCASE,originaltestcase)
				minimizedtestcase=self.Grid_Testcases.GetCellValue(i,MINIMIZED_TESTCASE)
				minimizedtestcase=self.ChangePath(minimizedtestcase)
				self.Grid_Testcases.SetCellValue(i,MINIMIZED_TESTCASE,minimizedtestcase)
			self.Grid_Testcases.AutoSize()

	def ChangePath(self,fuzz):
		if fuzz=="":
			return ""
		else:
			if self.pathform==PathForm.Absolute:
				fuzz=os.getcwd()+fuzz.lstrip(".")
				return fuzz
			elif self.pathform==PathForm.Relative:
				fuzz=fuzz.replace(os.getcwd(),".")
				return fuzz
			else:
				return ""
	
	def MenuItem_MinimizeFuzzOnMenuSelection( self, event ):
		if self.Grid_Testcases.GetCellValue(self.choised_row,MINIMIZED_TESTCASE)!="":
			dialog=FuzzingTool_Dialog_FuzzAlreadyMinimized_Child(None)
			dialog.ShowModal()
			dialog.Destroy()

		else:
			dialog=FuzzingTool_Dialog_MinimizeFuzz_Child(None,program=self.program,fuzz=self.Grid_Testcases.GetCellValue(self.choised_row,CRASH_TESTCASE))
			if dialog.ShowModal()==False:
				dialog.Destroy()
			else:
				minimizedfuzz=dialog.minimizedfuzz
				dialog.Destroy()
				if self.pathform==PathForm.Absolute:
					self.Grid_Testcases.SetCellValue(self.choised_row,MINIMIZED_TESTCASE,minimizedfuzz)
				elif self.pathform==PathForm.Relative:
					self.Grid_Testcases.SetCellValue(self.choised_row,MINIMIZED_TESTCASE,minimizedfuzz.replace(os.getcwd(),"."))
				self.Grid_Testcases.AutoSize()

				self.WriteFuzz(fuzztype=MINIMIZED_TESTCASE)

				gdbfile=open("./gdb_config_files/minimized/gdb_"+os.path.basename(minimizedfuzz),'w')
				gdbfile.write("start < \'"+minimizedfuzz+"\'")
				gdbfile.close()

	def MenuItem_InputTestcaseandRunOnMenuSelection( self, event ):
		# TODO: Implement MenuItem_InputTestcaseandRunOnMenuSelection
		crashtestcase=self.Grid_Testcases.GetCellValue(self.choised_row,CRASH_TESTCASE)
		originaltestcase=self.Grid_Testcases.GetCellValue(self.choised_row,ORIGINAL_TESTCASE)
		minimizedtestcase=self.Grid_Testcases.GetCellValue(self.choised_row,MINIMIZED_TESTCASE)
		dialog=FuzzingTool_Dialog_InputTestcaseandRun_Child(None,program=self.program,crashtestcase=crashtestcase,originaltestcase=originaltestcase,minimizedtestcase=minimizedtestcase)
		dialog.ShowModal()
		dialog.Destroy()

	def Grid_TestcasesOnGridLabelLeftClick( self, event ):
		if self.state==State.Initial:
			pass
		else:
			self.Text_ChoisedRow.SetLabel("Selected No. ")

			self.choised_row=event.GetRow()

			if self.choised_row==-1:
				self.TextCtrl_CrashTestcase.Clear()
				self.TextCtrl_OriginalTestcase.Clear()
				self.TextCtrl_MinimizedTestcase.Clear()

				self.EnableDebugMenu(False)
				
			elif self.Grid_Testcases.GetCellValue(self.choised_row,CRASH_TESTCASE)=="":
				self.EnableDebugMenu(False)
				
			else:
				self.Text_ChoisedRow.SetLabel("Selected No. "+str(self.choised_row+1))

				self.EnableDebugMenu(True)
				
				self.TextCtrl_CrashTestcase.Clear()
				self.TextCtrl_OriginalTestcase.Clear()
				self.TextCtrl_MinimizedTestcase.Clear()

				self.WriteFuzz(CRASH_TESTCASE)
				self.WriteFuzz(ORIGINAL_TESTCASE)
				self.WriteFuzz(MINIMIZED_TESTCASE)

	def WriteFuzz(self,fuzztype):
		if self.Grid_Testcases.GetCellValue(self.choised_row,fuzztype)=="":
			pass
		else:
			with open(file=self.Grid_Testcases.GetCellValue(self.choised_row,fuzztype),mode="rb") as crashtestcase:
						text=crashtestcase.read()
						if self.textform==TextForm.String:
							if fuzztype==CRASH_TESTCASE:
								self.TextCtrl_CrashTestcase.WriteText(text.decode(errors='replace'))
							elif fuzztype==ORIGINAL_TESTCASE:
								self.TextCtrl_OriginalTestcase.WriteText(text.decode(errors='replace'))
							elif fuzztype==MINIMIZED_TESTCASE:
								self.TextCtrl_MinimizedTestcase.WriteText(text.decode(errors='replace'))
						else:
							with open("tmp.txt",mode="w") as tmp:
								print(text,file=tmp)
							with open("tmp.txt",mode="r") as tmp:
								text=tmp.read()
								if fuzztype==CRASH_TESTCASE:
									self.TextCtrl_CrashTestcase.WriteText(text[2:-2])
								elif fuzztype==ORIGINAL_TESTCASE:
									self.TextCtrl_OriginalTestcase.WriteText(text[2:-2])
								elif fuzztype==MINIMIZED_TESTCASE:
									self.TextCtrl_MinimizedTestcase.WriteText(text[2:-2])
							os.remove("tmp.txt")
	
	def EnableDebugMenu(self,enable):
		self.MenuItem_MinimizeFuzz.Enable(enable)
		self.MenuItem_InputTestcaseandRun.Enable(enable)
		
