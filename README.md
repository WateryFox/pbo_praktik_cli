# CLI Book Management System

A Python-based Command-Line Interface (CLI) application developed using Object-Oriented Programming (OOP) principles to manage book inventories. The project features a modular architecture and persists data using CSV file storage.

---

## Features

- **Display Book List:** View all book records stored in the system.
- **Add New Book:** Interactively insert new book entries into the inventory.
- **Data Persistence:** Automatically save and retain records in `buku.csv`.
- **Modular Architecture (OOP):** Implements Object-Oriented Programming (`models.py`) for clean code separation and maintainability.

---

## Project Structure

```text
pbo_praktik_cli/
├── Main.py            # Main entry point and CLI menu navigation
├── models.py          # Data models and OOP classes
├── tambah_buku.py     # Module for adding new books
├── tampil_buku.py     # Module for displaying book records
├── buku.csv           # CSV data storage file
├── .gitignore         # Git ignore rules
└── LICENSE            # MIT License
