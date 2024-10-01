import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import logo from '/src/assets/logo.png'
import './Navbar.css'

function BrandBar() {
  return (
    <>
      <Navbar className="custom-navbar">
        <Container> 
          <Navbar.Brand href="#home">
            <div className="brand-content">
            <img
              src={logo}
              width="250"
              height="150"
              className="d-inline-block align-top"
              alt="React Bootstrap logo"
            />
            <h1>PlaygroundsCTF</h1>
            </div>
          </Navbar.Brand>
        </Container>
      </Navbar>
    </>
  );
}

export default BrandBar;