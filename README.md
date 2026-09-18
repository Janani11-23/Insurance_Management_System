# 🚗 SafeDrive Insurance Management System

A console-based **Insurance Management System** developed using **Python Object-Oriented Programming (OOP)** concepts.

This project demonstrates how **Encapsulation and Inheritance** can be applied to a real-world insurance management scenario involving **Car Insurance and Bike Insurance**.

---

## 📌 Project Overview

The **SafeDrive Insurance Management System** allows users to perform basic insurance operations through a menu-driven console application.

The system supports:

* 🚗 Car Insurance
* 🏍️ Bike Insurance
* 🔐 Policy authentication
* 📄 Policy purchase
* 💰 Premium payment
* 🏦 Insurance claim processing
* 📋 Policy details
* 💵 Premium tracking
* 🧾 Last transaction receipt

---

## 🛠️ Technologies Used

* **Python**
* **Object-Oriented Programming (OOP)**

---

## 🧠 OOP Concepts Used

### 🔒 1. Encapsulation

Sensitive policy information such as:

* Policy Number
* PIN
* Sum Assured
* Premium
* Last Transaction

is stored using **private attributes**.

Private methods are also used for:

* Authentication
* Receipt generation
* Base premium calculation

This helps demonstrate **data hiding and controlled access**.

---

### 🧬 2. Inheritance

`CarInsurance` and `BikeInsurance` inherit common functionality from the `Insurance` parent class.

```text
                Insurance
                /       \
               /         \
      CarInsurance    BikeInsurance
```

This allows common insurance operations to be reused instead of writing the same functionality separately.

---

### 🔄 3. Method Overriding

The insurance classes use different premium calculation logic based on the vehicle category.

* **Car Insurance:** 5% of Sum Assured
* **Bike Insurance:** 2% of Sum Assured

This demonstrates how inherited behavior can be customized for different subclasses.

---

### 🏗️ 4. Constructor

The `__init__()` constructor is used to initialize policy information such as:

* Policy holder name
* Policy number
* PIN
* Sum assured
* Vehicle number

---

### 🔗 5. `super()`

`super()` is used in the child classes to call the constructor of the parent `Insurance` class and initialize the common insurance details.

---

## ⚙️ Features

### 1️⃣ Buy Policy

The system calculates the initial premium based on the vehicle insurance type and creates a transaction receipt.

### 2️⃣ Pay Premium

The user is authenticated using the **Policy Number and PIN** before making a premium payment.

### 3️⃣ Claim Policy

Users can enter a claim amount, and the system validates that the claim does not exceed the available **Sum Assured**.

### 4️⃣ Show Policy Details

Displays the policy information after successful authentication.

### 5️⃣ Show Premium

Displays the current premium amount associated with the policy.

### 6️⃣ Last Transaction

Displays the latest insurance transaction receipt.

---

## 📋 Menu Options

```text
============ WELCOME TO SAFEDRIVE INSURANCE ============

1. Buy Policy
2. Pay Premium
3. Claim Policy
4. Show Policy Details
5. Show Premium
6. List Last Transaction
7. Exit
```

---

## 🚗 Vehicle Categories

The project contains two child classes:

### CarInsurance

```python
class CarInsurance(Insurance):
```

Vehicle Category:

```text
Four wheeler car
```

### BikeInsurance

```python
class BikeInsurance(Insurance):
```

Vehicle Category:

```text
Two wheeler bike
```

---

## 💡 What I Learned

Through this project, I practiced:

* Creating classes and objects
* Implementing Encapsulation
* Using private attributes and methods
* Implementing Inheritance
* Using `super()`
* Method overriding
* Constructors
* Conditional statements
* Loops
* User input handling
* String formatting
* Building a menu-driven console application

## 📂 Project Structure

```text
Python_Encapsulation_Inheritance_Project2/
│
├── encapsulation_inheritance_project2.py
└── README.md
```

---

## 🎯 Project Objective

The main objective of this project is to understand and practically implement **Python OOP concepts**, especially **Encapsulation and Inheritance**, by creating a simple real-world-style insurance management application.

---

## 👩‍💻 Author

**Janani S**

Learning Python and strengthening my Object-Oriented Programming skills through practical projects.
