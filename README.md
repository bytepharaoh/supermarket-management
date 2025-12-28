# Supermarket Management System

A desktop application for managing supermarket operations — built with **Java Swing** for the frontend and **MySQL** for backend data storage. This system includes user authentication, role‑based access control, and inventory management for efficient store operations.

## 🛠️ Features

- **User Authentication** — Secure login for system users.  
- **Role-Based Access Control** — Different privileges for Admin and Employee users.  
- **Inventory Management** — Add, update, delete, and view product stock levels.  
- **Database Management** — Structured MySQL database with optimized queries and data consistency.

## 💡 Technologies Used

- 🧩 **Java Swing** — Desktop GUI frontend for an intuitive user experience.  
- 🗄️ **MySQL** — Backend database for persistent data storage and retrieval.  
- 🔌 **JDBC** — Java database connectivity for executing SQL operations.

## 🗃️ System Overview

This application helps a supermarket manage its main operations by providing:

- Secure login system with role differentiation (Admin vs Employee).  
- Centralized inventory with real-time stock updates.  
- CRUD operations on products and stock items.  
- Well-designed database schema ensuring integrity and consistency.

## 🗂️ Database

The MySQL database includes tables for:

- **Users** — Employees and Admin accounts with role indicators.  
- **Products** — Items tracked in the supermarket inventory.  
- **Other related tables** — Records needed for core system features.

SQL queries are optimized to avoid data redundancy and maintain consistency across tables.

## 🚀 Getting Started

### Prerequisites

Make sure you have:

- Java JDK 8 or newer installed  
- MySQL Server running  
- MySQL Connector/J JDBC driver  

### Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/bytepharaoh/supermarket-management.git
   cd supermarket-management-system
   ```
  ## Setup MySQL database

Create a database (e.g., supermarket_db).

Import the provided SQL schema file with the required tables.

Configure database connection

Update database credentials (hostname, username, password) in your config file or connection class.

Build and Run

Open the project in your Java IDE (e.g., IntelliJ / NetBeans / Eclipse).

Run the main application class to launch the system.

## ❓ Usage

Launch the application and log in.

Depending on the user role, access different modules.

Admin: Full access — add/edit users, manage inventory.

Employee: Restricted access — typically inventory and operations allowed.

Use navigation menus to manage products, view stock levels, and perform actions.

