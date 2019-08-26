import psutil
import time

def searchprocess(pname):
	processName=pname
	listOfProcessObjects=[]
	for process in psutil.process_iter():
		try:
			processinfo = process.as_dict(attrs=['pid', 'name', 'create_time','memory_percent','cpu_times'])
			   # Check if process name contains the given name string.
			if processName.lower() in processinfo['name'].lower() :

				   listOfProcessObjects.append(processinfo)
				   mem=processinfo['memory_percent']
				   global total_mem_saved
				   total_mem_saved=total_mem_saved+mem
				   #print(int(total_mem_saved))
		except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
			#print("No Process Found")
			pass
	return listOfProcessObjects

def killprocess(processlist):
	for i in processlist:
		process=psutil.Process(i["pid"])
		process.terminate()
		#print(i["pid"])
	
def main():
	file=open('log.txt','a')
	processlist=searchprocess("chrome")  
	
	print("Total Chrome Process terminated:"+ str(len(processlist)))
	#print(check)
	for i in processlist:
		try:
			processlist=searchprocess("chrome")
			killprocess(processlist)
			processlist=searchprocess("chrome")  
		except Exception as e:
			file.write(str(e))
			pass
				
	file.close
	#print(e)
	print("Total Memory saved:"+ str(int(total_mem_saved)) +"%")
	command=input("press y to run again")
	if (command==(("y") or ("Y"))):
		main()
	else:
		exit()


if __name__ == '__main__':
	total_mem_saved=0.0
	main()
	