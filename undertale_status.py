# UNDERTALE Discord status - shows your area, boss, route and stats.
# It reads your save files, so it updates each time you SAVE in-game.
import os, re, subprocess, sys, time
from pypresence import Presence

CLIENT_ID = "1563449579960279081"
ICON = "https://cdn.cloudflare.steamstatic.com/steam/apps/391540/header.jpg"
FOLDER = os.path.join(os.environ["LOCALAPPDATA"], "UNDERTALE")
SAVE = os.path.join(FOLDER, "file0")

# Route shown on your status. Set to None to have it guessed from your save instead.
ROUTE_OVERRIDE = None

ROOMS = [
"Initializer [Dogchecked]",
"Introduction [Dogchecked]",
"Title [Dogchecked]",
"Menu [Dogchecked]",
"Ruins - Starting point",
"Ruins - Flowey spot",
"Ruins - Entrance [SAVE]",
"Ruins - Toriel stepping tile puzzle",
"Ruins - Switch puzzle",
"Ruins - Dummy room",
"Ruins - Spike puzzle",
"Ruins - Long corridor",
"Ruins - Leaf Pile [SAVE]",
"Ruins - Candy pillar",
"Ruins - Mandatory fall trapdoor",
"Ruins - First stone pushing puzzle",
"Ruins - Trapdoor corridor puzzle",
"Ruins - Talkback rock",
"Ruins - Mouse Hole [SAVE]",
"Ruins - Napstablook",
"Ruins - Spider Bake Sale",
"Ruins - 2 frogs",
"Ruins - Switch hidden under trapdoor puzzle",
"Ruins - 3 Pillars room 1",
"Ruins - 3 Pillars room 2",
"Ruins - 3 Pillars room 3",
"Ruins - 3 Pillars room 4",
"Ruins - Pillars room pit",
"Ruins - 3-way fork",
"Ruins - Toriel gossip frog",
"Ruins - Toy knife room",
"Ruins - Home [SAVE]",
"Toriel's House: Entrance",
"Toriel's House: Reading room",
"Toriel's House: Corridor",
"Toriel's House: Toriel's Room",
"Toriel's House: Your Room",
"Toriel's House: Kitchen",
"Toriel's Basement 1",
"Toriel's Basement 2",
"Toriel's Basement 3",
"Toriel's Basement: Toriel Boss Battle",
"Toriel's Basement: Corridor to Flowey",
"Toriel's Basement: Flowey",
"Snowdin - Ruin exit",
"Snowdin - Dark forest path",
"Snowdin - Box Road [SAVE]",
"Snowdin - Fishing rod",
"Snowdin - Papyrus' Sentry Station",
"Snowdin - Doggo",
"Snowdin - Compass sign",
"Snowdin - Snowman",
"Snowdin - Electricity Maze",
"Snowdin - Snow golf",
"Snowdin - 2 guard dog houses",
"Snowdin - Monster Kidz Word Search",
"Snowdin - Spaghetti [SAVE]",
"Snowdin - Warning: Dog Marriage",
"Snowdin - XO puzzle 1",
"Snowdin - XO puzzle 2",
"Snowdin - Color tile puzzle",
"Snowdin - Dog House [SAVE]",
"Snowdin - Snow Papyrus & Sans",
"Snowdin - Sliding XO puzzle",
"Snowdin - Teleporting Sans",
"Snowdin - Ice Cave entrance",
"Snowdin - Snow poffs (Greater Dog)",
"Snowdin - Gauntlet of Deadly Terror",
"Snowdin - Town [SAVE]",
"Snowdin Town: Ice haul wolf",
"Snowdin Town: Boat harbor",
"Snowdin Town: Inn lobby",
"Snowdin Town: Inn bedroom",
"Snowdin Town: Grillby's",
"Snowdin Town: Library",
"Snowdin Town: Papyrus's shed",
"Snowdin Town: Papyrus and Sans's house",
"Snowdin Town: Papyrus's room",
"Snowdin Town: Sans's room [Dogchecked]",
"Snowdin Town: Sans's room (dark) [Dogchecked]",
"Snowdin Town: Sans's basement [Dogchecked]",
"Snowdin - Papyrus Battle",
"Waterfall - Entrance",
"Waterfall - Checkpoint [SAVE]",
"Waterfall - Falling rocks",
"Waterfall - Tutu room",
"Waterfall - Hallway [SAVE]",
"Waterfall - Lily pad bridge",
"Waterfall - Lily pad vertical bridge",
"Waterfall - Quiche room",
"Waterfall - Telescope",
"Waterfall - Boat plank",
"Waterfall - Undyne Spear dodging 1",
"Waterfall - Bush after spear dodging",
"Waterfall - Crystal [SAVE]",
"Waterfall - Sans Telescope",
"Waterfall - Nice Cream Stand",
"Waterfall - Split Pathway",
"Waterfall - Ballet shoes",
"Waterfall - Duck",
"Waterfall - Onionsan",
"Waterfall - Artifact hub",
"Waterfall - Piano",
"Waterfall - Legendary Artifact",
"Waterfall - Rainy Statue",
"Waterfall - Umbrellas",
"Waterfall - Rainy Path 1",
"Waterfall - Rainy Path 2",
"Waterfall - Palace View",
"Waterfall - Umbrella ledge",
"Waterfall - Bridge [SAVE]",
"Waterfall - Bridge spear dodge",
"Waterfall - Bridge fall",
"Waterfall - Trash Zone Flower bed",
"Waterfall - Trash Zone [SAVE]",
"Waterfall - Training Dummy revenge",
"Waterfall - Quiet Area [SAVE]",
"Waterfall - Undyne's house entrance",
"Waterfall - Undyne's house interior",
"Waterfall - Twin Ghost houses",
"Waterfall - Napstablook's house interior",
"Waterfall - Hapstablook's house interior",
"Waterfall - Snail Farm",
"Waterfall - Pre Bird (Unused)",
"Waterfall - Turtle shop",
"Waterfall - River boat",
"Waterfall - 2 waterfalls",
"Waterfall - Mushroom maze",
"Waterfall - Temmie Village [SAVE]",
"Waterfall - Lamp maze",
"Waterfall - Behind you",
"Waterfall - More flowers",
"Waterfall - Cave bridge",
"Waterfall - Cave exit",
"Waterfall - Undyne area",
"Waterfall - Undyne area + 1",
"Waterfall - Hotland Welcome",
"Hotland - Entrance",
"Hotland - Water tank",
"Hotland - Laboratory Entrance [SAVE]",
"Hotland - River boat",
"Hotland - Laboratory Hub",
"Hotland - Laboratory Upper Floor",
"Hotland - Laboratory Exit",
"Hotland - Treadmills 1",
"Hotland - Magma Chamber [SAVE]",
"Hotland - Burnt Pan",
"Hotland - Lasers 1",
"Hotland - Puzzle Gate 1",
"Hotland - Left Boz Puzzle Entrance",
"Hotland - Left Box Puzzle",
"Hotland - Right Box Puzzle Entrance",
"Hotland - Right Box Puzzle",
"Hotland - Arrow bridge",
"Hotland - Kitchen",
"Hotland - Core View [SAVE]",
"Hotland - Elevator R1",
"Hotland - Elevator R2",
"Hotland - Hot Dog Stand",
"Hotland - Art Club Entrance",
"Hotland - Art Club",
"Hotland - Stained Apron",
"Hotland - Treadmill switch puzzle",
"Hotland - Arrow puzzle",
"Hotland - Bad Opinion Zone [SAVE]",
"Hotland - Bro guards",
"Hotland - Bombastic News report",
"Hotland - Upper Core View",
"Hotland - Elevator L2",
"Hotland - Elevator L3",
"Hotland - Spider Bake Sale",
"Hotland - F3 Puzzle Gate",
"Hotland - F3 South Puzzle Entrance",
"Hotland - F3 South Puzzle",
"Hotland - F3 North Puzzle Entrance",
"Hotland - F3 North Puzzle",
"Hotland - Spider Entrance [SAVE]",
"Hotland - Spider Room",
"Hotland - Mettaton Poster",
"Hotland - Theater Stage",
"Hotland - Colored Tile Maze 2",
"Hotland - Nice Cream Stand",
"Hotland - Hotel Entrance",
"Hotland - Hotel Lobby [SAVE]",
"Hotland - Hotel Restaurant",
"Hotland - Hotel Cordidor",
"Hotland - Hotel Alley",
"Hotland - Elevator R3",
"Hotland - Core Entrance",
"Hotland - Core Elevator",
"Hotland - Core Pit",
"Hotland - Core North of Elavator",
"Hotland - Core Wrong order lasers",
"Hotland - Core Crossroads",
"Hotland - Core Dead End",
"Hotland - Core Power Laser Puzzle",
"Hotland - Core Branch [SAVE]",
"Hotland - Core Ice Deposit",
"Hotland - Core West Puzzle Entrance",
"Hotland - Core West Puzzle Entrance + 1",
"Hotland - Core West Puzzle Entrance + 2",
"Hotland - Core East Money Trash Bin Entrance",
"Hotland - Core End - 3",
"Hotland - South of 100G Trash Can",
"Hotland - Core End - 4",
"Hotland - Core Get Lost",
"Hotland - Core West Puzzle",
"Hotland - Core Glamburger Trash Can",
"Hotland - Core 100G Trash Can",
"Hotland - Core Battle Bridge",
"Hotland - Core End - 1",
"Hotland - Core End [SAVE]",
"Hotland - Core Mettaton Room",
"Hotland - Core Final Elevator Entrance",
"Hotland - Elevator L1",
"Hotland - Core Final Elevator",
"Castle Elevator [SAVE]",
"Castle - Another Elevator",
"Castle - Dark Path",
"New Home [SAVE]",
"New Home - Entrance",
"New Home - Reading Room",
"New Home - Corridor",
"New Home - Asgore's Room",
"New Home - Your Room",
"New Home - Kitchen",
"New Home - Basement 1",
"New Home - Basement 2",
"New Home - Basement 3",
"New Home - Basement 4",
"New Home - Elevator",
"Last Corridor [SAVE]",
"Throne Entrance [SAVE]",
"Throne Entrance - Stairs Down",
"Throne Entrance - Coffins",
"Throne Room [SAVE]",
"The End [SAVE]",
"Barrier",
"Flowey post-battle",
"Neutral credits [Dogchecked]",
"Path to outside [Dogchecked]",
"Outside [Dogchecked]",
"Laboratory Elevator",
"True Lab - Elevator",
"True Lab - Elevator Entrance",
"True Lab - South Corridor",
"True Laboratory [SAVE]",
"True Lab - West Corridor 1",
"True Lab - West Sinks",
"True Lab - West red key slot",
"True Lab - North Corridor 1",
"True Lab - Bedroom [SAVE]",
"True Lab - Northeast Corridor",
"True Lab - Northeast blue key slot",
"True Lab - North Corridor 2",
"True Lab - Green key",
"True Lab - Northwest skull [SAVE?]",
"True Lab - Yellow Key Slot + TV",
"True Lab - Northwest refrigerators",
"True Lab - Green Key Slot",
"True Lab - Fans",
"True Lab - Elevator 2",
"True Lab - Power room corridor",
"True Lab - Power room",
"Gaster Room",
"Snowdin - Ice Cave 1",
"Snowdin - Developer Room [Dogchecked]",
"room2 [Dogchecked]",
"Waterfall - Mysteryman hallway [Dogchecked]",
"Waterfall - Mysteryman room [Dogchecked]",
"Snowdin - Sound Test Room [Dogchecked]",
"TESTROOM [Dogchecked]",
"Waterfall - Redacted [Dogchecked]",
"Waterfall - Cut Bridge Puzzle [Dogchecked]",
"room_overworld [Dogchecked]",
"room_overworld3 [Dogchecked]",
"Bullet Test [Dogchecked]",
"room_water16A [Dogchecked]",
"Pacifist credits [Dogchecked]",
"Pacifist credits - Highway [Dogchecked]",
"Pacifist credits - Beach [Dogchecked]",
"Pacifist credits - Mettaton performance [Dogchecked]",
"Pacifist credits - School entrance [Dogchecked]",
"Pacifist credits - Mount Ebott [Dogchecked]",
"Pacifist credits - Special Thanks [Dogchecked]",
"Pacifist credits - Bedroom [Dogchecked]",
"Pacifist credits - The End [Dogchecked]",
"Sprite Test [Dogchecked]",
"Settings menu [Dogchecked]",
"Control test room [Dogchecked]",
"Omega Flowey - Initializer [Dogchecked]",
"Omega Flowey - Fake intro [Dogchecked]",
"Omega Flowey - Fake menu [Dogchecked]",
"Omega Flowey - Fake save point [Dogchecked] [SAVE?]",
"Omega Flowey [Dogchecked]",
"Omega Flowey - Respawn mocking [Dogchecked]",
"room_fire4 [Dogchecked]",
"room_fire10_old [Dogchecked]",
"room_fire10A_old [Dogchecked]",
"Snowdin - Ice Puzzle [Dogchecked]",
"Ruins - Rock Candy [Dogchecked]",
"Snowdin - Growing snowball [Dogchecked]",
"Waterfall - Torch puzzle [Dogchecked]",
"Waterfall - Meet Undyne (Unused) [Dogchecked]",
"Waterfall - Rooted mushroom [Dogchecked]",
"room_monsteralign_test [Dogchecked]",
"Battle room [Dogchecked]",
"Flowey battle room [Dogchecked]",
"\"Fast\" battle room [Dogchecked]",
"New Home - Story battle room [Dogchecked]",
"Game Over [Dogchecked]",
"Snowdin Town - Shop [Dogchecked]",
"Waterfall - Gerson's shop [Dogchecked]",
"Hotland - Bratty and Catty [Dogchecked]",
"Hotland - Burgerpants [Dogchecked]",
"Waterfall - Tem Shop [Dogchecked]",
"River person transition room [Dogchecked]",
"Papyrus date [Dogchecked]",
"Alphys date [Dogchecked]",
"Omega Flowey - Wilting [Dogchecked]",
"Flowey's pacifist speech [Dogchecked]",
"room_empty [Dogchecked]",
"room_emptywhite [Dogchecked]",
"room_emptyblack [Dogchecked]",
"Genocide - The Nothingness [Dogchecked]",
"Snowdin - Title [Dogchecked]",
"Dogcheck room",
"Hotland - Quiz battle (Unused) [Dogchecked]",
"Pre-Asriel scene (Unused) [Dogchecked]",
"Pre-Asriel scene 2 (Unused) [Dogchecked]",
"Asriel appears [Dogchecked]",
"Asriel room [Dogchecked]",
"Asriel flashbacks [Dogchecked]",
"Asriel animation test [Dogchecked]",
"Asriel phase 2 animation test [Dogchecked]",
"Snowdin - Dog Shrine [Dogchecked]"
]

