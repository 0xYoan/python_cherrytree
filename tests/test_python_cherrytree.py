#!/usr/bin/env python

"""Tests for `python_cherrytree` package."""


import unittest

from python_cherrytree import python_cherrytree


class TestPython_cherrytree(unittest.TestCase):
    """Tests for `python_cherrytree` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.manager = python_cherrytree.SqlManager("./tests/CTF_template.ctb")

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_show_nodes(self):
        """Test show_nodes."""
        self.manager.show_nodes()

    def test_change_node_name(self):
        """Test change_node_name"""
        self.manager.change_node_name("Test", 22)

    def test_add_txt(self):
        """Test add_txt"""
        self.manager.add_txt("Text", 24)
