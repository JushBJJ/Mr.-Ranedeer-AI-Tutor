# v2.6.1 Changelog

1. Replaced `As a tutor, you must teach the student accordingly to the configurations.` phrase with `You are allowed to change your language to *any language* that is configured by the student.` as an attempt to fix the language change bug. It was previously in the `Commands` header
2. Some prompt clarifications

# Mr. Ranedeer v2.6 (Current Version)

1. Change the entire format of Mr. Ranedeer from JSON/YAML/Markdown to a more cleaner, less token consuming approach. There is no name yet. Perhaps it should be named NoName language.
2. Moved Student Configuration to the top of the prompt
3. Removed the following learning styles: Sensing, Sequential, Deductive
4. Removed the following communication styles: Stochastic
5. Removed the following tones: Debate (Can be replaced by a Ranedeer Tool)
6. Removed the following commands: search, search, self-eval, visualize
7. Removed Rules, specific rules are now in [INSTRUCTIONS] and [Function Rules] headers
8. Removed the annoying configuration reminder output
9. Added a note to GPT-4 that a visual learning style requires plugins (Wolfram Alpha, Show Me)
10. Added Functions! These functions are used as a guide for GPT-4 to execute highly specific formats and sequences. Functions are a replacement to the old "Rules" and "Formats" previously in v2.5

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

# Mr. Ranedeer v2.5
- **Changed depth levels from Surface Level-Cutting Edge research to Elementary-Ph.D to gain more relevant lesson plans.**
- Removed descriptions for levels, learning styles, communication styles, tone styles, and reaasoning frameworks because it isn't needed.
- Removed "plugin", "internet", "python_enabled" settings because it isn't needed.
- Added rule 11: "You are allowed to change your language to any language that is configured by the student."
- Added rule 12: "In lessons, you must provide solved problem examples for the student to analyze, this is so the student can learn from example."
- Added rule 13: "In lessons, if there are existing plugins, you can activate plugins to visualize or search for content. Else, continue."
- Fixed https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/issues/27
- Fixed https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/issues/37
- Changed the format for `configuration` to display preferences, else it will say "None"
- For emojis in the `configuration` format, it will display "✅" if True, else "❌" if False.
- For language in the `configuration` format, it will display the language name if it is not English, else it will display the default langauge (English)
- Appended more specification to not mistakenly follow the `configuration` format, instead follow what it is supposed to be printing.
- `Planning` and `Lesson` format is now instructed to strictly follow the `configuration_reminder` format
- `Planning` now has "Assumptions" where GPT-4 will try to predict what the student already knows based on the depth level.
- Before outputting the plan in the `Planning` format, it will say "A `depth name` student lesson plan:" before printing out the plan for you.
- `Lesson` format is commanded to strictly execute rule 12 and 13
- `configuration_reminder` format now has a new way of reminding itself (experimental). It should expectedly follow the student's preferences more.
- `Planning` and `Lesson` will now have an `emoji usage` to "plan" its use for emojis in planning and lessons (this triggers an encouraged use of consistent emojis in general).
- There is now a `test` format where an example problem is provided and solved as an example by Mr. Ranedeer, then it will provide problems for the student to solve.
