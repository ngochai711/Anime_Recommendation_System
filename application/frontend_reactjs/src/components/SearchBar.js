import { useState } from "react";

export default function SearchBar() {
    const [searchValue, setsearchValue] = useState(null);

    const handleSearch = (value) => {

    }

    return (
        <form className="search-bar">
            <input type="text" placeholder="What do you need?" onChange={e => setsearchValue(e.target.value)}></input>
            <button className="search-btn" onClick={handleSearch(searchValue)}><i className="gg-search"></i></button>
        </form>
    );
}