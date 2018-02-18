#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Audio Filter
# Generated: Sun Feb 18 22:30:18 2018
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
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class Audio_Filter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Audio Filter")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Audio Filter")
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

        self.settings = Qt.QSettings("GNU Radio", "Audio_Filter")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.variable_qtgui_range_4 = variable_qtgui_range_4 = 3000
        self.variable_qtgui_range_3 = variable_qtgui_range_3 = 3000
        self.variable_qtgui_range_2 = variable_qtgui_range_2 = 1
        self.variable_qtgui_range_1 = variable_qtgui_range_1 = 2700
        self.variable_qtgui_range_0 = variable_qtgui_range_0 = 200
        self.step = step = 10
        self.samp_rate = samp_rate = 6000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_range_4_range = Range(0, 3000, step, 3000, 200)
        self._variable_qtgui_range_4_win = RangeWidget(self._variable_qtgui_range_4_range, self.set_variable_qtgui_range_4, 'HIGH BLOCK', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_4_win)
        self._variable_qtgui_range_3_range = Range(0, 3000, step, 3000, 200)
        self._variable_qtgui_range_3_win = RangeWidget(self._variable_qtgui_range_3_range, self.set_variable_qtgui_range_3, 'LOW BLOCK', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_3_win)
        self._variable_qtgui_range_2_range = Range(0, 10, 0.1, 1, 200)
        self._variable_qtgui_range_2_win = RangeWidget(self._variable_qtgui_range_2_range, self.set_variable_qtgui_range_2, 'VOLUME', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_2_win)
        self._variable_qtgui_range_1_range = Range(0, 3000, step, 2700, 200)
        self._variable_qtgui_range_1_win = RangeWidget(self._variable_qtgui_range_1_range, self.set_variable_qtgui_range_1, 'Low  PASS', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_1_win)
        self._variable_qtgui_range_0_range = Range(0, 3000, step, 200, 200)
        self._variable_qtgui_range_0_win = RangeWidget(self._variable_qtgui_range_0_range, self.set_variable_qtgui_range_0, 'High PASS', "counter_slider", float)
        self.top_layout.addWidget(self._variable_qtgui_range_0_win)
        self.qtgui_waterfall_sink_x_0 = qtgui.waterfall_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"Output", #name
                1 #number of inputs
        )
        self.qtgui_waterfall_sink_x_0.set_update_time(0.10)
        self.qtgui_waterfall_sink_x_0.enable_grid(False)
        self.qtgui_waterfall_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_waterfall_sink_x_0.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_waterfall_sink_x_0.set_plot_pos_half(not False)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_waterfall_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_waterfall_sink_x_0.set_color_map(i, colors[i])
            self.qtgui_waterfall_sink_x_0.set_line_alpha(i, alphas[i])
        
        self.qtgui_waterfall_sink_x_0.set_intensity_range(-140, 10)
        
        self._qtgui_waterfall_sink_x_0_win = sip.wrapinstance(self.qtgui_waterfall_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_waterfall_sink_x_0_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	'Input', #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not False:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "float" == "float" or "float" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not False)
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.dc_blocker_xx_0 = filter.dc_blocker_ff(32, True)
        self.band_reject_filter_0 = filter.fir_filter_fff(1, firdes.band_reject(
        	1, samp_rate, variable_qtgui_range_3, variable_qtgui_range_4, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.fir_filter_fff(1, firdes.band_pass(
        	variable_qtgui_range_2, samp_rate, variable_qtgui_range_0, variable_qtgui_range_1, 10, firdes.WIN_HAMMING, 6.76))
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.audio_sink_0 = audio.sink(samp_rate, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.audio_source_0, 0), (self.dc_blocker_xx_0, 0))    
        self.connect((self.audio_source_0, 0), (self.qtgui_freq_sink_x_1, 0))    
        self.connect((self.band_pass_filter_0, 0), (self.band_reject_filter_0, 0))    
        self.connect((self.band_reject_filter_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.band_reject_filter_0, 0), (self.qtgui_waterfall_sink_x_0, 0))    
        self.connect((self.dc_blocker_xx_0, 0), (self.band_pass_filter_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Audio_Filter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_qtgui_range_4(self):
        return self.variable_qtgui_range_4

    def set_variable_qtgui_range_4(self, variable_qtgui_range_4):
        self.variable_qtgui_range_4 = variable_qtgui_range_4
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, self.variable_qtgui_range_3, self.variable_qtgui_range_4, 10, firdes.WIN_HAMMING, 6.76))

    def get_variable_qtgui_range_3(self):
        return self.variable_qtgui_range_3

    def set_variable_qtgui_range_3(self, variable_qtgui_range_3):
        self.variable_qtgui_range_3 = variable_qtgui_range_3
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, self.variable_qtgui_range_3, self.variable_qtgui_range_4, 10, firdes.WIN_HAMMING, 6.76))

    def get_variable_qtgui_range_2(self):
        return self.variable_qtgui_range_2

    def set_variable_qtgui_range_2(self, variable_qtgui_range_2):
        self.variable_qtgui_range_2 = variable_qtgui_range_2
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.variable_qtgui_range_2, self.samp_rate, self.variable_qtgui_range_0, self.variable_qtgui_range_1, 10, firdes.WIN_HAMMING, 6.76))

    def get_variable_qtgui_range_1(self):
        return self.variable_qtgui_range_1

    def set_variable_qtgui_range_1(self, variable_qtgui_range_1):
        self.variable_qtgui_range_1 = variable_qtgui_range_1
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.variable_qtgui_range_2, self.samp_rate, self.variable_qtgui_range_0, self.variable_qtgui_range_1, 10, firdes.WIN_HAMMING, 6.76))

    def get_variable_qtgui_range_0(self):
        return self.variable_qtgui_range_0

    def set_variable_qtgui_range_0(self, variable_qtgui_range_0):
        self.variable_qtgui_range_0 = variable_qtgui_range_0
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.variable_qtgui_range_2, self.samp_rate, self.variable_qtgui_range_0, self.variable_qtgui_range_1, 10, firdes.WIN_HAMMING, 6.76))

    def get_step(self):
        return self.step

    def set_step(self, step):
        self.step = step

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_waterfall_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.band_reject_filter_0.set_taps(firdes.band_reject(1, self.samp_rate, self.variable_qtgui_range_3, self.variable_qtgui_range_4, 10, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.variable_qtgui_range_2, self.samp_rate, self.variable_qtgui_range_0, self.variable_qtgui_range_1, 10, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=Audio_Filter, options=None):

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
