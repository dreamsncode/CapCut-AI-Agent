import pyautogui, time, os, subprocess
import pygetwindow as gw

FPS = 30  # Adjust if needed
CAPCUT_EXE = r"C:\Program Files\CapCut\CapCut.exe"
BOOT_DELAY = 10

def yn(q):
    return input(f"{q} (y/n): ").strip().lower().startswith("y")

def frames(hours, minutes, seconds, frm):
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds * FPS + frm

def split_here():
    pyautogui.hotkey('ctrl', 'b'); time.sleep(0.3)

def nudge(frames_fwd):
    for _ in range(frames_fwd):
        pyautogui.press('right'); time.sleep(0.01)

def delete_range(start_f, end_f):
    pyautogui.press('home'); time.sleep(0.2)
    nudge(start_f)
    split_here()
    nudge(end_f - start_f)
    split_here()
    pyautogui.press('left', presses=3, interval=0.15)
    pyautogui.click(); time.sleep(0.2)
    pyautogui.press('delete'); time.sleep(0.3)

def focus_capcut():
    for win in gw.getWindowsWithTitle("CapCut"):
        try:
            win.activate()
            print("✅ Focused CapCut window.")
            return True
        except:
            continue
    print("❌ Couldn't find CapCut window.")
    return False

# ─── Questions ───
is_open = yn("Is CapCut already open?")
want_delete = yn("Do you want to delete any clip sections?")

delete_jobs = []
while want_delete:
    print("\nEnter time to delete:")
    h1 = int(input("  START hours         : "))
    m1 = int(input("  START minutes       : "))
    s1 = int(input("  START seconds       : "))
    f1 = int(input("  START frames (0–29) : "))
    h2 = int(input("  END hours           : "))
    m2 = int(input("  END minutes         : "))
    s2 = int(input("  END seconds         : "))
    f2 = int(input("  END frames (0–29)   : "))
    delete_jobs.append([frames(h1, m1, s1, f1), frames(h2, m2, s2, f2)])
    want_delete = yn("Add another section?")

# ─── Launch or Focus CapCut ───
if not is_open:
    print("Opening CapCut…")
    subprocess.Popen([CAPCUT_EXE])
    time.sleep(BOOT_DELAY)
else:
    focused = focus_capcut()
    if not focused:
        print("⚠️ Please switch to CapCut manually.")

# ─── Execute deletions ───
print("\n▶ Starting in 5 s…")
time.sleep(5)

for start, end in sorted(delete_jobs, key=lambda x: x[0], reverse=True):
    delete_range(start, end)
    print(f"✅ Deleted {start/FPS:.2f}s–{end/FPS:.2f}s")

print("\n🏁 ALL DONE – review your timeline!")

