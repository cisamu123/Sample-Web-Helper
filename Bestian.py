import pyautogui as pg
pg.alert("Sites that I can open for you: yt and google WARNING: WRITE EVERYTHING AS WRITTEN IN THE EXAMPLE! WRITE EVERYTHING IN SMALL LETTERS! ", "Helper")
userInput = pg.prompt("Enter web-page: ", "Enterer")
yt = "yt"
google = "google"
twitch = "tw"
gmail = "gm"
translate = "tr"
maps = "mps"
drive = "dv"
docs = "dc"
clicker = "cl"
if userInput == yt:
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("www.youtube.com\n", 0)
	pg.hotkey("winleft", "up")
if userInput == google:
	GoogleuserInput = pg.prompt("Enter search query:  (Press Enter for skip)", "Enterer")
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("www.google.com\n", 0)
	pg.hotkey("winleft", "up")
	pg.typewrite(GoogleuserInput + "\n", 0)
if userInput == twitch:
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("twitch.tv\n", 0)
	pg.hotkey("winleft", "up")
if userInput == gmail:
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("mail.google.com\n", 0)
	pg.hotkey("winleft", "up")
if userInput == translate:
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("translate.google.com\n", 0)
	pg.hotkey("winleft", "up")
if userInput == maps:
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("www.google.com/maps\n", 0)
	pg.hotkey("winleft", "up")
if userInput == drive:
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("drive.google.com/drive/u/0/my-drive\n", 0)
	pg.hotkey("winleft", "up")
if userInput == docs:
	pg.hotkey("winleft")
	pg.typewrite("chrome\n", 0.1)
	pg.typewrite("docs.google.com/document/u/0/\n", 0)
	pg.hotkey("winleft", "up")