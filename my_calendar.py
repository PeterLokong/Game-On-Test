import calendar 
from colorama import Fore, Back, Style, init

#initialize colorama
init(autoreset=True)

#Function to print a classy calendar
def print_classy_calendar(year, month):
    
    #Title
    print(Fore.CYAN + Style.BRIGHT + "🎉 Welcome to Your Classy Calendar for the year of your choice! 🎉\n")

    #Let us display the calendar with some bit of style
    print(Fore.GREEN + Style.BRIGHT + f"Here is the calendar for {calendar.month_name[month]} {year}: Hope you'l Like it!\n")

    #Get the calendar for the specific Month and Year
    cal = calendar.month(year, month)

    #The we add some decorations for a classic touch
    print(Fore.YELLOW + Style.BRIGHT + f"{'-'*40}")
    print(Fore.MAGENTA + cal)
    print(Fore.YELLOW + "=" * 40)

    # Let us make it fun and Add ASCII Cartoon
def print_ascii_cartoon():
    cartoon = """
    (づ｡◕‿‿◕｡)づ  
    Keep smiling! Your calendar is ready!Hehehehe!!! ✨
    (｡♥‿♥｡)
     """
    print(Fore.CYAN + Style.BRIGHT + cartoon)


    # Get user input for year and month
year = int(input(Fore.YELLOW + "Enter the year (e.g., 2024): "))
month = int(input(Fore.YELLOW + "Enter the month (1-12): "))

#Call the function to print the calendar
print_classy_calendar(year, month)

#Call the function to print the ASCII Cartoon
print_ascii_cartoon()
