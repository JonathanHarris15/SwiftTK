import customtkinter as ctk
from PIL import Image

class Page:
    def __init__(self):
        self.onEnter = lambda: print("",end="")
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
        # Prevent concurrent reloads
        if self._reloading:
            return
        self._reloading = True
        try:
            # Basic validation
            if self._app is None or not hasattr(self._app, "root") or self._app.root is None:
                raise RuntimeError("Cannot reload page: app or app.root is not set")

            # Clear existing pages first to avoid duplicate widgets
            self._app.clear_pages()

            # Create the new frame using the promised factory
            if not callable(self._promised_frame):
                raise RuntimeError("Promised frame is not callable")
            self._frame = self._promised_frame(self._app.root)

            # Pack the created frame so it becomes visible
            self._frame.pack(fill="both", expand=True)
        finally:
            # Always clear the flag even if an exception is raised
            self._reloading = False

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
