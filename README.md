# Python for Odoo & ERP

Learning Python through practical ERP business scenarios, Odoo concepts, and business logic exercises.

This repository documents my journey learning Python as a companion to my Business Analyst / ERP learning path. The focus is not just learning the language, but understanding how programming concepts translate into business rules, data models, and ERP workflows.

The exercises use realistic business scenarios involving products, inventory, sales orders, purchasing, and other processes that appear in ERP systems. Later, I'll explore how Python is used in Odoo models, fields, relationships, and business logic.

## Learning Objectives

- Build a practical understanding of Python syntax and core programming concepts.
- Translate business requirements into executable business rules.
- Model common ERP concepts such as products, customers, vendors, sales orders, and purchase orders.
- Understand Python classes, objects, and relationships through business examples.
- Learn the fundamentals of Odoo's Python-based development model, including ORM concepts and model relationships.
- Develop the technical understanding needed to collaborate effectively with Odoo developers as a Business Analyst or Functional Consultant.

## Learning Roadmap

### Week 1 — Python Fundamentals

- Variables, data types, strings, and numbers
- Lists, tuples, sets, and dictionaries
- Conditional statements and loops
- Input, output, and basic debugging
- **Practical exercise:** Product catalog and inventory checker

### Week 2 — Functions and Business Logic

- Functions, parameters, and return values
- Scope, modules, and imports
- Input validation and exception handling
- Reusable business rules
- **Practical exercise:** Sales order calculations, discounts, and validation

### Week 3 — Object-Oriented Programming

- Classes, objects, attributes, and methods
- Constructors and object initialization
- Inheritance and composition
- Modeling relationships between business entities
- **Practical exercise:** Products, vendors, purchase orders, and order lines

### Week 4 — Python in Odoo

- Understanding Odoo's model-based architecture
- Models, fields, and the ORM
- Recordsets and relational fields
- Computed fields and `@api.depends`
- Onchange behavior and `@api.onchange`
- Understanding when a business requirement needs configuration, customization, or custom development
- **Practical exercise:** Read and explain an Odoo model and connect its code to business requirements

The roadmap is a working plan. Progress will depend on understanding and completing the exercises, rather than simply following the calendar.

## Learning Approach

Each topic follows a practical cycle:

1. Learn the concept.
2. Apply it to a business scenario.
3. Explain the logic in my own words.
4. Review mistakes and improve the implementation.
5. Connect the concept to ERP or Odoo where relevant.

The goal is to understand how and why the code works, not just to make a program run.

## Repository Structure

The repository will grow as exercises are completed. The initial structure is intentionally small.

```text
python-for-odoo-erp/
├── README.md
└── hello.py
```

As the learning track progresses, exercises will be organized by week and topic to keep the repository easy to navigate.

## Requirements

- Python 3.13 or a compatible Python version
- Visual Studio Code
- Microsoft Python extension for VS Code

## Getting Started

Clone the repository:

```bash
git clone <repository-url>
cd python-for-odoo-erp
```

Open the folder in Visual Studio Code.

Run the initial script:

```bash
python hello.py
```

The script confirms that Python is installed and the development environment can execute a Python file.

## Learning Resources

- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Official Odoo Documentation](https://www.odoo.com/documentation/)

These resources will be used selectively alongside practical exercises.

## Progress

- [x] Install Python and configure the VS Code environment
- [x] Run the first Python script
- [ ] Complete Python fundamentals and inventory exercises
- [ ] Practice functions and business rules
- [ ] Model business entities using object-oriented programming
- [ ] Explore Odoo's Python models and ORM

## Purpose

This is a learning repository focused on building practical Python knowledge for ERP and Odoo-related work. It complements my broader Business Analyst learning journey, where the emphasis is on understanding business processes, documenting requirements, and translating business needs into workable solutions.
