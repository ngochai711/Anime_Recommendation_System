import { Link } from "react-router-dom";
import SearchBar from "./SearchBar";
import User from "./User";
import '../styles/header.css';

export default function Header({ userToken }) {
    return (
        <div className="header">
            <nav className="nav-bar">
                <Link className="web-logo" to={`/${userToken}`}>Logo</Link>
                <ul>
                    <li>
                        <Link to={`/${userToken}`}>Home</Link>
                    </li>
                    <li>
                        <Link to={`/favorites/${userToken}`}>Favorite</Link>
                    </li>
                    <li>
                        <Link to={`/account/${userToken}`}>Account</Link>
                    </li>
                </ul>
                <SearchBar />
                <User userToken={ userToken } />
            </nav>
        </div>
    );
}
