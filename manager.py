# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:34:22 2025

@author: Harshith katakam
"""

from exceptions import DocumentNotFoundError, DuplicateDocumentError, EmptyContentError
from document import Document

class DocumentManager:
    def __init__(self):
        self.documents = {}  # doc_id -> Document object

    def add_document(self, document: Document):
        if document.doc_id in self.documents:
            raise DuplicateDocumentError("Document ID already exists.")
        if not document.content.strip():
            raise EmptyContentError("Document content cannot be empty.")
        self.documents[document.doc_id] = document

    def remove_document(self, doc_id):
        if doc_id not in self.documents:
            raise DocumentNotFoundError("Document not found.")
        del self.documents[doc_id]

    def list_documents(self):
        return list(self.documents.values())

    def get_document(self, doc_id):
        if doc_id not in self.documents:
            raise DocumentNotFoundError("Document not found.")
        return self.documents[doc_id]