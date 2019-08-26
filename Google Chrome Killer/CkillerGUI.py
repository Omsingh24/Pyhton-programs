import psutil
import time
import tkinter as tk 

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
	
def killthemall():
	file=open('log.txt','a')
	processlist=searchprocess("chrome")  
	global total_mem_saved
	total_mem_saved=0.0
	print("Total Chrome Process terminated:"+ str(len(processlist)))
	label2.config(text="Total Chromes Killed: "+str(int(len(processlist))))
	#print(check)
	for i in processlist:
		try:
			processlist=searchprocess("chrome")
			killprocess(processlist)
			processlist=searchprocess("chrome")  
		except Exception as e:
			pass
				
	file.close()
	#print(e)
	print("Total Memory saved:"+ str(int(total_mem_saved)) +"%")

	label1.config(text="Total Memory Saved: "+str(int(total_mem_saved)) +"%")
	
	

if __name__ == '__main__':
	total_mem_saved=0.0
	window = tk.Tk() 
	window.title('Chrome Killer') 
	window.geometry('250x70')
	button = tk.Button(window, text='Kill Them All', width=25, command=killthemall) 
	label1 = tk.Label(window, text="")
	label2 = tk.Label(window, text="")
	button.pack() 
	label1.pack()
	label2.pack()
	window.mainloop() 
	