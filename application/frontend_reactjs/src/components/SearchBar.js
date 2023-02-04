import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function SearchBar() {
    const [input, setInput] = useState("");

    const navigate = useNavigate();

    const handleSearch = () => {
        navigate(`/search/all?string=${input}&page=1&numperpage=50&sortby=score&order=desc`)
    }

    return (
        <div className="search-bar">
            <input type="text" placeholder="Search" onChange={e => setInput(e.target.value)}></input>
            <button className="search-btn" onClick={handleSearch}><i className="gg-search"></i></button>
        </div>
    );
}