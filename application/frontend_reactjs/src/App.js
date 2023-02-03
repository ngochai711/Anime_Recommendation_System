import Header from './components/Header'
import Footer from './components/Footer'
import Home from './pages/Home'
import Favorites from './pages/Favorites';
import Details from './pages/Details';
import Login from './pages/Login';
import Register from './pages/Register';
import { Route, Routes } from "react-router-dom";
import { useState } from 'react';

export default function App() {
  const [userToken, setuserToken] = useState(null);

  const onLoggedIn = (token) => {
    console.log(token)
    setuserToken(token)
  }

  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/favorites" element={<Favorites />} />
        <Route path='/details' element={<Details />} />
        <Route path='/login' element={<Login onLoggedIn={ onLoggedIn } />} />
        <Route path='/register' element={<Register onLoggedIn={ onLoggedIn } />} />
      </Routes>
      <Header userToken={userToken} />
      <Footer />
    </>
  );
}
