import Anime from '../components/Anime';
import Genre from '../components/Genre';
import Rating from '../components/Rating';
import '../styles/anime.css';

export default function Details() {
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
                            <img src="https://m.media-amazon.com/images/M/MV5BZTI1MjY3N2YtODczMy00MGQwLWI2NWMtODQwZTE3NTY5OTExXkEyXkFqcGdeQXVyMzgxODM4NjM@._V1_.jpg" alt="poster"></img>
                            <button className="btn-2">+ ADD TO LIST</button>
                        </div>
                        <div style={{ width: "800px", padding: "2rem", paddingBottom: "0rem" }}>
                            <div>
                                <h1 className="title-3">no game no life</h1>
                                <p className="anime-description">An urban legend states that those exceptionally gifted ptionally gifted at gaming will be sent a special game invitation, and the winners of the challenge will be whisked away to another world. When Sora and Shiro, two hikikomori NEETs who happen to be both siblings and notorious gamers, receive this invitation, they defeat it with ease. And like the legends tell, they're transported to another world where conflicts, peoples' lives and even country borders are decided by competitions and games. Always up for a challenge, the pair quickly take on the obstacles that come their way, whether it be restoring lowly humanity's good name compared with the other races or helping influence who will become the next king.</p>
                            </div>
                            <div style={{ marginTop: "2rem" }}>
                                <h3 className="sub-title-1">Alternative Titles:</h3>
                                <p className="anime-alt-titles">No Game, No Life, No Game No Life, NGNL, ノーゲーム・ノーライフ</p>
                            </div>
                            <div style={{ marginTop: "2rem" }}>
                                <h3 className="sub-title-1">Genres:</h3>
                                <div className="anime-genre">
                                    <Genre value={"Adventure"} />
                                    <Genre value={"Ecchi"} />
                                    <Genre value={"Fantasy"} />
                                    <Genre value={"Codependency"} />
                                    <Genre value={"High Stakes Games"} />
                                    <Genre value={"Isekai"} />
                                    <Genre value={"NEET"} />
                                </div>
                            </div>
                            <div style={{ display: "flex", marginTop: "1rem" }}>
                                <div style={{ width: "200px" }}>
                                    <Rating score={8.24} />
                                    <p className="anime-more-info">Episodes: 12</p>
                                    <p className="anime-more-info">Type: TV Series</p>
                                </div>
                                <div style={{ width: "200px" }}>
                                    <p className="anime-more-info">Score: 8.24</p>
                                    <p className="anime-more-info">Duration: 24 min</p>
                                    <p className="anime-more-info">Premiered: Summer 2014</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={"content-container-1 anime-producer"}>
                        <h1 className="title-2" style={{ textIndent: "0rem" }}>PRODUCERS</h1>
                        <div style={{ height: "fit-content", marginTop: "1.5rem" }}>
                            <h3 className="sub-title-1">Studio:</h3>
                            <p>MADHOUSE</p>
                        </div>
                        <div>
                            <h3 className="sub-title-1">Licensed by:</h3>
                            <div>
                                <p>AUS Hanabee</p>
                                <p>NA Sentai</p>
                                <p>Filmworks</p>
                                <p>SEA Medialink</p>
                                <p>UK MMV FIlms</p>
                            </div>
                        </div>
                        <div>
                            <h3 className="sub-title-1">Produced by:</h3>
                            <div>
                                <p>Yōhei Hayashi</p>
                                <p>Shō Tanaka</p>
                                <p>Mika Shimizu</p>
                                <p>Satoshi Fukao</p>
                                <p>Asako Shimizu</p>
                            </div>
                        </div>
                        <div>
                            <h3 className="sub-title-1">Aired date:</h3>
                            <p>From: Apr 9, 2014</p>
                            <p>To: Jun 25, 2014</p>
                        </div>
                    </div>
                </div>
            </div>
            <div className="page-section" style={{ paddingTop: "10rem", paddingBottom: "6rem" }}>
                <div className="content-container-2" style={{ width: "850px", marginLeft: "13rem" }}>
                    <h1 className="title-2">IF YOU LIKE THIS, YOU MAY ALSO LIKE</h1>
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