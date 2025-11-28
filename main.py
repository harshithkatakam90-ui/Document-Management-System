# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 16:32:00 2025

@author: Harshith katakam
"""

from document import Document
from manager import DocumentManager
from report import document_report, all_documents_report

def main():
    manager = DocumentManager()

    while True:
        print("\nDocument Management System")
        print("1. Add Document")
        print("2. Remove Document")
        print("3. View Documents")
        print("4. Document Report")
        print("5. All Documents Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            did = input("Document ID: ")
            title = input("Title: ")
            author = input("Author: ")
            content = input("Content: ")
            try:
                manager.add_document(Document(did, title, author, content))
                print("✅ Document added.")
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            did = input("Document ID: ")
            try:
                manager.remove_document(did)
                print("🗑️ Document removed.")
            except Exception as e:
                print("Error:", e)

        elif choice == "3":
            for d in manager.list_documents():
                print("-", d)

        elif choice == "4":
            did = input("Document ID: ")
            print(document_report(manager, did))

        elif choice == "5":
            print(all_documents_report(manager))

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()