import '../styles/home.css';

export default function Home() {
    return (
        <div className="page-content">
            <div className="container">
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
                <div className="weekly-top-anime">
                    <div className="title-1">
                        <div>
                            <h1>TOP 10 ANIME THIS WEEK</h1>
                            <div className="line-1"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}