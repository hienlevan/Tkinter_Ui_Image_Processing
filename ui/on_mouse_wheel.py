
def on_mouse_wheel(event, canvas):
    # Kiểm tra xem phím Ctrl có được giữ hay không
    if not event.state & 0x0004:
        return

    # Lấy tọa độ hiện tại của con trỏ chuột
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)

    # Phóng to/thu nhỏ ảnh
    if event.delta > 0:
        canvas.scale("image", x, y, 1.1, 1.1)
    else:
        canvas.scale("image", x, y, 0.9, 0.9)


def on_left_button_down(event, canvas):
    # Lưu trữ tọa độ hiện tại của con trỏ chuột
    canvas.scan_mark(event.x, event.y)


def on_mouse_move(event, canvas):
    # Di chuyển hình ảnh
    canvas.scan_dragto(event.x, event.y, gain=1)
