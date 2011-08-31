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

import util, sys
util.qtWrapImport('QtCore', globals(), ['QObject'])
from model.xoverstrand import XOverStrand3
from operation import Operation
from model.vbase import VBase
from model.loopstrand import LoopStrand

class InsertionToolOperation(Operation):
    logger = sys.stdout
    def __init__(self, vBase, undoStack):
        Operation.__init__(self, undoStack)
        strand = LoopStrand(vBase, 10)
        undoStack.beginMacro('InsertLoop')
        vstr, idx = vBase.vStrand(), vBase.vIndex()
        vstr.addStrand(strand, useUndoStack=True, undoStack=undoStack)
        vstr.connectStrand(idx - 1, idx, useUndoStack=True, undoStack=undoStack)
        vstr.connectStrand(idx, idx + 1, useUndoStack=True, undoStack=undoStack)
        undoStack.endMacro()