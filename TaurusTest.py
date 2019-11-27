import sys
from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication

app = TaurusApplication(sys.argv, cmd_line_parser=None,)
panel = Qt.QWidget()
layout = Qt.QHBoxLayout()
panel.setLayout(layout)

from taurus.qt.qtgui.display import TaurusLabel
w = TaurusLabel()
layout.addWidget(w)
w.model = 'ET7000_server/test/1/ai00'

panel.show()
sys.exit(app.exec_())
