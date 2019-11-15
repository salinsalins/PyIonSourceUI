import sys

import taurus
from taurus.external.qt import Qt
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.panel import TaurusModelChooser

from taurus.qt.qtgui.display import TaurusLabel, TaurusLed, LedStatus
from taurus.qt.qtgui.input import TaurusValueLineEdit, TaurusValueCheckBox, TaurusWheelEdit, TaurusValueSpinBox


app = TaurusApplication(sys.argv, cmd_line_parser=None)
panel = Qt.QWidget()
layout = Qt.QHBoxLayout()
panel.setLayout(layout)


#TaurusModelChooser() #
w1 = TaurusLabel()
w2 = TaurusLed()
w3 = TaurusValueCheckBox()   # or TaurusValueSpinBox or TaurusWheelEdit
w4 = TaurusLabel()
layout.addWidget(w1)
layout.addWidget(w2)
layout.addWidget(w3)
layout.addWidget(w4)
w1.model, w1.bgRole = 'ET7000_server/test/1/do00#label', ''
w2.model = 'ET7000_server/test/1/do00'
w3.model = 'ET7000_server/test/1/do00'
w4.model, w4.bgRole = 'ET7000_server/test/1/do00#rvalue.units', ''

#my_db = taurus.Authority()
#my_device = taurus.Device('ET7000_server/test/1')

panel.show()
sys.exit(app.exec_())