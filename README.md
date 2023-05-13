# __Environmental-Awareness-Discord-Bot__
 A Discord Bot that helps raise awareness to global warming and other environmental issues.

## __Avaliable commands__
* $help: gives a list of avaliable commands
* $fact: sends a fun fact about the envrionment and how pollution has impacted the world
* $animals {africa, australia, america, asia, europe, antartica}: By typing in $animals followed by a location, the bot will give you information about an endangered animal in the location and give you the reason why it's endangered. Interesting Photos and GIFs will also be attached to the message.

Aside from these commands, you can also chat with the Discord Bot, for example: "Why should we protect the environment?""What can I do to reduce my environmental impact"

Facts and information about animals are sourced from different websites, which are included in the Info_source file.

## __Use Discord Bot in Your Server__
Here is the <a href='https://discord.com/api/oauth2/authorize?client_id=1096833963311509574&permissions=8&scope=bot'> link</a> to the bot access

## __Installation__
1. Create your own Discord Bot Token and put it into the TOKEN = '{Token here}' in the main.py file.
2. Ensure you have the discord module downloaded.
3. Add the bot to your server.
4. Start chatting with the bot!
---
## __Inspiration__
Being an active user of Discord, I loved playing around and experiencing different Discord Bots. Despite my great interest, I never found the time to learn to code one myself. When I came across this competition and was creating a plan, creating a discord bot immediately came to my mind, since there were no restrictions as to how one would use code to advocate the importance of protecting the environment.

## __How I built it__
I first learned how to build a discord bot through Youtube videos. I used simple Discord commands to enable the bot to read messages and send ones themselves. Special messages (commands) make the bot respond accordingly, for this, I mainly used simple "if...else..." statements. 

After being inspired by machine learning, I later added the chat system by creating something similar to a chatbot. Instead of using given ML models, I coded my own program to compare user input with given data and append accuracy values into a list, the item with the highest accuracy values would be the expected response sent by the discord bot. If all the accuracy values in the list are 0, then the bot will reply "Sorry, I don't quite understand".

## __Challenges I ran into__
When building my own program to create something similar to a chatbot, to compare user input with given intents, I had to use multiple "for" loops within each other, which eventually became extremely confusing.

To solve this problem, I decided to write my ideas down on a piece of paper and graph my thinking process. By doing so, my plans and thought process were much more clear,  allowing me to code easier without being lost again.

## __Accomplishments that I'm proud of__
This is my first time coding a Discord Bot, I'm glad that it worked out, despite coming across many obstacles.
In the process of creating something similar to a chatbot, although I didn't understand how to do ML, I understood vaguely how it worked, which enabled me to create a simpler version of a chatbot, although not as smart as an AI chatbot.

## __What I learned__
When you're confused or lost while trying to write your ideas into code, drawing or graphing out your ideas by using simple boxes and lines helps sort out your thought process and makes coding much easier, especially when your ideas are complex.

## __What's Next for the Discord Bot__
**Improve Intellect:** In the future, either learning how to integrate ML into the Discord Bot or adding more data to the list of intents, will allow the bot to reply to the user more naturally.

**Adding More Fun Commands:** I was considering how to create a simple exploration game by using Discord. For example, the user gets to land in a  wild forest and will come across different animals in need of help or different disastrous events that occur due to global warming. The game interface would be a simple pixel screen with buttons below for the user to interact with, allowing the users to make decisions.

**Reminders:** Additionally, one could also add a reminder for the users to stay environmentally friendly. For example, asking a question or giving environmental tips every day.

Here's the <a href='https://www.youtube.com/watch?v=1BSHdKmOmqw&ab_channel=AlyssaDong'> video explaination</a> of the Discord Bot.

