import SearchBar from "./SearchBar"
import User from "./User"
import '../styles/header.css'
import { Link } from "react-router-dom";

export default function Header() {
    return (
        <div className="header">
            <nav className="nav-bar">
                <Link className="web-logo" to="/">Logo</Link>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/favorites">Favorite</Link>
                    </li>
                    <li>
                        <Link to="/account">Account</Link>
                    </li>
                </ul>
                <SearchBar />
                <User />
            </nav>
        </div>
    );
}
