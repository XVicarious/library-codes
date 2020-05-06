# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
__license__   = 'GPL v3'
__copyright__ = '2015,2016,2017,2018,2019 DaltonST <DaltonShiTzu@outlook.com>'
__my_version__ = "1.0.42"  # Technical changes after Python 3.8 testing with Calibre 4.99.2

from PyQt5.Qt import Qt,QRect,QPoint,QSize,QImage,QColor,QPainter,QWidget,QDialog,QVBoxLayout

from itertools import cycle

DEFAULT_COLORS = [0x3366cc, 0xdc3912, 0xff9900, 0x109618, 0x990099,
                  0x0099c6, 0xdd4477, 0x66aa00, 0xb82e2e, 0x316395,
                  0x994499, 0x22aa99, 0xaaaa11, 0x6633cc, 0x16d620]

#--------------------------------------------------------------------------------------------
class Chart(object):
    def __init__(self, data, colors=None):
        self.data = data
        self.colors = colors

        self._ref_col = 0
        self._ref_isv = True

    def drawLegend(self, painter, rectangle):
        SPACE = 2   # 2

        font_metrics = painter.fontMetrics()
        size = font_metrics.xHeight() * 4

        y = SPACE
        x0 = SPACE
        x1 = x0 + size + SPACE * 3

        w = rectangle.width() - size - SPACE
        w = int(w/2)
        tw = w - x1

        painter.save()
        painter.translate(rectangle.x(), rectangle.y())

        color = self._icolors()
        for i, column in enumerate(self._fetchLegendData()):
            if (y + size + SPACE * 2) >= (rectangle.y() + rectangle.height()) and i < (len(self.data.columns) - 1):
                painter.drawText(x1, y, tw, size, Qt.AlignLeft | Qt.AlignVCenter, "...")
                y += size + SPACE
                break

            text = font_metrics.elidedText(column, Qt.ElideRight, tw)
            painter.fillRect(x0, y, size, size, QColor(next(color)))
            painter.drawText(x1, y, tw, size, Qt.AlignLeft | Qt.AlignVCenter, text)
            y += size + SPACE

        painter.setPen(Qt.lightGray)
        painter.drawRect(0, 0, w, y)
        painter.restore()

    def _fetchLegendData(self):
        for i, column in enumerate(self.data.columns):
            if i != self._ref_col:
                yield column

    def _icolors(self):
        if self.colors is None:
            return cycle(DEFAULT_COLORS)
        return cycle(self.colors)
#--------------------------------------------------------------------------------------------
class PieChart(Chart):
    def draw(self, painter, rectangle):
        painter.save()
        painter.translate(rectangle.x(), rectangle.y())

        # Calculate Values
        vtotal = float(sum(row[not self._ref_col] for row in self.data.rows))
        values = [row[not self._ref_col] / vtotal for row in self.data.rows]

        # Draw Char
        start_angle = 90 * 16
        for color, v in zip(self._icolors(), values):
            span_angle = v * -360.0 * 16
            painter.setPen(Qt.white)
            painter.setBrush(QColor(color))
            painter.drawPie(rectangle, start_angle, span_angle)
            start_angle += span_angle

        painter.restore()

    def _fetchLegendData(self):
        for row in self.data.rows:
            yield row[self._ref_col]
#--------------------------------------------------------------------------------------------
class Viewer(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.graph = None

    def setGraph(self, func):
        self.graph = func
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        if self.graph is not None:
            self.graph.draw(painter, QRect(0, 0, event.rect().width() - 120, event.rect().height()))
            self.graph.drawLegend(painter, QRect(event.rect().width() - 120, 20, 120, event.rect().height() - 20))

        painter.end()
#--------------------------------------------------------------------------------------------
class DialogViewer(QDialog):
   def __init__(self):
        QDialog.__init__(self)
        self.viewer = Viewer()
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.viewer)

   def setGraph(self, func):
        self.viewer.setGraph(func)
#--------------------------------------------------------------------------------------------
class DataTable(object):
    def __init__(self):
        self.columns = []
        self.rows = []

    def addColumn(self, label):
        self.columns.append(label)

    def addRow(self, row):
        assert len(row) == len(self.columns)
        self.rows.append(row)
#--------------------------------------------------------------------------------------------
#END OF qpainter_charts.py