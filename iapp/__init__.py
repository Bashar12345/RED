from flask import Flask

app = Flask(__name__) 

if __name__ == '__main__':
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)




# def create_app(config_class=Config):
#     # run all package as initial flask app
   

#     return app