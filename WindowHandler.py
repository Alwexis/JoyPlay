import psutil
import pygetwindow as gw
import win32process
import time

def get_active_window_process_name():
    active_window = gw.getActiveWindow()
    _, process_id = win32process.GetWindowThreadProcessId(active_window._hWnd)
    process = psutil.Process(process_id)
    info = {
        "process_name": process.name(),
        "process_status": process.status(),
        "window_title": active_window.title
    }
    return info

def init():
    active_process_name = get_active_window_process_name()
    while True:
        time.sleep(1)
        new_process_name = get_active_window_process_name()
        if new_process_name != active_process_name:
            # print(f"Application changed to: {new_process_name['window_title']} ({new_process_name['process_name']})")
            active_process_name = new_process_name
            from Main import loadConfig
            loadConfig()