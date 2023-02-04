import { useEffect, useState } from "react"
import { useSearchParams } from "react-router-dom"
import Pagination from "../components/Pagination"

export default function SearchResults() {
    const [searchParams, ] = useSearchParams()
    const [results, setResults] = useState([])

    let name = searchParams.get("string");

    useEffect(() => {
        async function handleSearch() {
            await fetch(
                `https://abcdavid-knguyen.ddns.net:30002/search/all?string=${name}&page=1&numperpage=100&order=asc`, {
                    method: "GET"
                })
                .then(response => response.json()
                .then(response => {
                    console.log(response)
                    if (response["msg"] === "Completed")
                    {
                        let temp = response["info"]
                        setResults(temp)
                    }
                }))
                .catch(error => error.json()
                .catch(error => {
                    console.log(error)
                }))
        }

        handleSearch()
    }, [name])

    return (
        <div className="page" style={{ paddingTop: "3rem" }}>
            <div className="page-section">
                <img className="banner" src={process.env.PUBLIC_URL + "/Details_Page_Banner.png"} alt="banner"></img>
            </div>
            <div className="page-section">
                <div className="content-container-2"
                    style={{
                        marginTop: "10rem",
                        marginBottom: "5rem",
                        paddingBottom: "1rem",
                        marginLeft: "10rem",
                    }}>
                    <h1 className="title-2" style={{ fontSize: "2em" }}>RESULTS</h1>
                    <Pagination itemsPerPage={21} items={results} />
                </div>
            </div>
        </div>
    )
}