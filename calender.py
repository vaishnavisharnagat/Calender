import tkinter as tk
from tkinter import ttk, messagebox
import calendar
import json
import os
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

EVENT_FILE = "events.json"

today = datetime.now()
current_month = today.month
current_year = today.year

dark_mode = False


# ============================================================
# LOAD / SAVE EVENTS
# ============================================================

def load_events():
    if os.path.exists(EVENT_FILE):
        try:
            with open(EVENT_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            return {}
    return {}


events = load_events()


def save_events():
    with open(EVENT_FILE, "w", encoding="utf-8") as file:
        json.dump(events, file, indent=4)


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()
root.title("📅 Smart GUI Calendar")
root.geometry("850x700")
root.resizable(False, False)


# ============================================================
# COLORS
# ============================================================

LIGHT_BG = "#f5f5f5"
LIGHT_FG = "#222222"

DARK_BG = "#202124"
DARK_FG = "#ffffff"


# ============================================================
# HEADER
# ============================================================

title_label = tk.Label(
    root,
    text="📅 Smart Calendar",
    font=("Arial", 26, "bold")
)
title_label.pack(pady=15)


# ============================================================
# CONTROL FRAME
# ============================================================

control_frame = tk.Frame(root)
control_frame.pack(pady=5)


def previous_month():
    global current_month, current_year

    current_month -= 1

    if current_month == 0:
        current_month = 12
        current_year -= 1

    update_calendar()


def next_month():
    global current_month, current_year

    current_month += 1

    if current_month == 13:
        current_month = 1
        current_year += 1

    update_calendar()


def go_today():
    global current_month, current_year

    current_month = today.month
    current_year = today.year

    update_calendar()


previous_button = tk.Button(
    control_frame,
    text="⏮️ Previous",
    command=previous_month,
    font=("Arial", 11)
)
previous_button.grid(row=0, column=0, padx=5)


today_button = tk.Button(
    control_frame,
    text="📌 Today",
    command=go_today,
    font=("Arial", 11)
)
today_button.grid(row=0, column=1, padx=5)


next_button = tk.Button(
    control_frame,
    text="Next ⏭️",
    command=next_month,
    font=("Arial", 11)
)
next_button.grid(row=0, column=2, padx=5)


# ============================================================
# MONTH / YEAR SELECTION
# ============================================================

selection_frame = tk.Frame(root)
selection_frame.pack(pady=10)

tk.Label(
    selection_frame,
    text="Month:",
    font=("Arial", 11)
).grid(row=0, column=0, padx=5)

month_var = tk.IntVar(value=current_month)

month_combo = ttk.Combobox(
    selection_frame,
    textvariable=month_var,
    values=list(range(1, 13)),
    width=5,
    state="readonly"
)
month_combo.grid(row=0, column=1, padx=5)

tk.Label(
    selection_frame,
    text="Year:",
    font=("Arial", 11)
).grid(row=0, column=2, padx=5)

year_var = tk.IntVar(value=current_year)

year_spin = tk.Spinbox(
    selection_frame,
    from_=1900,
    to=2100,
    textvariable=year_var,
    width=6
)
year_spin.grid(row=0, column=3, padx=5)


def select_month_year():
    global current_month, current_year

    try:
        current_month = int(month_var.get())
        current_year = int(year_var.get())
        update_calendar()
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year.")


show_button = tk.Button(
    selection_frame,
    text="Show",
    command=select_month_year,
    font=("Arial", 10, "bold")
)
show_button.grid(row=0, column=4, padx=10)


# ============================================================
# CALENDAR DISPLAY
# ============================================================

calendar_frame = tk.Frame(root)
calendar_frame.pack(pady=10)

month_title = tk.Label(
    calendar_frame,
    text="",
    font=("Arial", 20, "bold")
)
month_title.pack(pady=5)

days_frame = tk.Frame(calendar_frame)
days_frame.pack()

day_buttons = []


def show_day_event(day):
    date_key = f"{current_year}-{current_month:02d}-{day:02d}"

    event = events.get(date_key, "")

    event_window = tk.Toplevel(root)
    event_window.title(f"Event - {date_key}")
    event_window.geometry("400x300")
    event_window.resizable(False, False)

    tk.Label(
        event_window,
        text=f"📅 {date_key}",
        font=("Arial", 16, "bold")
    ).pack(pady=15)

    tk.Label(
        event_window,
        text="📝 Add Note / Event:",
        font=("Arial", 11)
    ).pack()

    event_text = tk.Text(
        event_window,
        height=7,
        width=40,
        font=("Arial", 11)
    )
    event_text.pack(pady=10)

    if event:
        event_text.insert("1.0", event)

    def save_event():

        text = event_text.get("1.0", tk.END).strip()

        if text:
            events[date_key] = text
        else:
            events.pop(date_key, None)

        save_events()
        event_window.destroy()
        update_calendar()

        messagebox.showinfo(
            "Saved",
            f"Event saved for {date_key}"
        )

    tk.Button(
        event_window,
        text="💾 Save Event",
        command=save_event,
        font=("Arial", 11, "bold")
    ).pack(pady=5)


def update_calendar():

    global day_buttons

    month = current_month
    year = current_year

    month_var.set(month)
    year_var.set(year)

    month_title.config(
        text=f"{calendar.month_name[month]} {year}"
    )

    for widget in days_frame.winfo_children():
        widget.destroy()

    day_buttons = []

    # Weekday headers
    weekdays = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]

    for col, day_name in enumerate(weekdays):

        label = tk.Label(
            days_frame,
            text=day_name,
            font=("Arial", 11, "bold"),
            width=10,
            pady=8
        )

        label.grid(
            row=0,
            column=col
        )

    cal = calendar.monthcalendar(year, month)

    for row_index, week in enumerate(cal, start=1):

        for col_index, day in enumerate(week):

            if day == 0:
                label = tk.Label(
                    days_frame,
                    text="",
                    width=10,
                    height=3
                )

                label.grid(
                    row=row_index,
                    column=col_index
                )

            else:

                date_key = f"{year}-{month:02d}-{day:02d}"

                # Highlight today's date
                is_today = (
                    day == today.day
                    and month == today.month
                    and year == today.year
                )

                # Event indicator
                has_event = date_key in events

                button_text = str(day)

                if has_event:
                    button_text += "\n📝"

                button = tk.Button(
                    days_frame,
                    text=button_text,
                    width=9,
                    height=3,
                    font=("Arial", 10, "bold"),
                    command=lambda d=day: show_day_event(d)
                )

                if is_today:
                    button.config(
                        relief="solid",
                        bd=3
                    )

                button.grid(
                    row=row_index,
                    column=col_index,
                    padx=2,
                    pady=2
                )

                day_buttons.append(button)


