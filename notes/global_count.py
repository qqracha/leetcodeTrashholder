"""
Пример работы global
"""

click_count = 0
def handle_click():
    global click_count
    click_count += 1
    print(f"Click! Count = {click_count}")

def view_click():
    global click_count
    print(f"Now count click is {click_count}!")

for i in range(5):
    handle_click()

view_click()