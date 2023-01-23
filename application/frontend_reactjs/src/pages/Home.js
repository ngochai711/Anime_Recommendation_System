import Anime from '../components/Anime'
import '../styles/home.css';

export default function Home() {
    return (
        <div className="page">
            <div>
                <div className="page-section">
                    <div className="poster-slide">
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster"></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <img src={process.env.PUBLIC_URL + '/DemonSlayer_Pos.jpg'} alt="poster" style={{ display: "none" }}></img>
                        <div>
                            <span className="selected"></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                    </div>
                </div>
                <div className="page-section">
                    <div className="weekly-top-anime">
                        <div className="title-1">
                            <div>
                                <h1>TOP 10 ANIME THIS WEEK</h1>
                                <div className="line-1"></div>
                            </div>
                        </div>
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
                        <div className="see-more-btn">
                            <button>SEE MORE POPULAR THIS WEEK</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}