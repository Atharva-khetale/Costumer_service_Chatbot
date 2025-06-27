import re
import random
from together import Together


class CustomerServiceChatbot:
    def __init__(self):
        # Initialize Together AI client
        self.client = Together(api_key="7ad564112c5dd941ac70bfbe0c26f46028bab765a994a423cfe018f58f0e6b85")  # Replace with your actual API key

        # Local knowledge base for quick responses
        self.knowledge_base = {
            "greeting": ["Hello! Welcome to our customer service. How can I help you today?",
                         "Hi there! What can I assist you with?"],
            "hours": ["We're available 24/7 through this chat service.",
                      "Our customer service operates around the clock."],
            "location": ["We're a digital-first company headquartered in San Francisco.",
                         "Our main office is at 123 Tech Street, San Francisco."],
            "contact": ["You can reach our support team at support@company.com or +1-555-123-4567",
                        "Contact us via email at support@company.com or call +1-555-123-4567"],
            "returns": ["You can initiate returns within 30 days of purchase.",
                        "Our return policy allows returns within 30 days with original packaging."],
            "order": ["I can help with order tracking. Please provide your order number."]
        }

        # Patterns for intent recognition
        self.patterns = {
            "greeting": ["hi", "hello", "hey", "greetings"],
            "hours": ["open", "time", "hour", "available"],
            "location": ["where", "location", "address", "based"],
            "contact": ["contact", "phone", "number", "email", "reach"],
            "returns": ["return", "refund", "exchange"],
            "order": ["order", "parcel", "delivery", "track", "shipment"]
        }

    def get_local_response(self, user_input):
        """Handle common queries locally without API calls"""
        user_input = user_input.lower()

        # Check for specific intents
        for intent, keywords in self.patterns.items():
            if any(keyword in user_input for keyword in keywords):
                if intent in self.knowledge_base:
                    return random.choice(self.knowledge_base[intent])

        return None

    def generate_llm_response(self, conversation_history):
        """Generate response using Together AI's streaming API"""
        try:
            response = self.client.chat.completions.create(
                model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                messages=conversation_history,
                stream=True
            )

            full_response = ""
            print("Customer Service: ", end="", flush=True)
            for chunk in response:
                if hasattr(chunk, 'choices') and chunk.choices:
                    content = chunk.choices[0].delta.content
                    if content:
                        print(content, end="", flush=True)
                        full_response += content
            print()  # New line after streaming
            return full_response

        except Exception as e:
            print(f"\nError with LLM: {str(e)}")
            return "I'm having trouble processing your request. Please try again."

    def handle_conversation(self):
        """Main conversation loop"""
        conversation_history = [
            {
                "role": "system",
                "content": """You are a helpful customer service assistant for an e-commerce company. 
                Respond to customer inquiries professionally and politely. 
                Focus on resolving issues about orders, returns, and general questions.
                Ask for order numbers when relevant. Keep responses clear and concise."""
            }
        ]

        print("\nCustomer Service: Hello! How can I assist you today?")
        print("(Type 'exit' at any time to end the conversation)\n")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\nCustomer Service: Thank you for contacting us. Have a great day!")
                break

            # Add user message to conversation history
            conversation_history.append({"role": "user", "content": user_input})

            # First try local responses
            local_response = self.get_local_response(user_input)
            if local_response:
                print(f"Customer Service: {local_response}")
                conversation_history.append({"role": "assistant", "content": local_response})
                continue

            # For all other queries, use the LLM with streaming
            llm_response = self.generate_llm_response(conversation_history)
            conversation_history.append({"role": "assistant", "content": llm_response})


if __name__ == "__main__":
    bot = CustomerServiceChatbot()
    bot.handle_conversation()