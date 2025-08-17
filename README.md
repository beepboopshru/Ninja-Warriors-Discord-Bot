# Ninja Warriors Discord Bot

A custom moderation and utility bot built using [discord.py](https://discordpy.readthedocs.io/) for the **Ninja Warriors** guild.  
It provides moderation, application handling, ticketing, logging, and some fun commands.

---

## 🚀 Features

### 🔧 Moderation
- `>ban [user] [reason]` → Ban a user from the server.  
- `>mute [user] [reason]` → Assigns the "Muted" role to a user.  
- `>unmute [user]` → Removes mute from a user.  
- `>kick` (in `banme`) → Allows users to kick themselves (funny gimmick).  

### 🎫 Ticket & Applications
- `>ticket` → Creates a **ticket channel** with staff-only + user access.  
- `>apply` → Creates an **application channel** and randomly assigns a staff reviewer.  
- `>close` → Closes ticket/application channels.  
- `>acceptapp [user]` → Accept an application.  
- `>declineapp [user]` → Decline an application (DMs the applicant).  

### 📑 Embeds & Info
- `>test` → Displays an **About Us** guild embed.  
- `>text_apply` → Shows **application requirements**.  
- `>test2` → Displays **ticket usage information**.  

### 🎲 Fun Commands
- `>rng [number]` → Random number generator.  
- `>coinflip / >cf / >flip` → Coin flip (Heads/Tails).  
- `>ghost` → Ghost-pings everyone (Staff only).  
- `>banme` → User bans themselves.  
- `>ping` → Bot latency check.  

### 🎮 Presence / Activity
- On startup, bot randomly selects a **status/activity**.  
- `>presence` (Staff only) → Change bot presence again randomly.  

### 📝 Scrim Logger
- `>log` (Staff/GvG Captain) → Interactive logger that records scrim results and posts them to a log channel.  

### 🌐 Miscellaneous
- Connects to a **voice channel** on startup.  
- Sends logs to a specific bot-log channel.  
- Goodbye message (`>goodbye` for Managers).  

---

## ⚙️ Setup & Installation

1. **Clone the repo / copy files**  
   ```bash
   git clone <repo-url>
   cd <project-folder>
   ```

2. **Install dependencies**  
   Make sure Python 3.8+ is installed.  
   ```bash
   pip install discord.py
   ```

3. **Set up environment variables**  
   Create a `.env` or configure in your hosting environment:  
   ```
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

4. **Run the bot**  
   ```bash
   python bot.py
   ```

---

## 📂 File Structure

```
📦 discord-bot
 ┣ 📜 bot.py          # Main bot script
 ┣ 📜 alive.py        # Keeps bot alive (for Repl.it or hosting)
 ┣ 📜 README.md       # Project documentation
```

---

## 🔑 Permissions Required
When adding the bot to your server, make sure it has:
- `Manage Channels`
- `Manage Roles`
- `Kick Members`
- `Ban Members`
- `Send Messages`
- `Embed Links`
- `Read Message History`
- `Connect/Speak` (if VC features used)

---

## 🛡 Roles & Access
- **Staff** → Access to moderation, tickets, ghost ping, applications, mute/ban.  
- **Manager** → Access to goodbye/test embed commands.  
- **GvG Captain** → Can use scrim logger.  

---

## 🤝 Contributing
If you’d like to add features, feel free to fork the project and make a pull request.  

---

## ⚠️ Disclaimer
Some status messages and commands are made for **inside jokes / guild humor**.  
Change them if you’re adapting this bot for your own community.  
