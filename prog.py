
# HOW TO RUN THE PROGRAM:  python3 prog.py test1.cpy             

from os import name
import sys
f = open(sys.argv[1], "r")

endiamesos = open("endiamesos.int", "w")
symbol = open("symbolTable.sym", "w")
lex_syn = open("lex&syntax.int", "w")


class Lex():


    def __init__(self):
        self.inputChar = f.read(1)
        self.desmeumenes =["if","elif", "else","while","print","return","main","def","#def","#int","input","int","and","or","not","global" ]
        self.stringLine =''
        self.line_number =1
    
        
    def lex(self):
        
        initial_str = "start"
        i = 0
        desmeumenes = ["if","elif", "else", "while","print","return","main"]
        logicArray = ["and", "or", "not"]
        categories = ["number", "identifier", "keyword", "addOp", "mulOp", "relOp", "parenthesis", 
                "logicalOp","punctuation","error","assigment"]
        recognized_string = ''
        

        while initial_str not in categories:
             # ----- LEUKOI CHARACTERS -----
            if initial_str == "start" and (self.inputChar.isspace() or self.inputChar == "'") :  
                self.inputChar = f.read(1)
                initial_str = "start"
            

            #   ------ LETTERS -------
            elif initial_str == "start" and ((self.inputChar.isalpha() == True)  or self.inputChar == '"'): 
                initial_str = "letter"
                recognized_string += self.inputChar
            if initial_str == "letter":
                self.inputChar = f.read(1)
                if ((self.inputChar.isalpha()) or (self.inputChar.isnumeric())  or self.inputChar == '"'):
                    initial_str = "letter"
                    recognized_string += self.inputChar
                else:
                    if recognized_string in desmeumenes:
                        initial_str = "keyword"

                    elif recognized_string in logicArray:
                        initial_str = "logicalOp"
                    else:
                        initial_str = "identifier"


            # ----- EOF -----
            if(self.inputChar == ''):  
                recognized_string = ''
                initial_str = "error"
            
            # ----- for lines ----
            if self.inputChar == '\n' :
                  self.line_number+=1
        
    
           

            #       ------ DIGIT -----
            elif initial_str == "start" and self.inputChar.isnumeric():
                initial_str = "digit"
                recognized_string += self.inputChar
            if initial_str == "digit":
                self.inputChar = f.read(1)
                if self.inputChar.isnumeric():
                    initial_str = "digit"
                    recognized_string += self.inputChar
                else:
                    initial_str = "number"

            #  ----- addOperator -----
            elif initial_str == "start" and (self.inputChar == "+" or self.inputChar == "-"):
                initial_str = "addOp"
                recognized_string += self.inputChar
                self.inputChar = f.read(1)


            # ----- mulOperator -----
            elif initial_str == "start" and (self.inputChar == "*" or self.inputChar == "%"):
                initial_str = "mulOp"
                recognized_string += self.inputChar
                self.inputChar = f.read(1)


            # ----- punctuation -----
            elif initial_str == "start" and (self.inputChar == ";" or self.inputChar == "," or self.inputChar == ":"):
                initial_str = "punctuation"
                recognized_string += self.inputChar
                self.inputChar = f.read(1)


            # ----- plagia -----
            elif initial_str == "start" and self.inputChar == "/":
                initial_str = "saw /"
                recognized_string += self.inputChar
                if initial_str == "saw /":
                    self.inputChar = f.read(1)
                    if self.inputChar == "/":
                        initial_str = "mulOp"
                        recognized_string += self.inputChar
                        self.inputChar = f.read(1)
                    else:
                        initial_str = "error"

            # ----- parenthesis -----
            elif initial_str == "start" and ( self.inputChar == "(" or self.inputChar == ")"):
                initial_str = "parenthesis"
                recognized_string += self.inputChar
                self.inputChar = f.read(1)            


            # ----- ! -----
            elif initial_str == "start" and self.inputChar == "!":
                initial_str = "exclamation_mark"
                recognized_string += self.inputChar
                if initial_str == "exclamation_mark":
                    self.inputChar = f.read(1)
                    if self.inputChar == "=":
                        initial_str = "relOp"
                        recognized_string += self.inputChar
                        self.inputChar = f.read(1)
                    else:
                        initial_str = "error"

                        
            # ----- = -----
            elif initial_str == "start" and self.inputChar == "=":
                initial_str = "equal"
                recognized_string += self.inputChar
                if initial_str == "equal":
                    self.inputChar = f.read(1)
                    if self.inputChar == "=":
                        initial_str = "relOp"
                        recognized_string += self.inputChar
                        self.inputChar = f.read(1)
                    else:
                        initial_str = "assigment"

            

            # ----- < -----
            elif initial_str == "start" and self.inputChar == "<":
                initial_str = "smaller"
                recognized_string += self.inputChar
                if initial_str == "smaller":
                    self.inputChar = f.read(1)
                    if self.inputChar == "=" or self.inputChar == ">":
                        initial_str = "relOp"
                        recognized_string += self.inputChar
                        self.inputChar = f.read(1)
                    else:
                        initial_str = "relOp"

            # ----- > -----
            elif initial_str == "start" and self.inputChar == ">":
                initial_str = "smaller"
                recognized_string += self.inputChar
                if initial_str == "smaller":
                    self.inputChar = f.read(1)
                    if self.inputChar == "=" :
                        initial_str = "relOp"
                        recognized_string += self.inputChar
                        self.inputChar = f.read(1)
                    else:
                        initial_str = "relOp"

            # ---- # -----
            elif initial_str == "start" and self.inputChar == "#":
                initial_str = "saw #"
                recognized_string += self.inputChar
            if initial_str == "saw #":
                self.inputChar = f.read(1)
                if self.inputChar == "{" or self.inputChar == "}":
                    recognized_string += self.inputChar
                    initial_str = "parenthesis"
                    self.inputChar = f.read(1)
                elif self.inputChar == "#":
                    recognized_string += self.inputChar
                    initial_str = "comment"
                elif self.inputChar.isalpha():
                    initial_str = "word"
                    recognized_string += self.inputChar
                else:
                    initial_str ="error"
            if initial_str == "word":
                self.inputChar = f.read(1)
                if self.inputChar.isalpha():
                    recognized_string += self.inputChar
                    initial_str = "word"
                else:
                    initial_str ="error"

            if initial_str == "comment":
                self.inputChar = f.read(1)
                while self.inputChar != "#" and self.inputChar!="":
                    self.inputChar=f.read(1)
                if self.inputChar == "#":
                    recognized_string += self.inputChar
                    initial_str = "comment_close"
                if self.inputChar=="":
                        initial_str = "error"
                        break
            if initial_str == "comment_close":
                self.inputChar = f.read(1)
                if self.inputChar != "#":
                    recognized_string += self.inputChar
                    initial_str = "comment"
                elif self.inputChar=="#":
                    recognized_string += self.inputChar
                    initial_str = "start"
                    recognized_string = ''
                    self.inputChar = f.read(1)
                else:
                    initial_str = "error"
            
        
        token=Token(recognized_string,initial_str,self.line_number) 
        lex_syn.write(token.__str__() ) 
        lex_syn.write("\n" )    
        return token

