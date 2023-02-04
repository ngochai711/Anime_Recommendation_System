import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import '../styles/account.css';

export default function Account() {
    const [avatar, setAvatar] = useState(null)
    const [id, setId] = useState(null)
    const [email, setEmail] = useState(null)
    const [username, setUsername] = useState(null)
    const [birth, setBirth] = useState(null)
    const [gender, setGender] = useState(null)

    const navigate = useNavigate()

    let { token } = useParams()

    const handleChange = (e) => {
        setAvatar(URL.createObjectURL(e.target.files[0]))
    }

    const handleUsernameChange = (e) => {
        setUsername(e.target.value)
    }

    const handleBirthChange = (e) => {
        setBirth(e.target.value)
    }

    const handleGenderChange = (e) => {
        setGender(e.target.value)
    }

    async function handleSaveInfo() {
        console.log("username: ", username)
        console.log("birth: ", birth)
        console.log("gender: ",gender)
        console.log("token: ",token)
        await fetch(
            `https://abcdavid-knguyen.ddns.net:30002/personal/info/set`,{
                mode: "cors",
                method: "POST",
                headers: {
                    'Authorization': `Bearer ` + token,
                },
                body: JSON.stringify({
                    name: username,
                    birth: birth,
                    gender: gender
                })
            })
        .then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })
    }

    useEffect(() => {
        if (token === undefined) {
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
                            setId(response['info']['ID'])
                            setUsername(response['info']['Name'])
                            setBirth(response['info']['Birthdate'])
                            setGender(response['info']['Gender'])
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
                    <div className="content-container-1" style={{ marginTop: "10rem", marginBottom: "5rem" }}>
                        <h1 className="title-2" style={{ textIndent: "2rem" }}>ACCOUNT</h1>
                        
                        <div style={{ display: "flex", marginTop: "1rem", alignItems: "center", justifyContent: "space-evenly" }}>
                            <div>
                            <div style={{ display: 'block' }}>
                            <img src={avatar !== null ? avatar : "https://indonesia.postsen.com/content/uploads/2022/06/26/79d06b2df9.jpg"} alt="avatar" style={{
                                width: "100px", height: "100px",
                                marginLeft: "5rem",
                                borderRadius: "50%",
                            }}>
                            </img>
                            <input accept="image/*" type="file" onChange={e => handleChange(e)} value="" 
                            style={{ 
                                width: "100px" , marginLeft: "5.5rem", 
                                display: "block" }}/>
                        </div>
                                <div className="info">
                                    <label className="auth-label">Email</label>
                                    <input className="auth-input" type="text" value="user@gmail.com" disabled="true" style={{
                                        color: "#000000c4"
                                    }}></input>
                                </div>
                                <div className="info">
                                    <label className="auth-label">Password</label>
                                    <input className="auth-input" type="password" disabled="true" value="12345678" style={{
                                        color: "#000000c4"
                                    }}></input>
                                </div>
                            </div>
                            <div style={{ marginTop: "2rem" }}>
                                <div className="info">
                                    <label className="auth-label">username</label>
                                    <input className="auth-input" type="text" onChange={e => handleUsernameChange(e)} value={username}></input>
                                </div>
                                <div className="info">
                                    <label className="auth-label">Birth</label>
                                    <input className="auth-input" type="date" onChange={e => handleBirthChange(e)} value={birth}></input>
                                </div>
                                <div className="info">
                                    <label className="auth-label">Gender</label>
                                    <input className="auth-input" type="text" onChange={e => handleGenderChange(e)} value={gender}></input>
                                </div>
                            </div>
                        </div>
                        <button className="btn-2" style={{
                            marginTop: "2rem",
                            borderRadius: "10rem"
                        }} onClick={handleSaveInfo}>SAVE</button>
                    </div>
                </div>
            </div>
        </div>
    );
}