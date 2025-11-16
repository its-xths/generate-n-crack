# Generate-n-Crack: AI Password Analysis 🔐

A sophisticated web-based password analysis tool built with Brython, HTML, and CSS that evaluates password strength using advanced predictability algorithms including Brute Force analysis and Markov model pattern detection.

## 🌟 Features

### 🔒 Dual Analysis Methods
- **Brute Force Predictability**: Evaluates password strength based on entropy, length, and character set complexity
- **Markov Predictability**: Uses pattern recognition and character transition probabilities to detect common password structures

### 🎯 Two Input Modes
- **Random Generation**: Create secure passwords with customizable length and character sets
- **Custom Analysis**: Test your existing passwords against advanced predictability algorithms

### 📊 Comprehensive Security Metrics
- Real-time entropy calculation (in bits)
- Character set size analysis
- Visual strength meter with color-coded feedback
- Detailed predictability scoring

### 🎨 Modern UI/UX
- Glass-morphism design with dark theme
- Responsive layout for all devices
- Smooth animations and hover effects
- Intuitive card-based information display

## 🚀 Live Demo

[generate-n-crack](https://generate-n-crack.pages.dev/)

## 📸 Screenshots

<img width="1548" height="898" alt="image" src="https://github.com/user-attachments/assets/2fb25936-3ede-43d5-aa54-947bc8f482c1" />
<img width="887" height="302" alt="image" src="https://github.com/user-attachments/assets/88383714-5a67-4322-aa33-a055288e4646" />

## 🛠️ Installation

### Prerequisites
- Modern web browser with JavaScript enabled
- Python 3.7+ (for local development)
- Basic web server for local hosting

### Local Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/its-xths/generate-n-crack.git
   cd generate-n-crack
   ```

2. **Serve the files using a local server**
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   
   # Using PHP
   php -S localhost:8000
   ```

3. **Open your browser**
   Navigate to `http://localhost:8000`

### File Structure
```
generate-n-crack/
│
├── index.html          # Main application file
├── script.py           # Brython password analysis logic
├── design.css          # Styling and responsive design
└── README.md           # Project documentation
```

## 💡 How It Works

### Brute Force Predictability Algorithm
```python
# Based on information theory and entropy
- Calculates character set complexity (uppercase, lowercase, digits, symbols)
- Factors in password length and possible combinations
- Normalizes to a 0-1 predictability score
- Lower score = More secure against brute force attacks
```

### Markov Predictability Algorithm
```python
# Uses pattern recognition and statistical analysis
- Compares against common password patterns ("password", "123", etc.)
- Analyzes character transition probabilities
- Detects predictable sequences and common structures
- Lower score = More random and unpredictable
```

### Example Analysis
- **Weak Password**: "password123" 
  - Brute Force: Medium | Markov: High (common patterns detected)
- **Strong Password**: "X7#kL9$mN2@pQ"
  - Brute Force: Low | Markov: Low (high entropy, no patterns)

## 🎯 Usage

### Generating Random Passwords
1. Select "Generate Random" mode
2. Choose password length (6-50 characters)
3. Select character types (uppercase, lowercase, numbers, symbols)
4. Click "Generate Password"
5. View comprehensive analysis results

### Analyzing Custom Passwords
1. Select "Use Custom Password" mode  
2. Enter your password in the text field
3. Click "Analyze Custom Password"
4. Receive detailed predictability assessment

### Understanding Results
- **Green Indicators**: Strong security characteristics
- **Orange/Yellow Indicators**: Moderate security - consider improvements
- **Red Indicators**: High predictability - immediate changes recommended

## 🔬 Technical Details

### Built With
- **Frontend**: HTML5, CSS3 with modern flexbox/grid layouts
- **Client-side Python**: Brython 3.13.0
- **Styling**: Custom CSS with glass-morphism effects
- **Icons**: Font Awesome 6.4.0

### Algorithms Implemented
1. **Entropy Calculation** - Shannon entropy based on character set diversity
2. **Markov Chain Analysis** - Pattern recognition using transition matrices
3. **Brute Force Resistance** - Combinatorial complexity assessment
4. **Common Pattern Detection** - Dictionary-based predictability scoring

### Browser Compatibility
- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests or open issues for bugs and feature requests.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Brython community for client-side Python execution
- Font Awesome for beautiful icons
- Modern CSS techniques for the UI design
- Cybersecurity researchers for password analysis methodologies

## 🔒 Security Note

This tool is designed for educational purposes and password strength awareness. While it uses advanced analysis methods, real-world password security depends on many factors including hashing algorithms, salting, and overall system security practices.

---

**⭐ Star this repo if you find it helpful!**

**🔔 Watch for updates and new features!**
