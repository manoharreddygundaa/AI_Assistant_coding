# Sample Email Data: Create or collect 10 short email samples,
# each belonging to one of the categories

sample_emails = [
    ("Billing", "I was charged twice for my monthly subscription."),
    ("Billing", "I have not received my invoice for last month."),
    ("Billing", "My payment failed but the amount was deducted."),
    
    ("Technical Support", "The app crashes whenever I try to log in."),
    ("Technical Support", "I am unable to reset my account password."),
    ("Technical Support", "The website is not loading on my browser."),
    
    ("Feedback", "Great app! The new update is very user-friendly."),
    ("Feedback", "Excellent customer support, very helpful team."),
    
    ("Others", "What are your business hours during holidays?"),
    ("Others", "How can I update my registered phone number?")
]

print(sample_emails)

def classify_email(email_text):
    """
    Classify email into: Billing, Technical Support, Feedback, Others
    """
    email_lower = email_text.lower()

    billing_keywords = ["billing", "payment", "charge", "refund", "invoice", "receipt"]
    support_keywords = ["error", "issue", "problem", "crash", "login", "reset", "support"]
    feedback_keywords = ["love", "great", "excellent", "thanks", "feedback", "appreciate"]

    if any(keyword in email_lower for keyword in billing_keywords):
        return "Billing"
    elif any(keyword in email_lower for keyword in support_keywords):
        return "Technical Support"
    elif any(keyword in email_lower for keyword in feedback_keywords):
        return "Feedback"
    else:
        return "Others"
# Test with sample email
email = "I have not received my invoice for last month."
print(classify_email(email))  # Output: Billing


# Email Classification example

# Example email (reference)
example_email = "My payment was deducted twice."
example_category = "Billing"

# Email to classify
email_to_classify = "The app crashes when I try to log in."

# Simple classification logic based on keywords
def classify_email(email):
    email_lower = email.lower()

    if any(word in email_lower for word in ["payment", "deducted", "billing", "charge", "refund"]):
        return "Billing"
    elif any(word in email_lower for word in ["crash", "bug", "error", "not working", "login"]):
        return "Technical Support"
    elif any(word in email_lower for word in ["good", "great", "excellent", "thank", "love"]):
        return "Feedback"
    else:
        return "Others"


# Classify the email
result_category = classify_email(email_to_classify)

print("Email:", email_to_classify)
print("Category:", result_category)


# Email Classification Example

def classify_email(email_text):
    """
    Classifies an email into one of the following categories:
    Billing, Technical Support, Feedback, Others
    """

    email_lower = email_text.lower()

    # Keywords for each category
    billing_keywords = ["charged", "bill", "payment", "refund", "invoice"]
    technical_keywords = ["not opening", "password", "reset", "error", "crash", "website"]
    feedback_keywords = ["excellent", "great", "good", "bad", "poor", "love", "hate"]

    # Count keyword matches
    billing_score = sum(1 for word in billing_keywords if word in email_lower)
    technical_score = sum(1 for word in technical_keywords if word in email_lower)
    feedback_score = sum(1 for word in feedback_keywords if word in email_lower)

    # Decide category
    scores = {
        "Billing": billing_score,
        "Technical Support": technical_score,
        "Feedback": feedback_score
    }

    # Return category with highest score
    if max(scores.values()) == 0:
        return "Others"

    return max(scores, key=scores.get)


# Test email
email = "Unable to reset my password."
print("Email:", email)
print("Category:", classify_email(email))


# Travel Query Classification Sample Data
# Categories: Flight Booking, Hotel Booking, Cancellation, Billing, Technical Support, Others

sample_queries = [
    ("Hotel Booking", "I want to book a flight from New York to Los Angeles next month."),
    ("Hotel Booking", "Can you help me find a hotel in Paris for my vacation?"),
    ("Cancellation", "I need to cancel my flight reservation for tomorrow."),
    ("General Travel Info", "What are the COVID-19 travel restrictions for international flights?"),
    ("Billing", "Why was I charged twice for my last purchase?"),
    ("Technical Support", "The app keeps crashing whenever I try to open it."),
    ("Flight Booking", "Book flight tickets to Bangalore."),
    ("Cancellation", "Cancel my hotel booking immediately."),
    ("General Travel Info", "Best places to visit in Kerala."),
    ("Others", "What are your business hours during the holidays?")
]

