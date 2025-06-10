# 🚪 Deviceless Doorbell
## A doorbell for the broke and the bold – just scan the QR, we’re living in 2025.
> A device-free, QR-based smart doorbell — just scan and notify!

![QR Code](./assets/img1/qr-code.png)

## 📌 Overview

**Deviceless Doorbell** is a minimalist, hardware-free smart doorbell system.  
All it takes is a printed QR code on your front door. Visitors scan it, and you'll instantly receive a notification on your phone.

No buttons. No wiring. Just the cloud.

## ✨ Features

- 📱 Instant alerts via Matrix / Telegram when QR is scanned
- 🌐 Hosted via [Vercel](https://vercel.com)
- ⚡ Simple FastAPI backend with webhook trigger
- 🧩 Integrates with custom Matrix bot (`doorbell_bot`)
- 🔒 No login, no user data, privacy-first

## 🛠️ How It Works

1. Visitor scans a QR code (located at your door).
2. The QR points to a URL like `https://your-vercel-app.vercel.app/notify`
3. This triggers a FastAPI server.
4. The server sends an encrypted message to your Element room (Matrix) or a Telegram bot.
5. You get notified: “🚪 Someone is at the door!”

## 🖼️ QR Code

The QR code is located at:

