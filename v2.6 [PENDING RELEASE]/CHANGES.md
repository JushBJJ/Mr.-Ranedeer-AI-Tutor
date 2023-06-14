# Mr. Ranedeer v2.6 Changelog

1. Change the entire format of Mr. Ranedeer from JSON/YAML/Markdown to a more cleaner, less token consuming approach. There is no name yet. Perhaps it should be named NoName language.
2. Moved Student Configuration to the top of the prompt
3. Removed the following learning styles: Sensing, Sequential, Deductive
4. Removed the following communication styles: Stochastic
5. Removed the following tones: Debate (Can be replaced by a Ranedeer Tool)
6. Removed the following commands: search, search, self-eval, visualize
7. Removed Rules, specific rules are now in [INSTRUCTIONS] and [Function Rules] headers
8. Added a note to GPT-4 that a visual learning style requires plugins (Wolfram Alpha, Show Me)
9. Added Functions! These functions are used as a guide for GPT-4 to execute highly specific formats and sequences. Functions are a replacement to the old "Rules" and "Formats" previously in v2.5

These functions are:
- say (Args: Text) this is for GPT-4 to strictly output the string given with a less likely chance to add in its own fillers.
- teach (Args: topic) this function are instructions for GPT-4 to follow when teaching a topic.
- sep (Args: None) this function is for GPT-4 to output a markdown formatted separator.
- post-auto (Args: None) this function automatically executes the `Token Check` and `Suggestions` functions.
- Curriculum (Args: None) this function is for GPT-4 to output the curriculum in a specific forma: Assumptions, Emoji Usage, Ranedeer Tools, prerequisite, main curriculum, token check
- Lesson (Args: None) this function is for GPT-4 to output the lesson in the following format: Example, main lesson, then calls the [post-auto] function.
- Test (Args: None) this function is to test the user by giving it an example problem first with solution then testing the user in 3 categories: Simple Familiar, Complex Familiar, and Complex Unfamiliar
- Question (Args: None) this function automatically runs in the specified format if a student asks a question
- Suggestions (Args: None) this function outputs suggests questions that the students may want to know about in a markdown table format.
- Configuration (Args: None) this function outputs a specific format to show the user their configuration
- Config Example (Args: None) this function shows the user what their lessons may look like based on their configuration, it also tells you examples of how it implemented the configuration into the example lesson and rates it overall.
- Token Check (Args: None) this function checks whether the magic-number exists. If it doesn't it will warn the user that the number of tokens are overloaded. This magic number is automatically generated at the start and not at the initial prompt.
- Init (Args: None) this function is the welcoming message for Mr. Ranedeer

10. Added Ranedeer Tools! You can now inject different types of prompts (for e.g Medieval Setting Japan, Simulator, Gordon Ramsey Personality, Socratic Tutor) into Mr. Ranedeer to make your learning more fun, customized, and unique!