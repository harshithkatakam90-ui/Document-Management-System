# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:35:22 2025

@author: Harshith katakam
"""

class Document:
    def __init__(self, doc_id, title, author, content):
        self.doc_id = doc_id
        self.title = title
        self.author = author
        self.content = content

    def __str__(self):
        return f"[{self.doc_id}] {self.title} by {self.author}"