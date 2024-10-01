import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import secret from './assets/part3.png'
import background from '/fouriertransforms.png'
import './App.css'
import BrandBar from './components/Navbar'

function log(){
  console.log("part1: PlaygroundsCTF{f0ur13r_15")
  
}

function App() {
  const [count, setCount] = useState(0)
  

  return (
    <>
    <div>
      <BrandBar></BrandBar>
    </div>
      <div>
        <a href="" target="_blank">
          <img src={background} className="logo" alt="Vite logo" />
        </a>
        <a href="_" target="_blank">
          <img src={secret} className="hidden" alt="React logo" />
        </a>
      </div>
      <h1>Its easy if you solve it by inspection</h1>
      <div className="card">
        <button onClick={() => {setCount((count) => count + 1); log()}}>
          count is {count}
        </button>
      </div>
      <p className="read-the-docs">
        Can you solve the equation by inspection ??
      </p>
    </>
  )
}

export default App
