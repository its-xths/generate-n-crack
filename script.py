from browser import document, window, timer
import random
import string
import math

# Function to return a random lowercase character
def lowercase_char():
    return random.choice(string.ascii_lowercase)

# Function to return a random uppercase character
def uppercase_char():
    return random.choice(string.ascii_uppercase)

# Function to return a random digit
def digits_char():
    return random.choice(string.digits)

# Function to return a random punctuation character
def punctuation_char():
    allowed_punctuation = "!@#$%^&*()"
    return random.choice(allowed_punctuation)

# Function to create the core of the strong password
def strong_password_core(length):
    core_chars = []
    
    # Only add character types that are enabled
    if document["uppercase"].checked:
        core_chars.append(uppercase_char())
    if document["lowercase"].checked:
        core_chars.append(lowercase_char())
    if document["numbers"].checked:
        core_chars.append(digits_char())
    if document["symbols"].checked:
        core_chars.append(punctuation_char())
    
    # If no character types are selected, use all
    if not core_chars:
        core_chars = [uppercase_char(), lowercase_char(), digits_char(), punctuation_char()]
    
    # Ensure we have at least one of each selected type
    core_indexes = random.sample(range(length), min(len(core_chars), length))
    password_core = [None] * length
    
    for i, index in enumerate(core_indexes):
        password_core[index] = core_chars[i]
    
    return password_core

# Function to wrap the password core and fill the remaining characters
def strong_password_core_wrap(password_core):
    # Create a pool of characters based on selected options
    char_pool = ""
    if document["uppercase"].checked:
        char_pool += string.ascii_uppercase
    if document["lowercase"].checked:
        char_pool += string.ascii_lowercase
    if document["numbers"].checked:
        char_pool += string.digits
    if document["symbols"].checked:
        char_pool += "!@#$%^&*()"
    
    # If no options selected, use all character types
    if not char_pool:
        char_pool = string.ascii_letters + string.digits + "!@#$%^&*()"
    
    for i in range(len(password_core)):
        if password_core[i] is None:
            password_core[i] = random.choice(char_pool)
    return "".join(password_core)

# Function to calculate password strength
def calculate_strength(password):
    length = len(password)
    
    # Calculate character set size
    char_set_size = 0
    if any(c in string.ascii_lowercase for c in password):
        char_set_size += 26
    if any(c in string.ascii_uppercase for c in password):
        char_set_size += 26
    if any(c in string.digits for c in password):
        char_set_size += 10
    if any(c in "!@#$%^&*()" for c in password):
        char_set_size += 10
    
    # Calculate possible combinations
    combinations = char_set_size ** length
    
    # Estimate time to crack (assuming 1e12 guesses per second for a powerful computer)
    seconds = combinations / 1e12
    
    # Convert to human readable time
    if seconds < 60:
        time_text = f"{seconds:.2f} seconds"
        strength = 25
    elif seconds < 3600:
        time_text = f"{seconds/60:.2f} minutes"
        strength = 50
    elif seconds < 86400:
        time_text = f"{seconds/3600:.2f} hours"
        strength = 75
    else:
        years = seconds / 31536000
        if years > 1000000:
            time_text = "Over a million years"
            strength = 100
        else:
            time_text = f"{years:.2f} years"
            strength = min(100, 75 + (years / 1000) * 25)
    
    return strength, time_text, combinations

# Function to update strength meter
def update_strength_meter(password):
    strength, time_text, combinations = calculate_strength(password)
    
    strength_bar = document["strength-bar"]
    strength_text = document["strength-text"]
    
    # Update strength bar
    strength_bar.style.width = f"{strength}%"
    
    # Set color based on strength
    if strength < 40:
        strength_bar.style.backgroundColor = "#e74c3c"  # Red
        strength_level = "Weak"
        mood = "Harshit is sad"
    elif strength < 70:
        strength_bar.style.backgroundColor = "#f39c12"  # Orange
        strength_level = "Medium"
        mood = "Harshit is okay"
    elif strength < 90:
        strength_bar.style.backgroundColor = "#3498db"  # Blue
        strength_level = "Strong"
        mood = "Harshit is happy"
    else:
        strength_bar.style.backgroundColor = "#2ecc71"  # Green
        strength_level = "Very Strong"
        mood = "Harshit is very happy"
    
    strength_text.textContent = f"Strength: {strength_level}, {mood}"

# Function to generate password when the button is clicked
def generate_password(event):
    try:
        length = int(document["length"].value)
        if length < 4 or length > 300:
            document["password"].text = "Please enter a length between 4 and 300."
            document["strength-text"].text = ""
            document["strength-bar"].style.width = "0%"
        else:
            password_core = strong_password_core(length)
            password = strong_password_core_wrap(password_core)
            document["password"].text = password
            update_strength_meter(password)
            document["cracking-result"].text = "Click 'Simulate Cracking Process' to see the simulation"
            document["cracking-progress"].style.width = "0%"
    except ValueError:
        document["password"].text = "Please enter a valid number."
        document["strength-text"].text = ""
        document["strength-bar"].style.width = "0%"

# Function to copy password to clipboard
def copy_password(event):
    password = document["password"].text
    window.navigator.clipboard.writeText(password).then(
        lambda: window.alert("Password copied to clipboard!"),
        lambda: window.alert("Failed to copy password")
    )

# Function to simulate password cracking
def simulate_cracking(event):
    password = document["password"].text
    if not password or password.startswith("Please"):
        window.alert("Please generate a password first")
        return
    
    strength, time_text, combinations = calculate_strength(password)
    
    # Reset progress bar
    progress_bar = document["cracking-progress"]
    progress_bar.style.width = "0%"
    
    # Colors for the animated progress bar
    colors = [
        "#ff0000", "#ff4000", "#ff8000", "#ffbf00", 
        "#ffff00", "#bfff00", "#80ff00", "#40ff00", 
        "#00ff00", "#00ff40", "#00ff80", "#00ffbf", 
        "#00ffff", "#00bfff", "#0080ff", "#0040ff", 
        "#0000ff", "#4000ff", "#8000ff", "#bf00ff", 
        "#ff00ff", "#ff00bf", "#ff0080", "#ff0040"
    ]
    
    # Animate the cracking process
    duration = 3000  # 3 seconds animation
    steps = 100
    step_duration = duration / steps
    
    def update_progress(step):
        progress = (step / steps) * 100
        progress_bar.style.width = f"{progress}%"
        
        # Change color based on progress
        if step < steps:
            color_index = int((step / steps) * (len(colors) - 1))
            progress_bar.style.background = f"linear-gradient(90deg, {colors[color_index]}, {colors[(color_index + 6) % len(colors)]})"
        else:
            # When complete, set to green
            progress_bar.style.background = "#2ecc71"
        
        if step == steps:
            document["cracking-result"].text = f"Password cracked! Estimated real-world time: {time_text}"
        else:
            timer.set_timeout(lambda: update_progress(step + 1), step_duration)
    
    document["cracking-result"].text = "Cracking in progress..."
    update_progress(0)

# Set up event listeners
document["generate"].bind("click", generate_password)
document["copy-btn"].bind("click", copy_password)
document["simulate-cracking"].bind("click", simulate_cracking)