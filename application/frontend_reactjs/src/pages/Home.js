import React, { useEffect, useState } from 'react';
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
    process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg',
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
            <div className="page-section" style={{ paddingTop: "3rem" }}>
                <div className="content-container-1">
                    <h1 className="title-1" style={{ paddingBottom: "1rem" }}>TOP 10 ANIME THIS WEEK</h1>
                    <div className="anime-list">
                        <button className="prev-next-arrow"><i className="gg-chevron-left"></i></button>
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba" />
                        <button className="prev-next-arrow"><i className="gg-chevron-right"></i></button>
                    </div>
                    <button className="btn-1">SEE MORE POPULAR THIS WEEK</button>
                </div>
            </div>
            <div className="page-section" style={{ paddingTop: "5rem", paddingBottom: "5rem"}}>
                <div className="content-container-2">
                    <h1 className="title-1" style={{ paddingBottom: "1rem" }}>RECOMMENDED FOR YOU</h1>
                    <Pagination itemsPerPage={14} items={paginatedItems} />
                </div>
            </div>
        </div>
    );
}