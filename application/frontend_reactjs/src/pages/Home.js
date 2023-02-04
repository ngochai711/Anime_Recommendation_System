import Pagination from '../components/Pagination';
import Anime from '../components/Anime'
import '../styles/home.css'
import { Slide } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css';
import { useEffect, useState } from 'react';

export default function Home() {
    const [top10, ] = useState([21, 813, 11757, 6702, 501, 20, 30276, 235, 32281, 31240])
    const [top10poster, ] = useState([
        "https://m.media-amazon.com/images/M/MV5BODcwNWE3OTMtMDc3MS00NDFjLWE1OTAtNDU3NjgxODMxY2UyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg",
        "https://m.media-amazon.com/images/M/MV5BNGM5MTEyZDItZWNhOS00NzNkLTgwZTAtNWIzY2IzZmExOWMxXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_FMjpg_UX1000_.jpg",
        "https://cdn.myanimelist.net/images/anime/11/39717.jpg",
        "https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/18638d44e180fd1b51870106b88e46e4.jpe",
        "https://m.media-amazon.com/images/M/MV5BMGIzZmQ4YmUtZGQ4NC00OTkyLWE1MGUtMTQ3N2Y3N2E2NWEyXkEyXkFqcGdeQXVyODAzNzAwOTU@._V1_FMjpg_UX1000_.jpg",
        "https://m.media-amazon.com/images/M/MV5BMDI3ZDY4MDgtN2U2OS00Y2YzLWJmZmYtZWMzOTM3YWFjYmUyXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg",
        "https://m.media-amazon.com/images/M/MV5BZjRhZDk4NTktMjMxOS00NTk1LWI4ZDMtOWYyNTU2M2E1ODQwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg",
        "https://m.media-amazon.com/images/M/MV5BMzA1MmI0OGItODU3NS00ZTA0LWI2OTMtYjMyZDVmNjI2YzdlXkEyXkFqcGdeQXVyMTA0MTM5NjI2._V1_FMjpg_UX1000_.jpg",
        "https://m.media-amazon.com/images/M/MV5BNGYyNmI3M2YtNzYzZS00OTViLTkxYjAtZDIyZmE1Y2U1ZmQ2XkEyXkFqcGdeQXVyMTA4NjE0NjEy._V1_.jpg",
        "https://m.media-amazon.com/images/M/MV5BN2NlM2Y5Y2MtYjU5Mi00ZjZiLWFjNjMtZDNiYzJlMjhkOWZiXkEyXkFqcGdeQXVyNjc2NjA5MTU@._V1_FMjpg_UX1000_.jpg"
    ])
    const [wallpapers, ] = useState([
        "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
        "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
        "https://wallpaperaccess.com/full/1122002.jpg",
        "https://wallpaperaccess.com/full/52126.jpg",
        "https://wallpapers.com/images/featured/6ag1ry72uy2s9jmg.jpg",
        "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e6ebd090-fcc2-4fbf-8a3f-c895a6141c22/dabfa5y-acada8c1-88d7-42de-9c71-f8bf9eff8156.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2U2ZWJkMDkwLWZjYzItNGZiZi04YTNmLWM4OTVhNjE0MWMyMlwvZGFiZmE1eS1hY2FkYThjMS04OGQ3LTQyZGUtOWM3MS1mOGJmOWVmZjgxNTYuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.NeK5zNdLqwkyfbIYvt4DpVn7hEh2PuEXvGjUwgKc190",
        "https://lh3.googleusercontent.com/tIKDUuXUkDH8Xumjhx5lGxbBmp1phvZSEFqv8khp3Bu3pRGMwrLKzVEfAX2PxLuJ22J2KvphIcSV_hWJerY5JaeL1g=w640-h400-e365-rj-sc0x00ffffff",
        "https://wallpaperaccess.com/full/6326775.jpg",
        "https://www.wallpaperflare.com/static/223/216/944/re-zero-kara-hajimeru-isekai-seikatsu-rem-re-zero-emilia-re-zero-beatrice-re-zero-wallpaper.jpg"
    ])
    const [index, setIndex] = useState(0)
    const [topAnime, setTopAnime] = useState([21, 813, 11757, 6702, 501, 20, 30276])
    const [topPoster, setTopPoster] = useState([top10poster[0], top10poster[1], top10poster[2], top10poster[3], top10poster[4], top10poster[5], top10poster[6]])
    const [topAnimeObj, setTopAnimeObj] = useState([])
    const [recAnime, setRecAnime] = useState([])
    
    const onLeftArrow = () => {
        if (index > 0) {
            setIndex(prev => prev - 1)
            
            let temp1 = []
            let temp2 = []
            
            for (let i = index; i < index + 6; i++) {
                temp1.push(top10[i])
                temp2.push(top10poster[i])
            }
            
            setTopAnime(temp1)
            setTopPoster(temp2)

            console.log(topAnime)            
            console.log(topPoster)
        }
    }

    const onRightArrow = () => {
        if (index < 2) {
            setIndex(prev => prev + 1)
            
            let temp1 = []
            let temp2 = []
            
            for (let i = index; i < index + 6; i++) {
                temp1.push(top10[i])
                temp2.push(top10poster[i])
            }
            
            setTopAnime(temp1)
            setTopPoster(temp2)

            console.log(topAnime)            
            console.log(topPoster)
        }
    }

    function arrayUnique(array) {
        var a = array.concat();
        for(var i=0; i<a.length; ++i) {
            for(var j=i+1; j<a.length; ++j) {
                if(a[i] === a[j])
                    a.splice(j--, 1);
            }
        }
    
        return a;
    }

    useEffect(() => {
        const temp = []
        for (let i = 0; i < topAnime.length; i++) {
            temp.push(<Anime id={topAnime[i]} poster={topPoster[i]}/>)
        }
        setTopAnimeObj(temp) 
    }, [topAnime, topPoster])

    useEffect(() => {
        const getSimilarAnimes = async (id) => {
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002/search/detail/anime/${id}/similars`, {
                    mode: "cors",
                    method: "GET"
                })
                .then(response => response.json()
                .then(response => {
                    console.log(response)
                    if (response["msg"] === "Completed") {   
                        const similars = response['info']
                        const similarAnis = []
                        for (let i = 0; i < similars.length; i++) {
                            similarAnis.push(similars[i]["anime"]["ID"])
                        }
                        setRecAnime(prev => prev = arrayUnique(prev.concat(similarAnis)))
                    }
                }))
                .catch(error => {
                    console.log(error)
                })
        }

        for (let i = 0; i < 10; i++) getSimilarAnimes(top10[i])
    },[top10])

    return (
        <div className="page">
            <div className="page-section">
                <Slide
                    prevArrow={<button className="prev-next-arrow"><i className="gg-chevron-left"></i></button>}
                    nextArrow={<button className="prev-next-arrow"><i className="gg-chevron-right"></i></button>}
                    indicators={() => <button className="indicator"></button>}>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[0]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[1]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[2]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[3]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[4]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[5]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[6]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[7]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[8]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${wallpapers[9]})` }}></div>
                    </div>
                </Slide>
            </div>
            <div className="page-section" style={{ paddingTop: "7.5rem" }}>
                <div className="content-container-1">
                    <h1 className="title-1">TOP ANIME THIS WEEK</h1>
                    <div className="anime-list">
                        <button className="prev-next-arrow" onClick={onLeftArrow}><i className="gg-chevron-left"></i></button>
                        {topAnimeObj}
                        <button className="prev-next-arrow" onClick={onRightArrow}><i className="gg-chevron-right"></i></button>
                    </div>
                    <button className="btn-1">SEE MORE POPULAR THIS WEEK</button>
                </div>
            </div>
            <div className="page-section" style={{ paddingTop: "7.5rem", paddingBottom: "7.5rem"}}>
                <div className="content-container-2">
                    <h1 className="title-1">RECOMMENDED FOR YOU</h1>
                    <Pagination itemsPerPage={14} items={recAnime} />
                </div>
            </div>
        </div>
    );
}