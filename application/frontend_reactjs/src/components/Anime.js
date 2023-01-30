import '../styles/anime.css'
import { Link } from "react-router-dom"

export default function Anime({ poster, title, display, margin }) {
    if (display !== "none" )
    return (
        <Link className="anime" style={{ margin: margin+"rem" }} to="/details">
            <div className="anime-pic">
                <img src={poster} alt="poster"></img>
            </div>
            <div className="add-to-favorite">
                <button >+ Add To Favorite</button>
            </div>
            <div className="anime-title">{!title ? "Title" : title}</div>
        </Link>
    );
}