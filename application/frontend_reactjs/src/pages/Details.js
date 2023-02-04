import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Anime from '../components/Anime';
import Genre from '../components/Genre';
import Rating from '../components/Rating';
import '../styles/anime.css';

export default function Details({ token }) {
    const [anime, setAnime] = useState(null)
    const [posterId, setPosterId] = useState([])
    const [animePoster, setAnimePoster] = useState(null)
    const [animeGenres, setAnimeGenres] = useState(null)
    const [animeLisenses, setAnimeLisenses] = useState(null)
    const [animeProducers, setAnimeProducers] = useState(null)
    const [animeInfo, setAnimeInfo] = useState(null)
    const [animeAiredFrom, setAnimeAiredFrom] = useState(null)
    const [animeAiredTo, setAnimeAiredTo] = useState(null)
    const [similarAnimes, setSimilarAnimes] = useState(null)
    const [userRating, setUserRating] = useState(null)
    const [isFavorite, setIsFavorite] = useState(false)

    let { id } = useParams();

    const handleFavorite = async () => {
        setIsFavorite(!isFavorite)

        if (isFavorite) {
            let initRate = 8.0
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002'/personal/rating/set/${id}/point=${initRate}`, {
                    mode: "cors",
                    method: "POST",
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    }
                })
                .then(response => response.json()
                .then(response => {
                    console.log(response)
                    if (response['msg'] === "Completed")
                        setUserRating(initRate)
                }))
                .catch(error => error.json()
                .catch(error => {
                    console.log(error)
                }))
        }

        if (!isFavorite) {
            let rate = 0.0
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002'/personal/rating/set/${id}/point=${rate}`, {
                    mode: "cors",
                    method: "POST",
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    }
                })
                .then(response => response.json()
                .then(response => {
                    console.log(response)
                }))
                .catch(error => error.json()
                .catch(error => {
                    console.log(error)
                }))
        }
    }
    
    const updateRate = async () => {

    }
    useEffect( () => {
        async function getDetail() {
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002/search/detail/anime/${id}`, {
                    mode: "cors",
                    method: "GET"
                })
                .then(response => response.json())
                .then(response => {
                    console.log(response)
                    if (response["msg"] === "Completed") {   
                        setAnime(response['info']['anime'])
                        setAnimeInfo(response['info']['animeinfo'])
                        setPosterId(response['info']['anime']["rel_ImageAnime"])
                        let genres = response['info']['anime']['Genres'].split(', ')
                        let genreRows = []
                        for (let i = 0; i < genres.length; i++)
                            genreRows.push(<Genre value={genres[i]} />)
                        setAnimeGenres(genreRows)

                        let licenses = response['info']['animeinfo']['Licensors'].split(', ')
                        let licenseRows = []
                        for (let i = 0; i < licenses.length; i++)
                            licenseRows.push(<p>{licenses[i]}</p>)
                        setAnimeLisenses(licenseRows)

                        let producers = response['info']['animeinfo']['Producers'].split(', ')
                        let producersRows = []
                        for (let i = 0; i < producers.length; i++)
                            producersRows.push(<p>{producers[i]}</p>)
                        setAnimeProducers(producersRows)

                        let airedDate = response['info']['animeinfo']['Aired'].split(' to ')
                        setAnimeAiredFrom(airedDate[0])
                        setAnimeAiredTo(airedDate[1])
                    }
                })
                .catch(error => console.log(error))
        }

        async function getSimilarAnimes() {
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002/search/detail/anime/${id}/similars`, {
                    mode: "cors",
                    method: "GET"
                })
                .then(response => response.json()
                .then(response => {
                    console.log(response)
                    if (response["msg"] === "Completed") {   
                        let similars = response['info']
                        let similarAnis = []
                        for (let i = 0; i < similars.length; i++)
                            similarAnis.push(<li><Anime id={similars[i]["anime"]["ID"]} title={similars[i]["anime"]["Name"]} /></li>)
                            setSimilarAnimes(similarAnis)
                    }
                }))
                .catch(error => {
                    console.log(error)
                })
        }

        async function getRating() {
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002/personal/rating/get/${id}`, {
                    mode: "cors",
                    method: "GET",
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    }
                })
                .then(response => response.json()
                .then(response => {
                    console.log(response)
                    if (response["msg"] === "Completed") {   
                        if (response["info"] !== "No rating yet")
                            setIsFavorite(true)
                        else
                            setIsFavorite(false)
                    }
                }))
                .catch(error => error.json()
                .catch(error => {
                    console.log(error)
                }))
        }
        
        getDetail()
        getSimilarAnimes()
        getRating()
    },[id, token])

    useEffect(() => {
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

        getPoster()
    }, [posterId])

    return (
        <div className="page" style={{ paddingTop: "3rem" }}>
            <div className="page-section">
                <img className="banner" src={process.env.PUBLIC_URL + "/Details_Page_Banner.png"} alt="banner"></img>
            </div>
            <div className="page-section" style={{ paddingTop: "10rem" }}>
                <div className="anime-info">
                    <div className={"content-container-1 anime-overview"}>
                        <div style={{ width: "230px" }}>
                            <h1 className="title-2" style={{ textIndent: "0rem" }}>OVERVIEW</h1>
                            <img src={animePoster !== null ? 
                                animePoster : 
                                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSigkvS1zRk13D_wWyZrmK4kKaR0DsOSNzDmYC9m1Rk3NWhKsmD3s1uukJUhb1OEcs7nuQ&usqp=CAU"} alt="poster"></img>
                            { !isFavorite ? 
                                <button className="btn-2" onClick={ handleFavorite  } >+ ADD TO LIST</button> :
                                <div>
                                    <button className="btn-2" onClick={ handleFavorite } >UN - FAVORITE</button>
                                    <button className={"btn-2 score-btn"} onClick={ updateRate }>YOUR RATE<input placeholder={userRating}></input></button>
                                </div>
                            }
                        </div>
                        <div style={{ width: "800px", padding: "2rem", paddingBottom: "0rem" }}>
                            <div>
                                <h1 className="title-3">{anime !== null ? anime['Name'] : ""}</h1>
                                <p className="anime-description">{animeInfo !== null ? animeInfo['Synopsis'] : ""}</p>
                            </div>
                            <div style={{ marginTop: "2rem" }}>
                                <h3 className="sub-title-1">Alternative Titles:</h3>
                                <p className="anime-alt-titles">{animeInfo !== null ? `${animeInfo["Name_ENG"]}, ${animeInfo["Name_JPN"]}` : ""}</p>
                            </div>
                            <div style={{ marginTop: "2rem" }}>
                                <h3 className="sub-title-1">Genres:</h3>
                                <div className="anime-genre">
                                    {animeGenres}
                                </div>
                            </div>
                            <div style={{ display: "flex", marginTop: "1rem" }}>
                                <div style={{ width: "200px" }}>
                                    <Rating score={anime === null ? "" : anime['Score']} />
                                    <p className="anime-more-info">Episodes: {anime === null ? "" : anime['Episodes']}</p>
                                    <p className="anime-more-info">Type: {animeInfo === null ? "" : animeInfo['Type']}</p>
                                </div>
                                <div style={{ width: "200px" }}>
                                    <p className="anime-more-info">Score: {anime === null ? "" : anime['Score']}</p>
                                    <p className="anime-more-info">Duration: {animeInfo === null ? "" : animeInfo['Duration']}</p>
                                    <p className="anime-more-info">Premiered: {animeInfo === null ? "" : animeInfo['Premiered']}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={"content-container-1 anime-producer"}>
                        <h1 className="title-2" style={{ textIndent: "0rem" }}>PRODUCERS</h1>
                        <div style={{ height: "fit-content", marginTop: "1.5rem" }}>
                            <h3 className="sub-title-1">Studio:</h3>
                            <p>{animeInfo === null ? "" : animeInfo['Studio']}</p>
                        </div>
                        <div>
                            <h3 className="sub-title-1">Licensed by:</h3>
                            <div>{animeLisenses}</div>
                        </div>
                        <div>
                            <h3 className="sub-title-1">Produced by:</h3>
                            <div>{animeProducers}</div>
                        </div>
                        <div>
                            <h3 className="sub-title-1">Aired date:</h3>
                            <p>From: {animeAiredFrom === null ? "" : animeAiredFrom}</p>
                            <p>To: {animeAiredTo === null ? "" : animeAiredTo}</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="page-section" style={{ paddingTop: "10rem", paddingBottom: "6rem" }}>
                <div className="content-container-2" style={{ width: "850px", marginLeft: "13rem" }}>
                    <h1 className="title-2">IF YOU LIKE THIS, YOU MAY ALSO LIKE</h1>
                    <div className="recommended-list">
                        <ul>{similarAnimes}</ul>
                    </div>
                </div>
            </div>
        </div>
    );
}