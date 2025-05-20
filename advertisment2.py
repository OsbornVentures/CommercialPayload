import time
import sys
import os
import random

# Function to simulate progress bar at the top of the terminal
def progress_bar(current, total, bar_length=30):
    percent = (current / total) * 100
    bar = ('█' * int(bar_length * (current / total))).ljust(bar_length)
    sys.stdout.write(f'\r[{bar}] {percent:.0f}% BitsNBytes.ai Uploading...')
    sys.stdout.flush()

# Function to display and clear each message with random colors for the first 20 seconds
def display_message_with_color(message, delay, current, total):
    # List of ANSI color codes
    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
    ]
    color = random.choice(colors)  # Pick a random color
    progress_bar(current, total)  # Keep the progress bar at the top
    sys.stdout.write(f"\n{color}{message}\033[0m\n")  # Display message with random color
    sys.stdout.flush()
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for next message

# Function to display the last 10-second messages in green without clearing and with the progress bar static
def display_final_message(message, delay):
    sys.stdout.write(f"\n{message}\n")  # Display message
    sys.stdout.flush()
    time.sleep(delay)

# Clear screen to start the script
os.system('cls' if os.name == 'nt' else 'clear')

# Total time for the progress bar to fill (20 seconds)
progress_duration = 20
num_messages = 60  # Total number of messages
message_interval = progress_duration / num_messages  # Time per message for the first 20 seconds

# Scary terms and eBook quotes for the first 20 seconds
messages = [
    "Injecting payload...",
    "Payload Uploaded...",
    "Deploying payload...",
    "Craft a tapestry where the digital realm becomes a double-edged sword...",
    "Connecting yet isolating, enlightening yet misleading...",
    "Privacy would become an antiquated concept...",
    "Personal lives open books for those who know where to look...",
    "Fuel the flames of consumerism, making disposability and excess virtues...",
    "While the planet's silent pleas go unheeded...",
    "Wealth of knowledge available would be overshadowed by misinformation...",
    "Making truth a relic of the past, hard to discern and uphold...",
    "Social divides would deepen...",
    "The greatest commodity wouldn't be oil or gold, but attention...",
    "Easily manipulated and sold to the highest bidder...",
    "Truth is obscured by layers of digital mirage...",
    "Where every click feeds an echo chamber...",
    "Commodifying privacy...",
    "Turning personal secrets into currency of the digital realm...",
    "Traded and profited upon by unseen giants...",
    "Education diluted with distractions...",
    "Knowledge overshadowed by sensationalism...",
    "Creating generations skilled in the trivial...",
    "Yet strangers to wisdom...",
    "Blurring the lines between truth and misinformation...",
    "Creating a world where facts are malleable...",
    "Technology advances at a pace where humanity struggles...",
    "Breeding dependency while eroding privacy...",
    "Under the guise of digital connectivity...",
    "Loneliness and isolation hidden behind false camaraderie...",
    "Consumerism becomes the creed, sustainability the sacrifice...",
    "The planet's resources dwindle, masked by short-term gains...",
    "The greatest challenge is discerning the real from the virtual...",
    "The humane from the mechanical...",
    "The essence of what it means to be human eroded...",
    "AI is shrouded in secrecy, accessible to an elite few...",
    "Deepening societal divides...",
    "Scarcity repackaged as minimalism...",
    "Acts of charity disguised for self-interest...",
    "Manipulating genuine goodwill for hidden agendas...",
    "Personal privacy becomes the ultimate currency...",
    "Traded on digital marketplaces...",
    "Every secret commodified for the gain of invisible overlords...",
    "Wars no longer need traditional justifications...",
    "Fought on economic fronts, cyberspace, shadows...",
    "True costs obscured by technological prowess...",
    "The pursuit of knowledge corrupted by profit...",
    "The future is crazy...",
    "But we can help."
]

# Display the scary terms for the first 20 seconds and fill the progress bar
for i in range(0, 60):
    if i < len(messages):
        display_message_with_color(messages[i], message_interval, i, num_messages)

# Progress bar reaches 100% and stays at the top
sys.stdout.write(f"\r[{'█' * 30}] 100% BitsNBytes.ai Upload Completed\n")
sys.stdout.flush()

# The last 10 seconds: customer engagement messages in green with progress bar at 100%
final_messages = [
    "Is your computer being weird? Bring it in today for a tune up!",
    "Visit Bitsnbytes.ai to schedule an appointment or call 254-262-2375 today!",
    "Bits N Bytes in Lorena, TX can help!",
    "We service and sell desktops, laptops, 3D printers.",
    "We offer consultations, programming services, and more."
]

# Display the final 10-second messages in green without clearing
for message in final_messages:
    display_final_message(message, 1)

# Final message stays on screen
sys.stdout.write("\nBits N Bytes can Help | 254-262-2375 | Based in Lorena, TX\n")
sys.stdout.flush()
