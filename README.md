# UNDERTALE & DELTARUNE Discord Status

Shows what you're doing in UNDERTALE or DELTARUNE on your Discord profile:
the boss you're fighting, where you are, and your stats.

**UNDERTALE** shows:
- The boss you're at (Toriel, Papyrus, Undyne the Undying, Mettaton NEO, Sans, Asgore, Asriel...)
- Otherwise your area and room, like `Waterfall: Temmie Village`
- Your name, LV, HP, kills and route (Pacifist / Neutral / Genocide)
- GAME OVER screens and how many tries a boss has taken you

**DELTARUNE** shows:
- The boss you're at (King, Jevil, Spamton NEO, Tenna, the Roaring Knight, the Titan, Gerson, MIKE...)
- Otherwise your area and room, like `Dark Sanctuary: Gersonstudy`
- Your save name and chapter

## How to use

You need **Windows**, **Python** ([python.org](https://www.python.org/downloads/)) and the **Discord desktop app**.

1. Download this repo (green **Code** button > **Download ZIP**) and unzip it.
2. Open Discord.
3. Double-click **`Start Undertale Status.bat`** or **`Start Deltarune Status.bat`**.
   The first time, it installs the one package it needs (`pypresence`).
4. Leave the black window open and play. Close it when you're done.

Make sure **User Settings > Activity Privacy > Share your activity status** is on in Discord.

## How it works

It reads your save files (`%LOCALAPPDATA%\UNDERTALE` and `%LOCALAPPDATA%\DELTARUNE`),
so your status changes when you **save** or **load** a file, not live while you walk around.
It never changes your saves.

## Credits

- UNDERTALE room list: [Flowey's Time Machine](https://github.com/crumblingstatue/FloweysTimeMachine) by crumblingstatue
- DELTARUNE room list: [Tenna Project save editor](https://github.com/tennaproject/tenna-editor) by jjezewski (zlib license, see `TENNA-LICENSE.txt`)
- UNDERTALE and DELTARUNE are by Toby Fox. This is a fan project and is not affiliated with them.
