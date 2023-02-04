import Header from './components/Header'
import Footer from './components/Footer'
import Home from './pages/Home'
import Favorites from './pages/Favorites';
import Details from './pages/Details';
import Login from './pages/Login';
import Register from './pages/Register';
import { Route, Routes } from "react-router-dom";
import { useState } from 'react';
import SearchResults from './pages/SearchResults';
import Account from './pages/Account';

export default function App() {
  const [userToken, setuserToken] = useState("");

  const onLoggedIn = (token) => {
    setuserToken(token)
  }

  return (
    <>
      <Routes>
        <Route path="/:token?" element={<Home />} />
        <Route path="/favorites/:token?" element={<Favorites />} />
        <Route path='/anime/:id' element={<Details token={ userToken }/>} />
        <Route path='/account/:token?' element={<Account />} />
        <Route path='/login' element={<Login onLoggedIn={ onLoggedIn } />} />
        <Route path='/register' element={<Register onLoggedIn={ onLoggedIn } />} />
        <Route path='/search/:query' element={<SearchResults />} />
      </Routes>
      <Header userToken={userToken} />
      <Footer />
    </>
  );
}
