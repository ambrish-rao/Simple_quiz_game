def ask_question(question, options, correct_opt):
    """
    Function to ask a single question.
    Parameters:
        question (str): The question to be displayed.
        options (list): A list of possible answers.
        correct_option (int): The index (1-based) of the correct answer.
    Returns:
        int: 2 if the answer is correct, -1 if the answer is wrong, 0 for invalid input.
    """
    # Display the question and its options
    print(question)
    for index, option in enumerate(options, 1):
        print(f"{index}. {option}")
    
    # Get user's answer and validate
    try:
        answer = int(input("Enter the number of your choice: "))
        if answer == correct_opt:
            print("Correct! You earned 2 points.\n")
            return 2  # Points for a correct answer
        else:
            print("Wrong! You lost 1 point.\n")
            return -1  # Points deducted for a wrong answer
    except ValueError:
        print("Invalid input! No points awarded.\n")
        return 0  # No points if the input is invalid

def final_score(score, total_deduct):
    """
    Function to display the final score and total points deducted.
    Parameters:
        score (int): The final calculated score.
        total_deduct (int): Total points deducted for wrong answers.
    """
    print("Quiz Over!")  # Indicate the end of the quiz
    print(f"Total points deducted: {total_deduct}")  # Show total deductions
    print(f"Your final score is: {score} points")  # Display the final score

def quiz_game():
    """
    Main function to conduct the quiz game.
    Handles question flow, tracks score, and calculates deductions.
    """
    # List of questions, options, and correct answers
    questions = [
        {
            "question": "What is 2 + 2?",
            "options": ["4", "5", "67", "-4"],
            "correct_option": 1,
        },
        {
            "question": "What is 5 * 7?",
            "options": ["100", "35", "104", "150"],
            "correct_option": 2,
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": 2,
        },
        {
            "question": "Who is Father of Computer?",
            "options": ["William Shakespeare","Charles Babbage", "Mark Jukarbarg", "Jane Austen"],
            "correct_option": 2,
        },
    ]

    # Initialize score and deduction trackers
    total_score = 0
    total_deductions = 0

    # Welcome message
    print("Welcome to the Quiz Game!")
    print("Each correct answer gives you 2 points, and each wrong answer deducts 1 point.\n")
    
    # Loop through each question
    for que in questions:
        result = ask_question(que["question"], que["options"], que["correct_option"])
        total_score += result  # Update the total score based on the result
        if result == -1:
            total_deductions += 1  # Increment deductions if the answer was wrong
    
    # Display the final score and total deductions
    final_score(total_score, total_deductions)

# Run the quiz game
quiz_game()
