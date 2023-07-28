import ttkbootstrap as ttk
from tkinter import filedialog
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from config import *
import os

class Root(ttk.Window):
    def __init__(self, title: str, size: str, theme: str):
        super().__init__(title=title, themename=theme)
        self.geometry(size)

        self.file_path = ""
        self.files: list[str] = []
        self.file_index = 0
        self.file_count = 0

        navbar = NavBar(self)
        navbar.pack(fill=X)

        sidebar = SideBar(self)
        sidebar.pack(side=RIGHT, fill=Y)

        self.content_section = ScrolledFrame(master=self, bootstyle=DARK, autohide=True)
        self.content_section.pack(fill=BOTH, expand=YES)
        self.content_label = ttk.Label(master=self.content_section, text="No Content Here", bootstyle=[DARK, INVERSE])
        self.content_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    def open_folder(self):
        self.file_path = filedialog.askdirectory()
        self.files = [os.path.join(self.file_path, f) for f in os.listdir(self.file_path) if os.path.isfile(os.path.join(self.file_path, f))]
        self.file_count = len(self.files)-1
        self.file_index = 0
        print(self.files)
        print(root.file_path)
        self.open_folder_page(self.files[0])
    def open_folder_page(self, file_path: str):
        for widget in self.content_section.winfo_children():
            widget.destroy()
        
        with open(file_path, 'r') as f:
            content = f.readlines()

        formatted_content = '\n'.join(content)
        print(formatted_content)

        content_label = ttk.Label(master=self.content_section, text=formatted_content, font=(None, 20))
        content_label.pack(side=TOP, fill=BOTH, expand=YES)
    def next_file(self):
        if self.file_path:
            print(f'going to {self.files[self.file_index]}')
            if self.file_index < self.file_count:
                self.file_index += 1
                self.open_folder_page(self.files[self.file_index])
            else:
                self.file_index = 0
                self.open_folder_page(self.files[self.file_index])


class NavBar(ttk.Frame):
    def __init__(self, root):
        super().__init__(master=root, bootstyle=LIGHT)

        label = ttk.Label(master=self, text="Notes App", font=(None, 20), bootstyle=[LIGHT, INVERSE])
        label.pack(side=LEFT, padx=5, pady=5)

        button = ttk.Button(master=self, text="Open Folder", command=root.open_folder)
        button.pack(side=RIGHT, pady=5, padx=5)

class SideBar(ttk.Frame):
    def __init__(self, root: Root):
        super().__init__(master=root, bootstyle=SECONDARY)

        button = ttk.Button(master=self, text=">", command=root.next_file)
        button.pack(side=RIGHT, padx=10)

if __name__ == "__main__":
    root = Root("Notes App", f'{scrw}x{scrh}', "darkly")
    root.mainloop()