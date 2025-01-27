# CodeBloom - AI Coding Assistant for Novice Programmers

## Overview

This project is an **AI-powered coding assistant** designed specifically for novice programmers in introductory 
programming courses. The assistant helps students learn foundational programming concepts responsibly by providing 
restricted  AI assistance. Students must first complete **contextualised exercises** to earn badges for specific 
topics (e.g., loops, conditionals, functions). Once a badge is earned, the AI assistant unlocks features to provide help related to that topic, ensuring a **guided, structured learning experience**.

## Continue

This project leverages [Continue](https://continue.dev/), the leading open-source AI code assistant, as its frontend. 
Continue allows seamless integration of custom autocomplete and chat experiences directly within Visual Studio Code. 
By connecting to any models and any context, Continue provides an extensible platform to create personalised AI coding
workflows.

You can learn more about Continue or contribute to its development by visiting their [GitHub repository](https://github.com/continuedev/continue).

## Motivation

The widespread use of AI coding assistants, such as GitHub Copilot, has revolutionised programming. However, their application in educational settings poses unique challenges:

- Over-reliance on AI, reducing critical thinking.
- Limited understanding of fundamental coding concepts.
- Cognitive overload due to the complexity of AI-generated solutions.

This project addresses these challenges by integrating AI assistance in a way that **supports learning without replacing it**. By leveraging advancements in large language models (like GPT-4), this project creates a tool that enhances student learning, aligns with educators' goals, and ensures responsible integration of AI into programming education.

## Features

### 1. **Contextualised Exercises with Badge Unlocking**

- Students complete exercises focusing on foundational topics (e.g., **For Loops**, **Conditionals**, **Functions**).
- Upon successfully completing an exercise, they earn a **badge** that unlocks AI assistance for that specific topic.
- Exercises are automatically validated for correctness using tools like **Abstract Syntax Trees (ASTs)** to ensure solutions meet the required criteria.

### 2. **Adaptive AI Assistance**

- The assistant adapts its responses based on the student's progress:
  - If a student hasn't earned a badge for a topic (e.g., **While Loops**), the AI will not provide solutions involving that concept.
  - This encourages students to learn concepts independently before seeking AI assistance.
- Promotes mastery of topics by scaffolding help progressively.




## Getting Started
Follow these steps to set up the project and run the AI coding assistant locally:
### Prerequisites

1. Python 3.11 or later.
2. Libraries:
   - `flask`: For creating the server to run locally on.
   - `openai`: (or equivalent library for integrating an AI model).
   - `json`: For handling JSON data.
   - `re`: For regular expressions.
   - `importlib`: For module importing. 
   - `subprocess`: For running subprocesses. 
   - `unittest`: For testing functionalities. 
   - `io`: For input/output operations.
   - Additional tools for automated code validation (e.g., **UnitTest** libraries).
3. **Java Runtime Environment (JRE)**: Required to execute the Java `.jar` file for running unit tests. 
   - Ensure java is installed and added to your system's PATH. 
4. **JAR File**: Place the `junit-platform-console-standalone-1.11.4.jar` file in the root directory of this project. 
This file is required to run Java-based unit tests.
5. **MySQL Database**: This project requires a MySQL database for storing student data, badge information, and progress tracking. 
   - Install MySQL on your system or use a cloud-hosted MySQL service. 
   - Ensure that your MySQL server is running and accessible.
### Installation

1. Clone the repository:

   ```bash
   https://github.com/daniellebuggle/CodingAssistant.git

2. Install the required Python libraries:

    ```bash
   pip install flask openai

3. Verify that the Java .jar file is in the root directory:
    
    ```bash
   ls junit-platform-console-standalone-1.11.4.jar
   
4. Set up your OpenAI API key and database settings. Create a `.env` file in the root directory with the following content:

    ```
   OPENAI_API_KEY=your-api-key
   DB_HOST=database-host
   DB_USER=database-user
   DB_PASSWORD=your-password
   DB_Name=your-database
   ```
5. **Database Dependencies**:
   - Install the `mysql-connector` library to connect to the MySQL database:
     ```bash
     pip install mysql-connector
     ```
6. Database settings
   - You’ll need to create the necessary tables in your MySQL database. You can execute the provided SQL script to set up the schema.
   - Example SQL schema:
   ```sql
    CREATE TABLE students (
        student_id INT AUTO_INCREMENT PRIMARY KEY,
        student_name VARCHAR(255) NOT NULL
    );

    CREATE TABLE badges (
        badge_id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT NOT NULL,
        badge_name VARCHAR(255) NOT NULL,
        UNIQUE(student_id, badge_name),
        FOREIGN KEY (student_id) REFERENCES students(student_id)
            ON DELETE CASCADE ON UPDATE CASCADE
    );
   ```

### Usage
1. Run the backend server:
   ```bash
   python app.py
   ```

2. Open Visual Studio Code and install the [Continue](https://continue.dev/) extension.
3. You will need to programmatically configure **Continue** to use your AI model so you can use `config.ts`, which is 
located at `~/.continue/config.ts` (MacOS / Linux) or `%USERPROFILE%\.continue\config.ts` (Windows).
   - Within `config.ts` change it to have this script:
   ```typescript
   export function modifyConfig(config: Config): Config {
     // Adding custom model to the models array
     config.models.push({
       options: {
         title: "Your-LLM",
         model: "gpt-4o-mini",  // Replace with your actual model name
       },
       streamChat: async function* (prompt: string, options) {
         // API endpoint and token setup
         const api_endpoint = "YOUR-IP-ADRESS/v1/chat/completions";  // Replace with your API endpoint
         const token = "OPENAI_API_KEY"; // Replace with your API token
         
         // Make the API request to stream data from your model
         const response = await fetch(api_endpoint, {
           method: 'POST',
           headers: {
             'Content-Type': 'application/json',
             'Authorization': `Bearer ${token}`,
           },
           body: JSON.stringify({
             model: "gpt-4o-mini",  
             context: "You are a helpful coding assistant who will provide code answers to the user. " +
              "You do not offer explanations with the code. Just give a code answer. If the user " +
              "asks a question unrelated to generating a coding answer, respond by telling the user, " +
              "\"I can't help you with that, sorry.\"",
             messages: prompt,
           }),
         });
   
         // Check if the response is valid
         if (!response.body) {
           throw new Error("Failed to stream response from model.");
         }
   
         const reader = response.body.getReader();
         const decoder = new TextDecoder();
         let buffer = '';
   
         // Stream the response as it arrives
         while (true) {
           const { done, value } = await reader.read();
           if (done) break;
   
           buffer += decoder.decode(value, { stream: true });
   
           // Process each line of the response
           const lines = buffer.split('\n');
           for (const line of lines) {
             if (line.trim()) {
               try {
                 // Assuming the response is a JSON object with a 'content' field
                 const jsonData = JSON.parse(line);
                 yield jsonData.content; // Yield the content field as part of the stream
               } catch (e) {
                 console.error("Error parsing JSON:", e);
               }
             }
           }
           buffer = lines[lines.length - 1]; // Keep the last incomplete chunk
         }
       },
     });
   
     return config;
   }

4. Now you can use the **Continue** extension to connect to the running backend and interact with the AI assistant.