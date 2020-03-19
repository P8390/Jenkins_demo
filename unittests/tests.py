#!/usr/bin/env python
import unittest
import xmlrunner
from main_app.app import app as f_app


class TestHello(unittest.TestCase):

    def setUp(self):
        f_app.testing = True
        self.app = f_app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')

    def test_hello_name(self):
        rv = self.app.get('/hello/{name}')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    ###########################################
    unittest.main()
