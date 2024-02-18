import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import webbrowser

class MacrohardWebExplorer:
    def __init__(self, master):
        self.master = master
        master.title("Macrohard Web Explorer")

        self.url_entry = tk.Entry(master)
        self.url_entry.pack(fill=tk.X, padx=10, pady=5)

        self.go_button = tk.Button(master, text="Go", command=self.open_url)
        self.go_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.back_button = tk.Button(master, text="Back", command=self.go_back)
        self.back_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.forward_button = tk.Button(master, text="Forward", command=self.go_forward)
        self.forward_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=60, height=20)
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.history = []
        self.current_page_index = -1

    def open_url(self):
        url = self.url_entry.get()
        if url.startswith('http://') or url.startswith('https://'):
            webbrowser.open(url)
            self.history.append(url)
            self.current_page_index += 1
        else:
            webbrowser.open("http://" + url)
            self.history.append("http://" + url)
            self.current_page_index += 1

    def go_back(self):
        if self.current_page_index > 0:
            self.current_page_index -= 1
            webbrowser.open(self.history[self.current_page_index])

    def go_forward(self):
        if self.current_page_index < len(self.history) - 1:
            self.current_page_index += 1
            webbrowser.open(self.history[self.current_page_index])

root = tk.Tk()
browser = MacrohardWebExplorer(root)
root.mainloop()
