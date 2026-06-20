# Port Scanner Tool

A simple educational port scanner written in Python using the `socket` library.  
Designed for learning **network reconnaissance** and basic **ethical hacking / red team concepts**.

---

## 🎯 Features

- Scan a single IP or hostname  
- Scan a range of ports (e.g. 1–1000)  
- Detect open, closed, and filtered ports  
- Simple command-line interface  
- Basic error handling  

---

## 🛠️ Installation & Usage

### Clone the repository

```bash
git clone https://github.com/MahdiAmini12/Port-Scanner.git
cd Port-Scanner
```

### Run the tool

```bash
python main.py
```

### Example usage

```bash
python main.py -t 192.168.1.1 -p 1-500
```

---

## ⚠️ Important Notice

This tool is created strictly for educational purposes and authorized security testing only.

Do NOT use it on:

- Networks you do not own  
- Systems without explicit permission  

Unauthorized scanning may be illegal in your country.

---

## 🧠 Technologies Used

- Python 3  
- socket library  
- argparse  

---

## 📈 Future Improvements

- Multi-threading for faster scanning  
- Stealth scanning with random delays  
- Export results to JSON / CSV  
- Integration with Nmap for advanced scanning  

---

## 👨‍💻 Author

**Mohammad Mahdi Rasoul Amini**

- LinkedIn: https://www.linkedin.com/in/mohammadmahdirasoulamini  
- Medium: https://medium.com/@mohamadmahdiamini122

