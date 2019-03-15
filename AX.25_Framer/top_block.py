#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Mar 15 10:16:17 2019
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import epy_block_0
import epy_block_1
import pmt
import sip
import sys
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_edit_box_msg_0 = qtgui.edit_box_msg(qtgui.STRING, '', '', False, False, '')
        self._qtgui_edit_box_msg_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_edit_box_msg_0_win)
        self.epy_block_1 = epy_block_1.blk()
        self.epy_block_0 = epy_block_0.msg_block()
        self.digital_hdlc_framer_pb_0 = digital.hdlc_framer_pb('')
        self.digital_hdlc_deframer_bp_0 = digital.hdlc_deframer_bp(1, 500)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(8)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.intern("TEST"), 1000)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\mikol\\OneDrive\\Desktop\\Skole\\Semester 7\\Prosjekt\\AX.25_TEST\\receive_float.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.epy_block_0, 'msg_in'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.epy_block_0, 'msg_out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.msg_connect((self.epy_block_0, 'msg_out'), (self.digital_hdlc_framer_pb_0, 'in'))
        self.msg_connect((self.qtgui_edit_box_msg_0, 'msg'), (self.blocks_message_strobe_0, 'set_msg'))
        self.connect((self.blocks_null_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.epy_block_1, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.digital_hdlc_framer_pb_0, 0), (self.blocks_pack_k_bits_bb_0, 0))
        self.connect((self.digital_hdlc_framer_pb_0, 0), (self.digital_hdlc_deframer_bp_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
