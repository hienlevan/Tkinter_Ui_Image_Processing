from define import *


class App():
    def __init__(self, window) -> None:
        # Thiết lập Width Height
        window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT,
                        WINDOW_POSITION_RIGHT, WINDOW_POSITION_DOWN))
        # Title
        window.title("Project xử lý ảnh")

        # Thay đổi Icon
        window.iconbitmap(os.path.join(PATH_IMAGE, 'logo.ico'))

        # Background
        # window['bg'] = COLOR_BACKGROUND
        # window.resizable(False, False)
