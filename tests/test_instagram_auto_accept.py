#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_instagram_auto_accept
----------------------------------

Tests for `instagram_auto_accept` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from instagram_auto_accept import instagram_auto_accept
from instagram_auto_accept import cli



class TestInstagram_auto_accept(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'instagram_auto_accept.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output