# Copyright (c) 2002 New Information Paradigms Ltd
#
# This Software is released under the MIT License:
# http://www.opensource.org/licenses/mit-license.html
# See license.txt for more details.
#
# $Id: test_Creation.py,v 1.1.2.1 2003/07/22 19:02:03 chrisw Exp $

import Zope

from base import Base
from unittest import makeSuite,main

from Acquisition import aq_base
from Products.SimpleUserFolder.SimpleUserFolder import SimpleUserFolder

class Tests(Base):

    def testCreate(self):
        "Check that we can create a SimpleUserFolder"
        f = self._createFolder()
        f.manage_addProduct['SimpleUserFolder'].addSimpleUserFolder()
        suf = aq_base(f.acl_users)
        assert isinstance(suf,SimpleUserFolder), type(suf)

    def testCreateDuplicate(self):
        """Check that we can't create a SimpleUserFolder in a folder
           with an existing acl_users
        """
        f = self._createFolder(creatUserFolder=1)
        try:
            f.manage_addProduct['SimpleUserFolder'].addSimpleUserFolder()
        except:
            pass
        else:
            self.fail('No complaint about adding duplicate acl_users')

def test_suite():
    return makeSuite(Tests)

if __name__=='__main__':
    main(defaultTest='test_suite')
