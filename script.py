from browser import document, window, timer
import random
import string
import math

# ---------- Password Predictability Analysis ----------
COMMON_PATTERNS = [
    "password", "123", "admin", "qwerty", "letmein", "welcome",
    "user", "login", "abc", "iloveyou", "master", "hello",
    "monkey", "sunshine", "princess", "welcome", "football",
    "baseball", "mustang", "superman", "password1", "123456",
    "12345678", "123456789", "1234567890", "qwerty123", "1q2w3e4r"
]


_transition_counts = {}
_total_transitions = 0
for p in COMMON_PATTERNS:
    for i in range(len(p) - 1):
        a, b = p[i], p[i+1]
        _transition_counts.setdefault(a, {})
        _transition_counts[a][b] = _transition_counts[a].get(b, 0) + 1
        _total_transitions += 1


_transition_probs = {}
for a, targets in _transition_counts.items():
    s = float(sum(targets.values()))
    _transition_probs[a] = {b: targets[b] / s for b in targets}


class PredictabilityAnalyzer:
    @staticmethod
    def entropy(password):
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digits = any(c.isdigit() for c in password)
        has_symbols = any(not c.isalnum() for c in password)

        char_set = 0
        if has_lower: char_set += 26
        if has_upper: char_set += 26
        if has_digits: char_set += 10
        if has_symbols: char_set += 32 
        if char_set == 0:
            char_set = 26

        bits = math.log2(char_set) * len(password)
        return bits, char_set, {'upper': has_upper, 'lower': has_lower, 'digits': has_digits, 'symbols': has_symbols}

    @staticmethod
    def brute_force_predictability(entropy_bits, password_length, char_set_size):

        max_entropy = 128  
        
      
        predictability = 1.0 - min(1.0, entropy_bits / max_entropy)
        
    
        length_factor = max(0, (20 - password_length) / 20)  
        predictability += length_factor * 0.3
        
        
        char_set_factor = max(0, (94 - char_set_size) / 94) 
        predictability += char_set_factor * 0.2
        
        return min(1.0, predictability)

    @staticmethod
    def markov_score(password):
        
        pscore = 0.0
        pw = password.lower()

      
        pattern_matches = 0
        for pat in COMMON_PATTERNS:
            if pat in pw:
                pattern_matches += 1
                pscore += 0.4 

     
        trans_score = 0.0
        trans_count = 0
        for i in range(len(pw)-1):
            a, b = pw[i], pw[i+1]
            if a in _transition_probs and b in _transition_probs[a]:
                trans_score += _transition_probs[a][b]
                trans_count += 1
        
        if trans_count > 0:
            trans_avg = trans_score / trans_count
            pscore += trans_avg * 0.6

       
        pscore = max(0.0, min(1.0, pscore))
        
        return pscore

    @staticmethod
    def get_predictability_level(score):
        if score >= 0.7:
            return "High", "#e74c3c"
        elif score >= 0.4:
            return "Medium", "#f39c12"
        elif score >= 0.2:
            return "Low", "#3498db"
        else:
            return "Very Low", "#2ecc71"

    @staticmethod
    def get_overall_assessment(brute_force_score, markov_score):
        avg_score = (brute_force_score + markov_score) / 2
        if avg_score >= 0.6:
            return "Highly Predictable - Easy to crack"
        elif avg_score >= 0.4:
            return "Moderately Predictable - Could be stronger"
        elif avg_score >= 0.2:
            return "Fairly Unpredictable - Good security"
        else:
            return "Very Unpredictable - Excellent security"



def lowercase_char():
    return random.choice(string.ascii_lowercase)

def uppercase_char():
    return random.choice(string.ascii_uppercase)

def digits_char():
    return random.choice(string.digits)

def punctuation_char():
    return random.choice("!@#$%^&*")

def strong_password_core(length):
    core_chars = []
    if document["uppercase"].checked: core_chars.append(uppercase_char())
    if document["lowercase"].checked: core_chars.append(lowercase_char())
    if document["numbers"].checked: core_chars.append(digits_char())
    if document["symbols"].checked: core_chars.append(punctuation_char())

    if not core_chars:
        core_chars = [uppercase_char(), lowercase_char(), digits_char(), punctuation_char()]

    core_indexes = random.sample(range(length), min(len(core_chars), length))
    password_core = [None] * length

    for i, index in enumerate(core_indexes):
        password_core[index] = core_chars[i]

    return password_core

def strong_password_core_wrap(password_core):
    char_pool = ""
    if document["uppercase"].checked: char_pool += string.ascii_uppercase
    if document["lowercase"].checked: char_pool += string.ascii_lowercase
    if document["numbers"].checked: char_pool += string.digits
    if document["symbols"].checked: char_pool += "!@#$%^&*"

    if not char_pool:
        char_pool = string.ascii_letters + string.digits + "!@#$%^&*"

    for i in range(len(password_core)):
        if password_core[i] is None:
            password_core[i] = random.choice(char_pool)
    return "".join(password_core)

