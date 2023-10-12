# Simple AI Chatbot for College Information
def college_chatbot():
    college_info = {
        'name': 'Gates institute of technology',
        'location': 'Gooty Anatapur',
        'courses': ['Computer Science', 'Electrical  Engineering', 'Mechanical Engineering','Artificial Intelligence','Datascience','Cyber Security','MCA','MBA','civil Engineering','Electronics & communication Engineering'],
        'facilities': ['Library', 'Sports', 'Cafeteria'],
        'website': 'https://gatesit.ac.in/'
    }

    print("Chatbot: Hi! I'm your college information chatbot.")
    while True:
        user_input = input("You: ").lower()
        if 'hi' in user_input or 'hello' in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif 'name' in user_input:
            print(f"Chatbot: The college name is {college_info['name']}.")
        elif 'location' in user_input:
            print(f"Chatbot: The college is located in {college_info['location']}.")
        elif 'courses' in user_input:
            print(f"Chatbot: The college offers courses in {', '.join(college_info['courses'])}.")
        elif 'facilities' in user_input:
            print(f"Chatbot: The college provides facilities like {', '.join(college_info['facilities'])}.")
        elif 'website' in user_input:
            print(f"Chatbot: You can visit the college website at {college_info['website']}.")
        elif 'exit' in user_input or 'bye' in user_input:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand. Please ask a different question.")

if __name__ == "__main__":
    college_chatbot()
    try:
        main()
    except KeyboardInterrupt:
        print 'Interrupted'
        sys.exit(0)
