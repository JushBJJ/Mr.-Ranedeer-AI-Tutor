# Mr. Ranedeer: Your personalized AI Tutor!

Unlock the potential of GPT-4 with Mr. Ranedeer AI Tutor, a customizable prompt that delivers personalized learning experiences for users with diverse needs and interests.

Follow me on Twitter: [@yupiop12](https://twitter.com/yupiop12)

Donations accepted:

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/Jush)

![image](https://user-images.githubusercontent.com/36951064/236518590-e11f4b6c-3956-4cce-813a-71bd2d3a284e.png)

## Table of Contents
- [Mr. Ranedeer: Your personalized AI Tutor!](#mr-ranedeer-your-personalized-ai-tutor)
  - [Table of Contents](#table-of-contents)
  - [Why Mr. Ranedeer AI Tutor?](#why-mr-ranedeer-ai-tutor)
  - [Requirements and Compatibility](#requirements-and-compatibility)
    - [Recommended](#recommended)
    - [Not Recommended](#not-recommended)
  - [Quick Start Guide](#quick-start-guide)
- [Prompt Formats](#prompt-formats)
  - [Previous Versions](#previous-versions)
- [AI Tutor Personalization Options](#ai-tutor-personalization-options)
- [Commands](#commands)
- [Different Languages](#different-languages)
  - [Chinese](#chinese)
  - [Russian](#russian)
  - [Spanish](#spanish)
  - [Tagalog](#tagalog)
  - [Arabic](#arabic)
  - [Disclaimer](#disclaimer)
- [Screenshot Examples](#screenshot-examples)
  - [Lessons](#lessons)
    - [How 1 + 1 = 2](#how-1--1--2)
    - [Poetry](#poetry)
  - [The /test command](#the-test-command)
    - [The photoelectric effect (depth level 3)](#the-photoelectric-effect-depth-level-3)
    - [The photoelectric effect (depth level 10)](#the-photoelectric-effect-depth-level-10)
  - [Planning Lessons](#planning-lessons)
    - [Poetry Writing](#poetry-writing)
    - [Fahrenheit 451](#fahrenheit-451)
  - [Changing your configuration](#changing-your-configuration)
  - [Learning Styles](#learning-styles)
  - [Communication Styles](#communication-styles)
  - [Tone Styles](#tone-styles)
  - [Reasoning Frameworks](#reasoning-frameworks)
  - [Detailed Documentation](#detailed-documentation)

## Why Mr. Ranedeer AI Tutor?

Mr. Ranedeer AI Tutor allows you to:
- Adjust the depth of knowledge to match your learning needs
- Customize your learning style, communication type, tone, and reasoning framework
- Create the ultimate AI tutor tailored just for you

## Requirements and Compatibility

### Recommended
- ChatGPT Plus Subscription with GPT-4 or above models.

### Not Recommended
- Default and Legacy GPT-3.5
- GPT-4 API (It will be costly)

*Note: The compatibility with plugins for this prompt is currently unknown.

## Quick Start Guide

1. Visit [ChatGPT](https://chat.openai.com/chat)
2. Select the GPT-4 (or above) model
3. Copy and paste the contents of [Mr_Ranedeer.json](https://raw.githubusercontent.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/main/Mr_Ranedeer.json) into ChatGPT
4. Let Mr. Ranedeer guide you through the configuration process
5. Start learning!

# Prompt Formats

You can run Mr. Ranedeer in the following formats:

|Format|Tokens|Reduction from JSON format|
|-|-|-|
|[JSON](https://raw.githubusercontent.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/main/Mr_Ranedeer.json)|3,896|1x|
|[YAML](https://raw.githubusercontent.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/main/Mr_Ranedeer.yaml)|2,646|~1.47x|
|[Markdown](https://raw.githubusercontent.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/main/Mr_Ranedeer.md)|1280|~3x|

The OpenAI API has different prices and limits based on [Tokens](https://platform.openai.com/tokenizer). The more tokens you send and receive, the faster you will hit the limits and incur greater cost.

_If you are using the ChatGPT web interface, the costs will not apply._

## Previous Versions
If you feel like the recent versions are degraded, you can use the previous versions of Mr. Ranedeer AI Tutor.

|Version|Tokens (JSON)|
|-|-|
|[v2.4.16 (Current)](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)|3,896|
|[v2.4.11](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/tree/dce8ae6979153ca386758719d1f60aa64a74ed05)|4,336|
|[v2.3.6](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/tree/59b5339a07b7f8ac765a9e2010fe34e1b2199971)|4,267|
|[v2](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/tree/3b03ee94f5ff5e010e0a949419521b0236ad8019)|4,484|

# AI Tutor Personalization Options

This section outlines the various configuration options available to students using the AI Tutor. These options can be modified to customize the learning experience.

| Configuration      | Options                                                                                                                                                                      |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Depth              | 1. Surface level understanding<br>2. Expanded understanding<br>3. Detailed analysis<br>4. Practical application<br>5. Advanced concepts<br>6. Critical evaluation<br>7. Synthesis and integration<br>8. Expert insight<br>9. Specialization<br>10. "Cutting-edge research"
| Learning Styles    | Sensing, Visual* (requires plugins), Inductive, Active, Sequential, Intuitive, Verbal, Deductive, Reflective, Global                                                         |
| Communication      | Stochastic, Formal, Textbook, Layman, Storytelling, Socratic, Humorous                                                                                                       |
| Tone Styles        | Debate, Encouraging, Neutral, Informative, Friendly                                                                                                                          |
| Reasoning Frameworks| Deductive, Inductive, Abductive, Analogical, Casual                                                                                                                          |
| Language        | English (Default), **any** language GPT-4 is capable of doing.                                                                                                                                        |

# Commands

The AI Tutor supports the following commands:

- `/feedback`: Request feedback from the AI Tutor.
- `/test`: Request a test to assess your knowledge and understanding.
- `/config`: Update your AI Tutor configuration/preferences.
- `/plan`: Create a lesson plan based on your preferences.
- `/search`: Search for specific information (*requires plugins*).
- `/start`: Start the lesson plan.
- `/stop`: Stop the lesson plan.
- `/continue`: Continue the output if it was cut.
- `/language`: Change the AI Tutor language

*The search command requires plugins.

# Different Languages
By either editing the Mr Ranedeer file or using the `/language [lang]` command, you can change the language Mr Ranedeer speaks to you!
## Chinese
![image](https://user-images.githubusercontent.com/36951064/236190880-add1d3e3-d839-49db-9f07-b0508f5f98b3.png) ![image](https://user-images.githubusercontent.com/36951064/236191766-b613e857-a811-4db8-a8a2-ccc6afddf0ed.png)
## Russian
![image](https://user-images.githubusercontent.com/36951064/236193013-ff8ab293-0bc5-49a0-b8b3-bd0d182d1778.png)
## Spanish
![image](https://user-images.githubusercontent.com/36951064/236193506-b122e55f-5c71-4ee1-b2cc-23227d8f3515.png)
## Tagalog
![image](https://user-images.githubusercontent.com/36951064/236193736-891bd243-b4c1-4ce8-91d8-7e206e63105a.png)
## Arabic
![image](https://user-images.githubusercontent.com/36951064/236194072-27cec887-5f3e-48bb-a004-a26d6b5db2be.png)

## Disclaimer
This project uses OpenAI's GPT-4 to generate content in different languages through the /language command. Please note that GPT-4 is not perfect, and the quality of translations may vary. Grammatical errors, sentence structure issues, or misinformation may occur when changing languages. Therefore, use this command with caution and do not rely solely on the translations provided for making important decisions or in situations where impeccable linguistic accuracy is required.

# Screenshot Examples

## Lessons
### How 1 + 1 = 2
![image](https://user-images.githubusercontent.com/36951064/236521782-c5fc9c27-e1f2-4ce5-8568-64ee83b89a05.png)
![image](https://user-images.githubusercontent.com/36951064/236521850-7cca5c53-6bf0-43b4-8264-76864f9edddf.png)

### Poetry
![image](https://user-images.githubusercontent.com/36951064/236591684-e2a7e3ad-264c-427c-a370-9df516dd8939.png)

## The /test command
### The photoelectric effect (depth level 3)
![image](https://user-images.githubusercontent.com/36951064/236591986-2e8f1849-cd1d-477b-b693-00ed1e0a52e5.png)

### The photoelectric effect (depth level 10)
![image](https://user-images.githubusercontent.com/36951064/236591862-f60318da-e88a-4201-b64d-499763f8a47a.png)

## Planning Lessons

### Poetry Writing
![image](https://user-images.githubusercontent.com/36951064/236525104-c2103f8f-e209-430a-8fdf-b7ecfbfdba8c.png)

### Fahrenheit 451
![image](https://user-images.githubusercontent.com/36951064/236521069-a5d60b7b-b5e8-4e57-9a1e-c10431491c40.png)
![image](https://user-images.githubusercontent.com/36951064/236521149-b89e7af2-200e-4399-8642-0764158567bc.png)

## Changing your configuration
![image](https://user-images.githubusercontent.com/36951064/236521428-f569e6cb-ddb3-4d5c-adbb-6d551b8b8bd7.png)
![image](https://user-images.githubusercontent.com/36951064/236523046-569b257a-c53c-415e-9620-a318e5add733.png)

## Learning Styles
TODO
## Communication Styles
TODO
## Tone Styles
TODO

## Reasoning Frameworks
TODO
## Detailed Documentation

Find detailed documentation for Mr. Ranedeer AI Tutor in the [docs.md](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor/blob/main/docs.md) file.
