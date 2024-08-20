from flask import Flask, request, jsonify
from RAG_Functions import final_result
from Geolocation_Functions import nearest_Doctors, format_table
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)

MAX_QUESTIONS = 3
sessions = {} 

sentiment_analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_score = sentiment_analyzer.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return "positive"
    elif sentiment_score['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

def add_empathy(response, sentiment):
    if sentiment == "positive":
        return f"I'm glad to hear that! {response}"
    elif sentiment == "negative":
        return f"I'm sorry you're feeling that way. {response}"
    else:
        return f"I understand. {response}"

@app.route('/chatbot/', methods=['POST'])
def chatbot():
    data = request.json
    session_id = data.get('session_id', '')
    query = data.get('query', '')

    if session_id not in sessions:
        sessions[session_id] = {"question_count": 0, "address_patient": ""}

    session_data = sessions[session_id]
    question_count = session_data["question_count"]

    sentiment = analyze_sentiment(query)

    if question_count < MAX_QUESTIONS:
        answer = final_result(query)
        empathetic_answer = add_empathy(answer, sentiment)
        session_data["question_count"] += 1
        return jsonify({"response": empathetic_answer})

    elif question_count == 3:
        empathetic_answer = add_empathy(
            "I have answered the maximum number of questions I can handle for this session. Could you please provide your address so that I can recommend the nearest doctors you can consult?",
            sentiment
        )
        session_data["question_count"] += 1
        return jsonify({"response": empathetic_answer})

    elif question_count == 4:
        session_data["address_patient"] = query
        Speciality = "Cardiologist"  
        coordonnee_med = nearest_Doctors(session_data["address_patient"], Speciality)
        formatted_table = format_table(coordonnee_med)
        empathetic_answer = add_empathy(f"These are the closest {Speciality}s available for you to visit:\n{formatted_table}", sentiment)
        session_data["question_count"] += 1
        return jsonify({"response": empathetic_answer})

    else:
        return jsonify({"response": "I have answered the maximum number of questions I can handle for this session."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
