import SearchBar from "./SearchBar"

export default function Header() {
    return (
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
        </nav>
    );
}
