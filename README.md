```
# mani-vpn-bot

1. Put project files in your GitHub repo (root).
2. On Render: New -> Web Service -> Connect to GitHub -> select this repo.
3. In Render settings -> Environment -> add BOT_TOKEN with your bot token.
4. Deploy. Bot runs with polling mode.

Admin commands:
- /list -> list configs
- /del N -> delete config number N

How to add config:
- As admin, send a text, file (document) یا عکس to the bot and follow prompts.

When user sends receipt (photo/file), it is forwarded to admin with buttons to approve/reject.
```

---
