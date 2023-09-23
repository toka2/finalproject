import tkinter as tk
from tkinter import ttk, messagebox
import json
from PIL import Image, ImageTk
import webview
from tkinter import filedialog


class Home:
    def __init__(self, root, user_name):
        self.content_frame = None
        self.posts_listbox = None
        self.root = root
        self.root.geometry("1000x800")
        self.root.title("IsTock")



        self.json_file = "project_3.json"
        self.image_data = []

        self.user_name = user_name
        self.load_data()



        self.colors = {
            "background": "#f1f8e9",  # لون الخلفية العامة
            "top_bar": "#7e57c2",  # لون الشريط العلوي
            "sidebar": "#5e35b1",  # لون الشريط الجانبي
            "text": "#ffffff",  # لون النص
        }

        self.create_top_bar()
        self.create_sidebar()
        self.create_content_frame()

    def save_post(self, post_text):
        try:
            with open('Project_3.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []

        for user_data in data:
            if "name" in user_data and user_data["name"] == self.user_name:
                if "posts" not in user_data:
                    user_data["posts"] = []
                user_data["posts"].append({"text": post_text})
                break

        with open('Project_3.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        messagebox.showinfo('Success', 'Post saved successfully!')

    def create_top_bar(self):
        top_frame = tk.Frame(self.root, bg=self.colors["top_bar"])
        top_frame.pack(side="top", fill="x")

        icon1_img = tk.PhotoImage(file="imges/images.png").subsample(5)
        icon2_img = tk.PhotoImage(file="imges/video.png").subsample(5)
        icon3_img = tk.PhotoImage(file="imges/home.png").subsample(5)
        icon4_img = tk.PhotoImage(file="imges/image.png").subsample(5)

        icon1_button = tk.Button(top_frame, image=icon1_img, command=self.show_profile_content,
                                 bg=self.colors["top_bar"])

        icon2_button = tk.Button(top_frame, image=icon2_img, command=self.show_video_content,
                                 bg=self.colors["top_bar"])

        icon3_button = tk.Button(top_frame, image=icon3_img, command=self.show_home_content,
                                 bg=self.colors["top_bar"])

        icon4_button = tk.Button(top_frame, image=icon4_img, command=self.show_img_content,
                                 bg=self.colors["top_bar"])



        text_label = tk.Label(top_frame, text="SIC", font=("Russo One", 40), bg=self.colors["top_bar"],
                              fg="#ef9a9a")

        icon1_button.image = icon1_img
        icon2_button.image = icon2_img
        icon4_button.image = icon4_img
        icon3_button.image = icon3_img

        icon1_button.pack(side="left", padx=30)
        icon2_button.pack(side="left", padx=50)
        icon4_button.pack(side="left", padx=50)
        icon3_button.pack(side="left", padx=80)
        text_label.pack(side="right", padx=30)

    def show_home_content(self):
        self.clear_content()

        try:
            with open('Project_3.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []

        entry_frame = tk.Frame(self.content_frame, bg="#279eff")
        entry_frame.pack(side="top", fill="both")

        inner_frame = tk.Frame(entry_frame, bg="white")
        inner_frame.pack(expand=True, fill="both", pady=(20, 0))

        post_entry = tk.Entry(inner_frame, font=("Arial", 12), borderwidth=2, relief="solid")
        post_entry.pack(side="left", expand=True, fill="x", padx=(0, 20), pady=10)

        save_button = tk.Button(inner_frame, text="Save Post", command=lambda: self.save_post(post_entry.get()),
                                bg="#279eff", fg="white", relief="raised")
        save_button.pack(side="right", padx=20, pady=10)

        posts_frame = ttk.Frame(self.content_frame)
        posts_frame.pack(expand=True, fill="both")

        scrollbar = ttk.Scrollbar(posts_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.posts_listbox = tk.Listbox(posts_frame, selectmode=tk.SINGLE, height=20, font=("Arial", 14),
                                        yscrollcommand=scrollbar.set)
        self.posts_listbox.pack(expand=True, fill="both", padx=20, pady=(0, 20))
        scrollbar.config(command=self.posts_listbox.yview)

        for post_data in data:
            if "posts" in post_data and isinstance(post_data["posts"], list):
                for post in post_data["posts"]:
                    if "text" in post:
                        post_text = post["text"]
                        user_name = post_data.get("name", "Unknown")

                        self.posts_listbox.insert(0, post_text)

                        post_frame = ttk.Frame(self.posts_listbox)
                        post_frame.pack(expand=True, fill="both")

                        separator = ttk.Separator(post_frame, orient="horizontal")
                        separator.pack(expand=True, fill="both")

                        publisher_label = ttk.Label(post_frame, text=user_name, font=("Arial", 12))
                        publisher_label.pack(side="right", padx=10, pady=10)

                        post_label = ttk.Label(post_frame, text=post_text, font=("Arial", 14), wraplength=600,
                                               anchor="w", justify="left")
                        post_label.pack(side="left", expand=True, fill="both")


        for image_info in self.image_data:
            image_path = image_info["path"]
            image = Image.open(image_path)
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)

            user_name = image_info["user"]

            user_label = ttk.Label(self.posts_listbox, text=user_name, font=("Arial", 12))
            user_label.pack(expand=True, fill="both")

            image_label = tk.Label(self.posts_listbox, image=image)
            image_label.image = image
            image_label.pack(expand=True, fill="both")






    def show_profile_content(self):
        self.clear_content()

        try:
            with open('Project_3.json', 'r') as json_file:
                data = json.load(json_file)
        except FileNotFoundError:
            data = []

        posts_frame = ttk.Frame(self.content_frame)
        posts_frame.pack(expand=True, fill="both")

        scrollbar = ttk.Scrollbar(posts_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.posts_listbox = tk.Listbox(posts_frame, selectmode=tk.SINGLE, height=20, font=("Arial", 14),
                                        yscrollcommand=scrollbar.set)
        self.posts_listbox.pack(expand=True, fill="both", padx=20, pady=(0, 20))
        scrollbar.config(command=self.posts_listbox.yview)

        for post_data in data:
            if "posts" in post_data and isinstance(post_data["posts"], list):
                for post in post_data["posts"]:
                    if "text" in post and post_data.get("name") == self.user_name:
                        post_text = post["text"]

                        self.posts_listbox.insert(0, post_text)

                        post_frame = ttk.Frame(self.posts_listbox)
                        post_frame.pack(expand=True, fill="both")

                        separator = ttk.Separator(post_frame, orient="horizontal")
                        separator.pack(expand=True, fill="both")

                        post_label = ttk.Label(post_frame, text=post_text, font=("Arial", 14), wraplength=600,
                                               anchor="w", justify="left")
                        post_label.pack(side="left", expand=True, fill="both")



        for image_info in self.image_data:
            image_path = image_info["path"]
            image = Image.open(image_path)
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.posts_listbox, image=image)
            image_label.image = image
            image_label.pack(expand=True, fill="both")



    def show_video_content(self):
        self.clear_content()
        webview.create_window("Web Page", "https://www.youtube.com/", width=800, height=600)
        webview.start()


    def show_img_content(self):
        self.clear_content()
        image_grid_frame = tk.Frame(self.content_frame, bg=self.colors["background"])
        image_grid_frame.pack(expand=True, fill="both")

        select_image_button = tk.Button(image_grid_frame, text="Select Image",
                                        command=self.load_image, bg="#279eff", fg="white")
        select_image_button.pack(side="top", pady=10)

        self.image_display_frame = tk.Frame(self.content_frame, bg=self.colors["background"])
        self.image_display_frame.pack(expand=True, fill="both")

        for image_info in self.image_data:
            image_path = image_info["path"]
            image = Image.open(image_path)
            image = image.resize((200, 200))
            image = ImageTk.PhotoImage(image)

            image_label = tk.Label(self.image_display_frame, image=image)
            image_label.image = image
            image_label.pack(expand=True, fill="both")

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.gif")])
        if file_path:
            try:
                image = Image.open(file_path)
                image = image.resize((200, 200))
                image = ImageTk.PhotoImage(image)

                image_label = tk.Label(self.image_display_frame, image=image, bg=self.colors["background"])
                image_label.image = image

                image_label.pack(side="top", padx=10, pady=10)

                self.image_data.append({
                    "path": file_path,
                    "user": self.user_name
                })

                self.update_json_data()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to open the image: {str(e)}")

    def load_data(self):
        try:
            with open(self.json_file, 'r') as json_file:
                self.json_data = json.load(json_file)
                for user_data in self.json_data:
                    if user_data.get("name") == self.user_name and "images" in user_data:
                        self.image_data = user_data["images"]
        except FileNotFoundError:
            self.json_data = []

    def update_json_data(self):
        for user_data in self.json_data:
            if user_data.get("name") == self.user_name:
                user_data["images"] = self.image_data
                break

        with open(self.json_file, 'w') as json_file:
            json.dump(self.json_data, json_file, indent=4)





    def create_sidebar(self):
        sidebar_frame = tk.Frame(self.root, width=200, bg=self.colors["sidebar"])
        sidebar_frame.pack(side="right", fill="y")

        image = Image.open("imges/istockicon.png")
        image = image.resize((150, 110))
        image = ImageTk.PhotoImage(image)

        image_label = tk.Label(sidebar_frame, image=image, bg=self.colors["sidebar"])
        image_label.image = image

        page2_button = tk.Button(sidebar_frame, text="Games", command=self.show_games_content,
                                 bg=self.colors["sidebar"])
        page1_button = tk.Button(sidebar_frame, text="تسجيل الخروج", command=self.logout, bg=self.colors["sidebar"])

        separator = ttk.Separator(sidebar_frame, orient="horizontal")
        image_label.pack()
        separator.pack(fill="x", pady=15)

        page2_button.pack()
        page1_button.pack()

    def logout(self):

        self.root.quit()

    def show_games_content(self):
        self.clear_content()
        webview.create_window("Web Page", "https://gamesbarq.com/", width=800, height=600)
        webview.start()


    def create_content_frame(self):
        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack(side="top", fill="both", expand=True)
        self.show_home_content()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

#if __name__ == "__main__":
app = tk.Tk()
app.mainloop()
