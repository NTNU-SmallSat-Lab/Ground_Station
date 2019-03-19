#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: X_FSK
# Author: Erik Buer
# Generated: Fri Mar 15 16:44:31 2019
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import epy_block_0
import epy_block_0_0
import math
import sip
import sys
from gnuradio import qtgui


class X_FSK(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "X_FSK")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("X_FSK")
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

        self.settings = Qt.QSettings("GNU Radio", "X_FSK")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 172800
        self.SYMB_RATE = SYMB_RATE = 9600
        self.packet_len = packet_len = 1
        self.SYMB_LEN = SYMB_LEN = samp_rate/SYMB_RATE
        self.IF_SPACING = IF_SPACING = 3e3
        self.IF_FREQ_BIAS = IF_FREQ_BIAS = 28800

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_sink_x_0_0_0_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"VCO_Out", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_0_0_win)

        self.qtgui_sink_x_0_0_0_0.enable_rf_freq(False)



        self.qtgui_edit_box_msg_0 = qtgui.edit_box_msg(qtgui.STRING, '', '', False, False, '')
        self._qtgui_edit_box_msg_0_win = sip.wrapinstance(self.qtgui_edit_box_msg_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_edit_box_msg_0_win)
        self.interp_fir_filter_xxx_0_0 = filter.interp_fir_filter_ccc(1, (-0.00013469795521814376, 0.0001308875362155959, -0.00011044950952054933, 7.473641016986221e-05, -2.6959885872201994e-05, -2.8064707294106483e-05, 8.431650348939002e-05, -0.00013509293785318732, 0.00017365286475978792, -0.00019396768766455352, 0.00019153871107846498, -0.00016419168969150633, 0.00011271163384662941, -4.115998308407143e-05, -4.3259184167254716e-05, 0.00013084275997243822, -0.00021049147471785545, 0.000271111581241712, -0.00030308208079077303, 0.0002995455579366535, -0.0002573419187683612, 0.00017750899132806808, -6.538065645145252e-05, -6.96249189786613e-05, 0.0002144459867849946, -0.00035304095945321023, 0.00046736918739043176, -0.0005388417048379779, 0.0005503593711182475, -0.0004889002302661538, 0.0003483797481749207, -0.0001322634780080989, -0.00014472758630290627, 0.00045642597251571715, -0.0007668702164664865, 0.001033683423884213, -0.0012125809444114566, 0.0012620714260265231, -0.001147374277934432, 0.0008429177687503397, -0.00033344238181598485, -0.00038543171831406653, 0.0013055375311523676, -0.0024011905770748854, 0.0036183202173560858, -0.004854370374232531, 0.005923138931393623, -0.006490578409284353, 0.005942380055785179, -0.003061555325984955, -0.004920072853565216, 0.025858381763100624, -0.09178953617811203, 0.48881328105926514, 1.1650420427322388, 0.48881328105926514, -0.09178953617811203, 0.025858381763100624, -0.004920072853565216, -0.003061555325984955, 0.005942380055785179, -0.006490578409284353, 0.005923138931393623, -0.004854370374232531, 0.0036183202173560858, -0.0024011905770748854, 0.0013055375311523676, -0.00038543171831406653, -0.00033344238181598485, 0.0008429177687503397, -0.001147374277934432, 0.0012620714260265231, -0.0012125809444114566, 0.001033683423884213, -0.0007668702164664865, 0.00045642597251571715, -0.00014472758630290627, -0.0001322634780080989, 0.0003483797481749207, -0.0004889002302661538, 0.0005503593711182475, -0.0005388417048379779, 0.00046736918739043176, -0.00035304095945321023, 0.0002144459867849946, -6.96249189786613e-05, -6.538065645145252e-05, 0.00017750899132806808, -0.0002573419187683612, 0.0002995455579366535, -0.00030308208079077303, 0.000271111581241712, -0.00021049147471785545, 0.00013084275997243822, -4.3259184167254716e-05, -4.115998308407143e-05, 0.00011271163384662941, -0.00016419168969150633, 0.00019153871107846498, -0.00019396768766455352, 0.00017365286475978792, -0.00013509293785318732, 8.431650348939002e-05, -2.8064707294106483e-05, -2.6959885872201994e-05, 7.473641016986221e-05, -0.00011044950952054933, 0.0001308875362155959, -0.00013469795521814376))
        self.interp_fir_filter_xxx_0_0.declare_sample_delay(0)
        self.interp_fir_filter_xxx_0 = filter.interp_fir_filter_ccc(1, (-0.00013469795521814376, 0.0001308875362155959, -0.00011044950952054933, 7.473641016986221e-05, -2.6959885872201994e-05, -2.8064707294106483e-05, 8.431650348939002e-05, -0.00013509293785318732, 0.00017365286475978792, -0.00019396768766455352, 0.00019153871107846498, -0.00016419168969150633, 0.00011271163384662941, -4.115998308407143e-05, -4.3259184167254716e-05, 0.00013084275997243822, -0.00021049147471785545, 0.000271111581241712, -0.00030308208079077303, 0.0002995455579366535, -0.0002573419187683612, 0.00017750899132806808, -6.538065645145252e-05, -6.96249189786613e-05, 0.0002144459867849946, -0.00035304095945321023, 0.00046736918739043176, -0.0005388417048379779, 0.0005503593711182475, -0.0004889002302661538, 0.0003483797481749207, -0.0001322634780080989, -0.00014472758630290627, 0.00045642597251571715, -0.0007668702164664865, 0.001033683423884213, -0.0012125809444114566, 0.0012620714260265231, -0.001147374277934432, 0.0008429177687503397, -0.00033344238181598485, -0.00038543171831406653, 0.0013055375311523676, -0.0024011905770748854, 0.0036183202173560858, -0.004854370374232531, 0.005923138931393623, -0.006490578409284353, 0.005942380055785179, -0.003061555325984955, -0.004920072853565216, 0.025858381763100624, -0.09178953617811203, 0.48881328105926514, 1.1650420427322388, 0.48881328105926514, -0.09178953617811203, 0.025858381763100624, -0.004920072853565216, -0.003061555325984955, 0.005942380055785179, -0.006490578409284353, 0.005923138931393623, -0.004854370374232531, 0.0036183202173560858, -0.0024011905770748854, 0.0013055375311523676, -0.00038543171831406653, -0.00033344238181598485, 0.0008429177687503397, -0.001147374277934432, 0.0012620714260265231, -0.0012125809444114566, 0.001033683423884213, -0.0007668702164664865, 0.00045642597251571715, -0.00014472758630290627, -0.0001322634780080989, 0.0003483797481749207, -0.0004889002302661538, 0.0005503593711182475, -0.0005388417048379779, 0.00046736918739043176, -0.00035304095945321023, 0.0002144459867849946, -6.96249189786613e-05, -6.538065645145252e-05, 0.00017750899132806808, -0.0002573419187683612, 0.0002995455579366535, -0.00030308208079077303, 0.000271111581241712, -0.00021049147471785545, 0.00013084275997243822, -4.3259184167254716e-05, -4.115998308407143e-05, 0.00011271163384662941, -0.00016419168969150633, 0.00019153871107846498, -0.00019396768766455352, 0.00017365286475978792, -0.00013509293785318732, 8.431650348939002e-05, -2.8064707294106483e-05, -2.6959885872201994e-05, 7.473641016986221e-05, -0.00011044950952054933, 0.0001308875362155959, -0.00013469795521814376))
        self.interp_fir_filter_xxx_0.declare_sample_delay(0)
        self.epy_block_0_0 = epy_block_0_0.msg_block()
        self.epy_block_0 = epy_block_0.blk(Multiplication_Const=IF_SPACING, Accumulate_Const=IF_FREQ_BIAS)
        self.digital_hdlc_framer_pb_0 = digital.hdlc_framer_pb('')
        self.digital_hdlc_deframer_bp_0_0 = digital.hdlc_deframer_bp(1, 500)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(SYMB_LEN*(1+0.0), 0.25*0.175*0.175, 0.5, 0.175, 0.005)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(8*SYMB_LEN, True)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, SYMB_LEN)
        self.blocks_pdu_to_tagged_stream_1 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(SYMB_LEN, 0.01, 4000, 1)
        self.blocks_message_debug_0_0_0 = blocks.message_debug()
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_char*1, 'C:\\Users\\mikol\\OneDrive\\Desktop\\Skole\\Semester 7\\Prosjekt\\Software\\Ground_Station\\Ground_Station\\Received_data.bin', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(samp_rate/(2*math.pi*3e3/8.0))
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(-40, 1e-4, 0, True)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc((2*math.pi)/samp_rate)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.digital_hdlc_deframer_bp_0_0, 'out'), (self.blocks_message_debug_0_0_0, 'print_pdu'))
        self.msg_connect((self.digital_hdlc_deframer_bp_0_0, 'out'), (self.blocks_pdu_to_tagged_stream_1, 'pdus'))
        self.msg_connect((self.epy_block_0_0, 'msg_out'), (self.digital_hdlc_framer_pb_0, 'in'))
        self.msg_connect((self.qtgui_edit_box_msg_0, 'msg'), (self.epy_block_0_0, 'msg_in'))
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.interp_fir_filter_xxx_0, 0))
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.dc_blocker_xx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_1, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_repeat_0, 0), (self.epy_block_0, 0))
        self.connect((self.dc_blocker_xx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.digital_hdlc_deframer_bp_0_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))
        self.connect((self.digital_hdlc_framer_pb_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.epy_block_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.interp_fir_filter_xxx_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0, 0), (self.qtgui_sink_x_0_0_0_0, 0))
        self.connect((self.interp_fir_filter_xxx_0_0, 0), (self.analog_pwr_squelch_xx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "X_FSK")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_SYMB_LEN(self.samp_rate/self.SYMB_RATE)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_sink_x_0_0_0_0.set_frequency_range(0, self.samp_rate)
        self.analog_quadrature_demod_cf_0.set_gain(self.samp_rate/(2*math.pi*3e3/8.0))
        self.analog_frequency_modulator_fc_0.set_sensitivity((2*math.pi)/self.samp_rate)

    def get_SYMB_RATE(self):
        return self.SYMB_RATE

    def set_SYMB_RATE(self, SYMB_RATE):
        self.SYMB_RATE = SYMB_RATE
        self.set_SYMB_LEN(self.samp_rate/self.SYMB_RATE)

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_SYMB_LEN(self):
        return self.SYMB_LEN

    def set_SYMB_LEN(self, SYMB_LEN):
        self.SYMB_LEN = SYMB_LEN
        self.digital_clock_recovery_mm_xx_0.set_omega(self.SYMB_LEN*(1+0.0))
        self.blocks_repeat_0.set_interpolation(self.SYMB_LEN)
        self.blocks_moving_average_xx_0.set_length_and_scale(self.SYMB_LEN, 0.01)

    def get_IF_SPACING(self):
        return self.IF_SPACING

    def set_IF_SPACING(self, IF_SPACING):
        self.IF_SPACING = IF_SPACING
        self.epy_block_0.Multiplication_Const = self.IF_SPACING

    def get_IF_FREQ_BIAS(self):
        return self.IF_FREQ_BIAS

    def set_IF_FREQ_BIAS(self, IF_FREQ_BIAS):
        self.IF_FREQ_BIAS = IF_FREQ_BIAS
        self.epy_block_0.Accumulate_Const = self.IF_FREQ_BIAS


def main(top_block_cls=X_FSK, options=None):

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
