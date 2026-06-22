# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  - no matter the mode, the text it static and does not change. 
  - the enter button does not work to submit
  - even though the number is between 1 and 100, the guesser still said   higher when 100 was entered and lower when 1 was entered
  - 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|    Input    | Expected Behavior | Actual Behavior | Console Output / Error |
|-------------|-------------------|-----------------|------------------------|

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
| :--- | :--- | :--- | :--- |
| **Typed `95`** *(on an even attempt)* | The game should recognize the guess is too high and tell the user to go lower. | The game displayed an inaccurate hint stating: `📈 Go HIGHER!` | none *(The type mismatch error was caught silently by an inner `except TypeError:` block, forcing a broken alphabetical comparison)*. |
| **Pressed the `Enter` key** *(inside the text box)* | The application should capture the input value, increment the turn counter, and submit the guess. | The page reloaded but the game state completely bypassed the evaluation step, leaving the attempt count unchanged. | none |
| **Switched difficulty to `Easy`** | The main instructional info banner should dynamically change its text to read: *"Guess a number between 1 and 20."* | The sidebar configuration indicators updated to 1-20, but the main info text box still read: *"Guess a number between 1 and 100."* | none |



## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- I used Claude and Gemini.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- The AI suggested that the high/low hint string outputs were inverted. It suggested refractoring the check_guess function into logic_utils.py removing the broken code and replacing it with the correct logical operation. 

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

- N/A

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

- I went through the code and the ran the app and walked through the specific fix I just made. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

- I ran pytest on the game logic and added a test that guessed 9 when the secret was 100. It showed me the fix worked because it now says go higher instead of go lower. It also showed me the old tests were checking the wrong thing, so I had to fix those too.

- Did AI help you design or understand any tests? How?

- Yes. Claude wrote the test then explained exactly what it did to me. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

- it runs the script from top to bottom on every interaction and st.session_state keeps the data alive across the reruns. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  - Asking the AI to explain plainly why it did something and how it helped. 

- What is one thing you would do differently next time you work with AI on a coding task?

- Give myself more time to go over the code in depth. 

- In one or two sentences, describe how this project changed the way you think about AI generated code.

- It allowed me to see how seamlessly AI can generate and integrate its own code into exsisting code. This give me the mindset that just beacuse it it seamless does not mean it will always be right. As such, I must always ensure I check the work. 
