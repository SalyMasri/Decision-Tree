import dtree
import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QScrollArea

class MyPainting(QWidget):
    def __init__(self, tree):
        super().__init__()
        self.tree = tree
        self.xsize = 3000  # Large enough width to fit wide trees
        self.ysize = 1500  # Large enough height to fit deep trees

    def sizeHint(self):
        """Dynamically adjust window size based on tree structure."""
        return QtCore.QSize(self.xsize, self.ysize)

    def paintEvent(self, ev):
        """Handles tree rendering."""
        p = QtGui.QPainter()
        p.begin(self)
        p.setPen(QtGui.QPen(QtGui.QColor(0, 0, 0), 1))
        draw(p, self.tree, 50, 50)  # Increased margin for large trees
        p.end()

def draw(p, t, x, y):
    """Recursively draw tree nodes."""
    if isinstance(t, dtree.TreeLeaf):
        p.drawText(x - 3, y + 15, 'T' if t.cvalue else 'F')
        return x, x + 100
    xx = x
    anchors = []
    for b in t.branches:
        mid, xx = draw(p, t.branches[b], xx, y + 100)  # Increase Y distance for readability
        p.drawText(mid - 3, y + 98, str(b))
        anchors.append(mid)
    newMid = (x + xx) / 2
    p.drawText(newMid - 7, y + 20, t.attribute.name)
    p.drawEllipse(newMid - 15, y, 30, 30)  # Bigger ellipse for visibility
    for m in anchors:
        p.drawLine(newMid, y + 30, m, y + 100)
    return newMid, xx + 100

class MyMainWindow(QMainWindow):
    def __init__(self, tree, save_image=False, image_filename="tree_image.png"):
        super().__init__()
        self.tree = tree

        # Scroll Area setup
        self.scroll_area = QScrollArea(self)  # Enable scrolling
        self.paint = MyPainting(self.tree)
        self.scroll_area.setWidget(self.paint)
        self.scroll_area.setWidgetResizable(True)  # Adjust to widget size

        self.setCentralWidget(self.scroll_area)  # Attach scrollable widget
        self.resize(1600, 900)  # Set initial window size

        self.show()

        if save_image:
            QtCore.QTimer.singleShot(500, lambda: self.save_tree_image(image_filename))

    def save_tree_image(self, filename):
        """Capture the full tree visualization and save as PNG."""
        pixmap = QtGui.QPixmap(self.paint.sizeHint())  # Capture full widget
        self.paint.render(pixmap)  # Render full tree
        pixmap.save(filename, "PNG")  # Save as PNG
        print(f"✅ Tree image saved as {filename}")

def drawTree(tree, save_image=False, filename="tree_image.png"):
    """Displays and optionally saves the decision tree."""
    application = QApplication(sys.argv)
    win = MyMainWindow(tree, save_image=save_image, image_filename=filename)
    win.show()
    sys.exit(application.exec_())
