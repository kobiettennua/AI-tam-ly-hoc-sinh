import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key="dán_api_key_vào_đây")

# ----- Risk scoring rule-based -----
def calculate_risk(text):
    text = text.lower()
    score = 0

    danger_keywords = ["muốn chết", "tự tử", "không muốn sống", "kết thúc tất cả"]
    sad_keywords = ["vô vọng", "cô đơn", "không ai hiểu", "mệt mỏi"]

    for word in danger_keywords:
        if word in text:
            score += 5

    for word in sad_keywords:
        if word in text:
            score += 2

    if score >= 7:
        level = "Nguy cơ cao"
    elif score >= 4:
        level = "Căng thẳng"
    else:
        level = "Ổn định"

    return score, level


# ----- AI response -----
def get_ai_response(user_input, risk_level):
    system_prompt = f"""
    Bạn là trợ lý hỗ trợ tâm lý cho học sinh THCS–THPT.
    Phản hồi nhẹ nhàng, không phán xét.
    Không chẩn đoán bệnh.
    Nếu mức độ là '{risk_level}', hãy điều chỉnh mức độ khuyến nghị phù hợp.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    score, level = calculate_risk(user_input)
    ai_reply = get_ai_response(user_input, level)

    return jsonify({
        "reply": ai_reply,
        "risk_score": score,
        "risk_level": level
    })


if __name__ == "__main__":
    app.run(debug=True)