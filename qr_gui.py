from qr_service import generate_qr_image, save_image
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import qrcode


class QRApp:

    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.current_img = None

        title = tk.Label(root, text="QR Code Generator", font=("Arial", 16))
        title.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        generate_btn = tk.Button(root, text="Generate QR", command=self.generate_qr)
        generate_btn.pack(pady=5)

        save_btn = tk.Button(root, text="Save Image", command=self.save_qr)
        save_btn.pack(pady=5)

        self.qr_label = tk.Label(root)
        self.qr_label.pack(pady=20)

    def generate_qr(self):
        data = self.entry.get().strip()

        if not data:
            messagebox.showwarning("Input needed", "Please enter some text or URL.")
            return

        img = generate_qr_image(data)
        self.current_img = img

        img_resized = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img_resized)

        self.qr_label.config(image=tk_img)
        self.qr_label.image = tk_img

    def save_qr(self):
        if self.current_img is None:
            messagebox.showinfo("No QR", "Generate a QR code first.")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )

        if file_path:
            save_image(self.current_img, file_path)
            messagebox.showinfo("Saved", "QR Code saved successfully!")


root = tk.Tk()
app = QRApp(root)
root.mainloop()
