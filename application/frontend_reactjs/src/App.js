import Header from './components/Header'
import Footer from './components/Footer'
import Home from './pages/Home'
import Favorites from './pages/Favorites';
import { Route, Routes } from "react-router-dom";
import Details from './pages/Details';

export default function App() {
  return (
    <>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/favorites" element={<Favorites />} />
        <Route path='/details' element={<Details />} />
      </Routes>
      <Header />
      <Footer />
    </>
  );
}
