<div align="center">

# 📦 Smart Inventory Management System

### A clean, terminal-based inventory, sales & billing solution built with Python

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](#-license)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](#)
[![Made With](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=for-the-badge)](#)

**Developed by [Shahzaib](#)**

</div>

---

## 📖 Overview

**Smart Inventory Management System** is a lightweight, dependency-free, console-based application built entirely in Python. It allows shop owners and small businesses to manage products, track stock, process sales with discounts, and generate digital receipts — all backed by simple, persistent JSON storage.

No database setup. No external libraries. Just run and go.

---

## ✨ Features

- 🔐 **Secure Admin Login** — Simple authentication gate before accessing the dashboard
- 🗂️ **Product Catalog Management** — Add, view, and delete products with ease
- 📊 **Live Inventory Tracking** — Stock quantities update automatically after every sale
- 🛒 **Smart Shop (POS System)** — Search products by name or ID and generate instant bills
- 💸 **Discount Engine** — Built-in Student (10%) and Member (15%) discount tiers
- 🧾 **Auto-Generated Receipts** — Unique receipt numbers with date & time stamps
- 📜 **Sales History Log** — Full record of every transaction ever made
- 💾 **Persistent JSON Storage** — Data is saved locally and reloaded automatically on startup
- 🖥️ **Clean CLI Interface** — Organized menus for smooth navigation

---

## 🗺️ Application Flow

```
Login → Main Menu
          ├── Inventory Management
          │     ├── Product Catalog (Add / View / Delete)
          │     └── View Inventory
          └── Sales & Billing
                ├── Smart Shop (Search → Buy → Discount → Receipt)
                └── Sales History
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8** or higher installed on your system

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/smart-inventory-management-system.git

# 2. Move into the project directory
cd smart-inventory-management-system

# 3. Run the application
python main.py
```

> No external packages required — the project only uses Python's built-in standard library (`random`, `json`, `datetime`, `time`).

### Default Login Credentials

| Username | Password |
|----------|----------|
| `admin`  | `1234`   |

> ⚠️ For production/client use, it's recommended to move credentials to a config file or environment variable instead of hardcoding them.

---

## 🧩 Project Structure

```
smart-inventory-management-system/
├── main.py           # Core application logic
├── products.json      # Auto-generated: stores product catalog
├── sales.json          # Auto-generated: stores sales/receipt history
└── README.md            # Project documentation
```

---

## 🖼️ Preview

```
==================================================================
        SMART INVENTORY MANAGEMENT SYSTEM         
==================================================================
             Developed by: Shahzaib               
==================================================================

Loading System...
Welcome to the Dashboard!

Enter your username: admin
Enter your password: ****

Login Successful!

-------------------------------------------------
                    MAIN MENU         
-------------------------------------------------

1. Inventory Management
2. Sales & Billing
3. Exit
```

---

## 🛠️ Tech Stack

| Layer         | Technology            |
|---------------|------------------------|
| Language       | Python 3               |
| Data Storage   | JSON (file-based)      |
| Interface      | Command Line (CLI)     |

---

## 🔮 Future Enhancements

- [ ] GUI version using Tkinter or PyQt
- [ ] Multi-user role support (Admin / Cashier)
- [ ] Low-stock alerts & notifications
- [ ] Export sales reports to PDF/Excel
- [ ] Barcode scanner integration
- [ ] Password hashing for secure login

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](../../issues) or submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute it.

---

<div align="center">

### ⭐ If you find this project useful, consider giving it a star!

**Made with 💻 and ☕ by Shahzaib**

</div>
