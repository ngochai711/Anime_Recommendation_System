import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import Anime from "../components/Anime";
import Pagination from "../components/Pagination";
import '../styles/favorites.css'

const paginatedItems = [process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
];

export default function Favorites() {
    const [favAnimes, setFavAnimes] = useState([])

    const navigate = useNavigate()

    let { token } = useParams()

    useEffect(() => {
        if ( token === undefined ) navigate(`/login`) 
    }, [token, navigate])

    return (
        <div className="page" style={{ paddingTop: "3rem" }}>
            <div className="page-section">
                <img className="banner" src={process.env.PUBLIC_URL + "/Favorites_Page_Banner.png"} alt="banner"></img>
            </div>
            <div className="page-section" style={{ paddingTop: "10rem" }}>
                <div className="content-container-2"
                    style={{
                        paddingBottom: "1rem",
                        marginLeft: "10rem",
                    }}>
                    <h1 className="title-2" style={{ fontSize: "2em" }}>FAVORITES</h1>
                    <Pagination itemsPerPage={21} items={favAnimes} />
                </div>
            </div>
            <div className="page-section" style={{ paddingTop: "10rem", paddingBottom: "6rem" }}>
                <div className="content-container-1" style={{ width: "850px", marginLeft: "13rem" }}>
                    <h1 className="title-2">YOU MAY ALSO LIKE</h1>
                    <div className="recommended-list">
                        <ul>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                            <li>
                                <Anime />
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    );
}