'''
# Author: TronGuy
# Github: https://github.com/TronGuy
# License: MIT
'''
import os
from tkinter import *

def init():
		#processador
		p = smp.get()
		#memória
		m = memory.get()
		#kvm
		k = chk.get()
		#som
		s = sw.get()
		#hdd
		hd = hda.get()
		#iso
		cd = iso.get()
	
		if p == "" or m == "" :
			throwError("campos vazios!")
			
		if p != "" and k == 0 and s == 0 and m != "" and hd != "" and cd == "":
			os.system(f"qemu-system-x86_64 -vga virtio -smp {p} -m {m}G -hda {hd}")	
			
		if p != "" and k == 1 and s == 0 and m != "" and hd != "" and cd == "":
			os.system(f"qemu-system-x86_64 -enable-kvm -vga virtio -smp {p} -m {m}G -hda {hd}")
			
		if p != "" and m != "" and k == 1 and s == 1 and hd != "" and cd != "":
			os.system(f"qemu-system-x86_64 -enable-kvm -vga virtio -smp {p} -boot d -cdrom {cd} -m {m}G -hda {hd} -device intel-hda -soundhw all")		  
		if p != "" and m != "" and k == 1 and s == 1 and hd != "" and cd == "":
			os.system(f"qemu-system-x86_64 -enable-kvm -vga virtio -smp {p} -m {m}G -hda {hd} -device intel-hda -soundhw all")
		
		if p != "" and m != "" and k == 1 and cd != "" and s == 0 and hd != "":
			os.system(f"qemu-system-x86_64 -enable-kvm -vga virtio -smp {p} -m {m}G -hda {hd} -boot d -cdrom {cd}")

		if p != "" and m != "" and s == 1 and cd != "" and k == 0 and hd != "":
			os.system(f"qemu-system-x86_64  -vga virtio -smp {p} -device intel-hda -soundhw all -m {m}G -hda {hd} -boot d -cdrom {cd}")

		if p != "" and m != "" and s == 1 and cd != "" and k == 1 and hd == "":
			os.system(f"qemu-system-x86_64  -vga virtio -smp -soundhw all -device intel-hda {p} -m {m}G -boot d -cdrom {cd}")

		if p != "" and m != "" and s == 0 and cd != "" and k == 1 and hd == "":
			os.system(f"qemu-system-x86_64  -enable-kvm -vga virtio -smp  {p} -m {m}G -boot d -cdrom {cd}")

		if p != "" and m != "" and s == 1 and cd != "" and k == 0 and hd == "":
			os.system(f"qemu-system-x86_64  -vga virtio -smp  {p} -m {m}G -boot d -device intel-hda -soundhw all -cdrom {cd}")

		if p != "" and m != "" and s == 0 and k == 0 and cd != "" and hd == "":
			os.system(f"qemu-system-x86_64 -vga virtio -smp {p} -m {m}G -boot d -cdrom {cd}")


def throwError(status):
	error = Tk()
	error.geometry('235x80')
	error.title("ERRO")
	Label(error, text=f'o parâmetro de {status} está vazio!').place(x=10, y=10)
	Button(error,text="OK", command=error.destroy).place(x=105, y=30)	

def gui():
	try:
		global tk 
		tk = Tk()
		tk.geometry('680x420')
		tk.title("Qemu-Launcher")
		Label(tk, text="Quantidade de Processadores: ").place(x=10,y=10)
		Label(tk, text="Quantidade de Memória: ").place(x=10, y=70)
		global smp
		smp = Entry(tk)
		smp.place(x=10,y=30,width=50,height=20)
		global chk
		chk = IntVar()
		global sw
		sw = IntVar()
		global memory 
		memory = Entry(tk)
		memory.place(x=10, y=90, width=50,height=20)
		global hda
		hda = Entry(tk)
		Label(tk, text='HDA').place(x=10, y=118)
		global iso
		iso = Entry(tk)
		Label(tk, text='ISO').place(x=10, y=170)		
		iso.place(x=10, y= 195, width=400, height=20)
		hda.place(x=10, y=140, width=400, height=20)
		kvm = Checkbutton(tk, text="Habilitar KVM", variable=chk)
		kvm.place(x=10, y=220)
		global sound
		sound = Checkbutton(tk, text="Habilitar som", variable=sw)
		sound.place(x=130, y=220)
		Button(tk, text="Executar", command=init).place(x=10, y=250)
		Button(tk, text="Sair", command=tk.destroy).place(x=95, y=250)
	except KeyboardInterrupt:
		throwError("error")
	tk.mainloop()
try:
	gui()
except:	
	tk.destroy()
	global message 
	message = Tk()
	message.title("Algo não funcionou corretamente")
	message.geometry("235x80")
	Label(message, text=f'O programa foi interrompido!').place(x=10, y=10)
	Button(message,text="OK", command=message.destroy).place(x=105, y=30)	
	message.mainloop()
