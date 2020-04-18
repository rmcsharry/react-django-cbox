import React from 'react'
import Header from '../Header'
import Container from 'react-bootstrap/Container'
import Footer from '../Footer'

function Layout({children}) {
  return (
    <>
      <Header />
      <Container>
        {children}
      </Container>
      <Footer />
    </>
  );
}

export default Layout;
