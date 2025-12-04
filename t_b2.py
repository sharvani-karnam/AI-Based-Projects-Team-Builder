import customtkinter as ctk
import pandas as pd
from tkinter import messagebox

# ---------- APP SETTINGS ----------
ctk.set_appearance_mode("light")  # "dark" or "light"
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🤖 AI-Based Project Team Builder - BotVana")
app.geometry("900x700")

students = []

# ---------- MAIN LOGIC ----------

def add_student():
    """Add student details to memory."""
    name = name_entry.get()
    try:
        skill = float(skill_entry.get())
        rank = float(rank_entry.get())
        eff = float(eff_entry.get())
        avail = float(avail_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Enter valid numeric scores (1–10).")
        return

    if not name:
        messagebox.showerror("Error", "Name cannot be empty!")
        return

    students.append({
        "Name": name,
        "Skill": skill,
        "Rank": rank,
        "Efficiency": eff,
        "Availability": avail
    })

    name_entry.delete(0, "end")
    skill_entry.delete(0, "end")
    rank_entry.delete(0, "end")
    eff_entry.delete(0, "end")
    avail_entry.delete(0, "end")

    messagebox.showinfo("Added", f"{name} added successfully!")
    refresh_status()


def calculate_score(student):
    """Weighted AI logic to calculate total performance score."""
    return (0.3 * student["Skill"] +
            0.25 * student["Rank"] +
            0.25 * student["Efficiency"] +
            0.2 * student["Availability"])


def form_teams():
    """Create balanced teams ensuring each has one high scorer (≥7)."""
    if not students:
        messagebox.showwarning("Warning", "No students added!")
        return

    df = pd.DataFrame(students)
    df["Score"] = df.apply(calculate_score, axis=1)
    df = df.sort_values(by="Score", ascending=False).reset_index(drop=True)

    team_size = int(team_size_var.get())

    high = df[df["Score"] >= 7].values.tolist()
    low = df[df["Score"] < 7].values.tolist()

    teams = []
    team_index = 0

    while high or low:
        team = []
        # Add one high scorer if available
        if high:
            team.append(high.pop(0))
        # Fill remaining with low scorers or next high scorers
        while len(team) < team_size and (low or high):
            if low:
                team.append(low.pop(0))
            elif high:
                team.append(high.pop(0))
        teams.append(team)
        team_index += 1

    # Display results
    result_box.configure(state="normal")
    result_box.delete("1.0", "end")

    for i, team in enumerate(teams):
        result_box.insert("end", f"\nTEAM {i+1}\n")
        total_score = 0
        for member in team:
            result_box.insert("end", f"{member[0]} - Score: {member[-1]:.2f}\n")
            total_score += member[-1]
        avg_score = total_score / len(team)
        result_box.insert("end", f"→ Avg Score: {avg_score:.2f}\n{'-'*40}\n")

    result_box.configure(state="disabled")


def export_csv():
    """Export results to CSV."""
    if not students:
        messagebox.showwarning("Warning", "No data to export!")
        return
    df = pd.DataFrame(students)
    df["Score"] = df.apply(calculate_score, axis=1)
    df.to_csv("AI_Based_Team_Builder_Results.csv", index=False)
    messagebox.showinfo("Exported", "Data exported as AI_Based_Team_Builder_Results.csv")


def reset_data():
    """Clear all data."""
    students.clear()
    result_box.configure(state="normal")
    result_box.delete("1.0", "end")
    result_box.configure(state="disabled")
    refresh_status()
    messagebox.showinfo("Reset", "All student data cleared!")


def refresh_status():
    """Update student count display."""
    status_label.configure(text=f"🧑‍💻 Students Added: {len(students)}")


# ---------- GUI DESIGN ----------

title = ctk.CTkLabel(app, text="AI-Based Project Team Builder", font=ctk.CTkFont(size=24, weight="bold"))
title.pack(pady=15)

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=10, fill="x")

# Inputs
ctk.CTkLabel(frame, text="Name:").grid(row=0, column=0, padx=10, pady=8)
name_entry = ctk.CTkEntry(frame, width=180)
name_entry.grid(row=0, column=1)

ctk.CTkLabel(frame, text="Skill (1–10):").grid(row=0, column=2, padx=10)
skill_entry = ctk.CTkEntry(frame, width=80)
skill_entry.grid(row=0, column=3)

ctk.CTkLabel(frame, text="Rank (1–10):").grid(row=1, column=0, padx=10)
rank_entry = ctk.CTkEntry(frame, width=80)
rank_entry.grid(row=1, column=1)

ctk.CTkLabel(frame, text="Efficiency (1–10):").grid(row=1, column=2, padx=10)
eff_entry = ctk.CTkEntry(frame, width=80)
eff_entry.grid(row=1, column=3)

ctk.CTkLabel(frame, text="Availability (1–10):").grid(row=2, column=0, padx=10)
avail_entry = ctk.CTkEntry(frame, width=80)
avail_entry.grid(row=2, column=1)

add_btn = ctk.CTkButton(frame, text="Add Student", command=add_student)
add_btn.grid(row=2, column=3, padx=10, pady=8)

# Team settings
team_frame = ctk.CTkFrame(app, corner_radius=15)
team_frame.pack(padx=20, pady=10, fill="x")

ctk.CTkLabel(team_frame, text="Select Team Size:").grid(row=0, column=0, padx=10, pady=10)
team_size_var = ctk.StringVar(value="4")
ctk.CTkOptionMenu(team_frame, variable=team_size_var, values=["2", "3", "4", "5"]).grid(row=0, column=1, padx=10)

ctk.CTkButton(team_frame, text="Generate Teams", fg_color="#007acc", command=form_teams).grid(row=0, column=2, padx=15)
ctk.CTkButton(team_frame, text="Export CSV", fg_color="#4caf50", command=export_csv).grid(row=0, column=3, padx=15)
ctk.CTkButton(team_frame, text="Reset", fg_color="#d9534f", command=reset_data).grid(row=0, column=4, padx=15)

# Results
result_frame = ctk.CTkFrame(app, corner_radius=15)
result_frame.pack(padx=20, pady=10, fill="both", expand=True)

result_box = ctk.CTkTextbox(result_frame, font=("Consolas", 12))
result_box.pack(padx=10, pady=10, fill="both", expand=True)
result_box.configure(state="disabled")

status_label = ctk.CTkLabel(app, text="🧑‍💻 Students Added: 0", font=ctk.CTkFont(size=13))
status_label.pack(pady=5)

footer = ctk.CTkLabel(app, text="Developed by Team BotVana | AI-ML F Section", font=ctk.CTkFont(size=12, slant="italic"))
footer.pack(pady=5)

app.mainloop()
