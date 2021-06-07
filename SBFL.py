import glob
import os
import subprocess
import re
import pathlib

class SBFL:
    def __init__(self, program, success_testcase_dir, fault_testcase_dir, compilation_dir="", objectfiles_dir=[], targetfiles=[]):
        if success_testcase_dir[-1] != '/':
            success_testcase_dir = success_testcase_dir + '/'
        if fault_testcase_dir[-1] != '/':
            fault_testcase_dir = fault_testcase_dir + '/'
        if compilation_dir != "" and compilation_dir[-1] != '/':
            compilation_dir = compilation_dir + '/'
        if objectfiles_dir != []:
            objectfiles_dir = [dir + '/' if dir[-1] != '/' else dir for dir in objectfiles_dir]
        
        if targetfiles != []:
            self.targetfiles = [pathlib.Path(target) for target in targetfiles]

        self.program = program
        self.compilation_dir = compilation_dir
        self.objectfiles_dir = objectfiles_dir

        self.success_testcase = glob.glob(success_testcase_dir+"*")
        self.fault_testcase = glob.glob(fault_testcase_dir+"*")
        
        if fault_testcase_dir+"README.txt" in self.fault_testcase:
            self.fault_testcase.remove(fault_testcase_dir+"README.txt")
            
    def ExecSBFL(self):
        self.result = []
        success_testcase_gcovinfo = []
        fault_testcase_gcovinfo = []
        totalPass = len(self.success_testcase)
        totalFail = len(self.fault_testcase)

        if self.compilation_dir == "":
            os.chdir(os.path.dirname(self.program))
        else:
            os.chdir(self.compilation_dir)

        if self.objectfiles_dir == []:
            self.objectfiles_dir.append(os.path.dirname(self.program) + '/')
        
        self.targetfiles = [str(target.relative_to(self.compilation_dir)) for target in self.targetfiles]

        for testcase in self.success_testcase:
            for dir in self.objectfiles_dir:
                files = glob.glob(dir + "*.gcda")
                for file in files:
                    subprocess.call(["rm", file])
        
            files = glob.glob("./*.gcov")
            for file in files:
                subprocess.call(["rm", file])
        
            self.ExecOneTestcase(testcase)

            self.ExecGcov()

            gcovinfo = self.AnalyzeAllGcovFile()

            if success_testcase_gcovinfo == []:
                success_testcase_gcovinfo = [{"Sourcefile":info["Sourcefile"], "Count":1 if info["Count"] != 0 else 0, "Number":info["Number"], "Statement":info["Statement"]} for info in gcovinfo]
            else:
                for (info_success, info) in zip(success_testcase_gcovinfo, gcovinfo):
                    assert info_success["Sourcefile"] == info["Sourcefile"], "GcovAnalysisError:info_success_filename = {0} info_filename = {1}".format(info_success["Sourcefile"], info["Sourcefile"])
                    assert info_success["Number"] == info["Number"], "GcovAnalysisError:info_success_Number = {0} info_Number = {1}".format(info_success["Number"], info["Number"])
                    assert info_success["Statement"] == info["Statement"], "GcovAnalysisError:info_success_Statement = {0} info_Statement = {1}".format(info_success["Statement"], info["Statement"])
                    if info["Count"] != 0:
                        info_success["Count"] += 1
        
        for info_success in success_testcase_gcovinfo:
            assert info_success["Count"] <= totalPass, "GcovAnalysisError:info_success_Count = {0} > totalPass = {1}".format(info_success["Count"], totalPass)
        
        for testcase in self.fault_testcase:
            for dir in self.objectfiles_dir:
                files = glob.glob(dir + "*.gcda")
                for file in files:
                    subprocess.call(["rm", file])
        
            files = glob.glob("./*.gcov")
            for file in files:
                subprocess.call(["rm", file])
        
            self.ExecOneTestcase(testcase)

            self.ExecGcov()

            gcovinfo = self.AnalyzeAllGcovFile()

            if fault_testcase_gcovinfo == []:
                fault_testcase_gcovinfo = [{"Sourcefile":info["Sourcefile"], "Count":1 if info["Count"] != 0 else 0, "Number":info["Number"], "Statement":info["Statement"]} for info in gcovinfo]
            else:
                for (info_fault, info) in zip(fault_testcase_gcovinfo, gcovinfo):
                    assert info_fault["Sourcefile"] == info["Sourcefile"], "GcovAnalysisError:info_fault_filename = {0} info_filename = {1}".format(info_fault["Sourcefile"], info["Sourcefile"])
                    assert info_fault["Number"] == info["Number"], "GcovAnalysisError:info_fault_Number = {0} info_Number = {1}".format(info_fault["Number"], info["Number"])
                    assert info_fault["Statement"] == info["Statement"], "GcovAnalysisError:info_fault_Statement = {0} info_Statement = {1}".format(info_fault["Statement"], info["Statement"])
                    if info["Count"] != 0:
                        info_fault["Count"] += 1
        
        for info_fault in fault_testcase_gcovinfo:
            assert info_fault["Count"] <= totalFail, "GcovAnalysisError:info_fault_Count = {0} > totalFail = {1}".format(info_fault["Count"], totalFail)

        for (info_success, info_fault) in zip(success_testcase_gcovinfo, fault_testcase_gcovinfo):
            assert info_success["Sourcefile"] == info_fault["Sourcefile"], "GcovAnalysisError:info_success_filename = {0} info_fault_filename = {1}".format(info_success["Sourcefile"], info_fault["Sourcefile"])
            assert info_success["Number"] == info_fault["Number"], "GcovAnalysisError:info_success_Number = {0} info_fault_Number = {1}".format(info_success["Number"], info_fault["Number"])
            assert info_success["Statement"] == info_fault["Statement"], "GcovAnalysisError:info_success_Statement = {0} info_fault_Statement = {1}".format(info_success["Statement"], info_fault["Statement"])
            suspicious = self.Ochiai(info_fault["Count"], info_success["Count"], totalFail)
            assert suspicious <= 1.0, "OchiaiError:suspicious = {0} Statement = {1}".format(suspicious, info_success["Statement"])
            assert suspicious >= 0.0, "OchiaiError:suspicious = {0} Statement = {1}".format(suspicious, info_success["Statement"])
            self.result.append({"Sourcefile":info_success["Sourcefile"], "Number":info_success["Number"], "Statement":info_success["Statement"], "Suspicious":suspicious})
            
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        return self.result
    
    def ExecAllTestcase(self, testcase):
        for file in testcase:
            self.ExecOneTestcase(file)
    
    def ExecOneTestcase(self, testcase):
        input=open(testcase, "r")
        subprocess.run([self.program], stdin=input, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    def ExecGcov(self):
        files = []
        for dir in self.objectfiles_dir:
            files = files + glob.glob(dir + "*.gcda")
        
        for file in files:
            subprocess.run(["gcov","-p","-l", file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    def AnalyzeAllGcovFile(self):
        gcovfiles = glob.glob("./*.gcov")
        targetfiles = []
        for target in self.targetfiles:
            for gcovfile in gcovfiles:
                if target + ".gcov" == re.sub(".*[.]gcda##", "", gcovfile, 1).replace('#', '/'):
                    targetfiles.append(gcovfile)
        
        result = []
        for file in targetfiles:
            list = self.AnalyzeOneGcovFile(file)
            sourcefile = [r.get("Sourcefile") for r in result]
            if list[0]["Sourcefile"] in sourcefile:
                for l in list:
                    for r in result:
                        if l["Sourcefile"] == r["Sourcefile"] and l["Number"] == r["Number"] and l["Statement"] == r["Statement"]:
                            r["Count"] = r["Count"] + l["Count"]
                            break
            else:
                result = result + list
        return result
    
    def AnalyzeOneGcovFile(self, file):
        filename = os.path.basename(file).replace(".gcov","")
        with open(file) as f:
            lines = f.readlines()

            lines = [re.split(':', line, maxsplit=2) for line in lines]
            
            lines = [{"Sourcefile":re.sub(".*[.]gcda##", "", filename, 1).replace('#', '/'), "Count":int(line[0].strip().replace('-', '0').replace('#####', '0')), "Number":int(line[1].strip()), "Statement":line[2]} for line in lines if line[1].strip() != "0"]
        return lines
    
    def Ochiai(self, fail_s, pass_s, totalFail):
        if fail_s == 0:
            return 0.0
        else:
            return fail_s / pow(totalFail * (fail_s + pass_s), 0.5)
    
    def PrintOutput(self, sourcefile, ignore_safe_statement=True):
        if ignore_safe_statement == True:
            for info in self.result:
                if info["Sourcefile"] == sourcefile and info["Suspicious"] != 0:
                    print(info)
        else:
            for info in self.result:
                if info["Sourcefile"] == sourcefile:
                    print(info)
