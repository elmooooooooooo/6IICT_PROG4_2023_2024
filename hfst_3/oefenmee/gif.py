import tkinter as tk
from PIL import Image, ImageTk

class GIFViewer:
    def __init__(self, root, gif_path):
        self.root = root
        self.root.title("GIF Viewer")

        # Load the GIF
        self.gif = Image.open(gif_path)
        self.gif_frames = [ImageTk.PhotoImage(self.gif.seek(i)) for i in range(self.gif.n_frames)]

        # Create a label to display the GIF
        self.gif_label = tk.Label(root)
        self.gif_label.pack()

        # Button to start animation
        self.start_button = tk.Button(root, text="Start Animation", command=self.start_animation)
        self.start_button.pack()

        # Button to stop animation
        self.stop_button = tk.Button(root, text="Stop Animation", command=self.stop_animation)
        self.stop_button.pack()

        self.is_animating = False
        self.current_frame = 0

    def update_gif(self):
        frame = self.gif_frames[self.current_frame]
        self.gif_label.configure(image=frame)
        self.current_frame = (self.current_frame + 1) % len(self.gif_frames)
        if self.is_animating:
            self.root.after(100, self.update_gif)

    def start_animation(self):
        if not self.is_animating:
            self.is_animating = True
            self.update_gif()

    def stop_animation(self):
        self.is_animating = False

if __name__ == "__main__":
    root = tk.Tk()
    gif_path = "path/to/your/gif/file.gif"  # Replace with the path to your GIF file
    gif_viewer = GIFViewer(root, gif_path)
    root.mainloop()
