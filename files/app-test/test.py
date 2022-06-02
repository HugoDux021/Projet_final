import pytest
import sys, os
  
cwd = "/var/jenkins_home/workspace/pipelineprojet/files/app-python"
  
fd = 'false_dir / temp'
  
try: 
    os.chdir(fd) 
    print("Inserting inside-", os.getcwd()) 
      
except: 
    print("Something wrong with specified directory. Exception- ", sys.exc_info()) 
            
finally: 
    print("Restoring the path") 
    os.chdir(cwd) 
    print("Current directory is-", os.getcwd()) 

import lancement_QCM as lance_QCM

def test_get_nom():
    assert lance_QCM.hello('lucie') == 'Hello lucie'
