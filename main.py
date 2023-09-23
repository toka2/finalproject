import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
from homepage import Home

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("1000x800")
        self.configure(background='white')

        self.style = ttk.Style(self)
        self.style.configure('TButton',
                             foreground='#d50000',
                             font=('Helvetica', 15, 'bold'),
                             padding=(10, 5),
                             background='#ef9a9a')

        self.logo = tk.PhotoImage(file='imges/istockpremovebg.png')
        self.logo_lab = tk.Label(self, image=self.logo, bg="white")
        self.logo_lab.place(x=200, y=150)




        self.userLogin_label = tk.Label(
            self, text="Login Here", font="Helvetica  36 bold" , fg="#311b92", bg="white")
        self.userLogin_label.place(x=90, y=100)

        self.userEmail_label = tk.Label(
            self, text="Email", font="Helvetica 15 bold", bg="white")
        self.userEmail_label.place(x=90, y=180)

        self.userEmail = tk.Entry(self, font="Helvetica 12", bg="gray90")
        self.userEmail.place(x=90, y=210)

        self.userPassword_label = tk.Label(
            self, text="Password", font="Helvetica 15 bold", bg="white")
        self.userPassword_label.place(x=90, y=280)

        self.userPassword = tk.Entry(self, font="Helvetica 12", show="*", bg='gray90')
        self.userPassword.place(x=90, y=310)

        self.login_button = ttk.Button(
            self, text='Login', command=self.checkUserAccount)
        self.login_button.place(x=90, y=350)

        self.userRegister_label = tk.Label(
            self, text="Don't have an account?", font="Helvetica 10 bold", fg="#311b92", bg="white")
        self.userRegister_label.place(x=90, y=400)

        self.register_button = ttk.Button(
            self, text='Register', command=self.registerPage )
        self.register_button.place(x=90, y=430)

    def checkUserAccount(self):
        user_email = self.userEmail.get().lower().strip()
        user_password = self.userPassword.get().strip()

        file = open('Project_3.json', 'r')
        all_data = json.load(file)
        file.close()

        user_found = False
        for data in all_data:
            if "mail" in data and "Password" in data:
                if user_email == data['mail'] and user_password == data['Password']:
                    print(data['name'])
                    user_found = True

                    # فتح نافذة HomePage وتمرير اسم الحساب هنا
                    homepage = Home(self, user_name=data['name'])
                    homepage.show_home_content()
                    break

        if not user_found:
            messagebox.showwarning("Alert!", "Wrong email or password")
            self.userEmail.delete(0, 'end')
            self.userPassword.delete(0, 'end')

    def registerPage(self):
        register_window = RegisterPage()
        self.destroy()
        register_window.mainloop()


class RegisterPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Register Page")
        self.geometry("1000x800")
        self.configure(background='white')

        self.style = ttk.Style(self)
        self.style.configure('TButton',
                             foreground='#d50000',
                             font=('Helvetica', 12, 'bold'),
                             padding=(10, 5),
                             background='#EB496F')





        self.userRegister_label = tk.Label(
            self, text="Register Here", font="Impact 35 bold", fg="#311b92", bg="white")
        self.userRegister_label.place(x=90, y=40)

        self.userName_lable = tk.Label(
            self, text="Name", font="Helvetica 10 bold", bg="white")
        self.userName_lable.place(x=90, y=120)

        self.userName = tk.Entry(self, font="Helvetica 12", bg="gray90")
        self.userName.place(x=90, y=140)

        self.userPhone_lable = tk.Label(
            self, text="Phone number", font="Helvetica 10 bold", bg="white")
        self.userPhone_lable.place(x=90, y=180)

        self.userPhone = tk.Entry(self, font="Helvetica 12", bg="gray90")
        self.userPhone.place(x=90, y=200)

        self.userMail_lable = tk.Label(
            self, text="Email", font="Helvetica 10 bold", bg="white")
        self.userMail_lable.place(x=90, y=240)

        self.userMail = tk.Entry(self, font="Helvetica 12", bg="gray90")
        self.userMail.place(x=90, y=260)


        self.userPass_lable = tk.Label(
            self, text="Password", font="Helvetica 10 bold", bg="white")
        self.userPass_lable.place(x=90, y=300)

        self.userPass = tk.Entry(self, font="Helvetica 12", bg="gray90")
        self.userPass.place(x=90, y=320)



        self.register_button = ttk.Button(
            self, text='Register', command=self.store_in_db)
        self.register_button.place(x=90, y=380)

        self.Back_button = ttk.Button(
            self, text='Back', command=self.go_to_login_page)
        self.Back_button.place(x=200, y=380)

    def on_selection_change(self):
        city = self.cities.get()
        print(f"You selected: {city}")

    def go_to_login_page(self):
        self.destroy()
        login_page = LoginPage()
        login_page.mainloop()

    def store_in_db(self):
        userData = {"name": self.userName.get(), "phone": self.userPhone.get(), "mail": self.userMail.get(),
                    "Password": self.userPass.get()}


        file = open('Project_3.json', 'r')
        All_List_In_store = json.load(file)

        All_List_In_store.append(userData)

        file = open("Project_3.json", "w")
        json.dump(All_List_In_store, file, indent=2)
        file.close()
        messagebox.showinfo(
            'successful!', f"REGISTERED SUCCESSFULLY(:-")
        self.go_to_login_page()

app = LoginPage()
app.mainloop()
