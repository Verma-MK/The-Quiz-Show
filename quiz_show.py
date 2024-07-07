import random
import os

def fifty_fifty(options, correct_answer):
    incorrect_options = [option for option in options if option != correct_answer]
    eliminated_options = random.sample(incorrect_options, 2)
    remaining_options = [correct_answer] + eliminated_options
    remaining_options.sort()

    return remaining_options

def phone_a_friend(question, options):
    print(f"\n☎️ \033[1;34m Calling...\033[0m Your friend for help with the question: {question}")
    friend_answer = random.choice(options)
    print(f"Your friend thinks the answer is: {friend_answer}")
    return friend_answer

def ask_the_audience(options):
    audience_votes = [random.randint(1, 100) for _ in range(len(options))]
    total_votes = sum(audience_votes)

    audience_opinions = {}
    for option, votes in zip(options, audience_votes):
        audience_opinions[option] = votes / total_votes

    sorted_opinions = sorted(audience_opinions.items(), key=lambda x: x[1], reverse=True)

    print("\n🧮 Audience opinions on the options...")
    for option, percentage in sorted_opinions:
        print(f"{option}: \033[93m{percentage * 100:.2f} %\033[0m")
    return sorted_opinions[0][0]

def main():
    terminal_size = os.get_terminal_size()
    line_width = terminal_size.columns
    quiz_show_text = "\033[1;34m|[ ■..\033[0m\033[1;4;38;5;208m.THE QUIZ SHOW.\033[0m\033[1;34m..■ ]|\033[0m"
    visible_text_length = len("|[ ■..THE QUIZ SHOW..■ ]|")
    padding = (line_width - visible_text_length) // 2
    print(" " * padding + quiz_show_text)


    print("\n\033[91mDISCLAIMER !!!\033[0m - Use your lifelines wisely!\n")


    questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Rome", "Paris"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "George Orwell"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["African Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale"
    },
    {
        "question": "In which year did Christopher Columbus reach the Americas?",
        "options": ["1492", "1520", "1471", "1510"],
        "correct_answer": "1492"
    },
    {
        "question": "Which gas makes up the majority of the Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Nitrogen"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["Heart", "Liver", "Brain", "Skin"],
        "correct_answer": "Skin"
    },
    {
        "question": "Who painted the 'Mona Lisa'?",
        "options": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["Ag", "Au", "Fe", "Hg"],
        "correct_answer": "Au"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Carbon Dioxide"
    },
    {
        "question": "Who is the author of 'To Kill a Mockingbird'?",
        "options": ["J.D. Salinger", "George Orwell", "Harper Lee", "Mark Twain"],
        "correct_answer": "Harper Lee"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "South Korea", "Japan", "Vietnam"],
        "correct_answer": "Japan"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Jupiter"
    },
    {
        "question": "Who was the first woman to fly solo across the Atlantic Ocean?",
        "options": ["Amelia Earhart", "Bessie Coleman", "Sally Ride", "Valentina Tereshkova"],
        "correct_answer": "Amelia Earhart"
    },
    {
        "question": "Which gas is known as the 'Laughing Gas'?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrous Oxide", "Methane"],
        "correct_answer": "Nitrous Oxide"
    },
    {
        "question": "Which is the smallest planet in our solar system?",
        "options": ["Mars", "Venus", "Mercury", "Saturn"],
        "correct_answer": "Mercury"
    },
    {
        "question": "Who is the author of 'War and Peace'?",
        "options": ["Fyodor Dostoevsky", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
        "correct_answer": "Leo Tolstoy"
    },
    {
        "question": "What is the largest species of penguin?",
        "options": ["Emperor Penguin", "King Penguin", "Adélie Penguin", "Gentoo Penguin"],
        "correct_answer": "Emperor Penguin"
    },
    {
        "question": "What is the main gas that makes up the Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_answer": "Nitrogen"
    },
    {
        "question": "Who is the first President of India?",
        "options": [" Dr. Rajendra Prasad", "Pratibha Devisingh Patil", "Dr. Sarvepalli Radhakrishnan", "Dr. A.P.J. Abdul Kalam"],
        "correct_answer": " Dr. Rajendra Prasad"
    },
]


    lifelines = ["50:50", "Phone a Friend", "Ask the Audience"]

    money = 0

    for i, question_data in enumerate(questions, start=1):
        question = question_data["question"]
        options = question_data["options"]
        correct_answer = question_data["correct_answer"]

        print(f"🔸 Question {i}: {question}")
        for j, option in enumerate(options, start=1):
            print(f"🔹 {j}. {option}")


        while True:
            print(f"\n💠 Lifelines Left : {len(lifelines)} => {', '.join(lifelines)}")

            choice = input("Choose your lifeline / Enter 'answer' to answer the question : ").strip().lower()

            if choice == "50:50" and "50:50" in lifelines:
                remaining_options = fifty_fifty(options, correct_answer)
                print("Remaining options after using 50:50 lifeline:")
                for j, option in enumerate(remaining_options, start=1):
                    print(f"{j}. {option}")
                lifelines.remove("50:50")

            elif choice == "phone a friend" and "Phone a Friend" in lifelines:
                friend_answer = phone_a_friend(question, options)
                print(f"Your friend thinks the answer is: {friend_answer}")
                lifelines.remove("Phone a Friend")

            elif choice == "ask the audience" and "Ask the Audience" in lifelines:
                audience_answer = ask_the_audience(options)
                print(f"The audience suggests the answer is: {audience_answer}")
                lifelines.remove("Ask the Audience")
                
            elif choice == "answer":
                answer = int(input("Enter the number of your answer (1-4): "))
                if options[answer - 1] == correct_answer:
                    print("\n\033[92mHurray!!!🎉\033[0m You answered correctly...\n")
                    money += 100000
                    print(f"You have won Rs. {money}\n")
                else:
                    print("\n\033[91m❌ Oops!!!\033[0m that's the wrong answer...\n")
                break
            else:
                print("Invalid choice. Please choose a valid lifeline or 'answer' to answer the question.")

        if money == 2000000:

            terminal_size = os.get_terminal_size()
            line_width = terminal_size.columns
            congrats = "\033[92m🎊 🏆  Congratulations!!! 🏆 🎊\033[0m"
            visible_text_length = len("Congratulations!!!")
            padding = (line_width - visible_text_length) // 2
            print(" " * padding + congrats)
            break

    print(f"🏆 Thanks for playing The Quiz Show!, You won Rs. {money}.")

if __name__ == "__main__":
    main()