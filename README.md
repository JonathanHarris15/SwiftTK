# SwiftTK

[![PyPI](https://img.shields.io/pypi/v/SwiftTK)](https://pypi.org/project/SwiftTK/)

A lightweight, class-based page routing system for [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). 

**SwiftTK** simplifies the creation of multi-page GUI applications by managing frame switching, page history, and data passing between pages with minimal boilerplate.

## Features

* **Simple Page Management**: Easily add and switch between named pages.
* **Data Passing**: Send variables from one page to another during navigation.
* **Relative Positioning Helpers**: Built-in methods to place widgets using relative coordinates (0.0 - 1.0) for responsive layouts.
* **Lifecycle Hooks**: `onEnter` and `reload` methods to manage state when switching views.

## Installation

Install the package via pip:

```bash
pip install SwiftTK
```

## Recomended Structure
For best results, we recommend separating your pages into a src/pages directory to keep your project organized.
MyProject/
├── main.py                <-- Entry point
└── src/
    └── pages/             <-- Page modules    
        ├── HomePage.py
        └── SettingsPage.py

## Quick Start Guide
### 1. Create a Page
In SwiftTK, a page is defined by instantiating a `Page` object and assigning it a frame-building function using `set_frame`.
```python
import customtkinter as ctk
from swifttk import Page

# 1. Instantiate the Page object globally for this module
home_page = Page()

# 2. Define the UI Builder function
# This function must accept 'parent' and return the frame
def build_home_frame(parent):
    frame = ctk.CTkFrame(parent)
    
    ctk.CTkLabel(frame, text="Welcome to SwiftTK", font=("Arial", 24)).place(relx=0.5, rely=0.2, anchor="center")

    # Use the helper to add a navigation button
    home_page.add_button(frame, x=0.5, y=0.5, w=0.3, h=0.1, 
                         content="Go to Settings", 
                         command=lambda: home_page.to_Page("Settings"))
    
    return frame

# 3. Link the builder to the page
home_page.set_frame(build_home_frame)
```
### 2. Create the Entry Point
Import your page modules and register them to the Application
```python
from swifttk import Application
# Import your page modules
from src.pages import HomePage, SettingsPage 

# 1. Initialize the Application
app = Application("My Application", "800x600")

# 2. Register Pages
# Format: app.add_page(app_instance, page_object, "Page Name")
app.add_page(app, HomePage.home_page, "Home")
app.add_page(app, SettingsPage.settings_page, "Settings")

# 3. Launch
app.start_app()
```

## Documentation
### The `Page` Class
Inherit from this class to create your views.

Key Methods:

* `self.to_Page(page_name, info=[]):` Navigate to another page. info is a list of variable keys to pass along.

* `self.set_var(name, value):` Set a variable that triggers a page reload if changed.

* `self.add_button(...)` Helper wrappers for fast widget placement.

### The `Application` Class
The main entry point for your app.

* `Application(title, dimensions):` Initialize the window.

* `add_page(app, page_instance, page_name):` Register a page.

* `start_app():` Begin the main event loop.

License
Distributed under the MIT License. See LICENSE for more information.