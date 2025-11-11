# Password Generator & Cracking Simulator 🔐

![Password Generator](https://img.shields.io/badge/Password-Generator-brightgreen)
![Security](https://img.shields.io/badge/Security-Education-orange)
![Dark Mode](https://img.shields.io/badge/Dark-Mode-success)
![Responsive](https://img.shields.io/badge/Responsive-Design-blue)

A professional web application that generates strong passwords and simulates how long they would take to crack using brute force methods. Built with a sleek dark mode interface and real-time strength analysis.

![Project Preview](https://via.placeholder.com/800x400/0f0c29/ffffff?text=Password+Generator+%26+Cracking+Simulator)

## 🌟 Live Demo

[![Cloudflare Pages](https://img.shields.io/badge/🚀_Live_Demo-Click_Here-orange?style=for-the-badge&logo=cloudflare)](https://your-project.pages.dev)

## ✨ Features

### 🔒 Core Functionality
- **Strong Password Generation** with customizable length (6-300 characters)
- **Multiple Character Sets**: Uppercase, lowercase, numbers, and symbols
- **Real-time Strength Analysis** with visual indicators
- **Brute-force Cracking Simulation** with animated progress
- **One-click Copy** to clipboard functionality

### 🎨 User Experience
- **Professional Dark Theme** with gradient backgrounds
- **Responsive Design** that works on all devices
- **Interactive UI** with smooth animations and transitions
- **Visual Feedback** with color-coded strength meters
- **Mood-based Messages** showing password strength emotions

### 🔬 Educational Value
- **Password Entropy Calculations**
- **Brute-force Attack Visualization**
- **Security Best Practices** demonstration
- **Real-time Cracking Time Estimates**

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| **HTML5** | Structure & Semantics |
| **CSS3** | Styling & Animations |
| **Brython** | Python runtime in browser |
| **JavaScript** | Browser APIs & Clipboard |
| **Cloudflare Pages** | Deployment & Hosting |

## 📦 Installation

### Local Development
```bash
# Clone the repository
git clone https://github.com/its-xths/generate-n-crack.git

# Navigate to project directory
cd password-generator

# Open in your browser
# Simply open home.html in any modern web browser
```

### Requirements
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (for Brython CDN)
- No additional dependencies required

## 🎮 How to Use

1. **Set Password Length**
   - Choose between 6-300 characters (12 recommended)

2. **Select Character Types**
   - ✅ Uppercase letters (A-Z)
   - ✅ Lowercase letters (a-z)
   - ✅ Numbers (0-9)
   - ✅ Symbols (!@#$%^&*)

3. **Generate Password**
   - Click "Generate Password" button
   - View your secure password
   - Check strength indicator and mood message

4. **Simulate Cracking**
   - Click "Simulate Cracking Process"
   - Watch colorful progress animation
   - See estimated real-world cracking time

5. **Copy & Use**
   - Click "Copy" button to copy password
   - Use for your accounts and applications

## 🔬 Technical Implementation

### Password Generation Algorithm
```python
def generate_password(length, use_upper, use_lower, use_numbers, use_symbols):
    # Ensures at least one character from each selected type
    # Fills remaining positions randomly
    # Uses cryptographically secure random selection
```

### Strength Calculation
- **Character Set Analysis**: 26 uppercase + 26 lowercase + 10 numbers + 10 symbols
- **Entropy Calculation**: `log2(character_set_size ^ password_length)`
- **Cracking Time**: Based on 1 trillion guesses/second assumption

### Security Features
- Client-side only processing (no data sent to servers)
- Secure random number generation
- No password storage or logging
- Input validation and sanitization

## 📱 Responsive Design

The application is fully responsive and optimized for:
- **Desktop** (1200px+)
- **Tablet** (768px - 1199px)
- **Mobile** (320px - 767px)

## 🎨 UI/UX Features

### Dark Theme Colors
- **Primary Gradient**: `#667eea` to `#764ba2`
- **Background**: `#0f0c29` to `#24243e`
- **Cards**: `rgba(30, 30, 46, 0.8)` with backdrop blur
- **Text**: `#f7fafc` with proper contrast ratios

### Interactive Elements
- Hover effects and smooth transitions
- Glowing borders and shadows
- Animated progress bars
- Visual feedback for all actions

## 📊 Password Strength Scale

| Strength | Color | Mood Message | Typical Cracking Time |
|----------|-------|--------------|---------------------|
| **Weak** | 🔴 Red | "Harshit is sad" | Seconds to minutes |
| **Medium** | 🟠 Orange | "Harshit is okay" | Hours to days |
| **Strong** | 🔵 Blue | "Harshit is happy" | Months to years |
| **Very Strong** | 🟢 Green | "Harshit is very happy" | Centuries to millennia |

## 🔧 Customization

### Modify Character Sets
Edit the `punctuation_char()` function in Brython code:
```python
def punctuation_char():
    # Change this string to modify allowed symbols
    allowed_punctuation = "!@#$%^&*()"
    return random.choice(allowed_punctuation)
```

### Adjust Color Scheme
Modify CSS variables in the style section:
```css
.student-card {
    background: rgba(30, 30, 46, 0.8); /* Change card background */
    border: 1px solid rgba(102, 126, 234, 0.2); /* Change border color */
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines
- Follow existing code style
- Test on multiple browsers
- Ensure mobile responsiveness
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Harshit Sharma** 
- 💼 **Project**: Academic Project for External Practical Examination
- 📧 **Contact**: [harshitsharma.xt@gmail.com](mailto:harshitsharma.xt@gmail.com)
- 🔗 **Linkdin**: [@xtharshitsharma](https://www.linkedin.com/in/xtharshitsharma/)

## 🙏 Acknowledgments

- **Brython Team** for enabling Python in browsers
- **Cloudflare** for free hosting and global CDN
- **Modern CSS** community for design inspiration
- **Security Researchers** for password strength methodologies

## 📚 Learn More

### Password Security Best Practices
- Use at least 12 characters
- Combine multiple character types
- Avoid dictionary words and patterns
- Use unique passwords for different services
- Consider using a password manager

### Related Concepts
- **Brute-force Attacks**
- **Password Entropy**
- **Cryptographic Hashing**
- **Two-Factor Authentication**

---

<div align="center">

### ⭐ Don't forget to star this repository if you find it useful!

**Built with ❤️ using HTML, CSS, and Brython**

![Last Updated](https://img.shields.io/badge/Last_Updated-2025--DEC--11-green)
![Version](https://img.shields.io/badge/Version-1.0.0-blue)

</div>
