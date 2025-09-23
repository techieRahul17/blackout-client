import tkinter as tk
import keyboard

class BlackoutApp:
    def __init__(self, root):
        self.root = root
        self.blackout = False

        # Create fullscreen black overlay, but keep it hidden
        self.overlay = tk.Toplevel(root)
        self.overlay.attributes("-fullscreen", True)
        self.overlay.configure(bg="black")
        self.overlay.attributes("-topmost", True)
        self.overlay.overrideredirect(True)
        self.overlay.withdraw()  # start hidden

        # Register hotkeys
        keyboard.add_hotkey("insert", self.toggle_blackout)
        keyboard.add_hotkey("ctrl+alt+b", self.end_blackout)

        print("✅ Blackout system running...")
        print("➡ Press 'Insert' to toggle blackout.")
        print("➡ Press 'Ctrl+Alt+B' to exit blackout manually.")

        # Periodically check hotkeys
        self.check_keys()

    def toggle_blackout(self):
        print("[DEBUG] Insert pressed → toggling blackout")
        if self.blackout:
            self.end_blackout()
        else:
            self.start_blackout()

    def start_blackout(self):
        print("[INFO] Blackout ON")
        self.blackout = True
        self.overlay.deiconify()  # show overlay

    def end_blackout(self):
        if self.blackout:
            print("[INFO] Blackout OFF")
        self.blackout = False
        self.overlay.withdraw()  # hide overlay

    def check_keys(self):
        # Keeps Tkinter responsive while keyboard listener runs
        self.root.after(100, self.check_keys)


def main():
    root = tk.Tk()
    root.withdraw()  # hide main window
    app = BlackoutApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
