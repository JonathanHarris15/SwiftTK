import customtkinter as ctk

class Application:
    def __init__(self, title, dimensions):
        self._current_page = 0
        self._pages = []
        self._pages_names = []
        
        # Initialize CustomTkinter
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        
        self.root = ctk.CTk()
        self.root.title(title)
        self.root.geometry(dimensions)
        
        self.width = int(dimensions.split('x')[0])
        self.height = int(dimensions.split('x')[1])
    
    def add_page(self, app, page, pageName):
        page._app = app
        self._pages.append(page)
        self._pages_names.append(pageName)

    def clear_pages(self):
        for frame in self.root.winfo_children():
            frame.pack_forget()

    def start_app(self):
        if len(self._pages) < 1:
            print("WARNING: NO PAGES ADDED TO APPLICATION\nCANNOT START")
        else:
            page = self._pages[0]
            page.enter("*PROGRAM OPEN*")
            page._frame = page._promised_frame(self.root)
            page._frame.pack(fill="both", expand=True)
            self.root.mainloop()

    def set_Page(self, window, data_pass):
        self.clear_pages()
        if type(window) == int:
            index = window
        elif window in self._pages_names:
            index = self._pages_names.index(window)
        else:
            print(f"Page {window} not found.")
            return

        page = self._pages[index]
        page._vars.update(data_pass)
        page.enter(self._pages_names[self._current_page])
        page._frame = page._promised_frame(self.root)
        page._frame.master = self.root
        self._current_page = index
        c_frame = page._frame
        c_frame.pack(fill="both", expand=True)