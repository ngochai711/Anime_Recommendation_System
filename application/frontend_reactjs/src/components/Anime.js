import '../styles/anime.css'

export default function Anime({ poster, title, display }) {
    if (display !== "none" )
    return (
        <div className="anime">
            <div className="anime-pic">
                <img src={poster} alt="poster"></img>
            </div>
            <div className="add-to-favorite">
                <button >+ Add To Favorite</button>
            </div>
            <div className="anime-title">{title}</div>
        </div>
    );
}