import tkinter as tk
from tkinter import messagebox

class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

    def make_post(self, content):
        new_post = Post(len(self.posts) + 1, self.username, content)
        self.posts.append(new_post)
        return new_post

    def add_comment(self, post, comment_content):
        post.add_comment(self, comment_content)

    def send_message(self, receiver, message_content):
        new_message = Message(len(messages) + 1, self.username, receiver.username, message_content)
        messages.append(new_message)
        return new_message

class Post:
    def __init__(self, post_id, author, content):
        self.post_id = post_id
        self.author = author
        self.content = content
        self.comments = []

    def add_comment(self, user, comment_content):
        new_comment = Comment(len(self.comments) + 1, self.post_id, user.username, comment_content)
        self.comments.append(new_comment)

class Comment:
    def __init__(self, comment_id, post_id, author, content):
        self.comment_id = comment_id
        self.post_id = post_id
        self.author = author
        self.content = content

class Message:
    def __init__(self, message_id, sender, receiver, content):
        self.message_id = message_id
        self.sender = sender
        self.receiver = receiver
        self.content = content

# Dummy data
users = [
    User(1, "user1", "user1@example.com", "password1"),
    User(2, "user2", "user2@example.com", "password2"),
]

posts = []

messages = []

# GUI with tkinter
class SocialMediaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Social Media Platform")

        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)

        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="e")
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_label.grid(row=1, column=0, sticky="e")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login_user)
        self.login_button.grid(row=2, columnspan=2, pady=10)

    def login_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        for user in users:
            if user.username == username and user.password == password:
                self.show_user_interface(user)
                return

        messagebox.showerror("Error", "Invalid username or password")

    def show_user_interface(self, user):
        self.login_frame.destroy()

        self.user = user

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        self.welcome_label = tk.Label(self.main_frame, text=f"Welcome, {self.user.username}!")
        self.welcome_label.grid(row=0, columnspan=2, pady=10)

        self.post_label = tk.Label(self.main_frame, text="Create a Post:")
        self.post_label.grid(row=1, column=0, sticky="e")
        self.post_entry = tk.Entry(self.main_frame, width=50)
        self.post_entry.grid(row=1, column=1)

        self.post_button = tk.Button(self.main_frame, text="Post", command=self.make_post)
        self.post_button.grid(row=2, columnspan=2, pady=10)

        self.posts_frame = tk.Frame(self.main_frame)
        self.posts_frame.grid(row=3, columnspan=2, pady=10)

        self.load_posts()

    def make_post(self):
        content = self.post_entry.get()
        if content:
            new_post = self.user.make_post(content)
            self.load_posts()

    def load_posts(self):
        # Clear existing posts
        for widget in self.posts_frame.winfo_children():
            widget.destroy()

        # Load posts
        for post in self.user.posts:
            post_frame = tk.Frame(self.posts_frame, bd=1, relief=tk.RIDGE)
            post_frame.pack(padx=5, pady=5, fill=tk.X)

            author_label = tk.Label(post_frame, text=f"Author: {post.author}")
            author_label.pack(anchor=tk.W)

            content_label = tk.Label(post_frame, text=post.content)
            content_label.pack(anchor=tk.W)

            comments_button = tk.Button(post_frame, text="View Comments", command=lambda p=post: self.show_comments(p))
            comments_button.pack(anchor=tk.W)

    def show_comments(self, post):
        comments_window = tk.Toplevel(self.root)
        comments_window.title("Comments")

        comments_frame = tk.Frame(comments_window)
        comments_frame.pack(padx=20, pady=20)

        for comment in post.comments:
            comment_label = tk.Label(comments_frame, text=f"{comment.author}: {comment.content}")
            comment_label.pack(anchor=tk.W)

        comment_entry = tk.Entry(comments_frame, width=50)
        comment_entry.pack(anchor=tk.W)

        comment_button = tk.Button(comments_frame, text="Comment", command=lambda: self.add_comment(post, comment_entry.get()))
        comment_button.pack(anchor=tk.W)

    def add_comment(self, post, comment_content):
        if comment_content:
            post.add_comment(self.user, comment_content)
            self.show_comments(post)
            self.load_posts()

# Initialize the tkinter GUI
root = tk.Tk()
app = SocialMediaApp(root)
root.mainloop()
