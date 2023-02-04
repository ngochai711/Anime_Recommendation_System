from components import create_app
from components.inserter import InsertAnimeImages

App = create_app() 

if __name__ == "__main__":
    print(App.url_map)
    App.run(debug=True)
    
    InsertAnimeImages(2, 124)