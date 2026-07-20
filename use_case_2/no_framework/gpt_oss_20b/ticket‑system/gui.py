import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import datetime

API_BASE = "http://127.0.0.1:8000"

# ---------- Helper ----------
def api_post(endpoint, data):
    r = requests.post(f"{API_BASE}{endpoint}", json=data)
    r.raise_for_status()
    return r.json()

def api_get(endpoint):
    r = requests.get(f"{API_BASE}{endpoint}")
    r.raise_for_status()
    return r.json()

# ---------- Main Window ----------
class TicketApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Campus Ticket System")
        self.geometry("800x600")
        self.user_id = None
        self.role = None
        self.ticket_frames = {}
        self.build_login()

    # -------------------- Login --------------------
    def build_login(self):
        self.clear_frames()
        frm = ttk.Frame(self)
        frm.pack(expand=True)
        ttk.Label(frm, text="Login (no auth, just pick a role)").grid(row=0, column=0, columnspan=2, pady=10)
        ttk.Button(frm, text="Simple User", command=lambda: self.set_user('simple')).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(frm, text="Helpdesk Staff", command=lambda: self.set_user('helpdesk')).grid(row=1, column=1, padx=5, pady=5)

    def set_user(self, role):
        # Create a dummy user row (id autoincrement)
        user_resp = api_post("/tickets/", {"user_id":1, "category":"", "description":""})  # we will ignore the ticket
        self.user_id = user_resp["id"]
        self.role = role
        self.build_dashboard()

    # -------------------- Dashboard --------------------
    def build_dashboard(self):
        self.clear_frames()
        self.menu_frame = ttk.Frame(self, relief=tk.RIDGE)
        self.menu_frame.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(self.menu_frame, text="New Ticket", command=self.new_ticket_window).pack(side=tk.LEFT, padx=5)
        ttk.Button(self.menu_frame, text="Refresh", command=self.refresh_tickets).pack(side=tk.LEFT, padx=5)
        if self.role == 'helpdesk':
            ttk.Button(self.menu_frame, text="Analytics", command=self.analytics_window).pack(side=tk.LEFT, padx=5)

        self.tickets_container = ttk.Frame(self)
        self.tickets_container.pack(fill=tk.BOTH, expand=True)
        self.refresh_tickets()

    def clear_frames(self):
        for child in self.winfo_children():
            child.destroy()

    def refresh_tickets(self):
        for frame in self.ticket_frames.values():
            frame.destroy()
        self.ticket_frames.clear()

        # Decide which endpoint to call
        if self.role == 'helpdesk':
            endpoint = "/tickets/"
        else:
            endpoint = "/tickets/"

        # For demo we fetch all tickets. In production filter by status.
        r = requests.get(f"{API_BASE}{endpoint}")
        tickets = r.json() if isinstance(r.json(), list) else [r.json()]

        for ticket in tickets:
            self.add_ticket_frame(ticket)

    def add_ticket_frame(self, ticket):
        frame = ttk.Frame(self.tickets_container, relief=tk.GROOVE, borderwidth=2)
        frame.pack(fill=tk.X, padx=5, pady=5)
        self.ticket_frames[ticket['id']] = frame

        lbl = ttk.Label(frame, text=f"Ticket #{ticket['id']} | {ticket['status']} | {ticket['category']}")
        lbl.pack(side=tk.TOP, anchor='w')
        ttk.Label(frame, text=ticket['description']).pack(anchor='w')
        ttk.Button(frame, text="Open", command=lambda t=ticket: self.ticket_window(t)).pack(side=tk.RIGHT, padx=5)

    # -------------------- Ticket Window --------------------
    def ticket_window(self, ticket):
        win = tk.Toplevel(self)
        win.title(f"Ticket #{ticket['id']}")
        win.geometry("500x400")
        ttk.Label(win, text=f"Status: {ticket['status']}").pack(anchor='w')
        ttk.Label(win, text=f"Category: {ticket['category']}").pack(anchor='w')
        ttk.Label(win, text=f"Description:").pack(anchor='w')
        ttk.Label(win, text=ticket['description']).pack(anchor='w')
        ttk.Label(win, text="Messages:").pack(anchor='w')
        msg_box = scrolledtext.ScrolledText(win, height=10)
        msg_box.pack(fill=tk.BOTH, expand=True)
        # fetch messages
        m_resp = api_get(f"/tickets/{ticket['id']}/")
        for msg in m_resp.get('messages', []):
            ts = msg['ts']
            msg_box.insert(tk.END, f"[{ts}] User {msg['sender_id']}: {msg['content']}\n")
        # Input new message
        txt = tk.Text(win, height=3)
        txt.pack(fill=tk.X, padx=5, pady=5)
        def send_msg():
            content = txt.get("1.0", tk.END).strip()
            if content:
                api_post("/messages/", {
                    "ticket_id": ticket['id'],
                    "sender_id": self.user_id,
                    "content": content
                })
                txt.delete("1.0", tk.END)
                # refresh message list
                m_resp = api_get(f"/tickets/{ticket['id']}/")
                msg_box.delete('1.0', tk.END)
                for msg in m_resp.get('messages', []):
                    ts = msg['ts']
                    msg_box.insert(tk.END, f"[{ts}] User {msg['sender_id']}: {msg['content']}\n")
        ttk.Button(win, text="Send", command=send_msg).pack()
        # If helpdesk, show status changer
        if self.role == 'helpdesk':
            ttk.Label(win, text="Change status:").pack(anchor='w')
            var = tk.StringVar(value=ticket['status'])
            ttk.Combobox(win, textvariable=var, values=['open','active','closed']).pack(anchor='w')
            def change():
                new = var.get()
                api_post(f"/tickets/{ticket['id']}/status/", {"status": new})
                win.destroy()
                self.refresh_tickets()
            ttk.Button(win, text="Apply", command=change).pack(anchor='w')

    # -------------------- New Ticket Window --------------------
    def new_ticket_window(self):
        win = tk.Toplevel(self)
        win.title("New Ticket")
        ttk.Label(win, text="Category:").pack(anchor='w')
        cat_var = tk.StringVar(value="facility")
        ttk.Combobox(win, textvariable=cat_var, values=[
            "facility", "technical", "services"
        ]).pack(anchor='w')
        ttk.Label(win, text="Description:").pack(anchor='w')
        txt = tk.Text(win, height=5)
        txt.pack(fill=tk.X, padx=5, pady=5)
        def submit():
            desc = txt.get("1.0", tk.END).strip()
            if desc:
                api_post("/tickets/", {
                    "user_id": self.user_id,
                    "category": cat_var.get(),
                    "description": desc
                })
                win.destroy()
                self.refresh_tickets()
        ttk.Button(win, text="Submit", command=submit).pack(pady=5)

    # -------------------- Analytics Window --------------------
    def analytics_window(self):
        win = tk.Toplevel(self)
        win.title("Analytics")
        ttk.Label(win, text="Select Period (days):").pack(anchor='w')
        period_var = tk.IntVar(value=7)
        ttk.Entry(win, textvariable=period_var).pack(anchor='w')
        def show_open_unclosed():
            days = period_var.get()
            resp = api_get(f"/analytics/open-unclosed/{days}")
            messagebox.showinfo("Open & Unclosed", f"Open tickets in last {days} days: {resp['open_unclosed']}")
        ttk.Button(win, text="Open & Unclosed", command=show_open_unclosed).pack(pady=5)

        def show_avg_resolution():
            resp = api_get("/analytics/avg-resolution")
            txt = "\n".join([f"{row['month']} : {row['resolution']:.2f} hrs" for row in resp])
            messagebox.showinfo("Avg. Resolution", txt)
        ttk.Button(win, text="Avg. Resolution", command=show_avg_resolution).pack(pady=5)

        def show_active_cluster():
            resp = api_get("/analytics/active-cluster")
            txt = "\n".join([f"{k}: {v}" for k,v in resp.items()])
            messagebox.showinfo("Active Ticket Cluster", txt)
        ttk.Button(win, text="Active Ticket Cluster", command=show_active_cluster).pack(pady=5)

# ---------- Run ----------
if __name__ == "__main__":
    app = TicketApp()
    app.mainloop()