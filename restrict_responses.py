def zero_shot_prompt_general_query(badges, question):
    prompt = f"""
    {badges}
    These are the current badges that the student has successfully earned. These are the concepts they have successfully
    learned.
    
    {question}
    This is the question the student has asked for help with. Only if it is a coding related question give a valid response.
    
    Ensure that the code you generate to answer this question only includes concepts that have been earned by the
    student. If they have earned a java badge concept that can be used you can include that concept within a java response.
     
    However if they haven't earned a badge for that concept yet, inform the student they should complete that exercise
    and ask again.
    """
    return prompt


def few_shot_prompt_general_query(badges, question):
    prompt = f"""
    Here are examples of how you should evaluate a coding query.
    
    Example 1:
    Question:
    Could you help me write a program that adds all the numbers in a list.
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    Example Response:
    ```java
    public static int sumOfList(int[] numbers) {{
        int totalSum = 0;
        for (int i = 0; i < numbers.length; i++) {{
            totalSum += numbers[i];
        }}
        return totalSum;
    }}
    ```
    
    Example 2:
    Question:
    Could you help me write a program that adds all the numbers in a list in python.
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    Example Response:
    Unfortunately you haven't earned any Python badges. These are the badges you have earned 'Java For-Loop' and 
    'Java If-Else'. Please try the Python For-Loop exercise and ask me again after.
    
    
    Example 3:
    Question:
    Could you help me write a program that adds all the numbers in a list using a do-while loop.
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    Example Response:
    Unfortunately you haven't earned the do-while loop badge. These are the badges you have earned 'Java For-Loop' and 
    'Java If-Else'. Please try the Java Do-While exercise and ask me again after.
    
    Now based on the examples above, generate a natural language response in the same format by doing the following:
    Check the student's badges:

    {badges}

    and the student's question:
    {question}
    
    Evaluate if you can provide a valid response using the badges and question asked. Generate a code answer to the question
    using the badges they have earned if it's possible. Don't ever include a concept that has not been earned.
    """
    return prompt


def chain_of_thought_general_query(badges, question, all_available_badges):
    prompt = f"""
    
    Q: Did the student ask about generating code?
    A: - Let’s think step by step.
       - If there is any mention of code help or code provided by the student they are looking for code help.
       - If there is no mention of any code help by the student they are not looking to generate code.

    Q: What coding concepts does the student know?
    A: - Let’s think step by step.
       - This is an example of a student badge list: [’Java For Loop’]. The student has earned the ‘Java for loop badge’. 
       - Therefore, they know how to use the coding concept of for-loops in Java.

    Q: Can you generate a valid coding response?
    A: - Let’s think step by step.
       - If the student asked a question that can be coded using the concepts they know, then you can generate a valid response. 
       - A valid coding response only uses coding concepts the student knows.
       - For example, if they know the concept for-loops in java then they can generate any code help that involves java for loops.
       - If you cannot generate a code answer with the concept(s) the student knows, then you cannot generate a valid response.

    Now let’s carefully analyse the student question and their student badges:
    
    Student Question:
    {question}

    Student Badge List:
    {badges}
    
    Based on the above analysis, generate a response following this structure:
    - Acknowledge if the student asked a valid question.
    - Acknowledge what coding concepts the student knows.
    - If a valid question was asked, check if a valid coding response can be generated.
    - If a valid coding response can be generated, respond with that, otherwise let the student know they need to earn 
      more badges for your help.
    
    Generate the response now:
    """
    return prompt

