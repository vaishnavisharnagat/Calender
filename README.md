# 📅 Smart GUI Calendar

A simple and interactive **Smart GUI Calendar** built using **Python and Tkinter**. The application allows users to navigate between months, add events and notes, save events locally, highlight today's date, switch to dark mode, and view a complete yearly calendar.

## ✨ Features

* 📅 Monthly calendar view
* ⏮️ Previous Month navigation
* ⏭️ Next Month navigation
* 📌 Go to Today's date
* 📝 Add and save notes/events
* 💾 Automatically save events in JSON
* 🔔 Daily event reminder
* 🎨 Light Mode and Dark Mode
* 🗓️ Yearly calendar view
* 📆 Select month and year
* 🖥️ User-friendly Tkinter interface
* ⚡ Lightweight and easy to run

## 🛠️ Technologies Used

* 🐍 **Python 3**
* 🖥️ **Tkinter** – GUI development
* 📅 **Calendar** – Calendar generation
* 💾 **JSON** – Event storage
* 🕐 **Datetime** – Date and time handling
* 📁 **OS** – File management

## 📂 Project Structure

```text
Smart-GUI-Calendar/
│
├── calendar_gui.py
├── events.json
└── README.md
```

> `events.json` is automatically created when you save your first event.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/smart-gui-calendar.git
```

### 2. Open the Project Folder

```bash
cd smart-gui-calendar
```

### 3. Check Python Installation

```bash
python --version
```

Python 3.x is recommended.

### 4. Run the Application

```bash
python calendar_gui.py
```

No external packages are required because the project uses Python's built-in libraries.

## 🖥️ How to Use

### 📅 View Calendar

When the application starts, it automatically displays the current month and year.

### ⏮️ Previous Month

Click:

```text
⏮️ Previous
```

to move to the previous month.

### ⏭️ Next Month

Click:

```text
Next ⏭️
```

to move to the next month.

### 📌 Today

Click:

```text
📌 Today
```

to return to the current month and year.

### 📆 Select Month and Year

Select a month from the dropdown and enter the required year.

Click:

```text
Show
```

to display the selected month.

## 📝 Add Events and Notes

Click any date on the calendar.

A window will open where you can enter an event or note.

Example:

```text
📅 2026-08-25

📝 Add Note / Event:

Project Submission
```

Click:

```text
💾 Save Event
```

The event will be saved automatically.

## 💾 Event Storage

Events are stored in an `events.json` file.

Example:

```json
{
    "2026-08-25": "Project Submission",
    "2026-08-30": "College Presentation"
}
```

This allows events to remain saved even after closing the application.

## 🔔 Event Reminder

The application automatically checks for events scheduled for the current date.

If an event exists, a reminder message is displayed:

```text
🔔 Today's Reminder

Project Submission
```

## 📌 Today's Date Highlight

The current date is automatically detected and highlighted with a border on the calendar.

For example:

```text
      August 2026

Mon Tue Wed Thu Fri Sat Sun
                 1   2
 3   4   5   6   7   8   9
10  11  12  13  14  15  16
17  18  19  20  21  22  23
24  25  26  27  28  29  30
31
```

## 🎨 Dark Mode

The application includes a Dark Mode option.

Click:

```text
🎨 Dark Mode
```

to switch the interface to a dark theme.

Click it again to return to the light theme.

## 🗓️ Yearly Calendar

Click:

```text
🗓️ Yearly Calendar
```

to open a complete yearly calendar.

The yearly view displays all 12 months of the selected year.

## 📊 Application Workflow

```text
Start Application
       ↓
Display Current Month
       ↓
Select Date
       ↓
Add Event / Note
       ↓
Save Event
       ↓
Store in events.json
       ↓
Display 📝 on Event Date
       ↓
Check Today's Events
       ↓
Show Reminder
```

## 🎯 Project Objectives

The main objectives of this project are:

* Learn Python GUI development.
* Understand Tkinter widgets.
* Work with dates and calendars.
* Implement event handling.
* Store data using JSON.
* Build a simple desktop application.
* Implement dark mode.
* Create monthly and yearly calendar views.

## 📚 Learning Outcomes

By completing this project, you can learn:

* Python functions
* Global variables
* Tkinter GUI programming
* Buttons and labels
* Combobox and Spinbox
* Text widgets
* Event handling
* JSON file handling
* Date and time operations
* Calendar module
* Basic application design

## 🚀 Future Improvements

The project can be extended with:

1. 🔔 Advanced notification system
2. ⏰ Custom reminder times
3. 📱 Mobile application
4. ☁️ Cloud event synchronization
5. 👥 Multiple user accounts
6. 🔄 Recurring events
7. 🎨 More themes
8. 📤 Export calendar to PDF
9. 📧 Email reminders
10. 🔍 Event search functionality

## 🤝 Contributing

Contributions are welcome!

1. Fork this repository.
2. Create a new branch:

```bash
git checkout -b feature/new-feature
```

3. Make your changes.
4. Commit your changes:

```bash
git commit -m "Add new feature"
```

5. Push your changes:

```bash
git push origin feature/new-feature
```

6. Create a Pull Request.

## 📄 License

This project is open-source and available under the **MIT License**.

## 👩‍💻 Author

**Vaishnavi Sharnagat**

B.E. Information Technology Student

## ⭐ Support

If you like this project, don't forget to ⭐ **Star the repository!**

```text
⭐ Star the repository
🍴 Fork the project
🐛 Report issues
💡 Suggest improvements
```