class Token():

    def __init__(self,recognized_string, initial_str, line_number): 
        self.recognized_string = recognized_string
        self.initial_str = initial_str
        self.line_number = line_number
        self.__str__()

    def __str__(self):
        return  "Recognize : "+"[" + self.recognized_string + "]"  + "," + " Type : " +"["  + self.initial_str + "]" + ", Line : " + "["  + str(self.line_number) +"]"
    
class QuadPointerList():
    
    def __init__(self,op,op1,op2,op3,label):
        self.op = op
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3
        self.label = label
        
    def __str__(self):
        return f'{self.label} : {self.op} ,{self.op1} , {self.op2} ,{self.op3}'
        
class QuadList():
     
    def __init__(self):
        self.label = 0
        self.x = 0
        self.my_list=[]
        
    def newTemp(self):          
        nname = "T_"+ str(self.x)
        self.x += 1
        return nname
    
    def emptyList():
        my_list2=[]
        return my_list2

    def makeList(self,label):
        my_list1=[label]
        return my_list1

    def mergeList(list1,list2):
        my_list = []
        my_list.append(list1)
        my_list.append(list2)
        return my_list

    def genQuad(self,op, op1, op2, op3):
        self.my_list.append(QuadPointerList(op,op1, op2, op3,self.label))
        self.label += 1

    def nextQuad(self):
        return self.label

    def backpatch(self,my_list,label):
        for i in my_list :
            self.my_list[i].operand3 = label
 
class Table():

    def __init__(self):
        self.listTable = []
    
    def addScope(self,scope):
        self.listTable.append(scope)
    
    def deleteScope(self):
        self.listTable.pop()
              