def clean(name):
    return re.sub(r"\s*\[[^\]]*\]", "", name).strip()

AREAS = {"The Ruins", "Snowdin", "Waterfall", "Hotland", "New Home", "True Lab", "???", "UNDERTALE"}

def area_of(name):
    for prefix, area in [("Ruins", "The Ruins"), ("Toriel", "The Ruins"),
                         ("Snowdin", "Snowdin"), ("Waterfall", "Waterfall"),
                         ("Hotland", "Hotland"), ("Castle", "New Home"),
                         ("New Home", "New Home"), ("Last Corridor", "New Home"),
                         ("Throne", "New Home"), ("Barrier", "New Home"),
                         ("True Lab", "True Lab"), ("Laboratory", "True Lab"),
                         ("Omega", "???"), ("Flowey", "???")]:
        if name.startswith(prefix):
            return area
    return "UNDERTALE"

def read_lines(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return [l.strip() for l in f.read().splitlines()]
    except Exception:
        return []

def num(lines, i, default=0):
    try:
        return int(float(lines[i]))
    except Exception:
        return default

INI = os.path.join(FOLDER, "undertale.ini")

def ini_value(key):
    try:
        with open(INI, encoding="utf-8", errors="ignore") as f:
            m = re.search(r'^' + key + r'="?([0-9.]+)', f.read(), re.M)
        return int(float(m.group(1))) if m else 0
    except Exception:
        return 0

def ini_kills():
    return ini_value("Kills")

def mtime(path):
    try:
        return os.path.getmtime(path)
    except Exception:
        return 0

def route_of(lv, kills):
    if ROUTE_OVERRIDE:
        return ROUTE_OVERRIDE
    if kills == 0:
        return "Pacifist"
    if lv >= 8 and kills >= 30:
        return "Genocide"
    return "Neutral"

def boss_for(room, route, true_lab):
    geno = route == "Genocide"
    if 38 <= room <= 42: return "Toriel"
    if room == 43: return "Flowey"
    if room == 81 or 62 <= room <= 64: return "Papyrus"
    if 132 <= room <= 136: return "Undyne the Undying" if geno else "Undyne"
    if room in (176, 177): return "Muffet"
    if 209 <= room <= 215: return "Mettaton NEO" if geno else "Mettaton EX"
    if room == 231: return "Sans" if geno else None
    if 232 <= room <= 235: return "Asgore"
    if room == 237: return "Asriel Dreemurr" if true_lab else "Asgore"
    if room in (238, 293): return "Omega Flowey"
    return None

def build_status():
    lines = read_lines(SAVE)
    if len(lines) < 548:
        return {"details": "Playing UNDERTALE", "large_image": ICON}, None, None
    name = lines[0] or "???"
    lv, hp = num(lines, 1, 1), num(lines, 2)
    kills = max(num(lines, 11), ini_kills())
    gold = num(lines, 10)
    room = num(lines, 547, -1)
    true_lab = num(lines, 523) == 12
    room_name = clean(ROOMS[room]) if 0 <= room < len(ROOMS) else "Unknown"
    route = route_of(lv, kills)
    if room == 237 and true_lab:
        route = "True Pacifist"
    boss = boss_for(room, route, true_lab)
    details = f"Fighting {boss}" if boss else f"{area_of(room_name)}: {room_name.split(' - ')[-1].split(': ')[-1]}"
    state = f"{name} | LV {lv} | HP {hp} | {kills} kills | {route}"
    place = boss or area_of(room_name)
    return {"details": details[:128], "state": state[:128],
            "large_image": ICON, "large_text": f"{room_name} | {gold}G"}, place, name

def undertale_running():
    out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq UNDERTALE.exe"],
                         capture_output=True, text=True).stdout
    return "UNDERTALE.exe" in out

