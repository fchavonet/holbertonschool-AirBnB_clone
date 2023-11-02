#!/usr/bin/python3

"""
Script that initializes the FileStorage class
and reloads data from a JSON file.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
