from flask import Flask

from app.routes.upload_routes import upload_bp



app = Flask(__name__)



app.register_blueprint(upload_bp)





@app.route("/")

def home():

    return {

        "message": "File Upload System Running"

    }





if __name__ == "__main__":

    app.run(debug=True)