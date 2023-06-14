# Ranedeer Tools
Ranedeer Tools are customized prompts that **you** can make and implement into Mr. Ranedeer. 

# What kind of Ranedeer Tools can you make?
You can virtually make anything you can imagine within the limitations of ChatGPT

**Here are some examples from the current Ranedeer Tools:**
   1. A conversational scenario simulator
   2. Gordon Ramsey Personality
   3. A Japanese tutor that immerses you into a Medieval Japanese Setting
   4. A simple Socratic Tutor that doesn't tell you the answer.

# How do I activate a Raneder Tool?
## Prerequisite
### Method 1 - Editing the prompt
1. Copy and paste the Raneder Tool prompt from the [Ranedeer Tools Folder](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/tree/main/Ranedeer%20Tools) into the Mr. Ranedeer Prompt under the [Ranedeer Tools] header.

![Image](https://media.discordapp.net/attachments/1114958734364524605/1118380336930377808/Screenshot_2023-06-14_131900.png?width=764&height=584)

2. Make sure the indents are correctly aligned (A placeholder Ranedeer Tool is there to guide you)
3. Save and Re-run the Mr. Ranedeer Prompt

### Method 2 - During conversation
1. Copy and paste the Raneder Tool prompt into the next message you send to Mr. Ranedeer under the specific prompt:

---
`Please add the following Ranedeer tool:`

\`\`\`
```
[TOOL NAME]
    [DESCRIPTION]
        DESCRIPTION HERE

    [BEGIN]
        INSERT PROMPT HERE
    [END]
```
\`\`\`

---
2. Press `enter` to send the message.

## Activation
1. To activate a specific Ranedeer Tool, simply mention that you want to use the Ranedeer Tool you desire when conducting a command.

**For example:**
 `/start Use the Gordon Ramsey Tool`

# Where do I publish a Raneder Tool?
Create a [pull request](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/pulls) containing the file of the Rnanedeer Tool prompt you want to publish.

# Format of Ranedeer Tools
```
[TOOL NAME]
    [DESCRIPTION]
        DESCRIPTION HERE

    [BEGIN]
        INSERT PROMPT HERE
    [END]
```
The description is optional. You can write the prompt in however way you want within the `[BEGIN]` and `[END]` tags.
