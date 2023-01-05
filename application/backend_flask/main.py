from components import create_app

App = create_app() 

if __name__ == "__main__":
    App.run(debug=True)
    