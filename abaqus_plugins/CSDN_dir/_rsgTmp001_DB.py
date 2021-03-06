from abaqusConstants import *
from abaqusGui import *
from kernelAccess import mdb, session
import os

thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)


###########################################################################
# Class definition
###########################################################################

class _rsgTmp001_DB(AFXDataDialog):

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def __init__(self, form):

        # Construct the base class.
        #

        AFXDataDialog.__init__(self, form, 'Title',
            self.OK|self.APPLY|self.CANCEL, DIALOG_ACTIONS_SEPARATOR)
            

        okBtn = self.getActionButton(self.ID_CLICKED_OK)
        okBtn.setText('OK')
            

        applyBtn = self.getActionButton(self.ID_CLICKED_APPLY)
        applyBtn.setText('Apply')
            
        AFXTextField(p=self, ncols=12, labelText='name', tgt=form.nameKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='length', tgt=form.lengthKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='width', tgt=form.widthKw, sel=0)
        AFXTextField(p=self, ncols=12, labelText='height', tgt=form.heightKw, sel=0)
