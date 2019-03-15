import numpy as np
from gnuradio import gr


class blk(gr.sync_block):
    def __init__(self, Multiplication_Const=1.0, Accumulate_Const=1.0):
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Multiply Accumulate',   	# Name of block. Will show up in GRC
            in_sig=[np.single],				# Make input a single precision floating point
            out_sig=[np.single]				# Make output a single precision floating point
        )

        self.Multiplication_Const = Multiplication_Const
        self.Accumulate_Const = Accumulate_Const


    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = (input_items[0] * self.Multiplication_Const) + self.Accumulate_Const
        return len(output_items[0])
