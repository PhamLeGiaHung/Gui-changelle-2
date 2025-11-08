from guizero import App, Box, Text, PushButton

# Biến trạng thái ban đầu
state = "Red"
cooldown = 10

def change_light():
    global state
    if state == "Red":
        btn1.bg = "red"
        btn2.bg = "gray"
        btn3.bg = "gray"
        state = "Yellow"  # chuyển sang vàng sau đó
    elif state == "Yellow":
        btn1.bg = "gray"
        btn2.bg = "yellow"
        btn3.bg = "gray"
        state = "Green"
    elif state == "Green":
        btn1.bg = "gray"
        btn2.bg = "gray"
        btn3.bg = "green"
        state = "Red"

def countdown():
    global cooldown
    cooldown -= 1
    text2.value = f'Chuyển sau: {cooldown}s nữa'
    
    if cooldown <= 0:
        cooldown = 10
        text2.value = f'Chuyển sau: {cooldown}s nữa'
        change_light()
    
    # Gọi lại chính nó sau 1 giây
    app.after(1000, countdown)

# --- Giao diện ---
app = App(title="Đèn giao thông", width=200, height=300)
text = Text(app, text="🚦 Trụ đèn giao thông", size=14)

box = Box(app)
btn1 = PushButton(box, text="", width=10, height=5)
btn2 = PushButton(box, text="", width=10, height=5)
btn3 = PushButton(box, text="", width=10, height=5)

text2 = Text(app, text=f'Chuyển sau: {cooldown}s nữa')

# Bắt đầu
change_light()
app.after(1000, countdown)
app.display()
