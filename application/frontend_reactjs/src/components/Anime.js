import '../styles/anime.css'
import { Link } from "react-router-dom"
import { useEffect, useState } from 'react'

export default function Anime({ id, display, margin, poster = null, title = null}) {
    const [anime, setAnime] = useState(null)
    const [posterId, setPosterId] = useState([])
    const [animePoster, setAnimePoster] = useState(null)

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
                        setPosterId(response['info']['anime']["rel_ImageAnime"])
                    }
                })
                .catch(error => {
                    console.log(error)
                })   
        }

        async function getPoster() {
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002/utils/imageanime/${posterId[0]}`, {
                mode: "cors",
                method: "GET",
            })
                .then(response => response.blob())
                .then(blob => {
                    if (blob.type === "image/jpg") {
                        let poster = URL.createObjectURL(blob)
                        setAnimePoster(poster)
                    }
                })
                .catch(error => console.log(error))
        }

        getDetail()
        if (poster === null) getPoster()
    }, [id])

    if (display !== "none")
        return (
            <Link className="anime" style={{ margin: `${margin}rem` }} to={`/anime/${id}`}>
                <div className="anime-pic">
                    <img src={animePoster !== null ?
                        animePoster : poster !== null ? poster :
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSigkvS1zRk13D_wWyZrmK4kKaR0DsOSNzDmYC9m1Rk3NWhKsmD3s1uukJUhb1OEcs7nuQ&usqp=CAU"} alt="poster"></img>
                </div>
                <div className="add-to-favorite">
                    <button >+ Add To Favorite</button>
                </div>
                <div className="anime-title">{anime !== null ? anime['Name'] : title !== null ? title : "Title" }</div>
            </Link>
        );
}