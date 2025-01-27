import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import NavbarCreate from './components/Navbar';
import Menu from './components/Menu';
import About from './components/AboutUs';
import Cart from './components/Cart';
import Footer from './components/Footer';

function App() {
  return (
    <BrowserRouter>
      <div>
        <NavbarCreate /> 
        <Routes>
          <Route path="/" element={<Menu />} />
          <Route path="/about" element={<About />} />
          <Route path="/cart" element={<Cart />} />
        </Routes>
        <Footer />
      </div>
    </BrowserRouter>
  );
}

export default App;