class Scope(Table):

    def __init__(self,level):
        self.level = level
        self.mylist = []

    def addEntity(self,entity):
        self.mylist.append(entity)

    def __str__(self):
        my_str = ''.join(map(str, self.mylist))
        return "scope " + str(self.level) + ": " +  my_str   

class Entity(Scope):
    def __init__(self,name,level):
        super().__init__(level)
        self.name = name

    def __str__(self):
        return self.name

class Variable(Entity):

    def __init__(self,name,level,datatype,offset):
        super().__init__(name,level)
        self.datatype = datatype
        self.offset = offset

    def __str__(self): 
        return f' {self.name}/{str(self.offset)} ' 

class Procedure(Entity):

    def __init__(self,name,level,startingQuad,framelength):
        super().__init__(name,level)
        self.startingQuad = startingQuad
        self.framelength = framelength
        self.formalParameters = []
    
    def __str__(self): 
        x = sum(self.formalParameters)
        return f' name = {self.name}/{self.framelength}'

    
    def update(self,framelength,startingQuad):
        self.framelength = framelength
        self.startingQuad = startingQuad

    def addparameter(self,formalParameter):
        self.formalParameters.append(formalParameter)     

class FormalParameter(Procedure,Entity):

    def __init__(self,name,level,datatype,mode):
        super().__init__(name,level)
        self.datatype = datatype
        self.mode = mode

    def __str__(self):
        return "(in " + self.name + ")"       
        
class Parameter(FormalParameter,Variable):
    def __init__(self,name,level,datatype,mode,offset):
        super().__init__(name,level,datatype,mode,offset)   

class Function(Procedure):

    def __init__(self,name,level,datatype,startingQuad,framelength):
        super().__init__(name,level,startingQuad,framelength)
        self.datatype = datatype
        self.formalParameters = []

class TemporaryVariable(Variable):

    def __init__(self,name,level,datatype,offset):
        super().__init__(name,level,datatype,offset)  

class SymbolicConstant(Entity):

    def __init__(self,name,datatype,value):
        super().__init__(name)
        self.datatype = datatype
        self.value = value

