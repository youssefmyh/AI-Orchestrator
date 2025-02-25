import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = ["hello", "hi", "how are you", "bye"]
responses = ["Hello!", "Hi there!", "I'm fine, thanks!", "Goodbye!"]

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(data)

model = MultinomialNB()
model.fit(X_train, responses)

joblib.dump((vectorizer, model), "chatbot_service/model.pkl")
print("✅ Chatbot model trained!")
