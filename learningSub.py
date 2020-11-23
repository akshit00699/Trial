import subprocess
v1 = "IP"
v2 = "JP"
bashCmd = "sed s/%s.*/%s=%s/ Temp.cfg" %(v1,v1,v2) 
print(bashCmd.split())
op = subprocess.check_output(bashCmd.split(), cwd= 'home/aks/Downloads/bash-programming-course/')
print(op)
