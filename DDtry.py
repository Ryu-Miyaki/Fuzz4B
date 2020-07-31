from MyDD import MyDeltaDebuggingReducer, MyGrammarReducer
import os
import subprocess

class TryDeltaDebugging:
    def __init__(self,program,input,timeout=None):
        self.program=program
        inputfile=open(input,mode="rb")
        self.input=inputfile.read()
        inputfile.close()
        self.timeout=timeout

    def DeltaDebug(self):
        dd_reducer=MyDeltaDebuggingReducer(runner=self.program,log_test=False,timeout=self.timeout)
        self.output=dd_reducer.reduce(self.input)

    def GrammarReduce(self,grammar):
        grammar_reducer=MyGrammarReducer(runner=self.program,grammar=grammar,log_test=False,log_reduce=False,timeout=self.timeout)
        self.output=grammar_reducer.reduce(self.input.decode("utf-8","ignore"))

    def Out(self,dir='./',filename='reduced_input'):
        if dir[-1]!='/':
            dir=dir+'/'
        if os.path.exists(dir)==False:
            subprocess.call(["mkdir",dir])
        if type(self.output) is bytes:
            outputfile=open(dir+filename,"wb")
            outputfile.write(self.output)
        elif type(self.output) is str:
            outputfile=open(dir+filename,"w")
            outputfile.write(self.output)
        outputfile.close()