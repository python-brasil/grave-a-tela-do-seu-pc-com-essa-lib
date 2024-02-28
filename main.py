import customtkinter as ctk
import os
from screen_recorder_sdk import screen_recorder

class GravadorTela:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('300x200')
        self.root.resizable(False,False)
        self.itens_janela()
        
        self.root.mainloop()
    
    def itens_janela(self):
        self.lb_title = ctk.CTkLabel(
            master=self.root,
            text='Gravador de Tela',
            bg_color=self.root.cget('bg'),
            font=('Verdana', 25),
        )
        
        self.btn_play = ctk.CTkButton(
            master=self.root,
            text='Play',
            width=20,
            font=('Verdana', 15),
            command=self.play
        )
        
        self.btn_stop = ctk.CTkButton(
            master=self.root,
            text='Stop',
            width=20,
            font=('Verdana', 15),
            command=self.stop
        )
        
        self.btn_folder = ctk.CTkButton(
            master=self.root,
            text='Folder',
            width=20,
            font=('Verdana', 15),
            command=self.folder
        )
        
        self.lb_title.grid(row=0, columnspan=3,pady=30,padx=40)
        self.btn_play.grid(row=1, column=0, padx=(30,10))
        self.btn_stop.grid(row=1, column=1, padx=(30,10))
        self.btn_folder.grid(row=1, column=2, padx=(30,10))
    
    def play(self):
        screen_recorder.enable_dev_log()
        params = screen_recorder.RecorderParams()
        screen_recorder.init_resources(params)
        screen_recorder.start_video_recording(os.path.join("video.mp4"),30,8000000,True)
        
    def stop(self):
        screen_recorder.stop_video_recording()
        screen_recorder.free_resources()
        self.btn_play["state"] = "normal"
        self.btn_stop["state"] = "disabled"
        
    def folder(self):
        path = os.path.realpath(os.getcwd())
        os.startfile(path)
        
        
if __name__ == '__main__':
    GravadorTela()