import '../styles/anime.css'
import { Link } from "react-router-dom"
import { useEffect, useState } from 'react'

export default function Anime({ id, poster, title, display, margin }) {
    const [anime, setAnime] = useState(null)
    useEffect(() => {
        async function getDetail() {
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002/search/detail/anime/${id}`, {
                    mode: "cors",
                    method: "GET"
                })
                .then(response => response.json())
                .then(response => {
                    if (response["msg"] === "Completed") {   
                        setAnime(response['info']['anime'])
                    }
                })
                .catch(error => error.json()
                .catch(error => {
                    console.log(error)
                }))
        }

        getDetail()
    }, [id])    

    if (display !== "none" )
    return (
        <Link className="anime" style={{ margin: margin+"rem" }} to={`/anime/${id}`}>
            <div className="anime-pic">
                <img src={poster} alt="poster"></img>
            </div>
            <div className="add-to-favorite">
                <button >+ Add To Favorite</button>
            </div>
            <div className="anime-title">{anime === null ? "Title" : anime['Name']}</div>
        </Link>
    );
}