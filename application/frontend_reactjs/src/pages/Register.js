import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAlert } from "react-alert";
import '../styles/auth.css'

export default function Register({ onLoggedIn }) {
    const [email, setEmail] = useState(null);
    const [username, setUsername] = useState(null);
    const [password, setPassword] = useState(null);
    const [confirmPassword, setConfirmPassword] = useState(null);

    const alert = useAlert();
    const navigate = useNavigate();

    const handleLogin = async (email, password) => {
        await fetch(
            "https://abcdavid-knguyen.ddns.net:30002/auth/signin", {
                mode: "cors",
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    username_or_email: email,
                    password: password
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

    const handleRegister = async () => {
        if (password === null || password !== confirmPassword) 
        {
            console.log("onRegister");
            alert.show("mis-matched passwords!")
            return;
        }
        else 
        {
            await fetch(
                "https://abcdavid-knguyen.ddns.net:30002/auth/signup", {
                    mode: "cors",
                    method: "POST",
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ 
                            email: email,
                            name: "unnamed",
                            username: username,
                            password: password,
                        })
                    }
            )
            .then(response => response.json())
            .then(response => {
                if (response['msg'] === "Completed") handleLogin(email, password)
            })
            .catch(error => {
                console.log(error);
            });
        }
    }

    return (
        <div className="page" style={{ height: "827px", paddingTop: "3rem" }}>
            <div className={"content-container-1 login-container"} style={{ marginTop: "2rem", padding: "3rem" }}>
                <h1 className={"title-3 login-title"}>Create New Account</h1>
                <div className="login-form">
                    <label className="auth-label">Email</label>
                    <input className="auth-input" type="text" onChange={e => setEmail(e.target.value)}></input>
                    <label className="auth-label">Username</label>
                    <input className="auth-input" type="text" onChange={e => setUsername(e.target.value)}></input>
                    <label className="auth-label">Password</label>
                    <input className="auth-input" type="password" onChange={e => setPassword(e.target.value)}></input>
                    <label className="auth-label">Confirm Password</label>
                    <input className="auth-input" type="password" onChange={e => setConfirmPassword(e.target.value)}></input>
                    <button className={"btn-3 auth-btn"} style={{ marginTop: "2rem" }} onClick={handleRegister}>Verify</button>
                    <Link to="/login" className={"btn-2 auth-btn"}>Login</Link>
                </div>
            </div>
        </div>
    );
}