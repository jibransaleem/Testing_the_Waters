# # from flask import Flask, request, render_template, redirect, url_for

# app = Flask(__name__)

# @app.route('/', methods=["GET", "POST"])
# def index():
#     try:
#         if request.method == "GET":
#             return render_template('index.html')
#     except Exception as e:
#         return str(e)

# @app.route("/fail/<int:values>")
# def fail(values):
#     return f"<h1>You have failed to pass the exam with {values} score</h1>"

# @app.route("/success/<int:values>")  # Fixed typo here: 'sucess' -> 'success'
# def success(values):
#     return f"<h1>You have passed the exam with {values} score</h1>"

# @app.route("/result/<int:marks>")  # Matching the parameter name
# def res(marks):
#     result = ""
#     if marks < 50:
#         result = 'fail'  # Use 'fail' as route
#     else:
#         result = "success"  # Use 'success' as route
#     return redirect(url_for(result, values=marks))  # Dynamically call the correct route

# @app.route('/form')
# def form():
#     return render_template('form.html')

# if __name__ == "__main__":
#     app.run(debug=True)
