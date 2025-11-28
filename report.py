# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:33:02 2025

@author: Harshith katakam
"""

def document_report(manager, doc_id):
    if doc_id not in manager.documents:
        return "Document not found."
    doc = manager.documents[doc_id]
    lines = [
        f"Report for {doc.title} ({doc.doc_id})",
        f"Author: {doc.author}",
        f"Content Preview: {doc.content[:50]}..."
    ]
    return "\n".join(lines)

def all_documents_report(manager):
    lines = ["All Documents Report:"]
    for doc in manager.documents.values():
        lines.append(str(doc))
    return "\n".join(lines)