class Syn():

    def __init__(self):
        self.lexical =Lex()
        self.errorText = ''
        self.Quad = QuadList()
        self.table = Table()
        self.scope = Scope(0) 
        self.table.addScope(self.scope)

    def syn_analyzer(self):
        if self.program():
            print("---success---")
        else: print("---failed---")

    def error(self,string):
        print(string)
        return string
        
    def program(self):                                                                              
        self.token = self.lexical.lex()
        if self.declarations() :
            if self.def_function(): 
                return True
                if self.def_main_function(): 
                    return True
            else: return False
        else: return False
    
    def def_main_function(self):
        if self.token.recognized_string == "#def":
            self.token = self.lexical.lex()
            ident = self.token.recognized_string
            if self.token.initial_str == 'main':
                self.token = self.lexical.lex() 
                
                level = len( self.table.listTable)
                datatypeFunction = "Integer"
                startingQuad= 0
                framelength = 0
                function = Function(nameFunction,level,datatypeFunction,startingQuad,framelength)
                self.table.listTable[-1].addEntity(function)     
                scope = Scope(len(self.table.listTable))    
                self.table.addScope(scope)    
                            
                self.token = self.lexical.lex()
                            

                self.declarations()
                while self.def_function():         
                    continue
                self.Quad.genQuad("begin_block",ident ,"_","_")  
                startingQuad = self.Quad.label
                if self.code_block():
                    
                        self.Quad.genQuad("halt",ident ,"_","_") 
                        self.Quad.genQuad("end_block",ident ,"_","_") 
                        self.token = self.lexical.lex()               
                                      
                        for i in self.table.listTable:
                            p.write(str(i))
                            p.write("\n")
                        framelength = self.table.listTable[-1].mylist[-1].offset + 4                                    
                        self.table.listTable[-2].mylist[-1].update(framelength,startingQuad)    
                        self.table.deleteScope() 
                        return True
                    
                else:
                        errorText =''
                        return False   
                            
                        
                    
            else:
                errorText =''
                errorText = " --- missing 'main' --- "
                self.error(errorText)
                return False
        else:
            return False
    

    def def_function(self):
        if self.token.recognized_string == 'def':
            self.token = self.lexical.lex()
            ident = self.token.recognized_string
            if self.token.initial_str == 'identifier':
                identifierr = self.token.recognized_string
                self.token = self.lexical.lex()
                if self.token.recognized_string == '(':
                    self.token = self.lexical.lex()
                    if self.id_list():
                        if self.token.recognized_string == ')':
                            self.token = self.lexical.lex()
                            if self.token.recognized_string == ':':
                                nameFunction = ident 
                                level = len(self.table.listTable)
                                datatypeFunction = "Integer"
                                startingQuad = 0
                                framelength = 0
                                function = Function(nameFunction,level,datatypeFunction,startingQuad,framelength)
                                self.table.listTable[-1].addEntity(function)     
                                scope = Scope(len(self.table.listTable))    
                                self.table.addScope(scope)    

                                self.token = self.lexical.lex()
                                if self.token.recognized_string == '#{':
                                    self.token = self.lexical.lex()
                                    if self.declarations(): 
                                        while self.def_function():
                                            continue
                                        self.Quad.genQuad("begin_block",ident,"_","_")
                                        startingQuad = self.Quad.label
                                        if self.code_block():
                                            if self.token.recognized_string == '#}':
                                                self.Quad.genQuad("end_block",identifierr,"_","_")
                                                self.token = self.lexical.lex()
                                                for i in self.table.listTable:
                                                    symbol.write(str(i))
                                                    symbol.write("\n")
                                                framelength = self.table.listTable[-1].mylist[-1].offset + 4                                    
                                                self.table.listTable[-2].mylist[-1].update(framelength,startingQuad)    
                                                self.table.deleteScope() 
                                                return True
                                            else:
                                             
                                                return False 
                                        else: 
                                            errorText =''
                                            return False   
                                    else:
                                        errorText =''
                                        return False
                                else:
                                    errorText =''
                                    errorText = "--- missing '#{' ---"
                                    self.error(errorText)
                                    return False
                            else:
                                errorText =''
                                errorText =" --- missing ':' ---"
                                self.error(errorText)
                                return False
                        else:
                            errorText =''
                            errorText = "--- missing ')' ---"
                            self.error(errorText)
                            return False
                    else:
                        errorText =''
                        return False
                else:
                    errorText =''
                    errorText = " --- missing '(' ---"
                    self.error(errorText)
                    return False
            else:
                errorText =''
                errorText = "--- missing identifier ---"
                self.error(errorText)
                return False   
        else:
            errorText =''
            return False
    

    def declarations(self):
        while self.declaration_line():
            continue
        return True                   

    def declaration_line(self):
        if self.token.recognized_string == '#int' or self.token.recognized_string == 'global': 
            self.token = self.lexical.lex()
            if self.id_list():
                return True
            else: return False
        else: return False

    

    def id_list(self):
        if self.token.initial_str == 'identifier':
            name = self.token.recognized_string
            if(len(self.table.listTable[-1].mylist) == 0):
                variable = Variable(name, len(self.table.listTable),"Integer",12)
                self.table.listTable[-1].addEntity(variable)
            else:
                variable = Variable(name, len(self.table.listTable),"Integer",self.table.listTable[-1].mylist[-1].offset + 4)
                self.table.listTable[-1].addEntity(variable)
            self.token = self.lexical.lex()
            while self.token.recognized_string == ',':
                self.token = self.lexical.lex()
                if self.token.initial_str == 'identifier':
                    variable = Variable(name, len(self.table.listTable),"Integer",self.table.listTable[-1].mylist[-1].offset + 4)
                    self.table.listTable[-1].addEntity(variable)
                    self.token = self.lexical.lex()
                    return True   
                else:
                    errorText =''
                    errorText="--- missing identifier ---"
                    self.error(errorText)
                    return False
            return True
        else: return True




    def statement(self):
        if self.simple_statement():
            return True
        elif self.structured_statement():
            return True
        else: return False

    def code_block(self):
        if self.statement():
            while self.statement():
                continue  
            return True 
        else: return False   

    def simple_statement(self):
        if self.assigment_stat():
            return True
        elif self.print_stat():
            return True
        elif self.return_stat():
            return True
        else: return False

    def structured_statement(self):
        if self.if_stat():
            return True
        elif self.while_stat():
            return True
        else: return False

    def assigment_stat(self):
        if self.token.initial_str == 'identifier':
            ident = self.token.recognized_string
            self.token = self.lexical.lex()
            if self.token.recognized_string == '=':
                self.token = self.lexical.lex()   
                assign = self.token.recognized_string
                t0 = self.expression("")
                if t0:
                    self.Quad.genQuad("=",t0,"_", ident)                 
                    if self.token.recognized_string == ';':
                        self.token = self.lexical.lex()
                        return True
                    else:
                        errorText =''
                        errorText = " --- missing ';' --- "
                        self.error(errorText)
                        return False   
                else:
                    if self.token.recognized_string == 'int':
                        self.token = self.lexical.lex()
                        if self.token.recognized_string == '(':
                            self.token = self.lexical.lex()
                            if self.token.recognized_string == 'input':
                                self.token = self.lexical.lex()
                                if self.token.recognized_string == '(':
                                    self.token = self.lexical.lex()
                                    if self.token.recognized_string == ')':
                                        self.token = self.lexical.lex()
                                        if self.token.recognized_string == ')':
                                            
                                            self.token = self.lexical.lex()
                                            if self.token.recognized_string == ';':
                                                self.Quad.genQuad("in",ident,"_","_")
                                                self.token = self.lexical.lex()
                                                return True
                                            else:
                                                errorText =''
                                                errorText =" --- missing ';' ---"
                                                self.error(errorText)
                                                return False
                                        else:
                                            errorText =''
                                            errorText = "--- missing '(' ---"
                                            self.error()
                                            return False
                                    else:
                                        errorText =''
                                        errorText =" --- missing ')' ---"
                                        self.error(errorText)
                                        return False
                                else:
                                    errorText =''
                                    errorText =" --- missing ')' ---"
                                    self.error(errorText)
                                    return False
                            else:
                                errorText =''
                                errorText =" --- missing 'input' --- "
                                self.error(errorText)
                                return False
                        else:
                            errorText =''
                            errorText =" --- missing '(' ---"
                            self.error(errorText)
                            return False
                    else:
                        errorText =''
                        errorText =" --- missing 'int' ---"
                        self.error(errorText)
                        return False    
            else:
                errorText =''
                errorText =" --- missing '=' --- "
                self.error(errorText)
                return False
        else:
            errorText =''
            return False    
        
    def return_stat(self):
        if self.token.recognized_string == 'return':
            self.token = self.lexical.lex()
            if self.token.recognized_string == '(':
                self.token = self.lexical.lex()
                expres = self.expression([])
                if expres:
                    self.Quad.genQuad("retv",expres,"_","_")
                    if self.token.recognized_string == ')':
                        self.token = self.lexical.lex()
                        if self.token.recognized_string == ';':
                            self.token = self.lexical.lex()
                            return True 
                        else:
                            errorText =''
                            errorText = "--- missing ';' ---"
                            self.error(errorText)
                            return False
                    else:
                        errorText =''
                        errorText = "--- missing ')' ---"
                        self.error(errorText)
                        return False
                else:
                    errorText =''
                    return False
            else:
                errorText =''
                errorText = "--- missing '(' ---"
                self.error(errorText)
                return False        
        else:
            errorText =''
            return False


    def print_stat(self):
        if self.token.recognized_string == 'print':
            self.token = self.lexical.lex()
            if self.token.recognized_string == '(':
                self.token = self.lexical.lex()
                express = self.expression([])
                if express:    
                    self.Quad.genQuad("out",express,"_","_")
                    if self.token.recognized_string == ')':
                        self.token = self.lexical.lex()
                        if self.token.recognized_string == ';':
                            self.token = self.lexical.lex()
                            return True 
                        else:
                            errorText =''
                            errorText ="--- missing ';' ---"
                            self.error(errorText)
                            return False
                    else:
                        errorText =''
                        errorText =" --- missing ')' ---"
                        self.error(errorText)
                        return False
                else:
                    errorText =''
                    return False
            else:
                errorText =''
                errorText = " --- missing '(' ---"
                self.error(errorText)
                return False        
        else:
            errorText =''
            return False

    def while_stat(self):
        if self.token.recognized_string == 'while': 
            self.token = self.lexical.lex()
            condQuad = self.Quad.nextQuad()
            if self.token.recognized_string == '(':
                self.token = self.lexical.lex()  
                cond= self.condition([],[])
                if cond:
                    qtrue= cond[0]
                    qfalse = cond[1]
                    if self.token.recognized_string == ')':
                        self.token = self.lexical.lex()
                        if self.token.recognized_string == ':':
                            self.Quad.backpatch(qtrue,self.Quad.nextQuad())
                            self.token = self.lexical.lex()
                            stat = self.statement()
                            if stat:
                                self.Quad.genQuad('jump','_','_',condQuad)
                                self.Quad.backpatch(qfalse,self.Quad.nextQuad())
                                return True
                            else:
                                if self.token.recognized_string == '#{':
                                    self.token = self.lexical.lex()
                                    stats = self.code_block()
                                    if stats:
                                        if self.token.recognized_string == '#}':
                                            self.Quad.genQuad('jump','_','_',condQuad)
                                            self.Quad.backpatch(qfalse,self.Quad.nextQuad())
                                            self.token = self.lexical.lex()
                                            return True
                                        else:
                    
                                            return False
                                    else:
                                        errorText =''
                                        return False
                                else:
                                    errorText =''
                                    errorText = "--- missing '#{' ---"
                                    self.error(errorText)
                                    return False
                        else:
                            errorText=''
                            errorText = "--- missing ':' ---"
                            self.error(errorText)
                            return False
                    else:
                        errorText=''
                        errorText = "--- missing ')' ---"
                        self.error(errorText)
                        return False
                else:
                    errorText =''
                    return False
            else:
                errorText =''
                errorText = "--- missing '(' ---"
                self.error(errorText)
                return False
                
        else:
            errorText =''
            errorText = "--- missing 'while' ---"
            return False                
    
    def if_stat(self):
        if self.token.recognized_string == 'if':
            self.token = self.lexical.lex()
            if self.token.recognized_string == '(':
                self.token = self.lexical.lex()
                condition = self.condition([],[])
                if condition:
                    qtrue= condition[0]
                    qfalse = condition[1]
                    if self.token.recognized_string == ')':
                        self.token = self.lexical.lex()
                        if self.token.recognized_string == ':':     
                            self.Quad.backpatch(qtrue,self.Quad.nextQuad())
                            self.token = self.lexical.lex()
                            statement = self.statement()  
                            if statement:
                                if self.token.recognized_string == 'else':
                                    self.token = self.lexical.lex()
                                    if self.token.recognized_string == ':':
                                        self.token = self.lexical.lex()
                                        if statement:
                                            ifList = self.Quad.makeList(self.Quad.nextQuad())
                                            self.Quad.genQuad('jump','_','_','_')
                                            self.Quad.backpatch(qfalse,self.Quad.nextQuad())
                                            return True
                                        else:  
                                            if self.token.recognized_string == '#{':
                                                self.token = self.lexical.lex()
                                                states = self.statements()
                                                if states:
                                                    self.Quad.backpatch(ifList,self.Quad.nextQuad())
                                                    if self.token.recognized_string == '#}':
                                                        self.token = self.lexical.lex()
                                                        return True
                                                    else:
                                                        return False
                                                else:
                                                    errorText =''
                                                    return False
                                            else:
                                                errorText =''
                                                errorText = "--- missing '#{' ---"
                                                self.error(errorText)
                                                return False
                                    else:
                                        errorText =''
                                        errorText = "--- missing ':' ---"
                                        self.error(errorText)
                                        return False
                                else:
                                   
                                    return True 
                            else:
                                if self.token.recognized_string == '#{':
                                    self.token = self.lexical.lex()
                                    if self.statements():
                                        if self.token.recognized_string == '#}':
                                            self.token = self.lexical.lex()
                                            if self.token.recognized_string == 'else':
                                                self.token = self.lexical.lex()
                                                if self.token.recognized_string == ':':
                                                    self.token = self.lexical.lex()
                                                    if self.statement():
                                                        return True
                                                    else:
                                                        if self.token.recognized_string == '#{':
                                                            self.token = self.lexical.lex()
                                                            if self.statements():
                                                                if self.token.recognized_string == '#}':
                                                                    self.token = self.lexical.lex()
                                                                    return True
                                                                else:
                                                                    return False
                                                            else:
                                                                return False
                                                        else:
                                                            errorText =''
                                                            errorText = "--- missing '#{' ---"
                                                            self.error(errorText)
                                                            return False
                                                else:
                                                    errorText =''
                                                    errorText = "--- missing ':' ---"
                                                    self.error(errorText)
                                                    return False
                                            else:
                                                errorText =''
                                                return True 
                                        else:
                                            errorText =''
                                            errorText = "--- missing '#}' ---"
                                            self.error(self.token.recognized_string)
                                            errorText =''
                                            return False
                                    else: 
                                        errorText =''
                                        return False
                                else:
                                    errorText =''
                                    errorText = "--- missing '#{' ---"
                                    self.error(errorText)
                                    return False
                        else:
                            errorText =''
                            errorText = "--- missing ':' ---"
                            self.error(errorText)
                            return False
                    else:
                        errorText =''
                        errorText ="--- missing ')' ---"
                        self.error(errorText)
                        return False
                else:
                    errorText =''
                    return False
            else:
                errorText =''
                errorText = "--- missing '(' ---"
                self.error(errorText)
                return False
        else:
            errorText =''
            return False



    def expression(self,Eplace):
        now = self.token.recognized_string    
        if self.optional_sign() :
            T1place = self.term("") 
            if T1place:
                while self.token.initial_str == 'addOp':
                    op = self.token.recognized_string
                    self.token = self.lexical.lex()
                    T2place = self.term([])
                    if T2place:
                        w = self.Quad.newTemp()
                        self.Quad.genQuad(op, T1place, T2place, w)
                        T1place = w

                        if(len(self.table.listTable[-1].mylist) == 0):
                            temporary = TemporaryVariable(w, len(self.table.listTable), "Integer",12)
                            self.table.listTable[-1].addEntity(temporary)
                        else:
                            i = 1
                            while(type(self.table.listTable[-1].mylist[-i]) == Function):
                                i += 1
                            temporary = TemporaryVariable(w, len(self.table.listTable),"Integer", self.table.listTable[-1].mylist[-i].offset + 4)
                            self.table.listTable[-1].addEntity(temporary)


                        continue
                    else: return False 
                Eplace = T1place
                return Eplace
            else : 
                return False
        else:
            
            return False

    def term(self,Tplace):
        operand1 = self.token.recognized_string    
        F1place = self.factor("")
        if F1place:
            while self.token.initial_str == 'mulOp':
                op = self.token.recognized_string
                self.token = self.lexical.lex()   
                operand2 = self.token.recognized_string
                F2place= self.factor([])
                if F2place:
                    w = self.Quad.newTemp()
                    self.Quad.genQuad(op, operand1, operand2, w)
                    F1place = w

                    if(len(self.table.listTable[-1].mylist) == 0):
                        temporary = TemporaryVariable(w, "Integer",len(self.table.listTable), 12)
                        self.table.listTable[-1].addEntity(temporary)
                    else:
                        i = 1
                        while(type(self.table.listTable[-1].mylist[-i]) == Function):
                            i += 1
                        temporary = TemporaryVariable(w, len(self.table.listTable),"Integer", self.table.listTable[-1].mylist[-i].offset + 4)
                        self.table.listTable[-1].addEntity(temporary)

                    return F1place
                else:
                    return False
            Tplace = F1place  
            return Tplace
        else: return False

    def factor(self,Fplace):
        if self.token.initial_str == 'number':
            now = self.token.recognized_string
            Fplace = now
            self.token = self.lexical.lex()   
            return Fplace
        elif self.token.recognized_string == '(':
            self.token = self.lexical.lex()
            Eplace = self.expression([])
            if Eplace:
                if self.token.recognized_string == ')':
                    Fplace = Eplace
                    self.token = self.lexical.lex()
                    return Fplace
                else:
                    errorText =''
                    errorText = "--- missing ')' ---"
                    self.error(errorText)
                    return False
            else:
                return False
        elif self.token.recognized_string == 'int':
            return False    
        elif self.token.initial_str == 'identifier':    
            now1 = self.token.recognized_string
             
            IDplace = self.idtail(now1)
            if IDplace :
                #Fplace =IDplace
                return IDplace
            else:  return Fplace
        else: return False   

    def actual_par_list(self):
        Eplace =  self.expression("")
        if Eplace :
            self.Quad.genQuad("par",Eplace,"CV","_")
            while self.token.recognized_string == ',':
                self.token = self.lexical.lex()
                Eplace = self.expression([])
                if Eplace :
                    # self.Quad.genQuad("par",Eplace,"CV","_")
                    continue                                    
                else:
                    return False
            
            return True
        return True 

    def optional_sign(self):
        if self.token.initial_str == 'addOp':
            self.token = self.lexical.lex()
            return True
        else: return True
  

    def condition(self,Qtrue,Qfalse):
        R1 = self.bool_term([],[])
        if R1:
            Qtrue = R1[0]
            Qfalse= R1[1]
            while self.token.recognized_string == 'or':
                self.Quad.backpatch(Qfalse, self.Quad.nextquad())
                self.token = self.lexical.lex()
                R2 = self.bool_term()
                if R2:
                    Qtrue = R2[0]
                    Qfalse= R2[1]
                    Qtrue = self.Quad.mergeList(Qtrue,R2[0])
                    Qfalse = R2[1]
                    return Qtrue,Qfalse
                else: return Qfalse     
            return Qtrue,Qfalse
        else: return Qfalse       
   
    def idtail(self,Fplace):
        self.token = self.lexical.lex()
        if self.token.recognized_string == '(':
            self.token = self.lexical.lex()
            Eplace= self.actual_par_list()
            if Eplace :
                #self.Quad.genQuad("par",Eplace,"CV","_")
                variable = self.Quad.newTemp()
                
                if self.token.recognized_string == ')':
                    self.Quad.genQuad("par",variable,"ret","_")
                    self.Quad.genQuad("call","_","_",Fplace)
                    self.token = self.lexical.lex()

                   
                    if self.table.listTable[-1].mylist == []:
                        temporary = TemporaryVariable(variable, len(self.table.listTable),"Integer", 12)
                        self.table.listTable[-1].addEntity(temporary)
                    else:
                        i = 1
                        while(type(self.table.listTable[-1].mylist[-i]) == Function):
                            i += 1
                        temporary = TemporaryVariable(variable, len(self.table.listTable),"Integer", self.table.listTable[-1].mylist[-i].offset + 4)
                        self.table.listTable[-1].addEntity(temporary)  

                    return variable
                else:
                    errorText =''
                    errorText = "--- missing ')' ---"
                    self.error(errorText)
                    return False
            else: return False
        else: return Fplace     

    
    def bool_term(self, Qtrue, Qfalse):
        R1 = self.bool_factor([], [])
        if R1:
            Qtrue = R1[0]
            Qfalse = R1[1]
            while self.token.recognized_string == 'and':
                self.Quad.backpatch(Qtrue, self.Quad.nextquad())
                self.token = self.lexical.lex()
                R2 = self.bool_factor(True, False)
                if R2:
                    Qtrue = R2[0]
                    Qfalse = self.Quad.mergeList(Qfalse, R2[1])
                else:
                    return Qfalse
            return Qtrue, Qfalse
        else:
            return Qfalse


    def bool_factor(self,Rtrue,Rfalse):
        if self.token.recognized_string == 'not':
            self.token = self.lexical.lex()
            if self.token.recognized_string == '(':
                self.token = self.lexical.lex()
                B = self.condition()
                if B:
                    if self.token.recognized_string == ')':
                        Rfalse = B
                        Rtrue = not(B) 
                        self.token = self.lexical.lex()
                        return Rtrue,Rfalse
                    else:
                        errorText =''
                        errorText = "--- missing ')' ---"
                        self.error(errorText)
                        return Rfalse
                else:
                    Rtrue= True
                    return Rtrue
            else:
                errorText =''
                errorText = " --- missing '(' ---  "
                self.error(errorText)
                return False               
        elif self.token.recognized_string == '(':
            self.token = self.lexical.lex()
            B = self.condition()
            if B:
                if self.token.recognized_string == ')':
                    Rtrue = B
                    Rfalse = not(B)
                    self.token = self.lexical.lex()
                    return Rtrue,Rfalse
                else:
                    errorText =''
                    errorText = "--- missing ')' ---"
                    self.error(errorText)
                    return Rfalse  
            else:
                errorText =''
                Rfalse =  False
                return Rfalse     
        else:
            E1place = self.token.recognized_string
            E =  self.expression("")
            if E:
                if self.token.initial_str == "relOp":
                    op =  self.token.recognized_string
                    self.token = self.lexical.lex()
                    E2place  = self.token.recognized_string
                    E =  self.expression("")
                    if E:
                        label1 = self.Quad.nextQuad()
                        Rtrue = self.Quad.makeList(label1)
                        self.Quad.genQuad(op, E1place,E2place, '_')
                        Rfalse = self.Quad.makeList(self.Quad.nextQuad())
                        self.Quad.genQuad('jump', '_', '_', '_')
                        return Rtrue,Rfalse
                    else:
                        return Rfalse
                else:
                    return False
            else:
                return False


    
w=Syn()
w.syn_analyzer()
for i in w.Quad.my_list:
    endiamesos.write(str(i) + "\n")
