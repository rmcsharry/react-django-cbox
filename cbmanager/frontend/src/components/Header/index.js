import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Nav from 'react-bootstrap/Nav'

export default function Header() {
  return (
    <Navbar bg='light' expand='lg'>
      <Navbar.Brand href='#home'>
        <img
          src='/static/dashboard-logo.png'
          width='30'
          height='30'
          className='d-inline-block align-top'
          alt='Dashboard Logo'
        />
        Dashboard Demo
      </Navbar.Brand>
      <Navbar.Toggle aria-controls='basic-navbar-nav' />
      <Navbar.Collapse id='basic-navbar-nav'>
        <Nav className='mr-auto'>
          <Nav.Link href='/api'>Browse API</Nav.Link>
        </Nav>
        <Nav>
          <img
            src='/static/ProfilePic.jpg'
            width='40'
            height='40'
            style={{ borderRadius: '20px' }}
            className='d-inline-block align-top'
            alt='Dashboard Logo'
          />
          <Nav.Link href='http://richardmcsharry.com/'>Richard's Home</Nav.Link>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  )
}
