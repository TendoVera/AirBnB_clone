#!/usr/bin/python3
"""__init__ file initializes the FileStorage class"""
from models.engine.file_storage import FileStorage
"""Imports necessary modules or classes"""
storage = FileStorage()
"""Creates an instance of FileStorage"""
storage.reload()
