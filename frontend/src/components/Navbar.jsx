// import Container from 'react-bootstrap/Container';
// import Nav from 'react-bootstrap/Nav';
// import Navbar from 'react-bootstrap/Navbar';
// import NavDropdown from 'react-bootstrap/NavDropdown';
import React from 'react';
import '../style/Navbar.css';


function NavbarCreate(){
  return(
    <nav className="navbar">
      <div>
        <ul>
          <li><a href="/about">About Us</a></li>
          <li><a href="/">Menu</a></li>
          <li><a href="/cart">Cart</a></li>
        </ul>
      </div>
    </nav>
  );
}
export default NavbarCreate