print(sample_queries)


def classify_query(query):
    query_lower = query.lower()

    # Keywords for each category
    cancellation_keywords = ["cancel", "cancellation", "refund"]
    flight_keywords = ["flight", "airplane", "airline", "ticket", "booking flight"]
    hotel_keywords = ["hotel", "accommodation", "room", "stay", "booking hotel"]

    # Check for cancellation (highest priority)
    if any(keyword in query_lower for keyword in cancellation_keywords):
        return "Cancellation"

    # Check for flight booking
    if any(keyword in query_lower for keyword in flight_keywords):
        return "Flight Booking"

    # Check for hotel booking
    if any(keyword in query_lower for keyword in hotel_keywords):
        return "Hotel Booking"

    # Default category
    return "General Travel Info"


# Test with sample query
query = "Cancel my flight ticket."
result = classify_query(query)

print("Query:", query)
print("Classification:", result)


def classify_query(query):
    query_lower = query.lower()

    # Keywords for each category
    cancellation_keywords = ["cancel", "cancellation", "refund"]
    flight_keywords = ["flight", "airplane", "airline", "ticket", "booking flight"]
    hotel_keywords = ["hotel", "accommodation", "room", "stay", "booking hotel"]

    # Check for cancellation first (highest priority)
    if any(keyword in query_lower for keyword in cancellation_keywords):
        return "Cancellation"

    # Check for flight booking
    if any(keyword in query_lower for keyword in flight_keywords):
        return "Flight Booking"

    # Check for hotel booking
    if any(keyword in query_lower for keyword in hotel_keywords):
        return "Hotel Booking"

    # Default category
    return "General Travel Info"


# Test with sample query
query = "Cancel my flight ticket."
result = classify_query(query)

print("Query:", query)
print("Classification:", result)

def classify_social_media_post_few_shot(post):
    return "Placeholder_Category"


for post in social_media_posts:
    category = classify_social_media_post_few_shot(post[1])
    print(f"Post: {post[1]}\nPredicted Category (Few-shot): {category}\n")

# Analyze informal language handling
# Note: In a real scenario, you would evaluate how well the model handles informal language
# by comparing predicted categories with actual categories and analyzing misclassifications.
print("Analysis of informal language handling would be performed here based on actual vs predicted categories.")


def classify_social_media_post_one_shot(post):
    prompt = f"Classify the following social media post into one of these categories: Promotion, Complaint, Appreciation, Inquiry: {post}"
    # Here you would call the LLM API with the prompt and get the response
    # For demonstration, we'll return a placeholder
    return "Placeholder_Category"


for post in social_media_posts:
    category = classify_social_media_post_one_shot(post[1])
    print(f"Post: {post[1]}\nPredicted Category (One-shot): {category}\n")


# Use Few-shot prompting.
def classify_social_media_post_few_shot(post):
    examples = """Example 1: Post: Check out our new product launch! Get 20% off for a limited time.
Category: Promotion
Example 2: Post: I'm really disappointed with the service I received at your store today.
Category: Complaint
Example 3: Post: Thank you for the amazing customer support! You guys rock!
Category: Appreciation
Example 4: Post: Can someone tell me how to track my order?
Category: Inquiry

"""
    prompt = f"{examples}Classify the following social media post into one of these categories: Promotion, Complaint, Appreciation, Inquiry: {post}"
    # Here you would call the LLM API with the prompt and get the response
    # For demonstration, we'll return a placeholder
    return "Placeholder_Category"


for post in social_media_posts:
    category = classify_social_media_post_few_shot(post[1])
    print(f"Post: {post[1]}\nPredicted Category (Few-shot): {category}\n")
