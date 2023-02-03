import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

export default function User({ userToken }) {
    const [userName, setuserName] = useState(null);
    const [userAvatar, setuserAvatar] = useState(null);

    const getUserInfo = async (userToken) => {
        console.log('Bearer' + userToken)

        await fetch(
            "https://abcdavid-knguyen.ddns.net:30002/personal/info/get", {
                mode: "cors",
                method: "GET",
                headers: {
                    'Authorization': 'Bearer ' + userToken,
                    'Content-Type': 'application/json',
                } 
            }
        )
        .then(response => response.json()
        .then(response => {
            console.log(response)
            let username = response['info']['Name']
            setuserName(username)
        }))
        .catch(error => error.json())
        .catch(error => { console.log(error) })
    }

    useEffect(() => { 
        if (userToken !== null) getUserInfo(userToken) 
    }, [userToken]);

    
    if (userToken === null)    {
        return (
            <Link className="user" to="/login">Login</Link>
        );
    }

    return (
        <button className="user">
            <img className='user-avatar' src="https://indonesia.postsen.com/content/uploads/2022/06/26/79d06b2df9.jpg" alt="avatar"></img>
            <div className='user-name'>{userName}</div>
        </button>
    );
}
