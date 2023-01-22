import SearchBar from "./SearchBar"
import User from "./User"
import '../styles/header.css'

export default function Header() {
    return (
        <div className="header">
            <nav className="nav-bar">
                <a className="web-logo" href="/">Logo</a>
                <ul>
                    <li>
                        <a href="/">Home</a>
                    </li>
                    <li>
                        <a href="/favorite">Favorite</a>
                    </li>
                    <li>
                        <a href="/account">Account</a>
                    </li>
                </ul>
                <SearchBar />
                <User />
            </nav>
        </div>
    );
}
