import React from 'react';
import { Link } from 'react-router-dom';
import './css/Navbar.css';

const Navbar = ({ isLoggedIn, setIsLoggedIn }) => {
  const handleLoginLogout = () => {
    if (isLoggedIn) {
      setIsLoggedIn(false);
    } else {
      // Add login logic here, if needed
    }
  };

  return (
    <nav className="navbar">
      <Link to="/" className="navbar-link">CareerBuzz</Link>
      <Link to="/submit" className="navbar-link">Contribute</Link>
      <Link to="/profile" className="navbar-link">Profile</Link>
      <span className="navbar-spacer"></span>
      <a href="#" className="navbar-link" onClick={handleLoginLogout}>
        {isLoggedIn ? 'Logout' : 'Login'}
      </a>
    </nav>
  );
};

export default Navbar;
