"""Subclass of Dialog_CompilationError, which is generated by wxFormBuilder."""

import wx
import FuzzingTool
from FuzzingTool_Dialog_CompilationError import FuzzingTool_Dialog_CompilationError

# Implementing Dialog_CompilationError
class FuzzingTool_Dialog_CompilationError_Child( FuzzingTool_Dialog_CompilationError ):
	def __init__( self, parent ):
		FuzzingTool.Dialog_CompilationError.__init__( self, parent )

	# Handlers for Dialog_CompilationError events.
	def Button_OKOnButtonClick( self, event ):
		# TODO: Implement Button_OKOnButtonClick
		self.EndModal(True)


