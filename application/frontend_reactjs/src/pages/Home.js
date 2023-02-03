import Pagination from '../components/Pagination';
import Anime from '../components/Anime'
import '../styles/home.css'
import { Slide } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css';



const paginatedItems = [
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
    process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
];

const images = [
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg",
    process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
    "https://i.pinimg.com/originals/27/e4/16/27e4160b0e3d0b90cbcf6aee8e133951.jpg",
    "https://www.pixelstalk.net/wp-content/uploads/images6/Naruto-Wallpaper-HD-Free-download.jpg",
    "https://wallpapers.com/images/featured/c0pujiakubq5rwas.jpg",
    "https://cutewallpaper.org/cdn-cgi/mirage/dd19f2d06ebc24f541f142b37b4289ffa7de722a7607e39984c5c6dd4ce8defd/1280/21/dragon-ball-z-full-hd-wallpaper/Dragon-Ball-Z-1080p-Wallpaper-64+-images-.jpg"
];

export default function Home() {
    return (
        <div className="page">
            <div className="page-section">
                <Slide
                    prevArrow={<button className="prev-next-arrow"><i className="gg-chevron-left"></i></button>}
                    nextArrow={<button className="prev-next-arrow"><i className="gg-chevron-right"></i></button>}
                    indicators={() => <button className="indicator"></button>}>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[0]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[1]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[2]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[3]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[4]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[5]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[6]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[7]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[8]})` }}></div>
                    </div>
                    <div className="slide-layout">
                        <div style={{ "backgroundImage": `url(${images[9]})` }}></div>
                    </div>
                </Slide>
            </div>
            <div className="page-section" style={{ paddingTop: "7.5rem" }}>
                <div className="content-container-1">
                    <h1 className="title-1">TOP ANIME THIS WEEK</h1>
                    <div className="anime-list">
                        <button className="prev-next-arrow"><i className="gg-chevron-left"></i></button>
                        <Anime poster="https://m.media-amazon.com/images/M/MV5BODcwNWE3OTMtMDc3MS00NDFjLWE1OTAtNDU3NjgxODMxY2UyXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_FMjpg_UX1000_.jpg" title="One Piece" />
                        <Anime poster="https://m.media-amazon.com/images/M/MV5BZGFiMWFhNDAtMzUyZS00NmQ2LTljNDYtMmZjNTc5MDUxMzViXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg" title="Naruto Shippuden" />
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <Anime poster="https://m.media-amazon.com/images/M/MV5BODZkZjUxNmEtMGEyOS00ZDY5LTkxZDMtZTJkZDBiZTkyOWRkXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_.jpg" title="Neon Genesis Evangelion" />
                        <Anime poster="https://m.media-amazon.com/images/M/MV5BMTc4YTY0MDUtYWNmMi00NTRiLWE4NmItM2JiMmIzYmEwNGQzXkEyXkFqcGdeQXVyNTkwNzYyODM@._V1_.jpg" title="Neon Genesis Evangelion: Death & Rebirth" />
                        <Anime poster="https://m.media-amazon.com/images/M/MV5BM2ZkYTAwMGMtOGEwOS00MzBjLTgxOGYtZTYwY2E1ZjMyZmY4XkEyXkFqcGdeQXVyNTgyNTA4MjM@._V1_.jpg" title="Monster" />
                        <Anime poster="https://static.tvtropes.org/pmwiki/pub/images/cowboy_bebop_568c35f73e3c7.png" title="Cowboy Bebop" />
                        <button className="prev-next-arrow"><i className="gg-chevron-right"></i></button>
                    </div>
                    <button className="btn-1">SEE MORE POPULAR THIS WEEK</button>
                </div>
            </div>
            <div className="page-section" style={{ paddingTop: "7.5rem", paddingBottom: "7.5rem"}}>
                <div className="content-container-2">
                    <h1 className="title-1">RECOMMENDED FOR YOU</h1>
                    <Pagination itemsPerPage={14} items={paginatedItems} />
                </div>
            </div>
        </div>
    );
}