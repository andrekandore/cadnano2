# The MIT License
#
# Copyright (c) 2011 Wyss Institute at Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# http://www.opensource.org/licenses/mit-license.php

"""
selecttool
Created by Shawn Douglas on 2011-06-21.
"""

from abstractpathtool import AbstractPathTool
import util
from PyQt4.QtGui import QPen, QColor, QInputDialog
from PyQt4.QtCore import Qt, QPointF, SLOT, pyqtSlot
from model.enum import StrandType
from data.dnasequences import sequences

class AddSeqTool(AbstractPathTool):
    def __init__(self, controller, parent=None):
        AbstractPathTool.__init__(self, controller, parent)

    def mousePressPathHelix(self, pathHelix, event):
        strandType, idx = self.baseAtPoint(pathHelix, event.pos())
        dialog = QInputDialog(self.window())
        dialog.setWindowFlags(Qt.Dialog | Qt.Sheet)
        dialog.setWindowModality(Qt.WindowModal)
        dialog.setLabelText('Choose the sequence to be applied from 5\' to 3\' in the oligo you clicked on by name, or enter a sequence by hand:')
        dialog.setWindowTitle('Choose Sequence')
        dialog.setComboBoxEditable(True)
        dialog.setComboBoxItems(sequences.keys())
        dialog.open(self, SLOT("userChoseSeq(QString)"))
        self.dialog = dialog
        self.vh = pathHelix.vhelix()
        self.strandType = strandType
        self.idx = idx

    @pyqtSlot(str)
    def userChoseSeq(self, optionChosen):
        optionChosen = str(optionChosen)
        seqToUse = ""
        knownSeqNamedByChosenOption = sequences.get(optionChosen, None)
        sequenceAfterExtractionOfBasePairChars = util.strToDna(optionChosen)
        if knownSeqNamedByChosenOption:
            seqToUse = knownSeqNamedByChosenOption
        elif len(sequenceAfterExtractionOfBasePairChars)==len(optionChosen):
            seqToUse = sequenceAfterExtractionOfBasePairChars
        vh, strandType, idx = self.vh, self.strandType, self.idx
        vh.applySequenceAt(strandType, idx, seqToUse)
