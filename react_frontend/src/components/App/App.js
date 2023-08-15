// import useState and useEffect hooks
import {useState, useEffect} from 'react';
// import api file, to use function that fetches data
import * as apiFunctions from "../../api.js";
// import FizzBuzzList component
import FizzBuzzList from "../FizzBuzzList/FizzBuzzList";

function App() {
  // declare state variable for fizzBuzz array
  const [fizzBuzzArray, setFizzBuzzArray] = useState([]);

  //write a function that fetches data and set state of fizzBuzzArray
  async function getFizzBuzz() {
    const response = await apiFunctions.getFizzBuzz();
    setFizzBuzzArray(response);
  }

  console.log(fizzBuzzArray);

  //call getFizzBuzz function in useEffect
  // add empty array as dependency to only run when page loads
  useEffect(() => {
    getFizzBuzz()
  }, [])

  return (
    <div className="App">
      <h1>FizzBuzz</h1>
      <FizzBuzzList 
          fizzBuzzArray={fizzBuzzArray}/>
    </div>
  );
}

export default App;
