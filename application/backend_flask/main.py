from components import create_app

App = create_app() 

if __name__ == "__main__":
    print(App.url_map)
    App.run(debug=True)
    