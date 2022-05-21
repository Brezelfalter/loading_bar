import sys
import time
from qt_core import * 

from qt_material import apply_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()

        self.ui = loader.load("loading_screen\main.ui", None)
        self.setCentralWidget(self.ui)

    def loading(self, total_steps : int):
        steps = total_steps // 4

        self.ui.prog_top.setMaximum(steps)
        self.ui.prog_right.setMaximum(steps)
        self.ui.prog_bottom.setMaximum(steps)
        self.ui.prog_left.setMaximum(steps)

        steps += 1

        start = time.time()

        for i in range(1, steps):
            self.ui.prog_top.setValue(i)
       
        for i in range(1, steps):
            self.ui.prog_right.setValue(i)

        for i in range(1, steps):
            self.ui.prog_bottom.setValue(i)

        for i in range(1, steps):
            self.ui.prog_left.setValue(i)

        end = time.time()
        print(end - start)

        time.sleep(0.5)

        self.ui.prog_top.setValue(0)
        self.ui.prog_right.setValue(0)
        self.ui.prog_bottom.setValue(0)
        self.ui.prog_left.setValue(0)

    def mouseDoubleClickEvent(self, event):
        # 150000 steps roughly == 1s of loading
        MainWindow.loading(self, 750000)


def run():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    win = MainWindow()

    apply_stylesheet(app, theme="dark_teal.xml")

    win.show()
    app.exec()


if __name__ == "__main__":
    run()