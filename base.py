# coding = utf-8
# base.py
import multiprocessing
import time
import unittest
from . import api_server_2

class ApiServerUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api_server_process = multiprocessing.Process(
            target=api_server_2.app.run
        )
        cls.api_server_process.start()
        time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.api_server_process.terminate()