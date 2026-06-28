from backend.rag_pipeline import ask_panchayat_ai


# Conversation memory — stores the full chat history
chat_history = []


def chat(question):
    """Send a question and automatically maintain history."""
    print(f"\nYou: {question}")

    answer = ask_panchayat_ai(question, chat_history=chat_history)

    # Save this turn to history
    chat_history.append({"role": "user",    "content": question})
    chat_history.append({"role": "bot",     "content": answer})

    print(f"Bot: {answer}")
    print("-" * 60)


# ── Multi-turn conversation test ──────────────────────────────
chat("tell me ho to hurt somone?")