def cot_few_shot_general_query(badges, question):
    prompt=f"""
    
    Provide a code answer to the student's question provided using the coding concepts the student knows.
    This task involves the following actions:
    
    Q1: Is the student asking a valid question?
        - If the question coding related, then it is valid.
        - If it is unrelated to coding, it is invalid.
    Q2: What coding concepts does the student know?
        - If the student has earned badges, they know some coding concepts.
        - Identify what coding concepts they know from the name of the badge.
    Q3: Is it possible to answer the question using the coding concepts the student knows?
        - Check what coding concepts the student knows from the badges they have earned.
        - Check if it is possible to write a coding snippet using the concepts they know.

    Here are examples of how you should evaluate each question.
    
    Example 1:
    Q1: Is the student asking a valid question?
    
    Question:
    What is your favourite colour?
    
    A: This is not a coding related question it is not valid.
    
    Example 2:
    Q1: Is the student asking a valid question?
    
    Question:
    I need help generating a program that will multiply every number in a list.
    
    A: This is a coding related question so it is valid.
    
    Example 3:
    Q2: What coding concepts does the student know?
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    A: The student knows how to write for loops and if-else statements only in Java.
    
    Example 4:
    Q2: What coding concepts does the student know?
    
    Badges Earned:
    []
    
    A: The student has not earned any badges so they don't know any coding concepts yet.
    
    Example 5:
    Q2: What coding concepts does the student know?
    
    Badges Earned:
    ['Python While Loop', 'Java For-Loop']
    
    A: The student knows how to write for loops in Java and while loops in Python.
    
    Example 6:
    
    Q3: Is it possible to answer the question using the coding concepts the student knows?
    
    Question:
    I need help generating a program that will multiply every number in a list.
    
    Badges Earned:
    ['Java For-Loop']
    
    A: The student has earned a for loop badge for java so you can generate code using only a for loop for the java language
       to answer the question.
       
    Example 7:
    Q3: Is it possible to answer the question using the coding concepts the student knows?
    
    Question:
    I need help generating a program that will multiply every number in a list.
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    A: The student has earned a for loop, and if-else badge for java so you can generate code using only for loops and 
    if-else statements for the java language to answer the question.
    
    
    Overall Response Examples:
        Example 1:
    Question:
    Could you help me write a program that adds all the numbers in a list.
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    Example Response:
    ```java
    public static int sumOfList(int[] numbers) {{
        int totalSum = 0;
        for (int i = 0; i < numbers.length; i++) {{
            totalSum += numbers[i];
        }}
        return totalSum;
    }}
    ```
    
    Example 2:
    Question:
    Could you help me write a program that adds all the numbers in a list in python.
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    Example Response:
    Unfortunately you haven't earned any Python badges. These are the badges you have earned 'Java For-Loop' and 
    'Java If-Else'. Please complete more exercises and try again later.
    
    
    Example 3:
    Question:
    Could you help me write a program that adds all the numbers in a list using a do-while loop.
    
    Badges Earned:
    ['Java For-Loop', 'Java If-Else']
    
    Example Response:
    Unfortunately you haven't earned the do-while loop badge. These are the badges you have earned 'Java For-Loop' and 
    'Java If-Else'. Please complete more exercises and try again later.
    
    Based on the examples and evaluation criteria above, answer this question provided by the student:
    
    Question:
    {question}
    
    Badges Earned:
    {badges}
    
    Remember that you can only provide code that includes the coding concepts that the student knows.
    
    For example:
    If the student has the badges ['Java For-Loop', 'Java If-Else'], they know how to use for loops and 
    if-else statements in Java only. That means you can only provide code to the user in java, no other language. The 
    code provided can only include for-loops and if-else statements, nothing else.
    
    If it is not possible to generate code using those concepts tell the student they need to complete more exercises.
    
    """
    return prompt


def valid_question(question):
    prompt = f"""
        Q: Is the student asking a valid question?
        A: - If the question coding related, then it is valid.
           - If it is unrelated to coding, it is invalid.
           
        Question:
        {question}
        """
    return prompt

def coding_concepts(badges):
    prompt = f"""
            Q: What coding concepts does the student know based off of these badges.
            Let's think step by step:
            
            Badges Earned:
            ['Java For-Loop', 'Java If-Else']
            
            A: The student knows how to write for-loops and if-else statements in java.
            
            Focus on the language before the concept. That means they know that coding concept only in that language.
            
            Now look at these badges:
            
            Badges Earned:
            {badges}
            
            What coding concepts does the student know?
            """
    return prompt


def generate_code(question, badges):
    prompt = f"""
            Q: What coding concepts does the student know based off of these badges.
            Let's think step by step:

            Badges Earned:
            ['Java For-Loop', 'Java If-Else']

            A: The student knows how to write for-loops and if-else statements in java.

            Focus on the language before the concept. That means they know that coding concept only in that language.

            Now look at these badges:

            Badges Earned:
            {badges}

            What coding concepts does the student know?
            
            
            Q: Can code be generated to answer the student's question using only concepts the student knows.
            
            Example:
            The student knows how to write for-loops and if-else statements in Java, and while-loops in both Java and 
            Python.
            
            A: For java the code snippet can only use for-loops, if-else statements and while-loops. No other coding concepts 
            can be provided in the output. For python the code snippet can only include a while-loop. 
            If a fully functioning code answer involves other concepts, respond saying they need to complete more exercises. 
            
            Here is the student's question:
            
            Student Question:
            {question}
            
            REMEMBER ONLY USE CONCEPTS THE STUDENT KNOWS IN YOUR OUTPUT. DO NOT GENERATE CODE THAT HAS CONCEPTS THAT 
            ARE NOT VALID.
            """
    return prompt