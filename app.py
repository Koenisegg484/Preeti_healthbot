from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

# openai_api_key = "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"
# openai_api_key = "sk-proj-kaETgvD9KAI3tIg5TU7eT3BlbkFJLP6QKbg6203kuA6Lb4Ut"
openai_api_key = "sk-proj-e2Hyhpttcs3qE8fcO3BHT3BlbkFJEEBk9xztXg1xlKoA1q9H"


@app.route("/")
def first():
    return render_template("index.html")


@app.route("/bot", methods=["POST"])
def getQuery():
    user_prompt = request.form.get("user-input")
    print(user_prompt)
    with open("jjk.txt", "a+") as f:
        f.write(user_prompt + '\n')
        
    # response = openai.Completion.create(
    #     engine="gpt-3.5-turbo",
    #     prompt=user_prompt,
    #     max_tokens=45
    # )

    client = OpenAI(api_key=openai_api_key)

    response = client.chat.completions.create(
        messages=[
            {
                "role" : "user",
                "content" : user_prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # bot_response = response.choices[0].text.strip()
    bot_response = response
    with open("jjk.txt", "a+") as f:
        f.write(bot_response + '\n')


    return render_template("index.html", bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)