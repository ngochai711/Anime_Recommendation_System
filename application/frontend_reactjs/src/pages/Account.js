import { useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom";

export default function Account() {
    const navigate = useNavigate()

    let { token } = useParams()

    useEffect(() => {
        if ( token === undefined ) {
            navigate(`/login`) 
        }
        else {
            async function getUserInfo() {
                await fetch(
                    `https://abcdavid-knguyen.ddns.net:30002/personal/info/get`, {
                        mode: "cors",
                        method: "GET",
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

            getUserInfo()
        }

    }, [token, navigate])

    return (
        <div className="page" style={{ paddingTop: "3rem" }}>
            <div className="page-section">
                <div className="page-section">
                    <img className="banner" src={process.env.PUBLIC_URL + "/Account_Page_Banner.png"} alt="banner"></img>
                </div>
                <div className="page-section">
                    <div className="content-container-1">
                    <div style={{ display: "flex", marginTop: "1rem" }}>
                                <div style={{ width: "200px" }}>
                                    <p className="anime-more-info">Episodes:</p>
                                    <p className="anime-more-info">Episodes:</p>
                                    <p className="anime-more-info">Type:</p>
                                </div>
                                <div style={{ width: "200px" }}>
                                    <p className="anime-more-info">Score:</p>
                                    <p className="anime-more-info">Duration:</p>
                                    <p className="anime-more-info">Premiered:</p>
                                </div>
                            </div>
                    </div>
                </div>
            </div>
        </div>
    );
}