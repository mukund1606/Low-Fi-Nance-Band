# Low-Fi Nance Band


### Installation and Setup

```bash
git clone git@github.com:mukund1606/Low-Fi-Nance-Band.git
cd Low-Fi-Nance-Band
python3 -m venv venv -r packages.txt
sudo apt install < packages.txt # Not Sure About This. I am Windows User
```

# Setup Environment Variables for ChatGPT Lyrics Generation
#### Obtaining SESSION_TOKEN for ChatGPT

1. Go to https://chat.openai.com/chat and open the developer tools by `F12`.
2. Find the `__Secure-next-auth.session-token` cookie in `Application` > `Storage` > `Cookies` > `https://chat.openai.com`.
3. Copy the value in the `Cookie Value` field.

![SESSION_TOKEN](/src/assets/SESSION.png)

#### Get Conversation ID from URL(Optional)
![SESSION_TOKEN](/src/assets/CONVERSATION.png)


### .env File -
```bash 
SESSION_TOKEN="SESSION_TOKEN"
CONVERSATION_ID="CONVERSATION_ID"
```