# ============================================================
# DARK MODE
# ============================================================

def toggle_dark_mode():

    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:

        bg = DARK_BG
        fg = DARK_FG

    else:

        bg = LIGHT_BG
        fg = LIGHT_FG

    root.config(bg=bg)

    title_label.config(
        bg=bg,
        fg=fg
    )

    control_frame.config(bg=bg)
    selection_frame.config(bg=bg)
    calendar_frame.config(bg=bg)
    days_frame.config(bg=bg)

    month_title.config(
        bg=bg,
        fg=fg
    )

    for widget in control_frame.winfo_children():

        widget.config(
            bg=bg,
            fg=fg
        )

    for widget in selection_frame.winfo_children():

        if isinstance(widget, tk.Label):

            widget.config(
                bg=bg,
                fg=fg
            )


dark_button = tk.Button(
    root,
    text="🎨 Dark Mode",
    command=toggle_dark_mode,
    font=("Arial", 11)
)
dark_button.pack(pady=5)


# ============================================================
# YEARLY CALENDAR
# ============================================================

def show_yearly_calendar():

    year = int(year_var.get())

    yearly_window = tk.Toplevel(root)

    yearly_window.title(
        f"🗓️ Yearly Calendar - {year}"
    )

    yearly_window.geometry("1000x750")

    text = tk.Text(
        yearly_window,
        font=("Courier New", 9),
        width=110,
        height=40
    )

    text.pack(
        padx=10,
        pady=10
    )

    yearly_calendar = calendar.TextCalendar(
        firstweekday=0
    )

    text.insert(
        "1.0",
        yearly_calendar.formatyear(
            year,
            2,
            1,
            1,
            3
        )
    )

    text.config(
        state="disabled"
    )


year_button = tk.Button(
    root,
    text="🗓️ Yearly Calendar",
    command=show_yearly_calendar,
    font=("Arial", 11)
)
year_button.pack(pady=5)


# ============================================================
# REMINDER CHECK
# ============================================================

def check_reminders():

    date_key = (
        f"{today.year}-{today.month:02d}-{today.day:02d}"
    )

    if date_key in events:

        messagebox.showinfo(
            "🔔 Today's Reminder",
            events[date_key]
        )

    root.after(
        60000,
        check_reminders
    )


# ============================================================
# START APPLICATION
# ============================================================

root.config(bg=LIGHT_BG)

update_calendar()

root.after(
    1000,
    check_reminders
)

root.mainloop()