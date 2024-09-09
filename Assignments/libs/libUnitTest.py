from html import escape
from typing import Callable, Any, Iterable, List, Set, Tuple
from IPython.core.display import display, HTML
import uuid
import unittest
import io,contextlib

from traitlets import ValidateHandler


class testVariable(unittest.TestCase):
  """
  This clas assert the existence of variable and functions for :
  - int, float, string, list, dictionary, tuples.  
  """
  def __init__(self, *argc, **kwargs):
      #contructor the class super for don't overwrite __init__methods          
      unittest.TestCase.__init__(self,*argc)
      self.variable = kwargs
  
  def test_existence_var(self):
    """
    assert name of variable, search in global variables
    """  
    #type()    a=str(type(init_html))
    var_ = self.variable["var"]
    tf = var_ in globals()
    if(tf == True):
      None
    else:
      raise ValueError([],f"#- {var_} is not define")
    
  def test_Equalint(self):
    """
    assert int type of variable
    """      
    var_ = eval(self.variable["var"]) 
    self.assertEqual(type(var_), type(1),msg="#- {}={} migth be type int".format(self.variable["var"],var_))        

  def test_Equalfloat(self):
    """
    assert float type of variable
    """      
    var_ = eval(self.variable["var"])
    self.assertEqual(type(var_), type(1.0),msg="#- {}={} migth be type float".format(self.variable["var"],var_))        
  
  def test_Equalstring(self):
    """
    assert string type of variable
    """      
    var_ = eval(self.variable["var"])
    self.assertEqual(type(var_), type("test"),msg="#- {}={} migth be type string".format(self.variable["var"],var_))        

  def test_Equalcomplex(self):
      """
      assert string type of variable
      """      
      var_ = eval(self.variable["var"])
      self.assertEqual(type(var_), type(1+2.j),msg="#- {}={} migth be type string".format(self.variable["var"],var_))        

  def test_Equalfunctions(self):
     
      var_ = eval(self.variable["var"])
      gg = lambda x:1
      self.assertEqual(type(var_), type(gg),msg="#- {}={} migth be type string".format(self.variable["var"],var_))        

  def test_Equallist(self):
     
      var_ = eval(self.variable["var"])
      gg = [1,1,1,1]
      self.assertEqual(type(var_), type(gg),msg="#- {}={} migth be type string".format(self.variable["var"],var_))        

  def test_Equaltuple(self):
     
      var_ = eval(self.variable["var"])
      gg = (1,1)
      self.assertEqual(type(var_), type(gg),msg="#- {}={} migth be type string".format(self.variable["var"],var_))        


  def test_Equaldictionary(self):
     
      var_ = eval(self.variable["var"])
      gg = {"clave":"valor"}
      self.assertEqual(type(var_), type(gg),msg="#- {}={} migth be type string".format(self.variable["var"],var_))        


  def test_EqualSet(self):
     
      var_ = eval(self.variable["var"])
      gg = {(1,2)}
      self.assertEqual(type(var_), type(gg),msg="#- {}={} migth be type string".format(self.variable["var"],var_))        



class testOneOneFunction(unittest.TestCase):  
    def __init__(self, *argc, **kwargs):
      unittest.TestCase.__init__(self,*argc)#contructor the class super    
      if(len(kwargs)==0):
        self.fun_expected = None
        self.fun_test = None
        params_expected = None
        params_test = None

      else: 
        self.fun_expected = eval(kwargs["fun_expected"][0])
        self.fun_test = eval(kwargs["fun_test"][0])
        self.params_expected = kwargs["fun_expected"][1]
        self.params_test = kwargs["fun_test"][1]
     
    def test_Equalfunctions(self):        
     #   func_test[func_test]()               
        
        c=self.fun_expected(*self.params_expected)         
        d=self.fun_test(*self.params_test)  
       # print(c,d)       
        self.assertEqual(c,d,msg=f"#-The expect value is {c} and the functions test is {d}")        


class testOneValuesFunction(unittest.TestCase):  
    def __init__(self, *argc, **kwargs):
      unittest.TestCase.__init__(self,*argc)#contructor the class super    
      if(len(kwargs)==0):
        self.value_expected = None
        self.fun_test = None        
        params_test = None
      

      else: 
        self.value_expected = kwargs["val_expected"]
        self.fun_test = eval(kwargs["fun_test"][0])        
        self.params_test = kwargs["fun_test"][1]
     
    def test_Expectedvalue(self):                     
        c=self.value_expected
        d=self.fun_test(*self.params_test)       
        self.assertEqual(c,d,msg=f"#-The expect value is {c} and the functions test is {d}")        

    def test_Expectedvaluevalue(self):                     
        c=self.value_expected
        d=self.fun_test
        self.assertEqual(c,d,msg=f"#-The expect value is {c} and the functions test is {d}")        
    

