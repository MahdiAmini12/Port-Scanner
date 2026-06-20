# Port Scanner Tool

A simple educational port scanner written in Python using the `socket` library.  
Designed for learning network reconnaissance and basic red team techniques.

---

## 🎯 Features
- Scan a single IP or hostname
- Scan a range of ports (e.g. 1-1000)
- Show open, closed and filtered ports
- Basic command-line interface
- Error handling

---

## 🛠️ How to Use

```bash
# Clone the repository
git clone https://github.com/MahdiAmini12/Port-Scanner.git
cd Port-Scanner

# Run the scanner
python main.py
Example Usage
Bashpython main.py -t 192.168.1.1 -p 1-500

⚠️ Important Note
This tool is for educational and authorized testing purposes only.
Do not use this tool on any system or network that you do not own or do not have explicit permission to test. Unauthorized scanning may be illegal.

🧠 Technologies Used

Python 3
socket library
argparse for command-line arguments


📈 Future Improvements (Roadmap)

Multi-threading for faster scanning
Stealth scanning techniques (random delays)
Output results to JSON or CSV file
Better integration with tools like Nmap


👤 Author
Mohammad Mahdi Rasoul Amini
LinkedIn | Medium
