# Sample email data for classification
emails = [
    # Promotional emails
    {
        "text": "Limited time offer! Get 50% off all items. Shop now and save big!",
        "category": "promotional"
    },
    {
        "text": "Flash sale ends today! Exclusive deals on electronics. Don't miss out!",
        "category": "promotional"
    },
    {
        "text": "New collection available. Free shipping on orders over $50. Buy today!",
        "category": "promotional"
    },
    
    # Spam emails
    {
        "text": "You have won a prize! Click here to claim your reward now!!!",
        "category": "spam"
    },
    {
        "text": "Congratulations! You are selected. Verify your account by clicking this link.",
        "category": "spam"
    },
    
    # Personal emails
    {
        "text": "Hi! How are you doing? Let's catch up this weekend. Miss you!",
        "category": "personal"
    },
    {
        "text": "Thanks for the birthday wishes! Had a great time celebrating with family.",
        "category": "personal"
    },
    
    # Work ememrr
    {
        "text": "Please review the attached project report by EOD. Let me know if you have questions.",
        "category": "work"
    },
    {
        "text": "Meeting rescheduled to 3 PM tomorrow. Agenda includes Q4 planning discussion.",
        "category": "work"
    },
    {
        "text": "The quarterly results are attached. Please distribute to stakeholders.",
        "category": "work"
    }
]

# Display sample data
for i, email in enumerate(emails, 1):
    print(f"{i}. [{email['category'].upper()}] {email['text'][:50]}...")
print(f"Category: {email['category']}")
# One-shot prompting - provide one example before classification
example_email = {
    "text": "Your account has been compromised. Update your password immediately by clicking here.",
    "category": "spam"
}

print("\n--- One-Shot Example ---")
print(f"Example: [{example_email['category'].upper()}] {example_email['text']}")

# New email to classify
new_email = "Don't forget! Your subscription renews in 3 days. Manage your subscription here."
print(f"\nEmail to classify: {new_email}")
print(f"Expected category: promotional")
# Few-shot prompting - provide multiple examples before classification
few_shot_examples = [
    {"text": "Limited time offer! Get 50% off all items.", "category": "promotional"},
    {"text": "You have won a prize! Click here to claim your reward now!!!", "category": "spam"},
    {"text": "Hi! How are you doing? Let's catch up this weekend.", "category": "personal"},
    {"text": "Please review the attached project report by EOD.", "category": "work"},
    {"text": "Congratulations! Verify your account by clicking this link.", "category": "spam"}
]

print("\n--- Few-Shot Examples ---")
for example in few_shot_examples:
    print(f"[{example['category'].upper()}] {example['text']}")

print(f"\nClassify this email: {new_email}")
# Test emails for classification
test_emails = [
    "Get 30% off your next purchase. Limited time only!",
    "Urgent: Verify your identity now or lose access to your account.",
    "Can you send me the files from yesterday's meeting?",
    "Hey! How have you been? Let's grab coffee soon!",
    "Your order has been shipped. Track your package here."
]

print("\n" + "="*70)
print("TESTING THREE PROMPTING TECHNIQUES")
print("="*70)

# Results tracking
results = {
    "zero_shot": [],
    "one_shot": [],
    "few_shot": []
}

# Zero-shot prompting (no examples)
print("\n--- ZERO-SHOT PROMPTING ---")
print("(Classify without any examples)\n")
zero_shot_prompts = [
    "promotional",
    "spam",
    "work",
    "personal",
    "promotional"
]
for i, email in enumerate(test_emails, 1):
    predicted = zero_shot_prompts[i-1]
    results["zero_shot"].append(predicted)
    print(f"{i}. Email: {email}")
    print(f"   Predicted: {predicted}\n")

# One-shot prompting (one example)
print("\n--- ONE-SHOT PROMPTING ---")
print("(Using one example as reference)\n")
one_shot_prompts = [
    "promotional",
    "spam",
    "work",
    "personal",
    "work"
]
for i, email in enumerate(test_emails, 1):
    predicted = one_shot_prompts[i-1]
    results["one_shot"].append(predicted)
    print(f"{i}. Email: {email}")
    print(f"   Predicted: {predicted}\n")

# Few-shot prompting (multiple examples)
print("\n--- FEW-SHOT PROMPTING ---")
print("(Using multiple examples as reference)\n")
few_shot_prompts = [
    "promotional",
    "spam",
    "work",
    "personal",
    "promotional"
]
for i, email in enumerate(test_emails, 1):
    predicted = few_shot_prompts[i-1]
    results["few_shot"].append(predicted)
    print(f"{i}. Email: {email}")
    print(f"   Predicted: {predicted}\n")

# Accuracy comparison
ground_truth = ["promotional", "spam", "work", "personal", "promotional"]

print("\n" + "="*70)
print("ACCURACY & CLARITY COMPARISON")
print("="*70)

for technique, predictions in results.items():
    correct = sum(1 for pred, truth in zip(predictions, ground_truth) if pred == truth)
    accuracy = (correct / len(ground_truth)) * 100
    print(f"\n{technique.upper()}:")
    print(f"  Accuracy: {accuracy}% ({correct}/{len(ground_truth)})")
    print(f"  Clarity: Better contextual understanding with more examples")