def update_password_display(password, is_custom=False):
    document["password"].text = password

    if password and not password.startswith("Please") and not password.startswith("No password"):
  
        entropy_bits, char_set_size, char_flags = PredictabilityAnalyzer.entropy(password)
        brute_force_score = PredictabilityAnalyzer.brute_force_predictability(entropy_bits, len(password), char_set_size)
        markov_score_value = PredictabilityAnalyzer.markov_score(password)
        
      
        brute_force_level, brute_force_color = PredictabilityAnalyzer.get_predictability_level(brute_force_score)
        markov_level, markov_color = PredictabilityAnalyzer.get_predictability_level(markov_score_value)
        overall_assessment = PredictabilityAnalyzer.get_overall_assessment(brute_force_score, markov_score_value)

       
        document["password-length"].text = f"{len(password)} characters"
        document["character-set"].text = f"~{char_set_size} possible chars"
        document["entropy-bits"].text = f"{entropy_bits:.1f} bits"

    
        document["bruteforce-score"].text = brute_force_level
        document["bruteforce-score"].style.color = brute_force_color
        document["bruteforce-desc"].text = f"Score: {brute_force_score:.3f} - Based on entropy and search space"
        
        document["markov-score"].text = markov_level
        document["markov-score"].style.color = markov_color
        document["markov-desc"].text = f"Score: {markov_score_value:.3f} - Pattern-based analysis"

       
        overall_score = (brute_force_score + markov_score_value) / 2
        strength = 100 - (overall_score * 100)  
        strength_bar = document["strength-bar"]
        strength_text = document["strength-text"]
        strength_bar.style.width = f"{strength}%"

       
        if strength < 40:
            strength_bar.style.backgroundColor = "#e74c3c"
            strength_level = "Weak"
        elif strength < 70:
            strength_bar.style.backgroundColor = "#f39c12"
            strength_level = "Moderate"
        elif strength < 90:
            strength_bar.style.backgroundColor = "#3498db"
            strength_level = "Strong"
        else:
            strength_bar.style.backgroundColor = "#2ecc71"
            strength_level = "Very Strong"

        strength_text.textContent = f"Security Level: {strength_level} - {overall_assessment}"

        # Update predictability result
        res = document["predictability-result"]
        if overall_score >= 0.5:
            res.text = f"⚠️ This password shows high predictability patterns. Consider using a longer password with more character variety."
            res.style.background = "#fce4e4"
            res.style.color = "#b71c1c"
        else:
            res.text = f"✅ Good! This password shows low predictability with strong security characteristics."
            res.style.background = "#e8f8f5"
            res.style.color = "#065f46"

        if is_custom:
            res.text = "Custom password analysis - " + res.text
    else:
        # Reset all fields
        reset_analysis()

# ----------------- Event Handlers -----------------
def generate_password(event):
    try:
        length = int(document["length"].value)
        if length < 6 or length > 50:
            document["password"].text = "Please enter length between 6-50"
        else:
            password_core = strong_password_core(length)
            password = strong_password_core_wrap(password_core)
            update_password_display(password)
    except ValueError:
        document["password"].text = "Please enter valid number"

def analyze_custom_password(event):
    custom_password = document["custom-password"].value.strip()
    if not custom_password:
        document["password"].text = "Please enter a custom password"
        return
    if len(custom_password) < 4:
        document["password"].text = "Password too short (min 4 characters)"
        return
    update_password_display(custom_password, is_custom=True)

def copy_password(event):
    password = document["password"].text
    if password and not password.startswith("Please") and not password.startswith("No password"):
        window.navigator.clipboard.writeText(password).then(
            lambda: window.alert("Password copied!"),
            lambda: window.alert("Copy failed")
        )
    else:
        window.alert("No password to copy")

def toggle_mode(event):
    for btn in document.select(".toggle-btn"):
        btn.classList.remove("active")
    for section in document.select(".mode-section"):
        section.classList.remove("active")
    event.target.classList.add("active")
    if event.target.id == "toggle-random":
        document["random-section"].classList.add("active")
        document["password"].text = "No password generated yet"
        reset_analysis()
    else:
        document["custom-section"].classList.add("active")
        document["password"].text = "Enter custom password above"
        reset_analysis()

def reset_analysis():
    document["password-length"].text = "-"
    document["character-set"].text = "-"
    document["entropy-bits"].text = "-"
    document["bruteforce-score"].text = "-"
    document["bruteforce-score"].style.color = "#a0aec0"
    document["markov-score"].text = "-"
    document["markov-score"].style.color = "#a0aec0"
    document["bruteforce-desc"].text = "Based on entropy and search space"
    document["markov-desc"].text = "Pattern-based predictability analysis"
    document["strength-bar"].style.width = "0%"
    document["strength-text"].text = ""
    document["predictability-result"].text = "Generate or enter a password to analyze predictability"
    document["predictability-result"].style.background = "rgba(30, 30, 46, 0.8)"
    document["predictability-result"].style.color = "#a0aec0"
def initialize_app():
    document["generate"].bind("click", generate_password)
    document["analyze-custom"].bind("click", analyze_custom_password)
    document["copy-btn"].bind("click", copy_password)
    document["toggle-random"].bind("click", toggle_mode)
    document["toggle-custom"].bind("click", toggle_mode)
    
    document["password"].text = "No password generated yet"
    reset_analysis()

timer.set_timeout(initialize_app, 100)
