import unittest
import doctest
from doctest import DocTestSuite

from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import dm.ldapperson


class TestCase(ptc.PloneTestCase):

    class layer(PloneSite):

        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            ztc.installPackage(dm.ldapperson)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    optionflags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    return unittest.TestSuite([
    
        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='dm.ldapperson',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        DocTestSuite(
            module='dm.ldapperson.person',
            setUp=testing.setUp, tearDown=testing.tearDown,
            optionflags=optionflags),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='dm.ldapperson',
        #    test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='dm.ldapperson',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
