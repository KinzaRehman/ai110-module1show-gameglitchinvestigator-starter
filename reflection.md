# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When first starting the game you notice the title, and the prompt its telling the user to make a guess. It provides a range between 1 and 100. It says the number of attempts you have which is 7. But once you open the developer debug information t gives the secret and the attempts is 1. Show hint is checked off but you dont see a hint anywhere. 
- List at least two concrete bugs you noticed at the start  
(for example: "the hints were backwards").
It would say go lower, then go higher but it wouldn't accept floats/ decimals. Although the range is explicit 1-100, when Selecting 1, the hint says "Go lower". You can not go lower than the range. When submitting 101 multiple times it goes from hinting "Go Lower" to "Go Higher".  SO one major bug is that the range / context provided in the user instructions is not the range sepcifed in the code file. Another bug seems to be the Score is saved even when a new attempt is started and it goes into a negative amount. There is not logical math behind the score. It should range positively atleast unless its soemthing where you guess wrong so you lose points. If you insert the secret it does give you a "You won" so if the user gets the number correct then it does give a positive response! After you win, and you enter "New Game" it doesn't auto clear and start a new game. It says "You already won. STart a new game to play again. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| `1`  | Since the instructions state the valid range is 1–100, the game should not suggest a number lower than 1.| The game responds with "Go lower" even though 1 is already the lowest valid value. | No console error. Possible range validation or game logic issue. |
| `50.5` | The game should either accept decimal values or clearly inform the user that only whole numbers are allowed. | The game does not accept decimal values, and no clear explanation is provided to the user.| No console error. Input validation issue.|
| `101` entered multiple times| The game should consistently reject values outside the valid range or provide the same hint each time. | The hint changes from "Go Lower" to "Go Higher" after repeated submissions of the same value.| No console error. Inconsistent game logic. |
| Start a new attempt after incorrect guesses | The score should reset or follow a clearly defined scoring system when a new game begins| The previous score carries over and can become negative. | No console error. Score state is not resetting properly.|
| Correctly guess the secret number, then select "New Game" | The game should clear the previous win state and immediately start a fresh game. | The game continues displaying "You already won. Start a new game to play again." and does not fully reset. | No console error. Game state is not resetting after victory.|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Chatgpt, the chat column in VS Code and deepseek Ai. Chatgpt because I am new to SWE and Engineering, to review how to successfully run git commands in the terminal. The VS Code chat to read the app.py files, it provided a brief of what was insdie the file and how to go to the specific lines and code to change the commit. and Deep seek ai to reevaluate the code and the isntructions and better udnerstand the logic behind the application and why hints were reversed. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Chatgpt and both the assisting box identified the hint messages in the check_guess() function , it was reversed. THe AI pointed out that when the guess is higher then the return fucntion is set to "Go Higher" even though the guess surpasses the actaul answer. I verefied this by running it multiple times and looking at what it would output. The game always gave the wrong hint, proving  chats help! 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
This was based on a 0 shot promt where AI assumed all score calcuations were caused by update_score() function. After reviewing the application more and carefully testing different scenarios, I foudn that some of the unexpected score behavior was influened by how attempts were counted and stored in streamlit session state. I was reminded the rervaluate againt the actaul code and application bhevaiour. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
