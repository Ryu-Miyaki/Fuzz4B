import subprocess
import os
class MyDeltaDebuggingReducer(object):
    def __init__(self,runner,log_test=False,timeout=None):
        self.runner=runner
        self.log_test=log_test
        self.timeout=timeout
        self.reset()
    
    def reset(self):
        self.tests=0
        self.cache={}

    def execution(self,inp):
        if inp in self.cache:
            if self.log_test==True:
                print("cache :)")
            return self.cache[inp]
        try:
            input=open("./tmp/output"+str(self.tests),"r")
            subprocess.run([self.runner],stdin=input,stdout=self.devnull,stderr=self.devnull,timeout=self.timeout,check=True)
        except subprocess.TimeoutExpired:
            if self.log_test==True:
                print("timeout...")
            flag=True
        except subprocess.CalledProcessError:
            if self.log_test==True:
                print("crash!!")
            flag=False
        else:
            flag=True
        finally:
            self.cache[inp]=flag
            self.tests+=1
            input.close()
        return flag

    def reduce(self,inp):
        n=2
        if os.path.exists("./tmp"):
            subprocess.call(["rm","-r","tmp"])
        subprocess.call(["mkdir","tmp"])
        self.devnull=open(os.devnull,'w')

        while(len(inp)) >= 2:
            start=0
            subset_length=len(inp)/n
            some_complement_is_failing=False

            while start < len(inp):
                complement=inp[:int(start)]+inp[int(start+subset_length):]
                
                if self.log_test==True:
                    print("Test"+str(self.tests)+" start="+str(start)+" n="+str(n)+" subset_length="+str(subset_length)+"\n"+str(complement))
                
                output=open("./tmp/output"+str(self.tests),"wb")
                output.write(complement)
                output.close()

                if self.execution(complement)==False:
                    inp=complement
                    n=max(n-1,2)
                    some_complement_is_failing=True
                    break
                
                start+=subset_length
        
            if not some_complement_is_failing:
                if n == len(inp):
                    break
                n=min(n*2,len(inp))

        subprocess.call(["rm","-r","./tmp"])
        return inp