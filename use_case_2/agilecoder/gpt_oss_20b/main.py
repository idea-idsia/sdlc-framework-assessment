'''
Entry point – starts the role selection GUI and the Flask services.
'''
from gui import RoleSelectionWindow
from services import start_service_thread
if __name__ == '__main__':
    start_service_thread()          # Start micro‑services
    app = RoleSelectionWindow()     # Show role selection
    app.mainloop()