import streamlit as st

# Initialize a list to store flashcards
flashcards = []

def add_flashcard():
    question = st.text_input("Enter your question:")
    answer = st.text_input("Enter your answer:")
    if st.button("Add Flashcard"):
        flashcards.append({"question": question, "answer": answer})
        st.success("Flashcard added successfully!")

def study_flashcards():
    if not flashcards:
        st.warning("No flashcards found. Please add some first.")
        return

    import random
    random.shuffle(flashcards)

    for card in flashcards:
        st.write("**Question:**")
        st.write(card["question"])
        if st.button("Show Answer"):
            st.write("**Answer:**")
            st.write(card["answer"])

def main():
    st.title("Flashcard App")
    st.sidebar.title("Options")
    choice = st.sidebar.selectbox("Choose an action", ["Add Flashcard", "Study Flashcards"])

    if choice == "Add Flashcard":
        add_flashcard()
    elif choice == "Study Flashcards":
        study_flashcards()

if __name__ == "__main__":
    main()