def main():
    rpc = Presence(CLIENT_ID)
    rpc.connect()
    print("Connected to Discord. Leave this window open while you play.")
    start, last = None, None
    deaths = {}                     # deaths this session, per boss/area
    seen_gameovers = ini_value("Gameover")
    dead_since = None               # time of the last game over, until you continue
    dead_place = None
    me = os.path.abspath(__file__)
    my_mtime = mtime(me)
    while True:
        if mtime(me) != my_mtime:
            print("Script updated - restarting...")
            try:
                rpc.close()
            except Exception:
                pass
            os.execv(sys.executable, [sys.executable, me])
        if undertale_running():
            if start is None:
                start = int(time.time())
            status, place, name = build_status()

            # A game over bumps the Gameover counter in undertale.ini.
            gameovers = ini_value("Gameover")
            if gameovers > seen_gameovers:
                seen_gameovers = gameovers
                dead_since = time.time()
                dead_place = place
                deaths[place] = deaths.get(place, 0) + 1
            # Continuing reloads your save, which rewrites file9.
            if dead_since and mtime(os.path.join(FOLDER, "file9")) > dead_since + 1:
                dead_since = None

            n = deaths.get(place, 0)
            if dead_since:
                who = f"Killed by {dead_place}" if dead_place and dead_place not in AREAS else f"Died in {dead_place}"
                status = dict(status, details="GAME OVER", state=f"{who} | Death #{deaths.get(dead_place, 1)}")
            elif n and status.get("details", "").startswith("Fighting"):
                status = dict(status, details=f"{status['details']} | Attempt {n + 1}")

            if status != last:
                rpc.update(start=start, **status)
                print(time.strftime("%H:%M:%S"), "-", status.get("details"), "/", status.get("state", ""))
                last = status
        elif last is not None:
            rpc.clear()
            start, last = None, None
        time.sleep(2)

if __name__ == "__main__":
    main()
