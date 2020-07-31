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

from fuzzingbook.Parser import EarleyParser
from fuzzingbook.GrammarFuzzer import expansion_to_children,all_terminals

class MyGrammarReducer(object):
    def __init__(self,runner,grammar,log_test=False,log_reduce=False,timeout=None):
        self.runner=runner
        self.parser=EarleyParser(grammar)
        self.grammar=self.parser.grammar()
        self.start_symbol=self.parser.start_symbol()
        self.log_test=log_test
        self.log_reduce=log_reduce
        self.try_all_combinations=False
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
    
    def subtrees_with_symbol(self,tree,symbol,depth=-1,ignore_root=True):
        result=[]
        (child_symbol,children)=tree
        if depth<=0 and not ignore_root and child_symbol==symbol:
            result.append(tree)
        if depth!=0 and children is not None:
            for c in children:
                result+=self.subtrees_with_symbol(c,symbol,depth=depth-1,ignore_root=False)
        return result
    
    def possible_combinations(self,list_of_lists):
        if len(list_of_lists)==0:
            return []
        result=[]
        for e in list_of_lists[0]:
            if len(list_of_lists)==1:
                result.append([e])
            else:
                for c in self.possible_combinations(list_of_lists[1:]):
                    new_combination=[e]+c
                    result.append(new_combination)
        return result
    
    def number_of_nodes(self,tree):
        (symbol,children)=tree
        return 1+sum([self.number_of_nodes(c) for c in children])

    def alternate_reductions(self,tree,symbol,depth=-1):
        reductions=[]
        expansions=self.grammar.get(symbol,[])
        expansions.sort(key=lambda expansion: len(expansion_to_children(expansion)))
        for expansion in expansions:
            expansion_children=expansion_to_children(expansion)
            match=True
            new_children_reductions=[]
            for(alt_symbol, _) in expansion_children:
                child_reductions=self.subtrees_with_symbol(tree,alt_symbol,depth=depth)
                if len(child_reductions)==0:
                    match=False
                    break
                new_children_reductions.append(child_reductions)

            if not match:
                continue
            
            for new_children in self.possible_combinations(new_children_reductions):
                new_tree=(symbol,new_children)
                if self.number_of_nodes(new_tree) < self.number_of_nodes(tree):
                    reductions.append(new_tree)
                    if not self.try_all_combinations:
                        break
        
        reductions.sort(key=self.number_of_nodes)
        return reductions

    def symbol_reductions(self,tree,symbol,depth=-1):
        reductions=(self.subtrees_with_symbol(tree,symbol,depth=depth)+self.alternate_reductions(tree,symbol,depth=depth))
        unique_reductions=[]
        for r in reductions:
            if r not in unique_reductions:
                unique_reductions.append(r)
        return unique_reductions
    
    def reduce_subtree(self,tree,subtree,depth=-1):
        if os.path.exists("./tmp"):
            subprocess.call(["rm","-r","tmp"])
        subprocess.call(["mkdir","tmp"])
        self.devnull=open(os.devnull,'w')

        symbol,children=subtree
        if len(children)==0:
            return False

        if self.log_reduce==True:
            print("Reducing",all_terminals(subtree),"with depth",depth)
        
        reduced=False
        while True:
            reduced_child=False
            for i,child in enumerate(children):
                (child_symbol, _) = child
                for reduction in self.symbol_reductions(child,child_symbol,depth):
                    if self.number_of_nodes(reduction) >= self.number_of_nodes(child):
                        continue

                    if self.log_reduce==True:
                        print("Replacing",all_terminals(children[i]),"by",all_terminals(reduction))
                    children[i]=reduction

                    if self.log_test==True:
                        print("Test"+str(self.tests)+" "+all_terminals(tree))
                    
                    output=open("./tmp/output"+str(self.tests),"wb")
                    output.write(all_terminals(tree).encode())
                    output.close()

                    if self.execution(all_terminals(tree))==False:
                        if self.log_reduce==True:
                            print("New tree:",all_terminals(tree))
                        reduced = reduced_child = True
                        break
                    else:
                        children[i]=child
                    
            if not reduced_child:
                if self.log_reduce==True:
                    print("Tried all alternatives for", all_terminals(subtree))
                break

        for c in children:
            if self.reduce_subtree(tree,c,depth):
                reduced=True
        
        return reduced

    def reduce_tree(self,tree):
        return self.reduce_subtree(tree,tree)
    
    def parse(self,inp):
        tree, *_=self.parser.parse(inp)
        if self.log_reduce==True:
            print(all_terminals(tree))
        return tree
    
    def reduce(self,inp):
        tree=self.parse(inp)
        self.reduce_tree(tree)
        return all_terminals(tree)
