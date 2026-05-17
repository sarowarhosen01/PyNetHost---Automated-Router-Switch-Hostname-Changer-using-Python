# PyNetHost - Automated Router/Switch Hostname Changer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Telnet](https://img.shields.io/badge/Telnet-Client-green.svg)
![Cisco](https://img.shields.io/badge/Vendor-Cisco-red.svg)

A simple yet powerful Python script to **remotely change the hostname** of Cisco routers, switches, and other Telnet-enabled network devices using asynchronous Telnet.

---

## 📋 Overview

PyNetHost automates the process of logging into network devices, entering configuration mode, and changing the hostname — saving time for network engineers and students.

This project is ideal for **network automation beginners**, CCNA/CCNP labs, and small network environments.

---

## ✨ Features

- Asynchronous Telnet connection using `telnetlib3`
- Automatic login (User mode + Enable mode)
- Changes device hostname instantly
- Proper error handling and connection cleanup
- Easy to customize and extend
- Lightweight and fast

---

PyNetHost/
├── change_hostname.py
├── README.md


## 🛠️ Prerequisites

- Python 3.8 or higher
- `telnetlib3` library


---
### Install Required Package

```bash
pip install telnetlib3
```

Just copy the entire content above and save it as `README.md` in your GitHub repository.

Would you like me to also create:
- A more advanced version with argument support?
- A bulk device version (CSV support)?
- A SSH-based version?

Let me know!
