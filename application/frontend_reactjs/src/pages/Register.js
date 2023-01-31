import { Link } from "react-router-dom";
import '../styles/auth.css'

export default function Register() {
    return (
        <div className="page" style={{ height: "827px", paddingTop: "3rem" }}>
            <div className={"content-container-1 login-container"} style={{ marginTop: "2rem", padding: "3rem" }}>
                <h1 className={"title-3 login-title"}>Create New Account</h1>
                <form className="login-form">
                    <label className="auth-label">Email</label>
                    <input className="auth-input" type="text"></input>
                    <label className="auth-label">Username</label>
                    <input className="auth-input" type="text"></input>
                    <label className="auth-label">Password</label>
                    <input className="auth-input" type="password"></input>
                    <label className="auth-label">Confirm Password</label>
                    <input className="auth-input" type="password"></input>
                    <button className={"btn-3 auth-btn"} style={{ marginTop: "2rem" }} type="submit">Verify</button>
                    <Link to="/login" className={"btn-2 auth-btn"}>Login</Link>
                </form>
            </div>
        </div>
    );
}