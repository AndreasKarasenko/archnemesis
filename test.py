from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.Qt import Qt
import sys

from archnemesis_recipes import *


def main():
    app     = QtWidgets.QApplication(sys.argv)
    tree    = QtWidgets.QTreeWidget()
    headerItem  = QtWidgets.QTreeWidgetItem()
    item    = QtWidgets.QTreeWidgetItem()


    for i in tier4:
        parent = QtWidgets.QTreeWidgetItem(tree)
        parent.setText(0, "{}".format(i.name))
        parent.setFlags(parent.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
        # only applies to the first backward layer.
        # usually each x has at least one more backward layer.
        # TODO substitute next 6 lines with a recursive call
        if i.backward is not None:
            for x in i.backward:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                child.setText(0, "{}".format(x.name))
                child.setCheckState(0, Qt.Unchecked)
    tree.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

# for j in tier1:
#     print(j.backward is not None)

