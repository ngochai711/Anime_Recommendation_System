import Anime from '../components/Anime'
import '../styles/home.css';

export default function Home() {
    return (
        <div className="page-content">
            <div className="container">
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
                            <Anime poster="https://www.crunchyroll.com/imgsrv/display/thumbnail/480x720/catalog/crunchyroll/d48d4a62b0ac6381c87bd040b69b0a89.jpe" title="Kimetsu no Yaiba"/>
                            <Anime poster="https://animet.net/upload/images/2019/6/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e-tv-thumbnail.jpg" title="Youkoso Jitsuryoku Shugi Shijou"/>
                            <Anime poster="https://animet.net/upload/images/2019/6/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e-tv-thumbnail.jpg" title="Youkoso Jitsuryoku Shugi Shijou"/>
                            <Anime poster="https://animet.net/upload/images/2019/6/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e-tv-thumbnail.jpg" title="Youkoso Jitsuryoku Shugi Shijou"/>
                            <Anime poster="https://animet.net/upload/images/2019/6/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e-tv-thumbnail.jpg" title="Youkoso Jitsuryoku Shugi Shijou"/>
                            <Anime poster="https://animet.net/upload/images/2019/6/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e-tv-thumbnail.jpg" title="Youkoso Jitsuryoku Shugi Shijou"/>
                            <Anime poster="https://animet.net/upload/images/2019/6/youkoso-jitsuryoku-shijou-shugi-no-kyoushitsu-e-tv-thumbnail.jpg" title="Youkoso Jitsuryoku Shugi Shijou"/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}