import customtkinter as ctk
from PIL import Image

class Page:
    def __init__(self):
        self.onEnter = lambda: print("")
        self._frame = None
        self._vars = {}
        self._reloading = False
        self._entering = True
        self._app = None
        # Default to CTkFrame
        self._promised_frame = lambda parent: ctk.CTkFrame(parent)
        self.entered_from = "Start"

    # Routine automatically called when page is entered to set flags correctly
    def enter(self, start_page):
        self.entered_from = start_page
        self._entering = True
        self.onEnter()
        self._entering = False

    # Made to refresh the information on the page
    def reload(self):
        if not self._reloading:
            self._reloading = True
            # Pass the root as the parent when reloading
            self._frame = self._promised_frame(self._app.root)
            self._reloading = False
            self._app.clear_pages()
            c_frame = self._frame
            c_frame.master = self._app.root
            c_frame.pack(fill="both", expand=True)

    # The method to migrate to another page
    def to_Page(self, page, info=[]):
        self._entering = True
        push_info = {}
        for key, value in self._vars.items():
            if key in info:
                push_info[key] = value
        self._app.set_Page(page, push_info)

    # Sets a page variable in a way that will refresh the screen
    def set_var(self, name, value):
        self._vars[name] = value
        if not self._entering:
            self.reload()

    # Helpers for array manipulation
    def change_index(self, name, index, value):
        x = self.get_var(name)
        if x:
            x[index] = value
            self.set_var(name, x)
    
    def push(self, name, value):
        x = self.get_var(name)
        if x is None: x = []
        x.append(value)
        self.set_var(name, x)

    def get_var(self, name):
        return self._vars.get(name, None)
        
    def set_frame(self, frm):
        if callable(frm):
            self._promised_frame = frm
        else:
            print("set_frame() must take a function")

    def print_vars(self):
        for key, value in self._vars.items():
            print(f"-----> {key} <-----")
            print(value)