class testOneValuesVariables(unittest.TestCase):  
    def __init__(self, *argc, **kwargs):
      unittest.TestCase.__init__(self,*argc)#contructor the class super    
      if(len(kwargs)==0):
        self.value_expected = None       
        self.value_test=None

      else: 
        self.value_expected = kwargs["val_expected"]
        self.value_test = kwargs["val_test"]
  
    def test_Expectedvaluevalue(self):                     
        c=self.value_expected
        d=self.value_test
        self.assertEqual(c,d,msg=f"#-The expect value is {c} and the functions test is {d}")        
    




#suite.addTest(MyTest('test_something', extraArg))
def suite(object, name,*args,**kwargs):
    if(len(kwargs)==0):      
      suite = unittest.TestSuite()
      a=object()       
      suite.addTest(object(name))    
      return suite
    
    else: # For pass to the function the kwargs
      suite = unittest.TestSuite()
      a=object()    
      suite.addTest(object(name,**kwargs))    
      return suite
    

def add_test(object, methods_name,**kwargs ):
  "The output log is generate due to does'n find the correct way the not show the output in screen"
  "For practice and generality I prefer save the output in variables for working with this"

  with io.StringIO() as buf:
    with contextlib.redirect_stdout(buf):   
      d={}
      for n in methods_name:        
        runner = unittest.TextTestRunner(verbosity=2, stream=buf )#resultclass=unittest.TestResult)        
        result = runner.run(suite(object,n,**kwargs))  # add test case 
        d[n] = (result.wasSuccessful(),  result.errors,result.failures,result.testsRun)        
        output_log = buf.getvalue()  

  return d



class StatePointsV1():
  """
  Update the state for points
  """  
  def __init__(self):
    self.points = 0
    self.msg = ""
    self.hint = ""
    self.state= None
    self.dependence = False

  def update_state(self, status,status_prev, msg, dependence,hint="Hint"):
    if (dependence==True and status_prev==False ):
      self.state="skipped"
      self.msg = "Need resolve the before assignement "
      self.hint = "Need resolve the before assignement "

    else:      
      if(status==True):
        self.state="passed"
        self.msg = "Done"
        self.points+=1

      elif(status==False):
        self.state="failed"
        self.msg = msg
        
      else:
        self.state="skipped"
        self.msg = msg
      


testResultsStyle = """
<style>
  table { text-align: left; border-collapse: collapse; margin: 1em; caption-side: bottom; font-family: Sans-Serif; font-size: 12px}
  caption { text-align: left; padding: 5px }
  th, td { border: 2px solid #BFC9CA; padding: 5px }
  th { background-color: #BFC9CA }
  .passed { background-color: #76D7C4 }
  .failed { background-color: #EC7063 }
  .skipped { background-color: #EDBB99 }
  .score { background-color: #7DCEA0 }
  .results .points { display: none }
  .results .message { display: block; font-size:smaller; color:#D35400 }
  .results .note { display: block; font-size:smaller; font-decoration:italics }
  .results .passed::before  { content: "Passed" } 
  .results .skipped::before  { content: "Skipped" } 
  .results .failed::before  { content: "Failed" } 
  .grade .passed  .message:empty::before { content:"Passed" }
  .grade .failed  .message:empty::before { content:"Failed" }
  .grade .skipped .message:empty::before { content:"Skipped" }   
</style>
    """.strip()
class html_generation():
  cssClass:str="results"    
  def __init__(self):
    self.lines = []
    self.html = None

  def header(self):#is not necessary this part can be execute reading a external file with the initial configuration
    self.lines.append(testResultsStyle)
    self.lines.append("<table class='"+self.cssClass+"'>")
    self.lines.append("  <th class='test'>Test</th><th class='result'>Result</th></tr>")          
  
  def create_row(self,description,hint,message,status ):    


    descriptionHTML = escape(str(description)) #if (escapeHTML) else str(description)
    self.lines.append(f"<tr>")
  #  self.lines.append(f"  <td class='points'>{str(10)}</td>")
    self.lines.append(f"  <td class='test'>")
    self.lines.append(f"    {description}")
    if(len(hint)>0):
      self.lines.append(f"  <div class='note'>Hint: {escape(str(hint))}</div>")
      self.lines.append(f"    <hr/>")
    if(len(message)>0):    
      self.lines.append(f"    <div class='message'>{escape(str(message))}</div>")  
      self.lines.append(f"  </td>")
    self.lines.append(f"  <td class='result {status}'></td>")
    self.lines.append(f"</tr>")    
    self.html = "\n".join(self.lines)
    #self.lines=[]    
   
  def create_score(self,score):
    line=f"  <tr><th class='score'>Total Points</th><th class='score'>{escape(str(score))}</th></tr>"
    self.html+=line
    
   # f"{a}".join(self.html)
  
  
  def show_display(self):
    #html = "\n".join(lines)        
    self.html+="</table>\n"
    display(HTML(self.html))


