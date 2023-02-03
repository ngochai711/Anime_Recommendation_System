import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAlert } from "react-alert";
import '../styles/auth.css'

export default function Login({ onLoggedIn }) {
    const [username, setUsername] = useState("");
    const [pass, setPass] = useState("");

    const alert = useAlert();
    const navigate = useNavigate();

    const handleLogin = async () => {
        if (username === "" || pass === "")
        {
            alert.show("Empty fields!");
            return;
        }
        else
        {
            await fetch(
                "https://abcdavid-knguyen.ddns.net:30002/auth/signin", {
                    mode: "cors",
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        username_or_email: username,
                        password: pass
                    }) 
                }
            )
            .then(response => response.json()
            .then(response => {
                if (response['msg'] === "Completed")
                {
                    onLoggedIn(response['token']);
                    navigate('/');
                }
            }))
            .catch(error => {
                console.log(error);
            });
        }
    }

    return (
        <div className="page" style={{ height: "827px", paddingTop: "3rem" }}>
            <div className={"content-container-1 login-container"}>
                <h1 className={"title-3 login-title"}>Login</h1>
                <div className="login-form">
                    <label className="auth-label">Email/Username</label>
                    <input className="auth-input" type="text" onChange={e => setUsername(e.target.value)}></input>
                    <label className="auth-label">Password</label>
                    <input className="auth-input" type="password" onChange={e => setPass(e.target.value)}></input>
                    <button className={"btn-3 auth-btn"} style={{ marginTop: "2rem" }} onClick={handleLogin}>Verify</button>
                    <Link to="/register" className={"btn-2 auth-btn"}>Create New Account</Link>
                </div>
            </div>
        </div>
    );
}