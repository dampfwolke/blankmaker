from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PySide6.QtWidgets import QTabWidget


class AnimatedTabHelper:
    def __init__(self, tabwidget: QTabWidget):
        self.tabwidget = tabwidget
        self.current_index = tabwidget.currentIndex()
        self.tabwidget.currentChanged.connect(self._animate_tab_change)

        self.anim_old = None
        self.anim_new = None

    def _animate_tab_change(self, neuer_index):
        if neuer_index == self.current_index:
            return

        richtung = 1 if neuer_index > self.current_index else -1

        alt_widget = self.tabwidget.widget(self.current_index)
        neu_widget = self.tabwidget.widget(neuer_index)

        w = self.tabwidget.width()

        # Positioniere das neue Widget seitlich, ohne Layout zu stören
        neu_widget.move(richtung * w, 0)
        neu_widget.show()

        # Animation für das alte (verschwindende) Widget
        self.anim_old = QPropertyAnimation(alt_widget, b"pos")
        self.anim_old.setDuration(1300)
        self.anim_old.setStartValue(alt_widget.pos())
        self.anim_old.setEndValue(QPoint(-richtung * w, 0))
        self.anim_old.setEasingCurve(QEasingCurve.OutCubic)

        # Animation für das neue (kommende) Widget
        self.anim_new = QPropertyAnimation(neu_widget, b"pos")
        self.anim_new.setDuration(1000)
        self.anim_new.setStartValue(QPoint(richtung * w, 0))
        self.anim_new.setEndValue(QPoint(0, 0))
        self.anim_new.setEasingCurve(QEasingCurve.OutCubic)
        #self.anim_new.setEasingCurve(QEasingCurve.OutInExpo)

        self.anim_old.start()
        self.anim_new.start()

        self.current_index = neuer_index

