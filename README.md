# 🎬 CapCut AI Agent – Python Automation Toolkit

🚀 A Python-based automation system to enhance CapCut editing using keyboard & screen actions via **PyAutoGUI**.

This is part of a modular AI Agent project that aims to automate tasks like:
- Opening CapCut
- Deleting specific video sections
- B-roll marker (Coming soon)

---

## 🔧 Current Modules

### 1. `open_capcut.py`  
📂 *Launches CapCut automatically from your system.*

- Opens CapCut from the default install location.
- Built for 345x485 window resolution.
- Uses `pyautogui` for mouse movement & clicks.

**Run it with:**
```bash
python open_capcut.py
```
### 2. Capcut_split_and_delete.py
📂 Deletes specific sections of a clip based on timecodes.

- Prompts for start and end times in hours:minutes:seconds:frames

- Navigates using right key, splits using Ctrl+B

- Deletes the selected range

- Accepts multiple delete ranges
 ```bash
python Capcut_split_and_delete.py
```
## 📦 Python Dependencies
  Install the required Python packages: 
  
```bash
pip install pyautogui pygetwindow
```
Package	Purpose
pyautogui :-	Simulates mouse clicks and key presses for CapCut UI
pygetwindow :-	Finds and focuses the CapCut window automatically

##📁 File Structure

CapCut-AI-Agent/
├── open_capcut.py             # Script to auto-launch CapCut

├── Capcut_split_and_delete.py # Script to delete clips by time range

├── README.md                  # Project overview

🔜 Upcoming Modules
- capcut_broll_marker.py – Marks silence spots for B-roll placement
