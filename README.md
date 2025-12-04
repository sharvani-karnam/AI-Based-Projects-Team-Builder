# 🤖 AI-Based Project Team Builder (BotVana)

A modern desktop application that uses an AI-driven weighted scoring algorithm to automatically form balanced project teams. Built with Python and CustomTkinter for a sleek, user-friendly interface.

## 🧠 The "AI" Logic
This tool moves beyond random selection. It uses a **Rule-Based Heuristic Algorithm** to quantify student potential:
1.  **Weighted Scoring:** Calculates a "Performance Index" for each student based on specific weights:
    * Skill (30%)
    * Rank (25%)
    * Efficiency (25%)
    * Availability (20%)
2.  **Greedy Optimization:** Sorts students by their scores and uses a distribution algorithm to ensure every team gets a "High Performer" (Leader) while balancing the remaining skill levels evenly.

## ✨ Key Features
* **Modern GUI:** Built with `CustomTkinter` for a professional dark/light mode interface.
* **Dynamic Team Sizing:** Users can select team sizes of 2, 3, 4, or 5 members.
* **Data Export:** Saves the generated team structures and detailed scores directly to a CSV file.
* **Smart Validation:** Prevents errors by ensuring inputs are within the valid 1-10 scale.

## 🛠️ Tech Stack
* **Language:** Python 3.14
* **GUI Framework:** CustomTkinter
* **Data Handling:** Pandas

## 🚀 How to Run
1.  Install the required libraries:
    ```bash
    pip install customtkinter pandas
    ```
2.  Run the application:
    ```bash
    python team_builder.py
    ```

---
*Created by Sharvani Karnam - B.Tech AIML*
