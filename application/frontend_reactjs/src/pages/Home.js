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
                    <div className="badge-bar">
                        <span></span>
                    </div>
                </div>
                <div className='weekly-top-anime'>
                    <p>Home</p>
                </div>
            </div>
        </div>
    );
}