class add_configurations:
  dicc={}
  def __init__(self):
    self.methods_name=[]
    self.descriptions=[]
    self.nameExpr_=[]
    self.dependences=[]
    self.hint=[]

  def append_(self, method, description, name_var, dependences,hint=""):
    self.methods_name.append(method) 
    self.descriptions.append(description)    
    d={"var":name_var}
    self.nameExpr_.append(d)
    self.dependences.append(dependences)
    self.hint.append(hint)
    
  def append_function(self, method, description, \
                      fun_expected, fun_test, dependences,hint=""):
  # #Evaluamos
    kwargs = {}                                     #Configuration of functions
    kwargs["var"] = fun_test[0] #(sum_test,[1,1])
    kwargs["fun_expected"] = fun_expected #
    kwargs["fun_test"] = fun_test #(sum_test,[1,1])
    self.methods_name.append(method) 
    self.descriptions.append(description)    
    self.nameExpr_.append(kwargs)
    self.dependences.append(dependences)
    self.hint.append(hint)

  def append_function_values(self, method, description,\
                             val_expected, fun_test, dependences,hint=""):
  # #Evaluamos
    kwargs = {}                                     #Configuration of functions
    kwargs["var"] = fun_test[0] #(sum_test,[1,1])
    kwargs["val_expected"] = val_expected #
    kwargs["fun_test"] = fun_test #(sum_test,[1,1])
    self.methods_name.append(method) 
    self.descriptions.append(description)    
    self.nameExpr_.append(kwargs)
    self.dependences.append(dependences)
    self.hint.append(hint)
  
  def append_variables_values(self, method, description,\
                             val_expected, val_test, var,dependences,hint=""):
  # #Evaluamos
    kwargs = {}                                     #Configuration of functions
    kwargs["var"] = var #(sum_test,[1,1])
    kwargs["val_expected"] = val_expected #
    kwargs["val_test"] = val_test #(sum_test,[1,1])
    self.methods_name.append(method) 
    self.descriptions.append(description)    
    self.nameExpr_.append(kwargs)
    self.dependences.append(dependences)
    self.hint.append(hint)
  


  

#Extract error message
def extract_message(message_):
  #print(mensaje)
  for error_msg in message_[1:3]:
    if (len(error_msg)):
      msg=error_msg
  #print(msg)
  #nn = msg[0][1].find(" #-") #Mostrando la informacion que se define como mensaje en la clase3
  nn = msg[0][1].find("Error:") #Mostrando la informacion que se define como mensaje en la clase3
  
  
  error_message = msg[0][1][nn:]
  #print(error_message)
  return error_message




def runTest_v1(config_):

  html_ = html_generation() # init html
  html_.header()
  test_exercise = StatePointsV1()
  cache_prev=False

  for i,method_name in enumerate(config_.methods_name): 
    object_,method_ = method_name.split(".")    
    dependences = config_.dependences[i]
    descriptions =config_.descriptions[i]
    hint = config_.hint[i]

    #1. Check the exitence function
    Name_var = config_.nameExpr_[i]
    dicc = add_test(testVariable, ["test_existence_var"] ,**Name_var) # realized test
    state = dicc["test_existence_var"][0] #State True false and take the msg
    if not state:
      msg = extract_message(dicc["test_existence_var"])#"La funcion no fue definida"
    else:
      msg=""
    test_exercise.update_state(state,cache_prev,msg, test_exercise.dependence)

    #2. Unit testing of functions
    
    if state:   
      test_exercise.points+=-1     # Reduce one point
      kwargs = config_.nameExpr_[i]
      #Pasar como parametro       
      dicc = add_test(eval(object_), [method_] ,**kwargs) # realized test      
      state = dicc[method_][0] #State True false and take the msg
     
     
      test_exercise.dependence = dependences# Load the user define dependeces
      if state:
        test_exercise.dependence = False
        test_exercise.msg=""
      else:
         msg = extract_message(dicc[method_])#"La funcion no fue definida"

      test_exercise.update_state(state, cache_prev,msg, test_exercise.dependence)
      cache_prev=state#memory the previus state for skipping if the assignment before is no ok

    #create row with the information given 
    if(state):
      html_.create_row(descriptions,"",test_exercise.msg,test_exercise.state)
    else:
      html_.create_row(descriptions,hint,test_exercise.msg,test_exercise.state)

  #Include score in the html
  html_.create_score(test_exercise.points) 
  return html_.show_display(),test_exercise
